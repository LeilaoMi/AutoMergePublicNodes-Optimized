# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-11 19:48:06 |
| 运行耗时 | 299.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 82898 |
| 去重后节点 | 26904 |
| TCP 可达 | 3000 |
| 真实可用 | 422 |
| Verified 输出 | 80 |
| Global 输出 | 300 |
| All 输出 | 26904 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.5 |
| tcp | 82.0 |
| probe | 83.2 |
| real_test | 85.9 |
| china_check | 30.4 |
| write_verified | 0.0 |
| generate | 11.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50555 |
| vmess | 14233 |
| shadowsocks | 9311 |
| trojan | 6702 |
| hysteria2 | 1527 |
| http | 297 |
| shadowsocksr | 149 |
| socks | 55 |
| hysteria | 33 |
| tuic | 21 |
| anytls | 15 |

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
| 96.05 | trojan | 198.9 | 2.7 | 23.17 | 14.9 | 10.0 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.242 |
| 95.16 | trojan | 196.6 | 0.9 | 23.23 | 14.97 | 8.98 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.13 |
| 94.5 | trojan | 268.2 | 1.3 | 21.57 | 14.95 | 10.0 | 13.54 | 16.94 | Au1rxx-base64 | 167.88.61.175 |
| 94.41 | shadowsocks | 192.1 | 2.5 | 23.33 | 14.91 | 10.0 | 13.73 | 16.94 | Au1rxx-base64 | 95.215.201.18 |
| 94.31 | trojan | 199.3 | 0.6 | 23.16 | 14.98 | 10.0 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.121 |
| 93.78 | trojan | 208.4 | 4.6 | 22.95 | 14.83 | 8.97 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.76 |
| 93.23 | shadowsocks | 263.2 | 3.2 | 21.68 | 14.88 | 10.0 | 13.73 | 16.94 | Au1rxx-base64 | 156.146.38.170 |
| 92.28 | trojan | 203.2 | 1.8 | 23.07 | 14.93 | 6.3 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.142 |
| 92.12 | shadowsocks | 301.9 | 3.5 | 20.79 | 14.87 | 10.0 | 13.73 | 16.94 | Au1rxx-base64 | 156.146.38.168 |
| 92.1 | vless | 234.0 | 4.3 | 22.36 | 14.84 | 9.64 | 8.32 | 16.94 | Au1rxx-base64 | 195.123.240.65 |
| 91.75 | trojan | 208.5 | 12.7 | 22.95 | 14.52 | 6.3 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.31 |
| 91.64 | trojan | 220.6 | 3.3 | 22.67 | 14.87 | 9.99 | 13.54 | 16.94 | Au1rxx-base64 | 167.88.61.198 |
| 91.45 | shadowsocks | 303.9 | 3.5 | 20.74 | 14.87 | 10.0 | 13.73 | 16.94 | Au1rxx-base64 | 156.146.38.167 |
| 91.24 | trojan | 234.7 | 4.6 | 22.34 | 14.83 | 6.09 | 13.54 | 16.94 | Au1rxx-base64 | 167.88.61.85 |
| 90.91 | trojan | 217.8 | 4.6 | 22.74 | 14.83 | 9.99 | 13.54 | 16.94 | Au1rxx-base64 | 167.88.61.193 |
| 90.9 | trojan | 223.3 | 5.5 | 22.61 | 14.79 | 9.99 | 13.54 | 16.94 | Au1rxx-base64 | 167.88.61.20 |
| 90.47 | trojan | 197.9 | 2.2 | 23.2 | 14.92 | 4.37 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.147 |
| 89.79 | shadowsocks | 259.0 | 0.6 | 21.78 | 14.98 | 6.36 | 13.73 | 16.94 | Au1rxx-base64 | 156.146.38.169 |
| 89.73 | http | 200.4 | 0.9 | 23.14 | 14.97 | 0.0 | 14.82 | 19.8 | ermaozi | 138.199.35.215 |
| 89.71 | trojan | 211.9 | 0.2 | 22.87 | 14.99 | 3.87 | 13.54 | 16.94 | Au1rxx-base64 | 66.163.112.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.988 | 82 | 608 | prefer |
| Au1rxx-base64 | 0.777 | 0.709 | 189 | 1751 | prefer |
| mheidari-all | 0.768 | 0.692 | 91 | 14491 | prefer |
| Surfboard-tg-mixed | 0.767 | 0.688 | 199 | 8393 | prefer |
| SoliSpirit-all | 0.48 | 1.0 | 4 | 11151 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2629 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4981 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6306 | observe |
| barry-far-vless | 0.255 | None | 0 | 6516 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| ermaozi-get_subscribe | 0.226 | 0.5 | 2 | 464 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 60 |
| 204 | ProxyError | - | 42 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 8 |
| speed | ProxyError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| geo | ClientOSError | - | 2 |
| speed | TimeoutError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 92 | 80 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
