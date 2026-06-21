# 评分模板对比报告

本报告对比所有评分模板 YAML 文件。真实代理测试仍然决定节点是否可用，评分模板仅排序可用节点。

## 权重

| 模板 | latency | jitter | tcp | speed | fingerprint_resistance | protocol_history | source_history | 总和 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scoring.low_latency.yaml | 45 | 15 | 10 | 15 | 5 | 5 | 5 | 100 |
| scoring.source_quality.yaml | 18 | 13 | 10 | 5 | 5 | 22 | 27 | 100 |
| scoring.stability.yaml | 18 | 22 | 10 | 5 | 5 | 18 | 22 | 100 |
| scoring.yaml | 25 | 15 | 10 | 10 | 5 | 15 | 20 | 100 |

## 阈值

| 模板 | excellent_latency_ms | bad_latency_ms | bad_jitter_ms | excellent_tcp_latency_ms | bad_tcp_latency_ms | excellent_speed_kbps | bad_speed_kbps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scoring.low_latency.yaml | 100 | 1000 | 400 | 100 | 1000 | 500 | 10 |
| scoring.source_quality.yaml | 150 | 1400 | 400 | 100 | 1000 | 500 | 10 |
| scoring.stability.yaml | 150 | 1500 | 300 | 100 | 1000 | 500 | 10 |
| scoring.yaml | 120 | 1200 | 400 | 100 | 1000 | 500 | 10 |

## 默认值

| 模板 | missing_tcp_score | missing_history_score | missing_fingerprint_score |
| --- | --- | --- | --- |
| scoring.low_latency.yaml | 0.5 | 0.5 | 0.3 |
| scoring.source_quality.yaml | 0.5 | 0.5 | 0.3 |
| scoring.stability.yaml | 0.5 | 0.5 | 0.3 |
| scoring.yaml | 0.5 | 0.5 | 0.3 |

---

本文件由 `tools/scoring_profiles_report.py` 自动生成。
