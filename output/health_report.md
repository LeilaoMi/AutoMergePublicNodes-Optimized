# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-24 16:08:33 |
| 运行耗时 | 258.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 93158 |
| 去重后节点 | 24623 |
| TCP 可达 | 3000 |
| 真实可用 | 297 |
| Verified 输出 | 65 |
| Global 输出 | 300 |
| All 输出 | 24623 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 77.7 |
| probe | 77.6 |
| real_test | 64.8 |
| china_check | 22.1 |
| write_verified | 0.0 |
| generate | 9.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56442 |
| vmess | 17051 |
| shadowsocks | 11959 |
| trojan | 5875 |
| hysteria2 | 1351 |
| http | 212 |
| shadowsocksr | 162 |
| socks | 59 |
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
| 93.28 | shadowsocks | 255.3 | 0.5 | 21.87 | 14.98 | 8.97 | 13.66 | 17.8 | Au1rxx-base64 | 156.146.38.170 |
| 93.15 | hysteria2 | 267.7 | 2.3 | 21.58 | 14.91 | 9.08 | 13.85 | 17.8 | Au1rxx-base64 | 129.213.91.185 |
| 92.89 | shadowsocks | 308.2 | 2.5 | 20.64 | 14.91 | 10.0 | 13.66 | 17.8 | Au1rxx-base64 | 37.19.198.243 |
| 92.53 | shadowsocks | 247.8 | 2.3 | 22.04 | 14.91 | 10.0 | 13.66 | 17.8 | Au1rxx-base64 | 156.146.38.169 |
| 91.59 | shadowsocks | 249.5 | 6.8 | 22.0 | 14.75 | 10.0 | 13.66 | 17.8 | Au1rxx-base64 | 156.146.38.168 |
| 91.3 | shadowsocks | 304.0 | 1.7 | 20.74 | 14.94 | 10.0 | 13.66 | 17.8 | Au1rxx-base64 | 185.230.230.18 |
| 90.97 | shadowsocks | 362.2 | 4.2 | 19.39 | 14.84 | 9.87 | 13.66 | 17.8 | Au1rxx-base64 | 37.19.198.236 |
| 90.88 | vless | 329.5 | 11.0 | 20.15 | 14.59 | 10.0 | 10.17 | 17.8 | Au1rxx-base64 | 195.211.98.43 |
| 90.23 | shadowsocks | 381.0 | 5.2 | 18.96 | 14.81 | 10.0 | 13.66 | 17.8 | Au1rxx-base64 | 37.19.198.160 |
| 89.57 | vless | 365.8 | 4.1 | 19.31 | 14.85 | 9.93 | 10.17 | 17.8 | Au1rxx-base64 | 66.70.179.198 |
| 89.52 | shadowsocks | 313.6 | 1.8 | 20.52 | 14.93 | 8.8 | 13.66 | 17.8 | Au1rxx-base64 | 193.151.163.18 |
| 89.42 | vless | 334.9 | 0.7 | 20.03 | 14.97 | 8.9 | 10.17 | 17.8 | Au1rxx-base64 | 195.123.235.177 |
| 89.41 | vless | 306.8 | 2.8 | 20.68 | 14.89 | 10.0 | 10.17 | 17.8 | Au1rxx-base64 | 195.123.240.65 |
| 89.05 | vless | 339.6 | 10.7 | 19.92 | 14.6 | 8.88 | 10.17 | 17.8 | Au1rxx-base64 | 195.123.235.183 |
| 88.67 | vless | 309.8 | 1.1 | 20.61 | 14.96 | 9.37 | 10.17 | 17.8 | Au1rxx-base64 | 47.251.108.158 |
| 88.65 | shadowsocks | 331.8 | 1.0 | 20.1 | 14.96 | 10.0 | 13.66 | 17.8 | Au1rxx-base64 | 149.22.95.183 |
| 88.12 | vless | 390.8 | 1.1 | 18.73 | 14.96 | 9.22 | 10.17 | 17.8 | Au1rxx-base64 | 169.40.42.225 |
| 88.11 | vless | 409.1 | 2.3 | 18.31 | 14.91 | 9.14 | 10.17 | 17.8 | Au1rxx-base64 | 185.95.231.156 |
| 88.06 | vless | 429.4 | 0.5 | 17.84 | 14.98 | 10.0 | 10.17 | 17.8 | Au1rxx-base64 | 169.40.42.168 |
| 87.93 | trojan | 351.8 | 9.5 | 19.63 | 14.65 | 10.0 | 8.85 | 17.8 | Au1rxx-base64 | 66.23.203.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.934 | 0.93 | 43 | 567 | prefer |
| Au1rxx-base64 | 0.879 | 0.818 | 258 | 1587 | prefer |
| mheidari-all | 0.753 | 0.68 | 50 | 24286 | prefer |
| Surfboard-tg-vless | 0.519 | 1.0 | 5 | 5474 | observe |
| Surfboard-tg-mixed | 0.373 | 0.6 | 5 | 7219 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4911 | observe |
| Epodonios-all | 0.255 | None | 0 | 7679 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10364 | observe |
| barry-far-vless | 0.255 | None | 0 | 5757 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4150 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 43 |
| 204 | ProxyError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| speed | ClientOSError | - | 2 |
| geo | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 115 | 65 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
