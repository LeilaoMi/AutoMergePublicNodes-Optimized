# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-01 04:36:20 |
| 运行耗时 | 272.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 79985 |
| 去重后节点 | 22309 |
| TCP 可达 | 3000 |
| 真实可用 | 640 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22309 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.3 |
| tcp | 35.7 |
| probe | 73.8 |
| real_test | 123.0 |
| generate | 34.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50972 |
| vmess | 11049 |
| shadowsocks | 10041 |
| trojan | 6186 |
| hysteria2 | 1381 |
| http | 138 |
| shadowsocksr | 128 |
| socks | 76 |
| hysteria | 7 |
| tuic | 7 |

## 评分权重

| 因子 | 权重 |
| --- | --- |
| latency | 25.0 |
| jitter | 15.0 |
| tcp | 10.0 |
| speed | 10.0 |
| fingerprint_resistance | 5.0 |
| protocol_history | 15.0 |
| source_history | 20.0 |

## Top 节点评分

| 评分 | 协议 | 延迟(ms) | 抖动(ms) | 延迟分 | 抖动分 | TCP分 | 协议历史分 | 来源历史分 | 来源 | 服务器 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 85.41 | vless | 202.7 | 524.3 | 23.09 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.236.252.35 |
| 85.4 | vless | 203.0 | 500.7 | 23.08 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.239.67.231 |
| 85.4 | vless | 203.1 | 519.7 | 23.08 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.233.139.46 |
| 85.39 | vless | 203.4 | 488.3 | 23.07 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.235.43.210 |
| 85.33 | vless | 208.4 | 506.4 | 22.95 | 0.0 | 10.0 | 12.88 | 19.5 | Surfboard-tg-mixed | 172.235.38.85 |
| 85.29 | vless | 207.7 | 515.1 | 22.97 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.233.156.42 |
| 85.24 | vless | 209.8 | 510.7 | 22.92 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.233.156.118 |
| 85.21 | vless | 211.0 | 528.7 | 22.89 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 172.239.67.156 |
| 85.21 | hysteria2 | 236.3 | 547.4 | 22.31 | 0.0 | 10.0 | 14.46 | 19.44 | Au1rxx-base64 | 66.94.121.46 |
| 85.11 | vless | 215.4 | 519.8 | 22.79 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 64.23.229.123 |
| 85.06 | vless | 217.5 | 514.2 | 22.74 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 45.33.62.166 |
| 85.01 | vless | 215.6 | 511.2 | 22.79 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 45.33.62.226 |
| 85.01 | vless | 219.9 | 530.9 | 22.69 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 173.230.155.55 |
| 85.0 | vless | 222.9 | 528.4 | 22.62 | 0.0 | 10.0 | 12.88 | 19.5 | Surfboard-tg-mixed | 45.33.107.60 |
| 84.99 | vless | 220.8 | 529.8 | 22.67 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 45.33.107.237 |
| 84.83 | vless | 227.6 | 562.9 | 22.51 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 70.39.196.142 |
| 84.82 | vless | 228.1 | 535.3 | 22.5 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 173.255.242.56 |
| 84.74 | vless | 229.1 | 530.4 | 22.47 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 192.155.87.188 |
| 84.67 | vless | 234.3 | 547.5 | 22.35 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 50.116.9.184 |
| 84.64 | vless | 235.6 | 564.8 | 22.32 | 0.0 | 10.0 | 12.88 | 19.44 | Au1rxx-base64 | 74.207.245.124 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Au1rxx-base64 | 0.959 | 0.899 | 366 | 1549 | prefer |
| mheidari-all | 0.913 | 0.841 | 88 | 15162 | prefer |
| Surfboard-tg-mixed | 0.829 | 0.751 | 237 | 6997 | prefer |
| DeltaKronecker-all | 0.494 | 0.412 | 85 | 5904 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4657 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7837 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5908 | observe |
| barry-far-vless | 0.255 | None | 0 | 6067 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4025 | observe |
| Au1rxx-clash | 0.237 | None | 0 | 1549 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| Epodonios-all | 0.207 | 0.0 | 1 | 7436 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 47 |
| geo | ClientOSError | - | 30 |
| cn-block | TimeoutError | - | 19 |
| speed | TimeoutError | - | 16 |
| speed | ClientOSError | - | 15 |
| 204 | TimeoutError | - | 14 |
| 204 | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| geo | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
