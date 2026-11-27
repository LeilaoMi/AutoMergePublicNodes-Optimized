# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-27 08:51:40 |
| 运行耗时 | 269.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 78402 |
| 去重后节点 | 27160 |
| TCP 可达 | 3000 |
| 真实可用 | 393 |
| Verified 输出 | 51 |
| Global 输出 | 300 |
| All 输出 | 27160 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 82.1 |
| probe | 68.4 |
| real_test | 74.8 |
| china_check | 30.1 |
| write_verified | 0.0 |
| generate | 9.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45796 |
| vmess | 15140 |
| shadowsocks | 9732 |
| trojan | 5622 |
| hysteria2 | 1575 |
| http | 204 |
| shadowsocksr | 151 |
| socks | 113 |
| anytls | 35 |
| hysteria | 22 |
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
| 90.77 | shadowsocks | 262.2 | 2.1 | 21.71 | 14.92 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 156.146.38.168 |
| 89.66 | shadowsocks | 280.3 | 1.4 | 21.29 | 14.95 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 37.19.198.236 |
| 88.89 | shadowsocks | 284.8 | 1.3 | 21.18 | 14.95 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 37.19.198.160 |
| 88.12 | http | 259.2 | 0.6 | 21.78 | 14.98 | 0.0 | 14.38 | 19.48 | ermaozi | 172.64.69.89 |
| 88.02 | trojan | 253.5 | 0.4 | 21.91 | 14.98 | 10.0 | 12.19 | 16.44 | Au1rxx-base64 | 66.163.114.45 |
| 87.87 | trojan | 447.2 | 5.1 | 17.43 | 14.81 | 10.0 | 12.19 | 16.44 | Au1rxx-base64 | 66.23.203.21 |
| 87.18 | shadowsocks | 293.8 | 0.3 | 20.98 | 14.99 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 185.230.230.18 |
| 86.88 | shadowsocks | 303.0 | 0.3 | 20.77 | 14.99 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 45.86.51.18 |
| 86.87 | trojan | 298.2 | 2.1 | 20.88 | 14.92 | 9.53 | 12.19 | 16.44 | Au1rxx-base64 | 167.88.61.175 |
| 86.69 | vless | 376.4 | 0.3 | 19.06 | 14.99 | 10.0 | 10.04 | 16.44 | Au1rxx-base64 | 169.40.42.74 |
| 86.34 | trojan | 254.7 | 0.4 | 21.88 | 14.98 | 8.35 | 12.19 | 16.44 | Au1rxx-base64 | 66.163.114.132 |
| 86.31 | shadowsocks | 259.3 | 1.0 | 21.78 | 14.96 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 156.146.38.170 |
| 85.83 | http | 303.5 | 0.1 | 20.75 | 15.0 | 0.0 | 14.38 | 19.48 | ermaozi | 149.88.21.129 |
| 85.72 | shadowsocks | 322.6 | 0.7 | 20.31 | 14.97 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 173.244.56.9 |
| 85.57 | shadowsocks | 288.0 | 1.7 | 21.11 | 14.94 | 10.0 | 11.7 | 16.44 | Au1rxx-base64 | 37.19.198.244 |
| 85.51 | vless | 422.5 | 0.4 | 18.0 | 14.99 | 9.16 | 10.04 | 16.44 | Au1rxx-base64 | 169.40.42.89 |
| 85.47 | trojan | 296.1 | 0.1 | 20.92 | 15.0 | 8.11 | 12.19 | 16.44 | Au1rxx-base64 | 167.88.61.193 |
| 85.33 | trojan | 246.0 | 0.3 | 22.08 | 14.99 | 7.13 | 12.19 | 16.44 | Au1rxx-base64 | 66.163.114.245 |
| 85.26 | vless | 437.1 | 3.8 | 17.66 | 14.86 | 9.17 | 10.04 | 16.44 | Au1rxx-base64 | 169.40.42.202 |
| 85.25 | trojan | 293.3 | 0.1 | 20.99 | 15.0 | 8.1 | 12.19 | 16.44 | Au1rxx-base64 | 167.88.61.20 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | 1.0 | 53 | 422 | prefer |
| Surfboard-tg-mixed | 0.801 | 0.723 | 238 | 8568 | prefer |
| Au1rxx-base64 | 0.689 | 0.62 | 187 | 1751 | observe |
| mheidari-all | 0.658 | 0.58 | 100 | 14315 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| tg-LonUp_M | 0.365 | 1.0 | 3 | 173 | observe |
| tg-oneclickvpnkeys | 0.363 | 1.0 | 3 | 116 | observe |
| ermaozi-get_subscribe | 0.284 | 0.667 | 3 | 391 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 147 | observe |
| tg-proxy_mtm | 0.258 | 1.0 | 1 | 67 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4936 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11572 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5426 | observe |
| barry-far-vless | 0.255 | None | 0 | 5609 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 65 |
| 204 | ClientOSError | - | 63 |
| 204 | ProxyError | - | 11 |
| geo | ClientOSError | - | 9 |
| speed | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 6 |
| speed | TimeoutError | - | 5 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 63 | 51 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
