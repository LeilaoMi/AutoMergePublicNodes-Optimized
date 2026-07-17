# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-17 13:54:42 |
| 运行耗时 | 281.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 79167 |
| 去重后节点 | 24892 |
| TCP 可达 | 3000 |
| 真实可用 | 515 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24892 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.2 |
| tcp | 33.1 |
| probe | 55.6 |
| real_test | 141.3 |
| generate | 43.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45262 |
| trojan | 12769 |
| vmess | 10891 |
| shadowsocks | 9726 |
| hysteria2 | 270 |
| shadowsocksr | 123 |
| socks | 64 |
| http | 51 |
| hysteria | 8 |
| tuic | 3 |

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
| 79.7 | shadowsocks | 237.9 | 602.6 | 22.27 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 156.146.38.169 |
| 78.4 | shadowsocks | 287.0 | 760.0 | 21.13 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 156.146.38.167 |
| 76.71 | shadowsocks | 294.4 | 691.2 | 20.96 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 37.19.198.243 |
| 76.44 | shadowsocks | 294.5 | 694.7 | 20.96 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 37.19.198.236 |
| 76.29 | trojan | 249.3 | 613.7 | 22.01 | 0.0 | 10.0 | 13.8 | 13.48 | DeltaKronecker-all | 64.94.95.114 |
| 76.28 | trojan | 249.7 | 579.0 | 22.0 | 0.0 | 10.0 | 13.8 | 13.48 | DeltaKronecker-all | 64.94.95.115 |
| 74.75 | shadowsocks | 290.1 | 581.3 | 21.06 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 173.244.56.9 |
| 74.66 | shadowsocks | 351.6 | 882.8 | 19.64 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 50.114.177.235 |
| 74.13 | shadowsocks | 282.6 | 563.1 | 21.24 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 173.244.56.6 |
| 73.95 | shadowsocks | 278.2 | 515.3 | 21.34 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 108.181.0.177 |
| 73.91 | shadowsocks | 276.9 | 521.4 | 21.37 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 108.181.118.10 |
| 73.31 | shadowsocks | 301.6 | 686.6 | 20.8 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 37.19.198.244 |
| 73.29 | shadowsocks | 238.2 | 607.6 | 22.26 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 156.146.38.170 |
| 72.06 | shadowsocks | 379.5 | 918.4 | 18.99 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 108.181.57.93 |
| 71.95 | shadowsocks | 338.9 | 327.0 | 19.93 | 2.74 | 9.64 | 11.87 | 19.56 | Au1rxx-base64 | 149.22.87.204 |
| 71.5 | shadowsocks | 249.3 | 640.0 | 22.01 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 156.146.38.168 |
| 71.4 | trojan | 359.1 | 870.4 | 19.47 | 0.0 | 10.0 | 13.8 | 19.28 | mheidari-all | 64.94.95.118 |
| 71.32 | shadowsocks | 292.7 | 702.0 | 21.0 | 0.0 | 10.0 | 11.87 | 19.56 | Au1rxx-base64 | 37.19.198.160 |
| 70.8 | trojan | 408.6 | 403.5 | 18.32 | 0.0 | 9.62 | 13.8 | 19.56 | Au1rxx-base64 | 52.195.207.214 |
| 70.7 | trojan | 409.9 | 399.9 | 18.29 | 0.0 | 9.64 | 13.8 | 19.56 | Au1rxx-base64 | 35.72.9.75 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.961 | 0.885 | 191 | 16536 | prefer |
| Au1rxx-base64 | 0.933 | 0.936 | 94 | 150 | prefer |
| Surfboard-tg-mixed | 0.694 | 0.616 | 125 | 5276 | observe |
| DeltaKronecker-all | 0.535 | 0.455 | 312 | 8967 | observe |
| nscl5-all | 0.328 | 1.0 | 1 | 1821 | observe |
| xiaoji235-airport-v2ray-all | 0.322 | 1.0 | 1 | 1680 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4428 | observe |
| Epodonios-all | 0.255 | None | 0 | 6455 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6764 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4097 | observe |
| barry-far-vless | 0.255 | None | 0 | 4743 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5208 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 82 |
| speed | ClientOSError | - | 60 |
| 204 | TimeoutError | - | 45 |
| cn-block | TimeoutError | - | 22 |
| 204 | ClientOSError | - | 13 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 6 |
| 204 | ProxyError | - | 5 |
| geo | ClientOSError | - | 4 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
