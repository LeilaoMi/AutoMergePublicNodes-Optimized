# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-09 03:52:57 |
| 运行耗时 | 203.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 80290 |
| 去重后节点 | 24881 |
| TCP 可达 | 3000 |
| 真实可用 | 391 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24881 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 32.6 |
| probe | 47.1 |
| real_test | 81.9 |
| generate | 36.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46222 |
| trojan | 12876 |
| vmess | 10497 |
| shadowsocks | 9476 |
| hysteria2 | 839 |
| shadowsocksr | 139 |
| http | 136 |
| socks | 90 |
| hysteria | 8 |
| anytls | 5 |
| tuic | 2 |

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
| 78.7 | shadowsocks | 241.2 | 644.7 | 22.19 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 37.19.198.243 |
| 78.67 | shadowsocks | 242.8 | 646.9 | 22.16 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 37.19.198.244 |
| 77.98 | shadowsocks | 250.9 | 641.3 | 21.97 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 108.181.57.93 |
| 77.67 | shadowsocks | 286.0 | 779.6 | 21.16 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 37.19.198.236 |
| 76.67 | shadowsocks | 242.8 | 639.3 | 22.16 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 37.19.198.160 |
| 76.24 | trojan | 328.9 | 781.4 | 20.16 | 0.0 | 10.0 | 11.75 | 18.42 | DeltaKronecker-all | 45.32.198.247 |
| 75.69 | shadowsocks | 279.4 | 640.2 | 21.31 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 156.146.38.170 |
| 75.54 | shadowsocks | 278.2 | 630.8 | 21.34 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 156.146.38.168 |
| 75.27 | trojan | 361.3 | 882.4 | 19.42 | 0.0 | 10.0 | 11.75 | 18.12 | mheidari-all | 149.28.241.235 |
| 74.12 | shadowsocks | 236.4 | 609.8 | 22.31 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 198.98.53.130 |
| 74.01 | shadowsocks | 296.8 | 654.1 | 20.91 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 156.146.38.167 |
| 73.84 | shadowsocks | 360.6 | 866.8 | 19.43 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 185.196.61.82 |
| 73.84 | trojan | 361.6 | 882.6 | 19.41 | 0.0 | 10.0 | 11.75 | 18.12 | mheidari-all | 45.32.195.168 |
| 73.51 | trojan | 350.8 | 815.3 | 19.66 | 0.0 | 10.0 | 11.75 | 18.12 | mheidari-all | 64.94.95.118 |
| 72.31 | trojan | 397.4 | 918.2 | 18.58 | 0.0 | 10.0 | 11.75 | 18.42 | DeltaKronecker-all | 64.94.95.114 |
| 71.43 | shadowsocks | 301.0 | 564.5 | 20.81 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 108.181.118.10 |
| 71.37 | shadowsocks | 325.8 | 557.3 | 20.24 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 173.244.56.6 |
| 71.05 | trojan | 412.7 | 953.1 | 18.22 | 0.0 | 10.0 | 11.75 | 18.42 | DeltaKronecker-all | 64.94.95.117 |
| 71.01 | shadowsocks | 318.6 | 559.6 | 20.4 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 108.181.0.177 |
| 70.17 | shadowsocks | 358.7 | 636.5 | 19.47 | 0.0 | 10.0 | 13.61 | 16.9 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.936 | 0.946 | 56 | 128 | prefer |
| Surfboard-tg-mixed | 0.923 | 0.852 | 81 | 5750 | prefer |
| mheidari-all | 0.822 | 0.747 | 91 | 17104 | prefer |
| DeltaKronecker-all | 0.608 | 0.528 | 305 | 8321 | observe |
| xiaoji235-airport-v2ray-all | 0.4 | 0.75 | 4 | 2703 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4408 | observe |
| Epodonios-all | 0.255 | None | 0 | 6606 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6800 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4251 | observe |
| barry-far-vless | 0.255 | None | 0 | 4787 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5361 | observe |
| nscl5-all | 0.228 | None | 0 | 1319 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 86 |
| speed | ClientOSError | - | 55 |
| geo | ClientOSError | - | 19 |
| 204 | ClientOSError | - | 8 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | TimeoutError | - | 3 |
| 204 | ProxyError | - | 1 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 288 | 300 | - |
| global | False | 291 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
