# git-lab

git 练习沙盒。这里放的是"学 git"用的最小工程，不是生产代码。

## 目录

| 文件 | 说明 |
|---|---|
| `npu_check.py` | 最简 NPU 指标巡检脚本：读 CSV，打印利用率最高的前 N 张卡 |
| `sample_metrics.csv` | 给上面脚本用的样例数据（字段同 npu_metrics.csv） |
| `notes.txt` | 课堂笔记，随手记，故意留着不提交（第 1 课练习用） |

## 用法

```bash
python npu_check.py sample_metrics.csv --top 3
```

## 学习进度

- [x] 第 1 课：init / status / add / commit / log / show / restore
- [ ] 第 2 课：diff 三种用法、restore / revert / reset 的区别
- [ ] 第 3 课：分支与合并冲突
- [ ] 第 4 课：远程仓库、.gitignore、误提交密码怎么救
