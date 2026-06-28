# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-28 14:05:39 |
| 运行耗时 | 288.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 76210 |
| 去重后节点 | 22925 |
| TCP 可达 | 3000 |
| 真实可用 | 566 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22925 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 30.8 |
| probe | 62.0 |
| real_test | 159.9 |
| generate | 29.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43100 |
| trojan | 12218 |
| vmess | 11020 |
| shadowsocks | 9303 |
| hysteria2 | 229 |
| shadowsocksr | 156 |
| http | 135 |
| socks | 41 |
| hysteria | 6 |
| tuic | 2 |

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
| 78.86 | vless | 320.2 | 819.4 | 20.37 | 0.0 | 10.0 | 11.37 | 17.64 | mheidari-all | 47.253.226.114 |
| 77.8 | shadowsocks | 253.2 | 617.2 | 21.92 | 0.0 | 10.0 | 12.24 | 17.64 | mheidari-all | 198.98.53.130 |
| 76.75 | shadowsocks | 275.1 | 674.0 | 21.41 | 0.0 | 10.0 | 12.24 | 17.64 | mheidari-all | 108.181.57.93 |
| 76.7 | shadowsocks | 255.7 | 627.3 | 21.86 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 156.146.38.167 |
| 76.59 | shadowsocks | 260.2 | 645.1 | 21.75 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 156.146.38.168 |
| 76.48 | shadowsocks | 265.0 | 650.7 | 21.64 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 37.19.198.160 |
| 76.28 | shadowsocks | 273.6 | 665.5 | 21.44 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 37.19.198.244 |
| 76.28 | shadowsocks | 273.9 | 681.8 | 21.44 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 37.19.198.243 |
| 76.2 | shadowsocks | 257.1 | 629.6 | 21.83 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 156.146.38.170 |
| 75.52 | shadowsocks | 306.6 | 785.5 | 20.68 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 37.19.198.236 |
| 75.16 | vless | 286.2 | 675.5 | 21.15 | 0.0 | 10.0 | 11.37 | 13.64 | DeltaKronecker-all | 198.41.209.87 |
| 75.12 | vless | 297.0 | 701.5 | 20.9 | 0.0 | 10.0 | 11.37 | 16.78 | Surfboard-tg-mixed | 137.184.218.169 |
| 74.88 | shadowsocks | 247.9 | 615.0 | 22.04 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 156.146.38.169 |
| 74.51 | vless | 279.3 | 668.3 | 21.31 | 0.0 | 10.0 | 11.37 | 13.64 | DeltaKronecker-all | 104.25.161.29 |
| 73.43 | vless | 278.7 | 661.9 | 21.33 | 0.0 | 10.0 | 11.37 | 13.64 | DeltaKronecker-all | 104.19.142.226 |
| 72.99 | vless | 280.6 | 665.5 | 21.28 | 0.0 | 10.0 | 11.37 | 13.64 | DeltaKronecker-all | 104.17.90.246 |
| 72.27 | vless | 360.2 | 639.6 | 19.44 | 0.0 | 10.0 | 11.37 | 17.64 | mheidari-all | 34.213.172.16 |
| 71.61 | shadowsocks | 291.0 | 571.2 | 21.04 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 149.22.95.183 |
| 71.5 | vless | 325.9 | 639.1 | 20.23 | 0.0 | 10.0 | 11.37 | 16.78 | Surfboard-tg-mixed | 38.244.21.164 |
| 71.48 | shadowsocks | 287.4 | 585.4 | 21.12 | 0.0 | 10.0 | 12.24 | 16.6 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.865 | 0.787 | 333 | 16291 | prefer |
| Au1rxx-base64 | 0.794 | 0.8 | 55 | 109 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.716 | 243 | 5019 | prefer |
| DeltaKronecker-all | 0.538 | 0.457 | 105 | 6788 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1174 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7519 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7282 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3723 | observe |
| barry-far-vless | 0.255 | None | 0 | 4502 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5325 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 88 |
| 204 | TimeoutError | - | 26 |
| geo | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| speed | TimeoutError | - | 12 |
| geo | TimeoutError | - | 12 |
| 204 | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 7 |
| speed | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
