# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-12 20:11:41 |
| 运行耗时 | 306.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 83498 |
| 去重后节点 | 26911 |
| TCP 可达 | 3000 |
| 真实可用 | 383 |
| Verified 输出 | 61 |
| Global 输出 | 300 |
| All 输出 | 26911 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.5 |
| tcp | 81.3 |
| probe | 98.3 |
| real_test | 71.4 |
| china_check | 32.4 |
| write_verified | 0.0 |
| generate | 14.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50701 |
| vmess | 14593 |
| shadowsocks | 9455 |
| trojan | 6755 |
| hysteria2 | 1476 |
| http | 252 |
| shadowsocksr | 143 |
| socks | 54 |
| hysteria | 34 |
| tuic | 19 |
| anytls | 16 |

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
| 91.81 | trojan | 256.8 | 0.5 | 21.83 | 14.98 | 10.0 | 11.89 | 17.42 | Au1rxx-base64 | 167.88.61.175 |
| 91.14 | trojan | 259.6 | 1.8 | 21.77 | 14.93 | 8.76 | 11.89 | 17.42 | Au1rxx-base64 | 167.88.61.20 |
| 89.76 | shadowsocks | 275.3 | 0.7 | 21.41 | 14.97 | 10.0 | 13.03 | 17.42 | Au1rxx-base64 | 95.215.201.18 |
| 89.52 | trojan | 341.3 | 3.0 | 19.88 | 14.89 | 8.76 | 11.89 | 17.42 | Au1rxx-base64 | 167.88.61.198 |
| 89.3 | trojan | 294.1 | 1.0 | 20.97 | 14.96 | 10.0 | 11.89 | 17.42 | Au1rxx-base64 | 66.163.112.121 |
| 88.41 | trojan | 235.4 | 1.2 | 22.33 | 14.95 | 5.11 | 11.89 | 17.42 | Au1rxx-base64 | 167.88.61.85 |
| 87.89 | trojan | 295.1 | 4.4 | 20.95 | 14.83 | 8.6 | 11.89 | 17.42 | Au1rxx-base64 | 66.163.112.242 |
| 87.67 | http | 308.5 | 0.0 | 20.64 | 15.0 | 0.0 | 14.59 | 19.94 | ermaozi | 172.64.69.89 |
| 87.63 | shadowsocks | 316.6 | 1.3 | 20.45 | 14.95 | 10.0 | 13.03 | 17.42 | Au1rxx-base64 | 156.146.38.170 |
| 87.31 | shadowsocks | 303.6 | 2.0 | 20.75 | 14.92 | 10.0 | 13.03 | 17.42 | Au1rxx-base64 | 156.146.38.167 |
| 87.02 | http | 250.9 | 2.8 | 21.97 | 14.89 | 0.0 | 14.59 | 19.94 | ermaozi | 167.88.60.242 |
| 86.7 | trojan | 294.6 | 5.2 | 20.96 | 14.8 | 7.42 | 11.89 | 17.42 | Au1rxx-base64 | 66.163.112.13 |
| 86.42 | shadowsocks | 322.9 | 2.8 | 20.3 | 14.89 | 10.0 | 13.03 | 17.42 | Au1rxx-base64 | 156.146.38.168 |
| 85.71 | trojan | 297.0 | 1.6 | 20.9 | 14.94 | 7.42 | 11.89 | 17.42 | Au1rxx-base64 | 66.163.112.76 |
| 85.23 | shadowsocks | 361.1 | 1.5 | 19.42 | 14.94 | 10.0 | 13.03 | 17.42 | Au1rxx-base64 | 45.86.51.18 |
| 85.14 | hysteria2 | 339.5 | 44.5 | 19.92 | 13.33 | 3.45 | 14.06 | 17.42 | Au1rxx-base64 | 66.94.121.46 |
| 84.99 | shadowsocks | 365.8 | 5.0 | 19.31 | 14.81 | 10.0 | 13.03 | 17.42 | Au1rxx-base64 | 185.230.230.18 |
| 84.63 | trojan | 295.0 | 0.6 | 20.95 | 14.98 | 5.29 | 11.89 | 17.42 | Au1rxx-base64 | 66.163.112.142 |
| 84.19 | vless | 273.1 | 9.4 | 21.46 | 14.65 | 6.92 | 8.7 | 17.42 | Au1rxx-base64 | 45.63.53.81 |
| 84.12 | trojan | 421.0 | 8.1 | 18.03 | 14.7 | 10.0 | 11.89 | 17.42 | Au1rxx-base64 | 66.23.203.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.954 | 0.946 | 56 | 579 | prefer |
| Au1rxx-base64 | 0.876 | 0.81 | 168 | 1751 | prefer |
| Surfboard-tg-mixed | 0.799 | 0.721 | 215 | 8770 | prefer |
| mheidari-all | 0.747 | 0.673 | 55 | 14228 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4998 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2737 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11515 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6332 | observe |
| barry-far-vless | 0.255 | None | 0 | 6555 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4618 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 33 |
| test_one_timeout | 15.0s | - | 33 |
| speed | ClientOSError | - | 19 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 79 | 61 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
