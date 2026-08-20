# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-20 07:00:58 |
| 运行耗时 | 394.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 93905 |
| 去重后节点 | 25132 |
| TCP 可达 | 3000 |
| 真实可用 | 1247 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25132 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.7 |
| geo | 0.9 |
| tcp | 39.2 |
| probe | 83.2 |
| real_test | 220.8 |
| generate | 42.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52555 |
| trojan | 18402 |
| shadowsocks | 10546 |
| vmess | 10174 |
| hysteria2 | 1675 |
| shadowsocksr | 197 |
| http | 165 |
| socks | 131 |
| anytls | 33 |
| hysteria | 15 |
| tuic | 12 |

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
| 85.13 | trojan | 208.6 | 504.6 | 22.95 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 35.160.249.189 |
| 85.06 | hysteria2 | 219.6 | 215.0 | 22.69 | 6.94 | 9.99 | 14.21 | 20.0 | Au1rxx-base64 | 45.32.252.144 |
| 85.02 | trojan | 213.2 | 517.7 | 22.84 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 84.94 | trojan | 216.9 | 529.1 | 22.76 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 35.88.120.18 |
| 84.9 | trojan | 218.6 | 528.0 | 22.72 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 54.213.46.211 |
| 84.76 | trojan | 224.4 | 546.9 | 22.58 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 35.91.138.234 |
| 84.33 | trojan | 243.0 | 605.3 | 22.15 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 35.92.245.6 |
| 83.93 | trojan | 217.4 | 530.4 | 22.75 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 34.221.30.108 |
| 83.63 | trojan | 273.2 | 695.8 | 21.45 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 100.22.163.167 |
| 83.6 | trojan | 274.5 | 693.1 | 21.42 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 83.52 | shadowsocks | 214.6 | 575.2 | 22.81 | 0.0 | 10.0 | 14.71 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 82.42 | trojan | 325.8 | 847.2 | 20.24 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 81.67 | shadowsocks | 197.5 | 514.4 | 23.21 | 0.0 | 10.0 | 14.71 | 20.0 | Au1rxx-base64 | 94.72.127.58 |
| 80.9 | shadowsocks | 198.4 | 508.7 | 23.19 | 0.0 | 10.0 | 14.71 | 20.0 | Au1rxx-base64 | 62.146.171.57 |
| 80.58 | shadowsocks | 212.2 | 534.6 | 22.87 | 0.0 | 10.0 | 14.71 | 20.0 | Au1rxx-base64 | 154.12.242.150 |
| 80.47 | trojan | 266.9 | 675.3 | 21.6 | 0.0 | 10.0 | 14.68 | 20.0 | Au1rxx-base64 | 34.223.2.163 |
| 80.43 | shadowsocks | 207.6 | 484.6 | 22.97 | 0.0 | 10.0 | 14.71 | 20.0 | Au1rxx-base64 | 209.38.142.23 |
| 80.36 | trojan | 218.4 | 526.8 | 22.72 | 0.0 | 5.46 | 14.68 | 20.0 | Au1rxx-base64 | humorous-hawk.rooster465.autos |
| 79.6 | trojan | 253.1 | 639.4 | 21.92 | 0.0 | 5.5 | 14.68 | 20.0 | Au1rxx-base64 | communal-squid.rooster465.autos |
| 79.02 | trojan | 276.0 | 703.3 | 21.39 | 0.0 | 5.45 | 14.68 | 20.0 | Au1rxx-base64 | sure-bengal.rooster465.autos |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.975 | 712 | 1789 | prefer |
| zhangkai | 0.997 | 1.0 | 112 | 144 | prefer |
| mheidari-all | 0.962 | 0.885 | 278 | 21143 | prefer |
| Surfboard-tg-mixed | 0.829 | 0.751 | 257 | 6418 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5974 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4958 | observe |
| Epodonios-all | 0.255 | None | 0 | 7111 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7230 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5062 | observe |
| barry-far-vless | 0.255 | None | 0 | 5404 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4586 | observe |
| nscl5-all | 0.255 | None | 0 | 2418 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1789 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 47 |
| geo | ClientOSError | - | 23 |
| speed | TimeoutError | - | 20 |
| cn-block | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 10 |
| 204 | TimeoutError | - | 7 |
| speed | ClientOSError | - | 6 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
