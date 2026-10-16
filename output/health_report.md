# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 15:03:20 |
| 运行耗时 | 311.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99199 |
| 去重后节点 | 27691 |
| TCP 可达 | 3000 |
| 真实可用 | 393 |
| Verified 输出 | 79 |
| Global 输出 | 300 |
| All 输出 | 27691 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 87.1 |
| probe | 96.0 |
| real_test | 86.8 |
| china_check | 18.1 |
| write_verified | 0.0 |
| generate | 14.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58478 |
| vmess | 16400 |
| shadowsocks | 11980 |
| trojan | 10095 |
| hysteria2 | 1309 |
| http | 662 |
| shadowsocksr | 164 |
| socks | 59 |
| anytls | 29 |
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
| 94.06 | vless | 191.5 | 0.3 | 23.35 | 14.99 | 10.0 | 9.94 | 15.78 | Au1rxx-base64 | 131.143.180.110 |
| 91.54 | vless | 217.3 | 1.9 | 22.75 | 14.93 | 8.14 | 9.94 | 15.78 | Au1rxx-base64 | 154.12.38.202 |
| 90.9 | vless | 324.1 | 2.7 | 20.28 | 14.9 | 10.0 | 9.94 | 15.78 | Au1rxx-base64 | 51.81.203.63 |
| 89.12 | shadowsocks | 286.9 | 2.7 | 21.14 | 14.9 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 149.22.95.183 |
| 88.96 | hysteria2 | 348.9 | 3.8 | 19.7 | 14.86 | 10.0 | 13.85 | 15.78 | Au1rxx-base64 | 129.213.91.185 |
| 88.3 | vless | 206.5 | 0.1 | 23.0 | 15.0 | 4.58 | 9.94 | 15.78 | Au1rxx-base64 | 154.29.159.211 |
| 88.1 | http | 218.7 | 8.7 | 22.72 | 14.67 | 0.0 | 14.03 | 19.18 | ermaozi | fan.365747.xyz |
| 87.63 | vless | 319.9 | 6.5 | 20.37 | 14.76 | 10.0 | 9.94 | 15.78 | Au1rxx-base64 | 147.45.60.160 |
| 87.59 | vless | 256.8 | 0.9 | 21.83 | 14.96 | 7.56 | 9.94 | 15.78 | Au1rxx-base64 | 44.248.233.99 |
| 87.32 | http | 263.1 | 2.0 | 21.69 | 14.92 | 0.0 | 14.03 | 19.18 | ermaozi | 167.88.60.242 |
| 85.73 | shadowsocks | 289.6 | 2.7 | 21.07 | 14.9 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.167 |
| 85.73 | shadowsocks | 299.9 | 0.7 | 20.83 | 14.97 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.170 |
| 85.59 | shadowsocks | 294.7 | 0.4 | 20.96 | 14.99 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.168 |
| 85.02 | http | 228.0 | 5.1 | 22.5 | 14.81 | 0.0 | 14.03 | 19.18 | ermaozi | purposebydesig.club |
| 85.01 | shadowsocks | 375.6 | 0.2 | 19.08 | 14.99 | 7.86 | 11.3 | 15.78 | Au1rxx-base64 | 173.244.56.9 |
| 84.34 | shadowsocks | 287.2 | 1.2 | 21.13 | 14.95 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 173.244.56.6 |
| 83.16 | http | 204.6 | 2.3 | 23.04 | 14.91 | 0.0 | 14.03 | 19.18 | ermaozi | 138.199.35.198 |
| 82.96 | http | 208.2 | 5.5 | 22.96 | 14.79 | 0.0 | 14.03 | 19.18 | ermaozi | 138.199.35.216 |
| 82.96 | vless | 335.2 | 0.4 | 20.02 | 14.98 | 9.77 | 9.94 | 15.78 | Au1rxx-base64 | 156.246.88.125 |
| 82.8 | shadowsocks | 297.2 | 1.7 | 20.9 | 14.94 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 1.0 | 59 | 618 | prefer |
| Au1rxx-base64 | 0.833 | 0.755 | 424 | 1991 | prefer |
| mheidari-all | 0.625 | 0.55 | 20 | 23974 | observe |
| Surfboard-tg-mixed | 0.32 | 0.5 | 4 | 7090 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1991 | observe |
| Epodonios-all | 0.255 | None | 0 | 7568 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10094 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5572 | observe |
| barry-far-vless | 0.255 | None | 0 | 5822 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 61 |
| speed | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 6 |
| geo | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 4 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 4 |
| speed | ProxyError | - | 1 |
| cn-block | status | 530 | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 50 | 79 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
