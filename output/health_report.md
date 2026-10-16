# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 07:02:11 |
| 运行耗时 | 347.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99718 |
| 去重后节点 | 27907 |
| TCP 可达 | 3000 |
| 真实可用 | 475 |
| Verified 输出 | 43 |
| Global 输出 | 300 |
| All 输出 | 27907 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| geo | 1.5 |
| tcp | 89.7 |
| probe | 106.6 |
| real_test | 96.9 |
| china_check | 30.5 |
| write_verified | 0.0 |
| generate | 14.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58857 |
| vmess | 16436 |
| shadowsocks | 11811 |
| trojan | 10389 |
| hysteria2 | 1210 |
| http | 740 |
| shadowsocksr | 168 |
| socks | 59 |
| anytls | 25 |
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
| 98.52 | hysteria2 | 215.2 | 2.0 | 22.8 | 14.92 | 10.0 | 14.06 | 17.74 | Au1rxx-base64 | 179.255.104.98 |
| 95.39 | shadowsocks | 210.6 | 4.0 | 22.9 | 14.85 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 149.22.95.183 |
| 90.94 | vless | 248.7 | 3.3 | 22.02 | 14.88 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 216.234.140.15 |
| 89.75 | vless | 360.1 | 3.2 | 19.44 | 14.88 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 51.81.203.63 |
| 89.19 | shadowsocks | 311.9 | 0.1 | 20.56 | 15.0 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.167 |
| 89.06 | shadowsocks | 319.3 | 0.2 | 20.39 | 14.99 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.170 |
| 88.26 | shadowsocks | 321.1 | 0.1 | 20.34 | 14.99 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.169 |
| 87.77 | vless | 275.4 | 2.3 | 21.4 | 14.92 | 6.02 | 8.69 | 17.74 | Au1rxx-base64 | 44.248.233.99 |
| 87.6 | vless | 244.6 | 3.0 | 22.12 | 14.89 | 6.84 | 8.69 | 17.74 | Au1rxx-base64 | 131.143.180.110 |
| 87.33 | shadowsocks | 380.7 | 3.3 | 18.97 | 14.88 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.168 |
| 87.21 | vless | 320.8 | 1.4 | 20.35 | 14.95 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 147.45.60.160 |
| 86.56 | http | 256.7 | 0.9 | 21.84 | 14.97 | 0.0 | 14.67 | 20.0 | ermaozi | 172.64.68.89 |
| 86.3 | shadowsocks | 269.4 | 1.5 | 21.54 | 14.94 | 9.87 | 13.9 | 17.74 | Au1rxx-base64 | 149.22.87.204 |
| 86.25 | http | 324.7 | 0.6 | 20.26 | 14.98 | 0.0 | 14.67 | 20.0 | ermaozi | 149.22.88.65 |
| 86.03 | http | 272.4 | 5.1 | 21.47 | 14.81 | 0.0 | 14.67 | 20.0 | ermaozi | fan.365747.xyz |
| 85.82 | shadowsocks | 280.6 | 1.7 | 21.28 | 14.94 | 9.89 | 13.9 | 17.74 | Au1rxx-base64 | 149.22.87.241 |
| 85.27 | shadowsocks | 335.9 | 3.0 | 20.0 | 14.89 | 9.86 | 13.9 | 17.74 | Au1rxx-base64 | 149.22.87.240 |
| 85.01 | http | 270.6 | 5.3 | 21.51 | 14.8 | 0.0 | 14.67 | 20.0 | ermaozi | 138.199.35.198 |
| 84.86 | http | 275.6 | 1.2 | 21.4 | 14.96 | 0.0 | 14.67 | 20.0 | ermaozi | 138.199.35.214 |
| 84.79 | http | 275.7 | 1.1 | 21.39 | 14.96 | 0.0 | 14.67 | 20.0 | ermaozi | 138.199.35.202 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.907 | 0.888 | 89 | 693 | prefer |
| Au1rxx-base64 | 0.904 | 0.826 | 448 | 1992 | prefer |
| mheidari-all | 0.495 | 0.421 | 19 | 23985 | observe |
| Surfboard-tg-mixed | 0.427 | 0.34 | 47 | 7054 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7651 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10060 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5573 | observe |
| barry-far-vless | 0.255 | None | 0 | 5882 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| tg-oneclickvpnkeys | 0.211 | 0.5 | 2 | 79 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 76 |
| geo | ClientOSError | - | 16 |
| speed | ClientOSError | - | 14 |
| 204 | ProxyError | - | 6 |
| speed | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 5 |
| 204 | ClientOSError | - | 4 |
| speed | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| 204 | TimeoutError | - | 2 |
| cn-block | TimeoutError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 34 | 43 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
