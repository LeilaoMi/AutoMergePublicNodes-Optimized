# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-29 03:18:38 |
| 运行耗时 | 256.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 76585 |
| 去重后节点 | 21579 |
| TCP 可达 | 3000 |
| 真实可用 | 604 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21579 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| geo | 1.3 |
| tcp | 31.5 |
| probe | 53.7 |
| real_test | 134.4 |
| generate | 28.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44041 |
| trojan | 10978 |
| shadowsocks | 10547 |
| vmess | 10281 |
| hysteria2 | 496 |
| http | 98 |
| shadowsocksr | 74 |
| socks | 59 |
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
| 76.86 | hysteria2 | 252.7 | 689.4 | 21.93 | 0.0 | 6.42 | 12.35 | 17.16 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 76.45 | shadowsocks | 230.8 | 608.0 | 22.44 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 198.98.53.130 |
| 76.02 | shadowsocks | 249.3 | 673.2 | 22.01 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 37.19.198.244 |
| 75.95 | hysteria2 | 442.2 | 905.4 | 17.54 | 0.0 | 10.0 | 12.35 | 17.16 | Au1rxx-base64 | 159.223.157.129 |
| 75.86 | shadowsocks | 255.9 | 696.7 | 21.85 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 37.19.198.243 |
| 75.82 | shadowsocks | 257.8 | 694.7 | 21.81 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 37.19.198.236 |
| 75.32 | trojan | 326.1 | 888.9 | 20.23 | 0.0 | 10.0 | 10.93 | 17.16 | Au1rxx-base64 | 153.75.250.171 |
| 74.24 | vless | 301.9 | 677.8 | 20.79 | 0.0 | 10.0 | 10.83 | 14.34 | mheidari-all | 45.206.5.122 |
| 73.81 | shadowsocks | 344.5 | 960.3 | 19.8 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 37.19.198.160 |
| 73.37 | shadowsocks | 280.4 | 640.7 | 21.29 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 156.146.38.167 |
| 73.19 | hysteria2 | 352.8 | 690.5 | 19.61 | 0.0 | 10.0 | 12.35 | 17.16 | Au1rxx-base64 | 178.215.238.30 |
| 73.11 | shadowsocks | 353.1 | 876.0 | 19.6 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 185.196.61.82 |
| 72.93 | shadowsocks | 361.2 | 1000.7 | 19.42 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 68.168.222.210 |
| 72.71 | hysteria2 | 353.5 | 692.9 | 19.59 | 0.0 | 10.0 | 12.35 | 17.16 | Au1rxx-base64 | 62.210.124.146 |
| 72.57 | vless | 311.0 | 860.1 | 20.58 | 0.0 | 10.0 | 10.83 | 17.16 | Au1rxx-base64 | ezaccess1-x4g-ezaccess1-c619.up.railway.app |
| 72.21 | shadowsocks | 333.4 | 831.4 | 20.06 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 68.168.116.6 |
| 71.74 | shadowsocks | 286.4 | 659.9 | 21.15 | 0.0 | 10.0 | 10.85 | 17.16 | Au1rxx-base64 | 156.146.38.169 |
| 71.71 | vless | 416.8 | 1066.6 | 18.13 | 0.0 | 10.0 | 10.83 | 14.34 | mheidari-all | 158.69.112.254 |
| 71.65 | trojan | 307.8 | 658.7 | 20.65 | 0.0 | 10.0 | 10.93 | 17.16 | Au1rxx-base64 | 163.245.196.68 |
| 71.58 | vless | 394.5 | 778.9 | 18.65 | 0.0 | 10.0 | 10.83 | 14.34 | mheidari-all | 169.40.42.121 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.982 | 0.939 | 294 | 1151 | prefer |
| zhangkai | 0.977 | 0.985 | 65 | 167 | prefer |
| DeltaKronecker-all | 0.889 | 0.813 | 134 | 4038 | prefer |
| Surfboard-tg-mixed | 0.602 | 0.524 | 21 | 5708 | observe |
| mheidari-all | 0.487 | 0.406 | 347 | 17232 | observe |
| 10ium-ScrapeCategorize-Vless | 0.349 | 0.667 | 3 | 4972 | observe |
| tg-Farah_VPN | 0.263 | 1.0 | 1 | 200 | observe |
| Epodonios-all | 0.255 | None | 0 | 6752 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3968 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6491 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4480 | observe |
| barry-far-vless | 0.255 | None | 0 | 5026 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5059 | observe |
| nscl5-all | 0.246 | None | 0 | 1774 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 87 |
| speed | TimeoutError | - | 45 |
| speed | ClientOSError | - | 42 |
| cn-block | TimeoutError | - | 34 |
| geo | ClientOSError | - | 27 |
| 204 | TimeoutError | - | 10 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
