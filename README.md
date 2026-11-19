# devops

大模型运维/交付工具集。目标：把日常重复的巡检、压测、告警、交付检查沉淀成可复用的命令行工具。

## 已有工具

| 工具 | 用途 |
|---|---|
| `npu_check.py` | 读指标 CSV，按 `(node, chip)` 聚合，打印利用率最高的 N 张卡（NPU/GPU 通用） |

### npu_check.py

```bash
python npu_check.py sample_metrics.csv --top 3
```

CSV 字段：`ts,node,chip,util,vec,hbm_used_gb,power_w,temp_c,health`

## 规划

- [ ] `bench.py` 升级：支持 SSE 流式，测 TTFT / ITL / TPOT（当前版本只能测总延迟）
- [ ] 交付预检/验收脚本：从 bash 重写为 Python，输出 JSON 报告
- [ ] 指标看板与告警规则集

## 说明

`sample_metrics.csv` 为脱敏样例数据，不含任何真实环境信息。
