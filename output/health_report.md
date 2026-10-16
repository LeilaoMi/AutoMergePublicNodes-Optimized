# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 21:26:37 |
| 运行耗时 | 275.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99390 |
| 去重后节点 | 27723 |
| TCP 可达 | 3000 |
| 真实可用 | 453 |
| Verified 输出 | 91 |
| Global 输出 | 300 |
| All 输出 | 27723 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.5 |
| tcp | 89.1 |
| probe | 69.1 |
| real_test | 83.6 |
| china_check | 19.1 |
| write_verified | 0.0 |
| generate | 8.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58368 |
| vmess | 16700 |
| shadowsocks | 12081 |
| trojan | 10024 |
| hysteria2 | 1310 |
| http | 631 |
| shadowsocksr | 166 |
| socks | 58 |
| anytls | 29 |
| hysteria | 17 |
| tuic | 6 |

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
| 93.17 | shadowsocks | 216.4 | 1.5 | 22.77 | 14.94 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 173.244.56.6 |
| 92.18 | shadowsocks | 261.1 | 0.1 | 21.73 | 14.99 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 156.146.38.169 |
| 92.15 | shadowsocks | 262.1 | 0.4 | 21.71 | 14.98 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 156.146.38.170 |
| 91.99 | vless | 208.9 | 5.5 | 22.94 | 14.79 | 7.72 | 9.88 | 16.66 | Au1rxx-base64 | 154.29.159.211 |
| 91.71 | shadowsocks | 265.1 | 1.9 | 21.64 | 14.93 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 156.146.38.168 |
| 91.27 | shadowsocks | 274.9 | 0.5 | 21.42 | 14.98 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 156.146.38.167 |
| 91.12 | shadowsocks | 271.0 | 0.5 | 21.51 | 14.98 | 9.17 | 12.8 | 16.66 | Au1rxx-base64 | 173.244.56.9 |
| 90.93 | shadowsocks | 289.2 | 3.0 | 21.08 | 14.89 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 103.11.76.248 |
| 87.95 | shadowsocks | 293.8 | 1.0 | 20.98 | 14.96 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 149.22.95.183 |
| 87.69 | hysteria2 | 250.8 | 3.7 | 21.97 | 14.86 | 2.85 | 12.35 | 16.66 | Au1rxx-base64 | 66.94.121.46 |
| 87.48 | vless | 410.7 | 0.4 | 18.27 | 14.99 | 10.0 | 9.88 | 16.66 | Au1rxx-base64 | 51.81.203.63 |
| 86.95 | vless | 284.1 | 0.2 | 21.2 | 14.99 | 10.0 | 9.88 | 16.66 | Au1rxx-base64 | 147.45.60.160 |
| 86.65 | vless | 345.4 | 0.6 | 19.78 | 14.98 | 10.0 | 9.88 | 16.66 | Au1rxx-base64 | 95.111.212.241 |
| 85.33 | http | 290.0 | 1.6 | 21.06 | 14.94 | 0.0 | 14.51 | 19.82 | ermaozi | 138.199.35.198 |
| 85.08 | shadowsocks | 361.7 | 0.6 | 19.4 | 14.98 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 37.19.198.244 |
| 85.07 | vless | 225.1 | 22.6 | 22.57 | 14.15 | 10.0 | 9.88 | 16.66 | Au1rxx-base64 | 154.40.55.185 |
| 85.05 | shadowsocks | 363.2 | 2.0 | 19.37 | 14.93 | 10.0 | 12.8 | 16.66 | Au1rxx-base64 | 37.19.198.160 |
| 84.49 | vless | 346.7 | 1.7 | 19.75 | 14.93 | 9.83 | 9.88 | 16.66 | Au1rxx-base64 | 23.95.222.127 |
| 84.22 | vless | 220.0 | 0.1 | 22.68 | 15.0 | 0.0 | 9.88 | 16.66 | Au1rxx-base64 | 47.251.108.158 |
| 84.2 | trojan | 338.0 | 0.7 | 19.95 | 14.97 | 9.61 | 13.03 | 16.66 | Au1rxx-base64 | 108.61.186.37 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.976 | 0.967 | 60 | 618 | prefer |
| Au1rxx-base64 | 0.892 | 0.814 | 451 | 1995 | prefer |
| mheidari-all | 0.799 | 0.733 | 30 | 23910 | prefer |
| Surfboard-tg-mixed | 0.349 | 0.667 | 3 | 7222 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Surfboard-tg-vless | 0.259 | 0.333 | 3 | 5648 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1995 | observe |
| Epodonios-all | 0.255 | None | 0 | 7598 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10078 | observe |
| barry-far-vless | 0.255 | None | 0 | 5818 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4255 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 53 |
| speed | ClientOSError | - | 13 |
| 204 | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 3 |
| geo | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 81 | 91 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
