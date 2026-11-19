#!/usr/bin/env python3
"""npu_check.py — 最简 NPU 巡检：读指标 CSV，打印利用率最高的前 N 张卡。

CSV 字段: ts,node,chip,util,vec,hbm_used_gb,power_w,temp_c,health
用法: python npu_check.py sample_metrics.csv --top 3
"""
import argparse
import csv
import json


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def peak_by_chip(rows):
    """按 (node, chip) 聚合，取 util 峰值。"""
    peak = {}
    for r in rows:
        if not r.get("util"):
            continue
        key = (r["node"], r["chip"])
        util = float(r["util"])
        peak[key] = max(peak.get(key, 0.0), util)
    return peak


def main():
    ap = argparse.ArgumentParser(description="NPU 峰值利用率巡检")
    ap.add_argument("csv_path")
    ap.add_argument("--top", type=int, default=5, help="打印前 N 张卡")
    ap.add_argument("--json", action="store_true", help="输出 JSON，便于接入告警/报表")
    args = ap.parse_args()

    rows = load_rows(args.csv_path)
    peak = peak_by_chip(rows)
    if not peak:
        print("没有有效数据")
        return

    top = sorted(peak.items(), key=lambda kv: -kv[1])[: args.top]

    if args.json:
        print(json.dumps(
            {
                "samples": len(rows),
                "cards": len(peak),
                "top": [{"node": n, "chip": c, "util": u} for (n, c), u in top],
            },
            ensure_ascii=False,
        ))
        return

    print(f"样本 {len(rows)} 行，覆盖 {len(peak)} 张卡")
    print(f"{'node':20s} {'chip':>4s} {'util%':>7s}")
    for (node, chip), util in top:
        print(f"{node:20s} {chip:>4s} {util:>7.1f}")


if __name__ == "__main__":
    main()
