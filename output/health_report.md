# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-28 22:07:04 |
| 运行耗时 | 279.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 77033 |
| 去重后节点 | 20891 |
| TCP 可达 | 3000 |
| 真实可用 | 630 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 20891 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.4 |
| tcp | 34.5 |
| probe | 61.9 |
| real_test | 131.2 |
| generate | 44.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47115 |
| vmess | 10729 |
| shadowsocks | 10518 |
| trojan | 6586 |
| hysteria2 | 1721 |
| http | 176 |
| shadowsocksr | 124 |
| socks | 54 |
| hysteria | 7 |
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
| 82.47 | vless | 188.1 | 478.2 | 23.42 | 0.0 | 10.0 | 11.73 | 19.32 | Au1rxx-base64 | 192.220.9.89 |
| 81.47 | vless | 177.5 | 488.5 | 23.67 | 0.0 | 8.75 | 11.73 | 19.32 | Au1rxx-base64 | 31.58.50.200 |
| 81.32 | vless | 324.1 | 849.5 | 20.27 | 0.0 | 10.0 | 11.73 | 19.32 | Au1rxx-base64 | 15.204.97.216 |
| 80.63 | vless | 170.4 | 474.1 | 23.83 | 0.0 | 8.75 | 11.73 | 19.32 | Au1rxx-base64 | 64.23.229.123 |
| 80.51 | vless | 307.5 | 801.5 | 20.66 | 0.0 | 8.8 | 11.73 | 19.32 | Au1rxx-base64 | 15.204.97.206 |
| 80.12 | vless | 376.0 | 1010.7 | 19.07 | 0.0 | 10.0 | 11.73 | 19.32 | Au1rxx-base64 | 15.204.97.195 |
| 79.92 | shadowsocks | 287.4 | 673.2 | 21.13 | 0.0 | 10.0 | 13.47 | 19.32 | Au1rxx-base64 | 173.244.56.9 |
| 79.84 | shadowsocks | 214.2 | 532.0 | 22.82 | 0.0 | 8.73 | 13.47 | 19.32 | Au1rxx-base64 | 108.181.0.177 |
| 79.81 | shadowsocks | 242.3 | 538.6 | 22.17 | 0.0 | 8.85 | 13.47 | 19.32 | Au1rxx-base64 | 173.244.56.6 |
| 79.44 | shadowsocks | 234.1 | 585.5 | 22.36 | 0.0 | 8.79 | 13.47 | 19.32 | Au1rxx-base64 | 108.181.118.10 |
| 79.33 | vless | 194.2 | 499.5 | 23.28 | 0.0 | 10.0 | 11.73 | 19.32 | Au1rxx-base64 | 172.233.156.123 |
| 79.3 | trojan | 231.3 | 609.6 | 22.42 | 0.0 | 10.0 | 10.56 | 19.32 | Au1rxx-base64 | 14.1.28.76 |
| 79.23 | vless | 198.7 | 550.5 | 23.18 | 0.0 | 10.0 | 11.73 | 19.32 | Au1rxx-base64 | 45.33.62.226 |
| 79.2 | vless | 217.4 | 567.8 | 22.75 | 0.0 | 5.4 | 11.73 | 19.32 | Au1rxx-base64 | unesaa2.surup.shop |
| 78.77 | http | 420.1 | 1171.0 | 18.05 | 0.0 | 10.0 | 14.44 | 19.28 | zhangkai | 138.199.35.216 |
| 78.75 | http | 421.2 | 1172.1 | 18.03 | 0.0 | 10.0 | 14.44 | 19.28 | zhangkai | 138.199.35.198 |
| 78.71 | vless | 257.3 | 518.7 | 21.82 | 0.0 | 8.8 | 11.73 | 19.32 | Au1rxx-base64 | 166.88.186.151 |
| 78.67 | vless | 169.3 | 470.9 | 23.86 | 0.0 | 8.76 | 11.73 | 19.32 | Au1rxx-base64 | 50.116.13.24 |
| 78.65 | vless | 172.7 | 476.7 | 23.78 | 0.0 | 8.82 | 11.73 | 19.32 | Au1rxx-base64 | 173.255.242.56 |
| 78.6 | vless | 172.5 | 486.7 | 23.79 | 0.0 | 8.76 | 11.73 | 19.32 | Au1rxx-base64 | 173.230.155.55 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.949 | 352 | 1776 | prefer |
| zhangkai | 0.967 | 1.0 | 24 | 144 | prefer |
| mheidari-all | 0.949 | 0.878 | 82 | 14493 | prefer |
| DeltaKronecker-all | 0.889 | 0.816 | 87 | 4065 | prefer |
| Surfboard-tg-mixed | 0.758 | 0.68 | 181 | 6713 | prefer |
| tg-oneclickvpnkeys | 0.445 | 1.0 | 5 | 140 | observe |
| nscl5-all | 0.279 | 1.0 | 1 | 594 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4725 | observe |
| Epodonios-all | 0.255 | None | 0 | 6861 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7878 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5540 | observe |
| barry-far-vless | 0.255 | None | 0 | 5468 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4081 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 23 |
| cn-block | TimeoutError | - | 20 |
| geo | ClientOSError | - | 18 |
| 204 | ProxyError | - | 10 |
| speed | ClientOSError | - | 8 |
| speed | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
