# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-18 02:58:39 |
| 运行耗时 | 311.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 98 |
| 原始节点 | 82736 |
| 去重后节点 | 25440 |
| TCP 可达 | 3000 |
| 真实可用 | 756 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25440 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.3 |
| tcp | 34.7 |
| probe | 63.6 |
| real_test | 178.8 |
| generate | 26.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47449 |
| trojan | 13666 |
| vmess | 10979 |
| shadowsocks | 10087 |
| hysteria2 | 311 |
| shadowsocksr | 123 |
| http | 54 |
| socks | 53 |
| hysteria | 9 |
| tuic | 3 |
| anytls | 2 |

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
| 78.49 | shadowsocks | 197.3 | 495.9 | 23.21 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 173.244.56.9 |
| 78.47 | shadowsocks | 198.1 | 500.5 | 23.19 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 173.244.56.6 |
| 77.98 | shadowsocks | 197.6 | 473.9 | 23.2 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 108.181.118.10 |
| 77.61 | shadowsocks | 213.9 | 535.0 | 22.83 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 108.181.0.177 |
| 73.95 | shadowsocks | 278.4 | 640.0 | 21.33 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 156.146.38.170 |
| 73.94 | shadowsocks | 315.1 | 251.9 | 20.48 | 5.55 | 9.88 | 11.76 | 17.52 | Au1rxx-base64 | 149.22.87.241 |
| 73.83 | shadowsocks | 182.6 | 484.2 | 23.55 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 216.105.168.18 |
| 73.18 | shadowsocks | 293.1 | 685.8 | 20.99 | 0.0 | 10.0 | 11.76 | 17.52 | Au1rxx-base64 | 156.146.38.167 |
| 72.68 | trojan | 340.9 | 343.4 | 19.89 | 2.12 | 9.89 | 13.26 | 17.52 | Au1rxx-base64 | 13.112.180.140 |
| 72.61 | trojan | 343.3 | 343.3 | 19.83 | 2.13 | 9.89 | 13.26 | 17.52 | Au1rxx-base64 | 52.195.207.214 |
| 72.6 | trojan | 351.1 | 337.5 | 19.65 | 2.34 | 9.86 | 13.26 | 17.52 | Au1rxx-base64 | 13.112.1.163 |
| 72.45 | trojan | 347.1 | 341.5 | 19.74 | 2.19 | 9.83 | 13.26 | 17.52 | Au1rxx-base64 | 13.115.229.63 |
| 72.4 | trojan | 346.3 | 346.1 | 19.76 | 2.02 | 9.86 | 13.26 | 17.52 | Au1rxx-base64 | 18.176.53.202 |
| 72.28 | trojan | 346.3 | 348.4 | 19.76 | 1.93 | 9.87 | 13.26 | 17.52 | Au1rxx-base64 | 13.115.249.38 |
| 72.25 | trojan | 346.3 | 349.9 | 19.76 | 1.88 | 9.86 | 13.26 | 17.52 | Au1rxx-base64 | 18.183.224.87 |
| 72.24 | trojan | 344.1 | 350.7 | 19.81 | 1.85 | 9.88 | 13.26 | 17.52 | Au1rxx-base64 | 35.72.9.75 |
| 72.22 | trojan | 344.7 | 352.0 | 19.8 | 1.8 | 9.87 | 13.26 | 17.52 | Au1rxx-base64 | 18.177.136.64 |
| 72.15 | trojan | 345.9 | 345.0 | 19.77 | 2.06 | 9.87 | 13.26 | 17.52 | Au1rxx-base64 | 13.115.80.163 |
| 72.03 | trojan | 343.9 | 343.2 | 19.82 | 2.13 | 9.82 | 13.26 | 17.52 | Au1rxx-base64 | 43.207.117.135 |
| 71.91 | trojan | 344.0 | 341.4 | 19.81 | 2.2 | 9.29 | 13.26 | 17.52 | Au1rxx-base64 | arriving-koala.rooster465.autos |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| nscl5-all | 0.954 | 0.947 | 19 | 1976 | prefer |
| Au1rxx-base64 | 0.886 | 0.886 | 123 | 149 | prefer |
| mheidari-all | 0.757 | 0.678 | 534 | 16573 | prefer |
| Surfboard-tg-mixed | 0.676 | 0.596 | 337 | 5500 | observe |
| xiaoji235-airport-v2ray-all | 0.547 | 0.778 | 9 | 4321 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4428 | observe |
| DeltaKronecker-all | 0.255 | 0.17 | 135 | 8967 | observe |
| Epodonios-all | 0.255 | None | 0 | 6707 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6869 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4227 | observe |
| barry-far-vless | 0.255 | None | 0 | 4834 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5263 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 224 |
| geo | TimeoutError | - | 97 |
| geo | ClientOSError | - | 39 |
| speed | TimeoutError | - | 37 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 12 |
| 204 | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
