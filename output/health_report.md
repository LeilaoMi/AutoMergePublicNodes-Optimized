# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-28 06:00:25 |
| 运行耗时 | 317.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 97707 |
| 去重后节点 | 26826 |
| TCP 可达 | 3000 |
| 真实可用 | 527 |
| Verified 输出 | 68 |
| Global 输出 | 300 |
| All 输出 | 26826 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.5 |
| tcp | 79.1 |
| probe | 99.3 |
| real_test | 92.0 |
| china_check | 25.2 |
| write_verified | 0.0 |
| generate | 13.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57234 |
| vmess | 17654 |
| shadowsocks | 12929 |
| trojan | 8094 |
| hysteria2 | 1369 |
| shadowsocksr | 164 |
| http | 162 |
| socks | 54 |
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
| 98.55 | hysteria2 | 243.2 | 1.0 | 22.15 | 14.96 | 10.0 | 14.0 | 18.94 | Au1rxx-base64 | 129.213.91.185 |
| 95.82 | shadowsocks | 256.7 | 2.0 | 21.84 | 14.92 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 37.19.198.243 |
| 95.74 | shadowsocks | 253.5 | 6.1 | 21.91 | 14.77 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 37.19.198.244 |
| 95.67 | shadowsocks | 261.3 | 3.2 | 21.73 | 14.88 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 37.19.198.236 |
| 95.57 | shadowsocks | 248.9 | 0.2 | 22.02 | 14.99 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 193.151.163.18 |
| 94.74 | vless | 355.3 | 5.6 | 19.55 | 14.79 | 10.0 | 11.46 | 18.94 | Au1rxx-base64 | 169.40.42.104 |
| 94.36 | vless | 378.7 | 1.4 | 19.01 | 14.95 | 10.0 | 11.46 | 18.94 | Au1rxx-base64 | 169.40.42.235 |
| 93.47 | vless | 295.4 | 2.4 | 20.94 | 14.91 | 7.31 | 11.46 | 18.94 | Au1rxx-base64 | 66.70.179.198 |
| 93.43 | vless | 395.3 | 0.6 | 18.63 | 14.98 | 10.0 | 11.46 | 18.94 | Au1rxx-base64 | 169.40.42.163 |
| 93.35 | shadowsocks | 333.2 | 7.1 | 20.06 | 14.73 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 45.86.51.18 |
| 93.23 | trojan | 425.1 | 6.4 | 17.94 | 14.76 | 10.0 | 14.59 | 18.94 | Au1rxx-base64 | 69.164.240.85 |
| 93.21 | vless | 342.2 | 6.1 | 19.86 | 14.77 | 8.18 | 11.46 | 18.94 | Au1rxx-base64 | 169.40.42.202 |
| 92.93 | shadowsocks | 358.4 | 3.0 | 19.48 | 14.89 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 15.204.233.41 |
| 92.55 | shadowsocks | 344.0 | 21.8 | 19.81 | 14.18 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 15.204.246.132 |
| 92.43 | shadowsocks | 381.7 | 1.9 | 18.94 | 14.93 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 193.151.160.9 |
| 92.3 | vless | 346.4 | 2.4 | 19.76 | 14.91 | 10.0 | 11.46 | 18.94 | Au1rxx-base64 | 169.40.42.231 |
| 91.93 | vless | 361.3 | 3.7 | 19.41 | 14.86 | 7.26 | 11.46 | 18.94 | Au1rxx-base64 | 185.95.231.156 |
| 91.89 | shadowsocks | 293.5 | 1.2 | 20.98 | 14.95 | 9.77 | 14.12 | 18.94 | Au1rxx-base64 | 156.146.38.170 |
| 91.81 | shadowsocks | 286.9 | 1.8 | 21.14 | 14.93 | 10.0 | 14.12 | 18.94 | Au1rxx-base64 | 156.146.38.167 |
| 91.02 | trojan | 381.4 | 8.8 | 18.95 | 14.67 | 10.0 | 14.59 | 18.94 | Au1rxx-base64 | 66.23.203.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.966 | 0.959 | 74 | 467 | prefer |
| Au1rxx-base64 | 0.946 | 0.88 | 334 | 1707 | prefer |
| zhangkai | 0.923 | 1.0 | 19 | 43 | prefer |
| Surfboard-tg-mixed | 0.755 | 0.677 | 161 | 7522 | prefer |
| roosterkid-openproxylist-v2ray | 0.494 | 0.875 | 8 | 150 | observe |
| mheidari-all | 0.46 | 0.377 | 77 | 24790 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 10431 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4988 | observe |
| Epodonios-all | 0.255 | None | 0 | 8008 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5538 | observe |
| barry-far-vless | 0.255 | None | 0 | 5751 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4500 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 94 |
| geo | ClientOSError | - | 32 |
| 204 | ProxyError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 3 |
| speed | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 85 | 68 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
