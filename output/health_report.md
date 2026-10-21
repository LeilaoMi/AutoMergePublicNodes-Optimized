# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-21 05:05:37 |
| 运行耗时 | 315.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 95380 |
| 去重后节点 | 26617 |
| TCP 可达 | 3000 |
| 真实可用 | 445 |
| Verified 输出 | 118 |
| Global 输出 | 300 |
| All 输出 | 26617 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.6 |
| tcp | 83.2 |
| probe | 91.7 |
| real_test | 88.6 |
| china_check | 30.9 |
| write_verified | 0.1 |
| generate | 12.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56815 |
| vmess | 16881 |
| shadowsocks | 11908 |
| trojan | 8111 |
| hysteria2 | 1218 |
| http | 171 |
| shadowsocksr | 164 |
| socks | 65 |
| anytls | 24 |
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
| 94.49 | shadowsocks | 248.0 | 4.5 | 22.04 | 14.83 | 8.88 | 14.32 | 18.42 | Au1rxx-base64 | 156.146.38.168 |
| 94.31 | shadowsocks | 238.5 | 0.9 | 22.26 | 14.97 | 8.34 | 14.32 | 18.42 | Au1rxx-base64 | 156.146.38.167 |
| 93.39 | shadowsocks | 278.5 | 0.6 | 21.33 | 14.98 | 8.34 | 14.32 | 18.42 | Au1rxx-base64 | 156.146.38.170 |
| 92.19 | vless | 239.0 | 2.5 | 22.25 | 14.91 | 6.25 | 11.76 | 18.42 | Au1rxx-base64 | 45.32.69.110 |
| 91.74 | vless | 245.0 | 6.9 | 22.11 | 14.74 | 6.25 | 11.76 | 18.42 | Au1rxx-base64 | 45.63.53.81 |
| 91.19 | hysteria2 | 292.7 | 0.3 | 21.0 | 14.99 | 4.35 | 13.93 | 18.42 | Au1rxx-base64 | 129.213.91.185 |
| 91.06 | vless | 241.6 | 0.6 | 22.19 | 14.98 | 5.3 | 11.76 | 18.42 | Au1rxx-base64 | 144.202.126.147 |
| 90.42 | trojan | 344.6 | 6.2 | 19.8 | 14.77 | 7.57 | 12.86 | 18.42 | Au1rxx-base64 | 66.23.203.21 |
| 89.61 | shadowsocks | 277.7 | 1.2 | 21.35 | 14.95 | 8.12 | 14.32 | 18.42 | Au1rxx-base64 | 173.244.56.9 |
| 88.61 | shadowsocks | 329.4 | 1.8 | 20.15 | 14.93 | 8.66 | 14.32 | 18.42 | Au1rxx-base64 | 173.244.56.6 |
| 88.41 | vless | 291.3 | 2.2 | 21.04 | 14.92 | 6.12 | 11.76 | 18.42 | Au1rxx-base64 | 154.29.145.196 |
| 87.94 | shadowsocks | 338.6 | 1.0 | 19.94 | 14.96 | 7.81 | 14.32 | 18.42 | Au1rxx-base64 | 37.19.198.244 |
| 87.66 | shadowsocks | 327.1 | 9.4 | 20.21 | 14.65 | 8.49 | 14.32 | 18.42 | Au1rxx-base64 | 149.22.95.183 |
| 87.19 | vless | 441.5 | 5.5 | 17.56 | 14.79 | 7.18 | 11.76 | 18.42 | Au1rxx-base64 | 51.81.203.63 |
| 86.74 | hysteria2 | 437.7 | 12.3 | 17.65 | 14.54 | 7.16 | 13.93 | 18.42 | Au1rxx-base64 | 66.94.121.46 |
| 86.15 | shadowsocks | 365.4 | 4.2 | 19.32 | 14.84 | 8.11 | 14.32 | 18.42 | Au1rxx-base64 | 103.11.76.248 |
| 85.53 | vless | 360.0 | 2.2 | 19.44 | 14.92 | 5.28 | 11.76 | 18.42 | Au1rxx-base64 | 154.12.38.202 |
| 84.77 | shadowsocks | 373.6 | 0.1 | 19.13 | 15.0 | 7.87 | 14.32 | 18.42 | Au1rxx-base64 | 95.215.201.18 |
| 84.74 | vless | 238.8 | 1.1 | 22.25 | 14.96 | 0.0 | 11.76 | 18.68 | mheidari-all | 47.251.108.158 |
| 84.63 | vless | 278.7 | 0.9 | 21.33 | 14.97 | 5.38 | 11.76 | 18.42 | Au1rxx-base64 | 15.204.97.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.959 | 0.952 | 63 | 516 | prefer |
| zhangkai | 0.932 | 0.963 | 27 | 31 | prefer |
| Au1rxx-base64 | 0.922 | 0.866 | 277 | 1451 | prefer |
| Surfboard-tg-mixed | 0.835 | 1.0 | 14 | 7115 | prefer |
| mheidari-all | 0.575 | 0.495 | 198 | 23653 | observe |
| SoliSpirit-all | 0.391 | 1.0 | 2 | 10017 | observe |
| roosterkid-openproxylist-v2ray | 0.372 | 0.8 | 5 | 150 | observe |
| ermaozi | 0.314 | 1.0 | 2 | 76 | observe |
| DeltaKronecker-all | 0.291 | 0.25 | 12 | 3519 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| tg-oneclickvpnkeys | 0.271 | 0.667 | 3 | 74 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4967 | observe |
| Epodonios-all | 0.255 | None | 0 | 7598 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5552 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 102 |
| geo | ClientOSError | - | 21 |
| speed | ClientOSError | - | 18 |
| 204 | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | TimeoutError | - | 1 |
| 204 | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 94 | 118 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
