# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-24 11:20:26 |
| 运行耗时 | 293.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 92774 |
| 去重后节点 | 24601 |
| TCP 可达 | 3000 |
| 真实可用 | 398 |
| Verified 输出 | 115 |
| Global 输出 | 300 |
| All 输出 | 24601 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.3 |
| geo | 1.5 |
| tcp | 75.1 |
| probe | 92.7 |
| real_test | 80.4 |
| china_check | 21.3 |
| write_verified | 0.1 |
| generate | 12.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56262 |
| vmess | 16796 |
| shadowsocks | 11926 |
| trojan | 5899 |
| hysteria2 | 1341 |
| http | 287 |
| shadowsocksr | 165 |
| socks | 51 |
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
| 95.39 | hysteria2 | 220.7 | 2.7 | 22.67 | 14.9 | 5.73 | 13.93 | 19.16 | Au1rxx-base64 | 66.94.121.46 |
| 94.95 | shadowsocks | 245.8 | 1.1 | 22.09 | 14.96 | 9.38 | 13.62 | 19.16 | Au1rxx-base64 | 149.22.95.183 |
| 94.69 | vless | 219.9 | 4.1 | 22.69 | 14.85 | 9.24 | 8.75 | 19.16 | Au1rxx-base64 | 195.123.240.65 |
| 94.42 | vless | 238.3 | 3.2 | 22.26 | 14.88 | 9.37 | 8.75 | 19.16 | Au1rxx-base64 | 44.248.233.99 |
| 93.24 | vless | 171.2 | 4.1 | 23.81 | 14.85 | 6.67 | 8.75 | 19.16 | Au1rxx-base64 | 47.251.108.158 |
| 92.67 | vless | 314.9 | 3.3 | 20.49 | 14.88 | 9.39 | 8.75 | 19.16 | Au1rxx-base64 | 51.81.203.63 |
| 90.9 | shadowsocks | 259.9 | 0.0 | 21.76 | 15.0 | 9.43 | 13.62 | 19.16 | Au1rxx-base64 | 173.244.56.9 |
| 90.79 | shadowsocks | 291.3 | 2.2 | 21.04 | 14.92 | 9.16 | 13.62 | 19.16 | Au1rxx-base64 | 156.146.38.169 |
| 90.04 | http | 191.9 | 2.5 | 23.34 | 14.91 | 0.0 | 14.29 | 20.0 | ermaozi | 172.64.68.89 |
| 89.78 | vless | 201.1 | 1.8 | 23.12 | 14.93 | 5.32 | 8.75 | 19.16 | Au1rxx-base64 | 172.236.227.60 |
| 89.54 | http | 193.3 | 1.4 | 23.3 | 14.95 | 0.0 | 14.29 | 20.0 | ermaozi | 138.199.35.210 |
| 89.47 | http | 198.0 | 0.2 | 23.19 | 14.99 | 0.0 | 14.29 | 20.0 | ermaozi | 138.199.35.214 |
| 89.05 | http | 237.7 | 0.4 | 22.28 | 14.98 | 0.0 | 14.29 | 20.0 | ermaozi | 172.64.69.89 |
| 89.02 | http | 212.4 | 3.4 | 22.86 | 14.87 | 0.0 | 14.29 | 20.0 | ermaozi | 138.199.35.195 |
| 88.05 | trojan | 405.3 | 2.2 | 18.4 | 14.92 | 8.98 | 13.38 | 19.16 | Au1rxx-base64 | 66.23.203.21 |
| 87.58 | trojan | 238.2 | 1.2 | 22.26 | 14.95 | 0.33 | 13.38 | 19.16 | Au1rxx-base64 | 216.106.186.32 |
| 87.45 | shadowsocks | 349.8 | 1.6 | 19.68 | 14.94 | 8.98 | 13.62 | 19.16 | Au1rxx-base64 | 185.215.132.18 |
| 87.32 | trojan | 235.8 | 1.2 | 22.32 | 14.96 | 0.0 | 13.38 | 19.16 | Au1rxx-base64 | resources.findlocaljobnetworkandbuildcommunityconnections.com |
| 87.04 | http | 211.8 | 3.1 | 22.87 | 14.88 | 0.0 | 14.29 | 20.0 | ermaozi | 138.199.35.198 |
| 86.82 | vless | 266.6 | 1.7 | 21.61 | 14.94 | 6.39 | 8.75 | 19.16 | Au1rxx-base64 | 173.249.210.179 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.987 | 0.975 | 79 | 608 | prefer |
| Au1rxx-base64 | 0.89 | 0.829 | 252 | 1579 | prefer |
| mheidari-all | 0.88 | 0.814 | 43 | 23868 | prefer |
| Surfboard-tg-mixed | 0.74 | 0.663 | 104 | 7180 | prefer |
| tg-oneclickvpnkeys | 0.444 | 1.0 | 5 | 113 | observe |
| 10ium-HighSpeed | 0.345 | 1.0 | 2 | 839 | observe |
| roosterkid-openproxylist-v2ray | 0.275 | 0.667 | 3 | 150 | observe |
| Surfboard-tg-vless | 0.272 | 0.286 | 7 | 5436 | observe |
| chromego_merge | 0.264 | 1.0 | 1 | 236 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 55 | observe |
| Epodonios-all | 0.255 | None | 0 | 7652 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| barry-far-vless | 0.255 | None | 0 | 5737 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4150 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 50 |
| geo | ClientOSError | - | 14 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| geo | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 161 | 115 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
