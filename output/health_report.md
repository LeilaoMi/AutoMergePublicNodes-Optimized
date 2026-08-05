# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-05 03:00:10 |
| 运行耗时 | 336.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86570 |
| 去重后节点 | 24353 |
| TCP 可达 | 3000 |
| 真实可用 | 652 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24353 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.3 |
| tcp | 36.6 |
| probe | 63.3 |
| real_test | 204.1 |
| generate | 25.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50880 |
| vmess | 13093 |
| trojan | 10778 |
| shadowsocks | 10247 |
| hysteria2 | 1288 |
| socks | 79 |
| http | 77 |
| shadowsocksr | 74 |
| anytls | 21 |
| hysteria | 19 |
| tuic | 14 |

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
| 83.74 | hysteria2 | 286.4 | 783.6 | 21.15 | 0.0 | 10.0 | 14.29 | 19.3 | Au1rxx-base64 | 138.124.68.188 |
| 83.71 | hysteria2 | 283.3 | 781.5 | 21.22 | 0.0 | 10.0 | 14.29 | 19.3 | Au1rxx-base64 | 159.223.157.129 |
| 82.43 | trojan | 263.2 | 695.6 | 21.68 | 0.0 | 10.0 | 14.45 | 19.3 | Au1rxx-base64 | 153.75.250.171 |
| 82.42 | http | 293.2 | 769.1 | 20.99 | 0.0 | 10.0 | 14.73 | 19.7 | zhangkai | 156.146.59.33 |
| 82.11 | vless | 238.6 | 544.0 | 22.26 | 0.0 | 10.0 | 10.55 | 19.3 | Au1rxx-base64 | 216.227.161.95 |
| 81.36 | hysteria2 | 284.0 | 769.0 | 21.2 | 0.0 | 7.57 | 14.29 | 19.3 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.13 | shadowsocks | 225.2 | 591.1 | 22.57 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 198.98.53.130 |
| 80.45 | shadowsocks | 254.2 | 684.3 | 21.89 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 37.19.198.243 |
| 80.44 | shadowsocks | 254.8 | 685.2 | 21.88 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 37.19.198.236 |
| 80.41 | shadowsocks | 255.9 | 691.7 | 21.85 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 37.19.198.160 |
| 79.6 | shadowsocks | 291.2 | 793.5 | 21.04 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 37.19.198.244 |
| 79.58 | vless | 273.0 | 658.8 | 21.46 | 0.0 | 10.0 | 10.55 | 19.3 | Au1rxx-base64 | 88.218.44.4 |
| 77.88 | trojan | 303.9 | 653.5 | 20.74 | 0.0 | 10.0 | 14.45 | 19.3 | Au1rxx-base64 | 163.245.196.68 |
| 77.55 | shadowsocks | 283.3 | 664.2 | 21.22 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 156.146.38.169 |
| 77.25 | shadowsocks | 316.7 | 763.4 | 20.45 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 156.146.38.167 |
| 76.89 | shadowsocks | 274.9 | 636.4 | 21.41 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 156.146.38.168 |
| 76.89 | shadowsocks | 347.2 | 838.0 | 19.74 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 185.196.61.82 |
| 76.83 | vless | 250.6 | 654.2 | 21.98 | 0.0 | 10.0 | 10.55 | 19.3 | Au1rxx-base64 | 159.89.87.21 |
| 76.67 | hysteria2 | 354.3 | 684.5 | 19.58 | 0.0 | 10.0 | 14.29 | 19.3 | Au1rxx-base64 | 62.210.124.146 |
| 76.47 | shadowsocks | 404.6 | 1126.2 | 18.41 | 0.0 | 10.0 | 13.26 | 19.3 | Au1rxx-base64 | 68.168.222.210 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.945 | 401 | 1440 | prefer |
| zhangkai | 0.984 | 1.0 | 51 | 72 | prefer |
| Surfboard-tg-mixed | 0.651 | 0.577 | 26 | 5655 | observe |
| DeltaKronecker-all | 0.354 | 0.274 | 716 | 5788 | observe |
| tg-oneclickvpnkeys | 0.318 | 1.0 | 2 | 161 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5251 | observe |
| Epodonios-all | 0.255 | None | 0 | 6252 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7076 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4478 | observe |
| barry-far-vless | 0.255 | None | 0 | 4815 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5141 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 4655 | observe |
| mheidari-all | 0.25 | 0.157 | 51 | 20244 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 291 |
| speed | ClientOSError | - | 133 |
| geo | ClientOSError | - | 55 |
| cn-block | TimeoutError | - | 55 |
| speed | TimeoutError | - | 29 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 10 |
| 204 | TimeoutError | - | 9 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
