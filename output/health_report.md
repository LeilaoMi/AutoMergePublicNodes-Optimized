# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-21 18:49:14 |
| 运行耗时 | 357.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 93362 |
| 去重后节点 | 23312 |
| TCP 可达 | 3000 |
| 真实可用 | 1135 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23312 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 0.9 |
| tcp | 39.2 |
| probe | 69.4 |
| real_test | 196.9 |
| generate | 44.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51618 |
| trojan | 18708 |
| shadowsocks | 10585 |
| vmess | 10282 |
| hysteria2 | 1604 |
| shadowsocksr | 206 |
| http | 167 |
| socks | 132 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 13 |

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
| 83.35 | trojan | 237.9 | 547.1 | 22.27 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 128.14.181.220 |
| 81.36 | http | 272.1 | 628.1 | 21.48 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 81.32 | http | 269.3 | 618.5 | 21.54 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 80.44 | shadowsocks | 294.8 | 784.1 | 20.95 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 80.34 | shadowsocks | 299.2 | 781.1 | 20.85 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 80.28 | shadowsocks | 301.7 | 792.6 | 20.79 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 79.87 | trojan | 264.8 | 520.5 | 21.65 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 35.91.98.35 |
| 79.77 | trojan | 270.3 | 530.9 | 21.52 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 34.223.2.163 |
| 79.7 | shadowsocks | 326.9 | 826.6 | 20.21 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 79.66 | hysteria2 | 290.1 | 634.3 | 21.06 | 0.0 | 10.0 | 14.32 | 16.16 | mheidari-all | 150.241.102.127 |
| 79.55 | trojan | 284.9 | 577.7 | 21.18 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 79.54 | trojan | 278.1 | 565.4 | 21.34 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 44.243.85.47 |
| 79.45 | trojan | 282.2 | 561.1 | 21.25 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 34.222.243.142 |
| 79.42 | trojan | 287.0 | 590.7 | 21.13 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 79.38 | trojan | 283.3 | 572.8 | 21.22 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 79.37 | trojan | 284.0 | 572.4 | 21.2 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 35.91.138.234 |
| 79.36 | trojan | 280.8 | 568.3 | 21.28 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 44.251.158.80 |
| 79.34 | trojan | 291.6 | 591.5 | 21.03 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 54.245.126.186 |
| 79.33 | trojan | 286.0 | 578.0 | 21.16 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 35.90.27.143 |
| 79.25 | trojan | 286.4 | 578.7 | 21.15 | 0.0 | 10.0 | 14.64 | 20.0 | Au1rxx-base64 | 35.88.210.26 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.982 | 678 | 1933 | prefer |
| zhangkai | 0.997 | 1.0 | 113 | 144 | prefer |
| mheidari-all | 0.99 | 0.914 | 220 | 21956 | prefer |
| Surfboard-tg-mixed | 0.905 | 0.829 | 181 | 6488 | prefer |
| nscl5-all | 0.391 | 1.0 | 2 | 3031 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 177 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5148 | observe |
| Epodonios-all | 0.255 | None | 0 | 7155 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7163 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5287 | observe |
| barry-far-vless | 0.255 | None | 0 | 5535 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4091 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 13 |
| geo | TimeoutError | - | 13 |
| 204 | TimeoutError | - | 11 |
| speed | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| 204 | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| speed | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
