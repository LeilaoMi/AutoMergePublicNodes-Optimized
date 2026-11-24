# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-24 10:09:07 |
| 运行耗时 | 269.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 79067 |
| 去重后节点 | 27838 |
| TCP 可达 | 3000 |
| 真实可用 | 355 |
| Verified 输出 | 80 |
| Global 输出 | 300 |
| All 输出 | 27838 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| geo | 1.4 |
| tcp | 83.0 |
| probe | 74.5 |
| real_test | 66.8 |
| china_check | 30.4 |
| write_verified | 0.0 |
| generate | 9.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47125 |
| vmess | 14995 |
| shadowsocks | 9332 |
| trojan | 5441 |
| hysteria2 | 1591 |
| http | 209 |
| shadowsocksr | 165 |
| socks | 125 |
| anytls | 40 |
| hysteria | 32 |
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
| 95.79 | shadowsocks | 227.5 | 0.2 | 22.51 | 14.99 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 156.146.38.170 |
| 95.56 | shadowsocks | 237.2 | 0.5 | 22.29 | 14.98 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 156.146.38.168 |
| 94.49 | shadowsocks | 250.6 | 0.3 | 21.98 | 14.99 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 95.215.201.18 |
| 91.48 | shadowsocks | 309.0 | 0.3 | 20.62 | 14.99 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 37.19.198.236 |
| 91.33 | shadowsocks | 310.9 | 0.5 | 20.58 | 14.98 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 37.19.198.243 |
| 91.22 | shadowsocks | 286.1 | 0.2 | 21.15 | 14.99 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 173.244.56.6 |
| 91.14 | shadowsocks | 312.9 | 0.1 | 20.53 | 15.0 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 45.86.51.18 |
| 91.08 | shadowsocks | 310.7 | 0.3 | 20.59 | 14.99 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 37.19.198.244 |
| 91.04 | shadowsocks | 360.2 | 0.2 | 19.44 | 14.99 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 193.151.160.9 |
| 91.03 | trojan | 282.7 | 3.3 | 21.23 | 14.88 | 10.0 | 13.65 | 17.92 | Au1rxx-base64 | 167.88.61.175 |
| 90.78 | shadowsocks | 279.8 | 1.0 | 21.3 | 14.96 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 173.244.56.9 |
| 90.47 | shadowsocks | 322.0 | 2.4 | 20.32 | 14.91 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 185.230.230.18 |
| 90.31 | shadowsocks | 356.8 | 1.5 | 19.52 | 14.94 | 9.89 | 14.37 | 17.92 | Au1rxx-base64 | 193.151.160.18 |
| 90.05 | trojan | 376.8 | 5.7 | 19.06 | 14.79 | 10.0 | 13.65 | 17.92 | Au1rxx-base64 | 66.23.203.21 |
| 89.08 | shadowsocks | 319.3 | 0.6 | 20.39 | 14.98 | 10.0 | 14.37 | 17.92 | Au1rxx-base64 | 193.151.163.18 |
| 88.73 | trojan | 286.6 | 0.2 | 21.14 | 14.99 | 9.78 | 13.65 | 17.92 | Au1rxx-base64 | 167.88.61.193 |
| 88.14 | vless | 246.5 | 0.8 | 22.07 | 14.97 | 8.24 | 6.65 | 17.92 | Au1rxx-base64 | 45.63.53.81 |
| 87.71 | trojan | 285.9 | 2.4 | 21.16 | 14.91 | 9.78 | 13.65 | 17.92 | Au1rxx-base64 | 167.88.61.198 |
| 87.7 | hysteria2 | 264.0 | 0.8 | 21.67 | 14.97 | 8.01 | 12.69 | 17.92 | Au1rxx-base64 | 8.209.247.109 |
| 87.64 | trojan | 291.7 | 1.6 | 21.03 | 14.94 | 9.8 | 13.65 | 17.92 | Au1rxx-base64 | 167.88.61.20 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.983 | 0.981 | 54 | 460 | prefer |
| mheidari-all | 0.926 | 0.857 | 63 | 15386 | prefer |
| Surfboard-tg-mixed | 0.85 | 0.772 | 202 | 8220 | prefer |
| Au1rxx-base64 | 0.833 | 0.767 | 129 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ermaozi-get_subscribe | 0.284 | 0.667 | 3 | 388 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 167 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5064 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11363 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5327 | observe |
| barry-far-vless | 0.255 | None | 0 | 5849 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 48 |
| 204 | ProxyError | - | 15 |
| 204 | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 82 | 80 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
