# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 16:52:07 |
| 运行耗时 | 311.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99080 |
| 去重后节点 | 27737 |
| TCP 可达 | 3000 |
| 真实可用 | 409 |
| Verified 输出 | 81 |
| Global 输出 | 300 |
| All 输出 | 27737 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| geo | 1.6 |
| tcp | 86.1 |
| probe | 95.5 |
| real_test | 89.4 |
| china_check | 17.4 |
| write_verified | 0.0 |
| generate | 14.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58328 |
| vmess | 16378 |
| shadowsocks | 12064 |
| trojan | 10071 |
| hysteria2 | 1302 |
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
| 95.2 | hysteria2 | 248.0 | 4.3 | 22.04 | 14.84 | 10.0 | 13.24 | 16.58 | Au1rxx-base64 | 129.213.91.185 |
| 92.72 | vless | 248.0 | 7.1 | 22.04 | 14.73 | 10.0 | 9.37 | 16.58 | Au1rxx-base64 | 147.45.60.160 |
| 92.26 | shadowsocks | 265.2 | 1.6 | 21.64 | 14.94 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 37.19.198.244 |
| 92.19 | shadowsocks | 266.7 | 2.3 | 21.6 | 14.91 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 37.19.198.236 |
| 91.99 | shadowsocks | 266.7 | 7.7 | 21.6 | 14.71 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 37.19.198.243 |
| 91.7 | shadowsocks | 279.5 | 7.9 | 21.31 | 14.71 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 37.19.198.160 |
| 89.98 | vless | 375.1 | 1.7 | 19.09 | 14.94 | 10.0 | 9.37 | 16.58 | Au1rxx-base64 | 185.95.231.156 |
| 89.14 | shadowsocks | 295.2 | 0.2 | 20.95 | 14.99 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 156.146.38.167 |
| 88.51 | shadowsocks | 297.2 | 1.3 | 20.9 | 14.95 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 156.146.38.168 |
| 88.49 | shadowsocks | 322.3 | 1.4 | 20.32 | 14.95 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 156.146.38.170 |
| 87.82 | vless | 432.8 | 10.5 | 17.76 | 14.61 | 9.5 | 9.37 | 16.58 | Au1rxx-base64 | 159.89.87.21 |
| 87.76 | http | 260.9 | 1.6 | 21.74 | 14.94 | 0.0 | 14.26 | 19.82 | ermaozi | 198.44.135.19 |
| 87.18 | vless | 338.1 | 6.7 | 19.95 | 14.75 | 6.89 | 9.37 | 16.58 | Au1rxx-base64 | 195.211.98.43 |
| 86.69 | shadowsocks | 279.1 | 0.8 | 21.32 | 14.97 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 156.146.38.169 |
| 86.04 | hysteria2 | 401.5 | 1.2 | 18.48 | 14.96 | 9.89 | 13.24 | 16.58 | Au1rxx-base64 | 62.210.124.146 |
| 85.94 | vless | 338.7 | 11.9 | 19.94 | 14.55 | 10.0 | 9.37 | 16.58 | Au1rxx-base64 | 104.243.33.154 |
| 85.8 | vless | 316.9 | 1.8 | 20.44 | 14.93 | 10.0 | 9.37 | 16.58 | Au1rxx-base64 | 131.143.180.110 |
| 85.78 | vless | 300.5 | 7.8 | 20.82 | 14.71 | 6.5 | 9.37 | 16.58 | Au1rxx-base64 | 66.70.179.198 |
| 84.63 | shadowsocks | 335.7 | 4.1 | 20.01 | 14.85 | 10.0 | 13.1 | 16.58 | Au1rxx-base64 | 173.244.56.6 |
| 84.35 | http | 354.8 | 2.7 | 19.57 | 14.9 | 0.0 | 14.26 | 19.82 | ermaozi | 206.223.183.16 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.991 | 0.983 | 58 | 618 | prefer |
| Au1rxx-base64 | 0.833 | 0.755 | 444 | 1991 | prefer |
| mheidari-all | 0.762 | 0.7 | 20 | 23974 | prefer |
| Surfboard-tg-mixed | 0.391 | 1.0 | 2 | 7090 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 79 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1991 | observe |
| Epodonios-all | 0.255 | None | 0 | 7602 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9917 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5572 | observe |
| barry-far-vless | 0.255 | None | 0 | 5822 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 70 |
| speed | ClientOSError | - | 15 |
| 204 | ProxyError | - | 12 |
| 204 | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| geo | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 77 | 81 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
