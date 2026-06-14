# 评分模板对比报告

本报告对比所有评分模板 YAML 文件。真实代理测试仍然决定节点是否可用，评分模板仅排序可用节点。

## 权重

| 模板 | latency | jitter | tcp | protocol_history | source_history | 总和 |
| --- | --- | --- | --- | --- | --- | --- |
| scoring.low_latency.yaml | 55 | 15 | 10 | 10 | 10 | 100 |
| scoring.source_quality.yaml | 20 | 15 | 10 | 25 | 30 | 100 |
| scoring.stability.yaml | 20 | 25 | 10 | 20 | 25 | 100 |
| scoring.yaml | 35 | 15 | 10 | 20 | 20 | 100 |

## 阈值

| 模板 | excellent_latency_ms | bad_latency_ms | bad_jitter_ms | excellent_tcp_latency_ms | bad_tcp_latency_ms |
| --- | --- | --- | --- | --- | --- |
| scoring.low_latency.yaml | 100 | 1000 | 400 | 100 | 1000 |
| scoring.source_quality.yaml | 150 | 1400 | 400 | 100 | 1000 |
| scoring.stability.yaml | 150 | 1500 | 300 | 100 | 1000 |
| scoring.yaml | 120 | 1200 | 400 | 100 | 1000 |

## 默认值

| 模板 | missing_tcp_score | missing_history_score |
| --- | --- | --- |
| scoring.low_latency.yaml | 0.5 | 0.5 |
| scoring.source_quality.yaml | 0.5 | 0.5 |
| scoring.stability.yaml | 0.5 | 0.5 |
| scoring.yaml | 0.5 | 0.5 |

---

本文件由 `tools/scoring_profiles_report.py` 自动生成。
