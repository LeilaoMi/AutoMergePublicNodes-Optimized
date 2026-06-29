# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-29 15:59:52 |
| 运行耗时 | 199.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 77445 |
| 去重后节点 | 23263 |
| TCP 可达 | 3000 |
| 真实可用 | 444 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23263 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| geo | 1.4 |
| tcp | 31.9 |
| probe | 48.5 |
| real_test | 89.5 |
| generate | 24.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43656 |
| trojan | 12978 |
| vmess | 10953 |
| shadowsocks | 9261 |
| hysteria2 | 247 |
| shadowsocksr | 156 |
| http | 136 |
| socks | 51 |
| hysteria | 6 |
| tuic | 1 |

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
| 78.94 | vless | 268.2 | 733.2 | 21.57 | 0.0 | 10.0 | 10.85 | 16.52 | mheidari-all | 47.253.226.114 |
| 76.11 | shadowsocks | 235.5 | 629.1 | 22.33 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 37.19.198.236 |
| 76.08 | shadowsocks | 236.7 | 632.7 | 22.3 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 37.19.198.243 |
| 75.87 | shadowsocks | 245.5 | 656.2 | 22.09 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 37.19.198.244 |
| 75.86 | shadowsocks | 251.5 | 607.1 | 21.96 | 0.0 | 10.0 | 11.38 | 16.52 | mheidari-all | 198.98.53.130 |
| 75.24 | shadowsocks | 256.4 | 661.7 | 21.84 | 0.0 | 10.0 | 11.38 | 16.52 | mheidari-all | 108.181.57.93 |
| 72.71 | shadowsocks | 285.8 | 656.1 | 21.16 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 156.146.38.169 |
| 71.86 | shadowsocks | 286.0 | 673.1 | 21.16 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 156.146.38.168 |
| 71.52 | shadowsocks | 286.0 | 661.2 | 21.16 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 156.146.38.167 |
| 71.33 | shadowsocks | 281.6 | 632.1 | 21.26 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 156.146.38.170 |
| 71.31 | vless | 281.2 | 682.0 | 21.27 | 0.0 | 10.0 | 10.85 | 11.42 | DeltaKronecker-all | 162.159.252.15 |
| 70.85 | vless | 354.1 | 615.7 | 19.58 | 0.0 | 10.0 | 10.85 | 11.42 | DeltaKronecker-all | 193.9.49.65 |
| 70.37 | vless | 319.4 | 861.2 | 20.38 | 0.0 | 10.0 | 10.85 | 14.14 | Surfboard-tg-mixed | 137.184.218.169 |
| 70.09 | shadowsocks | 279.6 | 759.1 | 21.31 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 37.19.198.160 |
| 70.06 | vless | 349.5 | 640.4 | 19.69 | 0.0 | 10.0 | 10.85 | 16.52 | mheidari-all | 38.244.20.164 |
| 69.6 | vless | 383.6 | 632.4 | 18.9 | 0.0 | 10.0 | 10.85 | 16.52 | mheidari-all | 34.213.172.16 |
| 69.6 | vless | 454.3 | 1145.2 | 17.26 | 0.0 | 10.0 | 10.85 | 14.14 | Surfboard-tg-mixed | 130.107.73.148 |
| 69.31 | vless | 290.9 | 719.3 | 21.04 | 0.0 | 10.0 | 10.85 | 11.42 | DeltaKronecker-all | 162.159.44.191 |
| 69.16 | shadowsocks | 302.6 | 573.1 | 20.77 | 0.0 | 10.0 | 11.38 | 16.4 | Au1rxx-base64 | 173.244.56.9 |
| 69.15 | vless | 372.2 | 1058.9 | 19.16 | 0.0 | 10.0 | 10.85 | 14.14 | Surfboard-tg-mixed | 174.129.45.76 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.852 | 0.871 | 31 | 80 | prefer |
| mheidari-all | 0.805 | 0.728 | 169 | 15881 | prefer |
| Surfboard-tg-mixed | 0.799 | 0.72 | 279 | 5497 | prefer |
| DeltaKronecker-all | 0.589 | 0.509 | 110 | 7004 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4653 | observe |
| Epodonios-all | 0.255 | None | 0 | 7616 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7472 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3986 | observe |
| barry-far-vless | 0.255 | None | 0 | 4553 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5278 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.226 | None | 0 | 1269 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 89 |
| 204 | ClientOSError | - | 16 |
| geo | ClientOSError | - | 15 |
| cn-block | TimeoutError | - | 14 |
| geo | TimeoutError | - | 12 |
| cn-block | ClientOSError | - | 11 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 7 |
| speed | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
