# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-27 05:22:04 |
| 运行耗时 | 334.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 96396 |
| 去重后节点 | 26562 |
| TCP 可达 | 3000 |
| 真实可用 | 479 |
| Verified 输出 | 129 |
| Global 输出 | 300 |
| All 输出 | 26562 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.5 |
| tcp | 81.9 |
| probe | 104.0 |
| real_test | 100.2 |
| china_check | 24.8 |
| write_verified | 0.1 |
| generate | 14.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56704 |
| vmess | 17408 |
| shadowsocks | 12675 |
| trojan | 7634 |
| hysteria2 | 1433 |
| http | 266 |
| shadowsocksr | 169 |
| socks | 58 |
| anytls | 25 |
| hysteria | 18 |
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
| 90.93 | vless | 260.3 | 3.9 | 21.75 | 14.85 | 9.68 | 9.31 | 15.34 | Au1rxx-base64 | 169.40.42.35 |
| 90.46 | vless | 247.9 | 7.4 | 22.04 | 14.72 | 9.05 | 9.31 | 15.34 | Au1rxx-base64 | 169.40.42.235 |
| 90.42 | vless | 260.4 | 0.4 | 21.75 | 14.98 | 9.04 | 9.31 | 15.34 | Au1rxx-base64 | 167.17.69.171 |
| 90.13 | shadowsocks | 243.8 | 1.6 | 22.13 | 14.94 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 37.19.198.236 |
| 89.9 | shadowsocks | 250.5 | 3.8 | 21.98 | 14.86 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 37.19.198.160 |
| 89.64 | shadowsocks | 239.7 | 4.1 | 22.23 | 14.85 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 185.230.230.18 |
| 89.47 | shadowsocks | 251.7 | 1.1 | 21.95 | 14.96 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 193.151.163.18 |
| 89.14 | vless | 356.0 | 1.3 | 19.54 | 14.95 | 10.0 | 9.31 | 15.34 | Au1rxx-base64 | 169.40.42.229 |
| 88.95 | shadowsocks | 247.4 | 5.2 | 22.05 | 14.8 | 9.04 | 11.72 | 15.34 | Au1rxx-base64 | 37.19.198.243 |
| 88.62 | vless | 308.0 | 1.0 | 20.65 | 14.96 | 8.36 | 9.31 | 15.34 | Au1rxx-base64 | 195.123.235.183 |
| 88.56 | vless | 241.0 | 18.1 | 22.2 | 14.32 | 7.39 | 9.31 | 15.34 | Au1rxx-base64 | 195.123.235.177 |
| 88.26 | vless | 376.5 | 3.4 | 19.06 | 14.87 | 9.68 | 9.31 | 15.34 | Au1rxx-base64 | 169.40.42.225 |
| 88.11 | shadowsocks | 290.5 | 1.0 | 21.05 | 14.96 | 9.04 | 11.72 | 15.34 | Au1rxx-base64 | 37.19.198.244 |
| 87.74 | shadowsocks | 313.1 | 9.3 | 20.53 | 14.65 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 15.204.246.132 |
| 87.7 | shadowsocks | 320.7 | 5.5 | 20.35 | 14.79 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 15.204.233.41 |
| 87.64 | shadowsocks | 327.8 | 2.8 | 20.19 | 14.89 | 10.0 | 11.72 | 15.34 | Au1rxx-base64 | 45.86.51.18 |
| 87.49 | vless | 384.0 | 2.5 | 18.89 | 14.91 | 9.04 | 9.31 | 15.34 | Au1rxx-base64 | 185.95.231.156 |
| 87.23 | vless | 370.1 | 3.6 | 19.21 | 14.86 | 8.51 | 9.31 | 15.34 | Au1rxx-base64 | 169.40.42.202 |
| 87.15 | trojan | 399.6 | 2.7 | 18.53 | 14.9 | 10.0 | 14.05 | 15.34 | Au1rxx-base64 | 66.23.203.21 |
| 87.14 | vless | 362.3 | 5.0 | 19.39 | 14.81 | 8.5 | 9.31 | 15.34 | Au1rxx-base64 | 169.40.42.74 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.81 | 0.743 | 401 | 1700 | prefer |
| ermaozi | 0.742 | 0.722 | 90 | 603 | prefer |
| Surfboard-tg-mixed | 0.728 | 0.65 | 123 | 7143 | prefer |
| mheidari-all | 0.425 | 0.341 | 85 | 24431 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| DeltaKronecker-all | 0.322 | 0.25 | 16 | 3004 | observe |
| roosterkid-openproxylist-v2ray | 0.275 | 0.667 | 3 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7632 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5408 | observe |
| barry-far-vless | 0.255 | None | 0 | 5620 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4466 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1700 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 115 |
| geo | ClientOSError | - | 42 |
| speed | ClientOSError | - | 33 |
| 204 | ProxyError | - | 15 |
| cn-block | ProxyError | - | 12 |
| geo | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 96 | 129 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
