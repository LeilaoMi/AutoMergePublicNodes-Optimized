# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-18 11:27:50 |
| 运行耗时 | 328.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98405 |
| 去重后节点 | 27711 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 143 |
| Global 输出 | 300 |
| All 输出 | 27711 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| geo | 1.5 |
| tcp | 86.2 |
| probe | 95.2 |
| real_test | 100.3 |
| china_check | 23.2 |
| write_verified | 0.1 |
| generate | 13.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57295 |
| vmess | 16483 |
| shadowsocks | 11980 |
| trojan | 9945 |
| hysteria2 | 1651 |
| http | 749 |
| shadowsocksr | 170 |
| socks | 85 |
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
| 94.24 | vless | 207.9 | 1.8 | 22.96 | 14.93 | 8.19 | 9.2 | 18.96 | Au1rxx-base64 | 154.29.145.196 |
| 93.16 | vless | 200.1 | 29.0 | 23.14 | 13.91 | 9.95 | 9.2 | 18.96 | Au1rxx-base64 | 67.209.184.133 |
| 92.72 | vless | 203.5 | 0.3 | 23.07 | 14.99 | 7.5 | 9.2 | 18.96 | Au1rxx-base64 | 47.251.25.74 |
| 91.8 | vless | 263.1 | 56.3 | 21.69 | 12.89 | 10.0 | 9.2 | 18.96 | Au1rxx-base64 | 154.40.55.185 |
| 91.69 | shadowsocks | 298.6 | 19.5 | 20.87 | 14.27 | 10.0 | 14.4 | 18.96 | Au1rxx-base64 | 156.146.38.170 |
| 91.55 | vless | 293.8 | 0.9 | 20.98 | 14.97 | 10.0 | 9.2 | 18.96 | Au1rxx-base64 | 95.111.212.241 |
| 91.33 | vless | 194.5 | 3.0 | 23.28 | 14.89 | 10.0 | 9.2 | 18.96 | Au1rxx-base64 | 23.95.222.127 |
| 91.19 | shadowsocks | 314.1 | 1.9 | 20.51 | 14.93 | 6.89 | 14.4 | 18.96 | Au1rxx-base64 | 103.11.76.248 |
| 91.14 | vless | 417.7 | 3.4 | 18.11 | 14.87 | 10.0 | 9.2 | 18.96 | Au1rxx-base64 | 51.81.203.63 |
| 91.04 | vless | 216.1 | 2.4 | 22.78 | 14.91 | 9.87 | 9.2 | 18.96 | Au1rxx-base64 | 195.123.240.65 |
| 90.92 | hysteria2 | 291.2 | 18.4 | 21.04 | 14.31 | 10.0 | 13.24 | 18.96 | Au1rxx-base64 | 66.94.121.46 |
| 89.69 | http | 192.9 | 0.4 | 23.31 | 14.99 | 0.0 | 14.11 | 19.78 | ermaozi | 167.88.60.242 |
| 89.62 | http | 194.1 | 1.4 | 23.28 | 14.95 | 0.0 | 14.11 | 19.78 | ermaozi | voteshirleysew.club |
| 89.62 | hysteria2 | 343.4 | 0.2 | 19.83 | 14.99 | 7.33 | 13.24 | 18.96 | Au1rxx-base64 | 129.213.91.185 |
| 89.0 | http | 200.0 | 1.1 | 23.15 | 14.96 | 0.0 | 14.11 | 19.78 | ermaozi | 138.199.35.215 |
| 88.91 | vless | 210.5 | 0.7 | 22.9 | 14.97 | 2.88 | 9.2 | 18.96 | Au1rxx-base64 | 154.12.38.202 |
| 88.84 | http | 208.0 | 0.2 | 22.96 | 14.99 | 0.0 | 14.11 | 19.78 | ermaozi | 138.199.35.202 |
| 88.76 | http | 231.4 | 1.3 | 22.42 | 14.95 | 0.0 | 14.11 | 19.78 | ermaozi | fan.365747.xyz |
| 88.74 | http | 210.4 | 1.5 | 22.91 | 14.94 | 0.0 | 14.11 | 19.78 | ermaozi | 138.199.35.199 |
| 88.73 | http | 210.3 | 2.0 | 22.91 | 14.93 | 0.0 | 14.11 | 19.78 | ermaozi | 138.199.35.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.98 | 0.961 | 102 | 710 | prefer |
| Au1rxx-base64 | 0.879 | 0.804 | 378 | 1920 | prefer |
| Surfboard-tg-mixed | 0.58 | 0.5 | 52 | 7030 | observe |
| DeltaKronecker-all | 0.478 | 0.396 | 101 | 4750 | observe |
| mheidari-all | 0.418 | 0.5 | 10 | 23769 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4983 | observe |
| Epodonios-all | 0.255 | None | 0 | 7561 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9785 | observe |
| barry-far-vless | 0.255 | None | 0 | 5830 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4246 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.252 | None | 0 | 1920 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 78 |
| geo | ClientOSError | - | 30 |
| 204 | TimeoutError | - | 16 |
| 204 | ProxyError | - | 14 |
| speed | ClientOSError | - | 10 |
| cn-block | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 5 |
| speed | TimeoutError | - | 3 |
| geo | TimeoutError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 130 | 143 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
