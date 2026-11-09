# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-09 23:32:47 |
| 运行耗时 | 299.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81722 |
| 去重后节点 | 26721 |
| TCP 可达 | 3000 |
| 真实可用 | 481 |
| Verified 输出 | 49 |
| Global 输出 | 300 |
| All 输出 | 26721 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 79.3 |
| probe | 97.4 |
| real_test | 81.2 |
| china_check | 18.6 |
| write_verified | 0.0 |
| generate | 14.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49396 |
| vmess | 14228 |
| shadowsocks | 9167 |
| trojan | 6995 |
| hysteria2 | 1579 |
| shadowsocksr | 148 |
| http | 99 |
| socks | 50 |
| hysteria | 23 |
| tuic | 21 |
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
| 97.03 | trojan | 235.0 | 6.9 | 22.34 | 14.74 | 10.0 | 14.29 | 18.92 | Au1rxx-base64 | 167.88.61.175 |
| 94.73 | trojan | 235.2 | 3.0 | 22.33 | 14.89 | 8.07 | 14.29 | 18.92 | Au1rxx-base64 | 167.88.61.198 |
| 94.23 | trojan | 286.8 | 3.7 | 21.14 | 14.86 | 10.0 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.114.45 |
| 93.88 | trojan | 179.4 | 2.0 | 23.62 | 14.93 | 4.62 | 14.29 | 18.92 | Au1rxx-base64 | 216.106.186.32 |
| 93.66 | trojan | 265.2 | 6.2 | 21.64 | 14.77 | 8.05 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.114.132 |
| 93.57 | trojan | 290.3 | 3.0 | 21.06 | 14.89 | 10.0 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.112.121 |
| 93.46 | trojan | 270.3 | 1.3 | 21.52 | 14.95 | 7.65 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.114.245 |
| 93.41 | trojan | 286.5 | 3.2 | 21.15 | 14.88 | 8.07 | 14.29 | 18.92 | Au1rxx-base64 | 167.88.61.20 |
| 91.84 | trojan | 355.9 | 0.1 | 19.54 | 15.0 | 7.55 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.114.106 |
| 91.77 | hysteria2 | 246.6 | 4.0 | 22.07 | 14.85 | 3.0 | 13.93 | 18.92 | Au1rxx-base64 | 66.94.121.46 |
| 91.76 | trojan | 265.9 | 0.7 | 21.62 | 14.97 | 7.55 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.114.114 |
| 91.72 | trojan | 271.8 | 0.2 | 21.48 | 14.99 | 7.0 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.114.126 |
| 91.1 | trojan | 292.0 | 1.6 | 21.02 | 14.94 | 7.95 | 14.29 | 18.92 | Au1rxx-base64 | 66.163.112.242 |
| 90.92 | trojan | 239.2 | 2.8 | 22.24 | 14.89 | 4.63 | 14.29 | 18.92 | Au1rxx-base64 | 167.88.61.85 |
| 90.77 | vless | 239.6 | 0.7 | 22.23 | 14.97 | 6.86 | 10.13 | 18.92 | Au1rxx-base64 | 47.251.108.158 |
| 90.03 | trojan | 183.9 | 0.2 | 23.52 | 14.99 | 0.81 | 14.29 | 18.92 | Au1rxx-base64 | 216.106.186.33 |
| 89.64 | shadowsocks | 321.4 | 1.9 | 20.34 | 14.93 | 10.0 | 13.73 | 18.92 | Au1rxx-base64 | 156.146.38.167 |
| 89.56 | vless | 279.3 | 5.3 | 21.31 | 14.8 | 7.73 | 10.13 | 18.92 | Au1rxx-base64 | 195.123.240.65 |
| 89.56 | shadowsocks | 319.8 | 0.2 | 20.37 | 14.99 | 10.0 | 13.73 | 18.92 | Au1rxx-base64 | 156.146.38.170 |
| 89.29 | trojan | 180.6 | 0.6 | 23.6 | 14.98 | 0.0 | 14.29 | 18.92 | Au1rxx-base64 | www.findlocaljobnetworkandbuildcommunityconnections.com |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.935 | 0.859 | 198 | 8250 | prefer |
| ermaozi | 0.93 | 0.95 | 20 | 518 | prefer |
| mheidari-all | 0.923 | 0.849 | 106 | 14061 | prefer |
| Au1rxx-base64 | 0.88 | 0.812 | 245 | 1751 | prefer |
| DeltaKronecker-all | 0.349 | 0.667 | 3 | 2754 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11213 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6133 | observe |
| barry-far-vless | 0.255 | None | 0 | 6103 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 56 |
| 204 | ProxyError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 5 |
| speed | ClientOSError | - | 5 |
| speed | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| geo | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | status | 530 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 48 | 49 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
