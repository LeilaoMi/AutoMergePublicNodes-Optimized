# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-24 22:40:12 |
| 运行耗时 | 262.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 78228 |
| 去重后节点 | 27398 |
| TCP 可达 | 3000 |
| 真实可用 | 363 |
| Verified 输出 | 86 |
| Global 输出 | 300 |
| All 输出 | 27398 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.5 |
| tcp | 81.3 |
| probe | 82.8 |
| real_test | 53.8 |
| china_check | 26.1 |
| write_verified | 0.0 |
| generate | 11.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46594 |
| vmess | 14962 |
| shadowsocks | 9158 |
| trojan | 5474 |
| hysteria2 | 1623 |
| shadowsocksr | 146 |
| http | 105 |
| socks | 86 |
| anytls | 45 |
| hysteria | 23 |
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
| 93.48 | trojan | 191.6 | 7.3 | 23.34 | 14.73 | 10.0 | 11.25 | 16.66 | Au1rxx-base64 | 167.88.61.175 |
| 92.92 | shadowsocks | 231.7 | 3.6 | 22.42 | 14.87 | 10.0 | 12.97 | 16.66 | Au1rxx-base64 | 149.22.95.183 |
| 92.91 | shadowsocks | 237.2 | 0.2 | 22.29 | 14.99 | 10.0 | 12.97 | 16.66 | Au1rxx-base64 | 173.244.56.6 |
| 92.69 | shadowsocks | 230.3 | 0.6 | 22.45 | 14.98 | 10.0 | 12.97 | 16.66 | Au1rxx-base64 | 173.244.56.9 |
| 92.43 | shadowsocks | 231.8 | 2.9 | 22.41 | 14.89 | 10.0 | 12.97 | 16.66 | Au1rxx-base64 | 95.215.201.18 |
| 91.92 | trojan | 172.5 | 0.1 | 23.78 | 15.0 | 9.73 | 11.25 | 16.66 | Au1rxx-base64 | 167.88.61.198 |
| 91.78 | vless | 217.7 | 0.5 | 22.74 | 14.98 | 7.96 | 9.44 | 16.66 | Au1rxx-base64 | 45.63.53.81 |
| 89.12 | http | 204.9 | 11.9 | 23.03 | 14.55 | 0.0 | 14.38 | 19.66 | ermaozi | 172.64.68.89 |
| 87.69 | shadowsocks | 303.7 | 1.3 | 20.75 | 14.95 | 10.0 | 12.97 | 16.66 | Au1rxx-base64 | 156.146.38.170 |
| 87.43 | shadowsocks | 339.3 | 1.0 | 19.92 | 14.96 | 10.0 | 12.97 | 16.66 | Au1rxx-base64 | 156.146.38.168 |
| 87.4 | trojan | 230.9 | 2.4 | 22.43 | 14.91 | 6.65 | 11.25 | 16.66 | Au1rxx-base64 | 167.88.61.85 |
| 87.04 | hysteria2 | 212.2 | 20.1 | 22.87 | 14.25 | 0.0 | 13.5 | 18.52 | mheidari-all | 172.87.24.53 |
| 86.17 | hysteria2 | 217.3 | 1.7 | 22.75 | 14.94 | 5.5 | 13.5 | 16.66 | Au1rxx-base64 | 66.94.121.46 |
| 85.97 | vless | 203.9 | 1.3 | 23.06 | 14.95 | 0.0 | 9.44 | 18.52 | mheidari-all | 172.235.53.103 |
| 85.95 | vless | 205.6 | 0.9 | 23.02 | 14.97 | 0.0 | 9.44 | 18.52 | mheidari-all | 172.233.129.179 |
| 85.85 | vless | 210.8 | 0.3 | 22.9 | 14.99 | 0.0 | 9.44 | 18.52 | mheidari-all | 156.229.167.109 |
| 85.84 | vless | 210.0 | 1.1 | 22.92 | 14.96 | 0.0 | 9.44 | 18.52 | mheidari-all | 172.235.49.52 |
| 85.76 | vless | 208.7 | 3.9 | 22.95 | 14.85 | 0.0 | 9.44 | 18.52 | mheidari-all | 172.236.238.71 |
| 85.7 | vless | 211.9 | 3.4 | 22.87 | 14.87 | 0.0 | 9.44 | 18.52 | mheidari-all | 172.236.231.45 |
| 85.7 | vless | 213.7 | 2.4 | 22.83 | 14.91 | 0.0 | 9.44 | 18.52 | mheidari-all | 172.233.139.98 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.949 | 98 | 1751 | prefer |
| ermaozi | 0.975 | 1.0 | 23 | 366 | prefer |
| Surfboard-tg-mixed | 0.958 | 0.884 | 129 | 8239 | prefer |
| mheidari-all | 0.932 | 0.856 | 153 | 14970 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ermaozi-get_subscribe | 0.333 | 0.75 | 4 | 322 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4839 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11536 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5468 | observe |
| barry-far-vless | 0.255 | None | 0 | 5508 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4546 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 26 |
| cn-block | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 3 |
| 204 | ProxyError | - | 2 |
| 204 | TimeoutError | - | 2 |
| cn-block | TimeoutError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 80 | 86 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
