# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-20 20:36:55 |
| 运行耗时 | 309.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82572 |
| 去重后节点 | 27861 |
| TCP 可达 | 3000 |
| 真实可用 | 368 |
| Verified 输出 | 41 |
| Global 输出 | 300 |
| All 输出 | 27861 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.6 |
| tcp | 85.7 |
| probe | 92.4 |
| real_test | 77.0 |
| china_check | 33.8 |
| write_verified | 0.0 |
| generate | 13.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48174 |
| vmess | 15046 |
| shadowsocks | 10399 |
| trojan | 6918 |
| hysteria2 | 1547 |
| http | 167 |
| shadowsocksr | 151 |
| socks | 120 |
| hysteria | 24 |
| tuic | 14 |
| anytls | 12 |

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
| 90.7 | vless | 253.2 | 5.2 | 21.92 | 14.81 | 6.83 | 11.86 | 16.62 | Au1rxx-base64 | 45.63.53.81 |
| 87.82 | shadowsocks | 277.0 | 12.3 | 21.36 | 14.54 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 156.146.38.168 |
| 87.75 | shadowsocks | 287.5 | 1.9 | 21.12 | 14.93 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 95.215.201.18 |
| 87.25 | shadowsocks | 325.2 | 4.3 | 20.25 | 14.84 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 37.19.198.236 |
| 87.1 | http | 305.3 | 2.0 | 20.71 | 14.93 | 0.0 | 14.4 | 19.6 | ermaozi | 172.64.68.89 |
| 87.08 | shadowsocks | 276.0 | 0.1 | 21.39 | 15.0 | 4.74 | 13.33 | 16.62 | Au1rxx-base64 | 156.146.38.169 |
| 86.5 | shadowsocks | 384.8 | 0.2 | 18.87 | 14.99 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 45.86.51.18 |
| 86.36 | vless | 370.2 | 4.4 | 19.21 | 14.84 | 9.11 | 11.86 | 16.62 | Au1rxx-base64 | 159.89.87.21 |
| 86.18 | shadowsocks | 327.8 | 4.8 | 20.19 | 14.82 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 37.19.198.243 |
| 86.16 | shadowsocks | 327.9 | 6.7 | 20.19 | 14.75 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 193.151.163.18 |
| 86.06 | shadowsocks | 357.9 | 2.8 | 19.49 | 14.9 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 193.151.160.9 |
| 85.88 | vless | 376.5 | 2.0 | 19.06 | 14.92 | 10.0 | 11.86 | 16.62 | Au1rxx-base64 | 169.40.42.35 |
| 85.77 | vless | 386.8 | 5.7 | 18.82 | 14.78 | 9.24 | 11.86 | 16.62 | Au1rxx-base64 | 167.17.69.171 |
| 85.19 | shadowsocks | 218.7 | 0.6 | 22.72 | 14.98 | 0.0 | 13.33 | 18.66 | mheidari-all | 137.184.89.151 |
| 85.16 | shadowsocks | 219.7 | 0.5 | 22.69 | 14.98 | 0.0 | 13.33 | 18.66 | mheidari-all | 104.238.140.45 |
| 85.05 | shadowsocks | 332.6 | 1.6 | 20.08 | 14.94 | 10.0 | 13.33 | 16.62 | Au1rxx-base64 | 185.230.230.18 |
| 84.77 | hysteria2 | 251.4 | 29.7 | 21.96 | 13.89 | 2.92 | 10.38 | 16.62 | Au1rxx-base64 | 66.94.121.46 |
| 84.53 | http | 342.5 | 1.5 | 19.85 | 14.94 | 0.0 | 14.4 | 19.6 | ermaozi | 23.133.176.14 |
| 84.52 | shadowsocks | 245.2 | 1.9 | 22.1 | 14.93 | 0.0 | 13.33 | 18.66 | mheidari-all | 167.17.67.171 |
| 84.31 | shadowsocks | 357.2 | 2.9 | 19.51 | 14.89 | 8.34 | 13.33 | 16.62 | Au1rxx-base64 | 193.151.160.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.882 | 0.889 | 27 | 492 | prefer |
| mheidari-all | 0.875 | 0.8 | 115 | 14341 | prefer |
| Surfboard-tg-mixed | 0.847 | 0.77 | 213 | 8704 | prefer |
| Au1rxx-base64 | 0.676 | 0.608 | 158 | 1751 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2910 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 166 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 130 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5045 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11804 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5734 | observe |
| barry-far-vless | 0.255 | None | 0 | 5776 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 65 |
| 204 | ProxyError | - | 39 |
| cn-block | ProxyError | - | 8 |
| 204 | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| speed | TimeoutError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 60 | 41 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
