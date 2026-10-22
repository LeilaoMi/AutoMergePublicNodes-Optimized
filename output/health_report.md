# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-22 17:24:24 |
| 运行耗时 | 293.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 96736 |
| 去重后节点 | 26708 |
| TCP 可达 | 3000 |
| 真实可用 | 351 |
| Verified 输出 | 111 |
| Global 输出 | 300 |
| All 输出 | 26708 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.5 |
| tcp | 81.9 |
| probe | 94.7 |
| real_test | 72.9 |
| china_check | 21.0 |
| write_verified | 0.1 |
| generate | 14.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57365 |
| vmess | 17217 |
| shadowsocks | 12363 |
| trojan | 7935 |
| hysteria2 | 1348 |
| http | 239 |
| shadowsocksr | 166 |
| socks | 58 |
| anytls | 22 |
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
| 92.33 | shadowsocks | 231.3 | 2.1 | 22.42 | 14.92 | 9.15 | 12.92 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 91.88 | shadowsocks | 220.3 | 0.7 | 22.68 | 14.97 | 8.39 | 12.92 | 16.92 | Au1rxx-base64 | 156.146.38.168 |
| 89.39 | vless | 252.9 | 8.1 | 21.92 | 14.7 | 8.43 | 9.22 | 16.92 | Au1rxx-base64 | 45.63.53.81 |
| 89.18 | vless | 255.1 | 11.6 | 21.87 | 14.56 | 8.42 | 9.22 | 16.92 | Au1rxx-base64 | 45.32.69.110 |
| 88.78 | shadowsocks | 240.1 | 1.1 | 22.22 | 14.96 | 8.76 | 12.92 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 88.69 | shadowsocks | 352.1 | 7.1 | 19.63 | 14.73 | 8.99 | 12.92 | 16.92 | Au1rxx-base64 | 185.215.132.18 |
| 88.63 | shadowsocks | 350.4 | 0.6 | 19.67 | 14.98 | 8.64 | 12.92 | 16.92 | Au1rxx-base64 | 185.215.132.9 |
| 88.34 | shadowsocks | 280.9 | 1.4 | 21.28 | 14.95 | 8.92 | 12.92 | 16.92 | Au1rxx-base64 | 173.244.56.6 |
| 87.75 | vless | 254.2 | 1.2 | 21.89 | 14.96 | 6.7 | 9.22 | 16.92 | Au1rxx-base64 | 144.202.126.147 |
| 86.86 | vless | 245.4 | 2.6 | 22.1 | 14.9 | 5.61 | 9.22 | 16.92 | Au1rxx-base64 | 45.76.172.197 |
| 86.78 | shadowsocks | 327.6 | 1.7 | 20.19 | 14.94 | 8.82 | 12.92 | 16.92 | Au1rxx-base64 | 37.19.198.243 |
| 86.75 | hysteria2 | 278.9 | 5.3 | 21.32 | 14.8 | 8.12 | 12.27 | 16.92 | Au1rxx-base64 | 129.213.91.185 |
| 86.61 | shadowsocks | 297.1 | 3.2 | 20.9 | 14.88 | 8.89 | 12.92 | 16.92 | Au1rxx-base64 | 173.244.56.9 |
| 86.35 | shadowsocks | 325.3 | 5.2 | 20.25 | 14.81 | 8.85 | 12.92 | 16.92 | Au1rxx-base64 | 37.19.198.236 |
| 85.71 | vless | 339.6 | 5.4 | 19.92 | 14.8 | 8.11 | 9.22 | 16.92 | Au1rxx-base64 | 5.34.178.120 |
| 85.52 | shadowsocks | 392.0 | 3.3 | 18.7 | 14.88 | 8.89 | 12.92 | 16.92 | Au1rxx-base64 | 193.151.160.9 |
| 85.51 | shadowsocks | 362.0 | 0.2 | 19.4 | 14.99 | 8.88 | 12.92 | 16.92 | Au1rxx-base64 | 45.86.51.18 |
| 85.15 | shadowsocks | 326.5 | 2.2 | 20.22 | 14.92 | 6.91 | 12.92 | 16.92 | Au1rxx-base64 | 37.19.198.160 |
| 84.95 | trojan | 418.0 | 5.1 | 18.1 | 14.81 | 9.12 | 11.16 | 16.92 | Au1rxx-base64 | 66.23.203.21 |
| 84.89 | shadowsocks | 393.7 | 5.2 | 18.66 | 14.8 | 8.9 | 12.92 | 16.92 | Au1rxx-base64 | 193.151.160.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.995 | 0.986 | 70 | 573 | prefer |
| mheidari-all | 0.83 | 0.757 | 70 | 24062 | prefer |
| Au1rxx-base64 | 0.82 | 0.761 | 251 | 1529 | prefer |
| Surfboard-tg-mixed | 0.735 | 0.66 | 53 | 7066 | prefer |
| DeltaKronecker-all | 0.314 | 0.333 | 9 | 3641 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 70 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 7538 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10555 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5426 | observe |
| barry-far-vless | 0.255 | None | 0 | 5601 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4164 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 67 |
| speed | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 6 |
| geo | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | TimeoutError | - | 2 |
| 204 | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 123 | 111 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
