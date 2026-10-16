# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 11:41:24 |
| 运行耗时 | 310.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99280 |
| 去重后节点 | 27669 |
| TCP 可达 | 3000 |
| 真实可用 | 469 |
| Verified 输出 | 21 |
| Global 输出 | 300 |
| All 输出 | 27669 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.5 |
| tcp | 86.8 |
| probe | 86.1 |
| real_test | 92.2 |
| china_check | 27.0 |
| write_verified | 0.0 |
| generate | 11.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58421 |
| vmess | 16409 |
| shadowsocks | 11906 |
| trojan | 10276 |
| hysteria2 | 1256 |
| http | 740 |
| shadowsocksr | 165 |
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
| 96.58 | vless | 188.8 | 0.8 | 23.41 | 14.97 | 10.0 | 10.12 | 18.08 | Au1rxx-base64 | 131.143.180.110 |
| 93.93 | vless | 303.7 | 0.6 | 20.75 | 14.98 | 10.0 | 10.12 | 18.08 | Au1rxx-base64 | 154.12.38.202 |
| 93.68 | shadowsocks | 301.2 | 0.5 | 20.81 | 14.98 | 10.0 | 13.81 | 18.08 | Au1rxx-base64 | 149.22.95.183 |
| 92.15 | vless | 295.3 | 1.4 | 20.94 | 14.95 | 8.08 | 10.12 | 18.08 | Au1rxx-base64 | 44.248.233.99 |
| 92.04 | hysteria2 | 343.8 | 1.9 | 19.82 | 14.93 | 10.0 | 14.12 | 18.08 | Au1rxx-base64 | 129.213.91.185 |
| 91.55 | vless | 293.4 | 0.7 | 20.99 | 14.97 | 7.39 | 10.12 | 18.08 | Au1rxx-base64 | 23.95.222.127 |
| 91.49 | vless | 409.4 | 0.3 | 18.3 | 14.99 | 10.0 | 10.12 | 18.08 | Au1rxx-base64 | 51.81.203.63 |
| 91.09 | hysteria2 | 224.2 | 1.4 | 22.59 | 14.95 | 3.25 | 14.12 | 18.08 | Au1rxx-base64 | starlink-ft.251313.xyz |
| 90.86 | shadowsocks | 227.4 | 3.8 | 22.51 | 14.86 | 7.89 | 13.81 | 18.08 | Au1rxx-base64 | 173.244.56.9 |
| 90.86 | shadowsocks | 302.1 | 1.7 | 20.78 | 14.93 | 10.0 | 13.81 | 18.08 | Au1rxx-base64 | 156.146.38.168 |
| 90.76 | hysteria2 | 250.3 | 26.4 | 21.98 | 14.01 | 4.87 | 14.12 | 18.08 | Au1rxx-base64 | 66.94.121.46 |
| 90.44 | vless | 317.2 | 1.5 | 20.44 | 14.94 | 10.0 | 10.12 | 18.08 | Au1rxx-base64 | 147.45.60.160 |
| 90.19 | shadowsocks | 293.3 | 0.5 | 20.99 | 14.98 | 10.0 | 13.81 | 18.08 | Au1rxx-base64 | 156.146.38.167 |
| 89.7 | shadowsocks | 339.3 | 1.1 | 19.92 | 14.96 | 10.0 | 13.81 | 18.08 | Au1rxx-base64 | 156.146.38.169 |
| 89.66 | vless | 252.0 | 4.6 | 21.94 | 14.83 | 4.69 | 10.12 | 18.08 | Au1rxx-base64 | tk1.high-speed-test-56424.me |
| 89.33 | shadowsocks | 235.5 | 2.1 | 22.33 | 14.92 | 4.19 | 13.81 | 18.08 | Au1rxx-base64 | 173.244.56.6 |
| 88.94 | shadowsocks | 384.7 | 7.7 | 18.87 | 14.71 | 7.97 | 13.81 | 18.08 | Au1rxx-base64 | 103.11.76.248 |
| 86.81 | vless | 204.4 | 0.5 | 23.05 | 14.98 | 5.84 | 10.12 | 18.08 | Au1rxx-base64 | 154.29.159.211 |
| 86.25 | shadowsocks | 386.0 | 1.1 | 18.84 | 14.96 | 10.0 | 13.81 | 18.08 | Au1rxx-base64 | 37.19.198.160 |
| 86.22 | vless | 346.0 | 2.9 | 19.77 | 14.89 | 8.07 | 10.12 | 18.08 | Au1rxx-base64 | 195.211.98.43 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.988 | 86 | 693 | prefer |
| Au1rxx-base64 | 0.848 | 0.77 | 473 | 1990 | prefer |
| mheidari-all | 0.58 | 0.5 | 26 | 23871 | observe |
| Surfboard-tg-mixed | 0.465 | 0.714 | 7 | 7090 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1990 | observe |
| Epodonios-all | 0.255 | None | 0 | 7568 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10088 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5572 | observe |
| barry-far-vless | 0.255 | None | 0 | 5827 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 70 |
| speed | ClientOSError | - | 15 |
| 204 | TimeoutError | - | 11 |
| geo | ClientOSError | - | 9 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| speed | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| cn-block | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 43 | 21 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
