# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-04 19:25:53 |
| 运行耗时 | 193.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 78729 |
| 去重后节点 | 23672 |
| TCP 可达 | 3000 |
| 真实可用 | 202 |
| Verified 输出 | 202 |
| Global 输出 | 208 |
| All 输出 | 23672 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 31.0 |
| probe | 47.4 |
| real_test | 70.3 |
| generate | 38.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45339 |
| trojan | 12689 |
| vmess | 10543 |
| shadowsocks | 9501 |
| hysteria2 | 297 |
| shadowsocksr | 144 |
| http | 135 |
| socks | 71 |
| hysteria | 6 |
| tuic | 3 |
| anytls | 1 |

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
| 76.9 | shadowsocks | 225.3 | 601.9 | 22.56 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 108.181.118.10 |
| 76.57 | shadowsocks | 239.8 | 615.4 | 22.23 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 108.181.0.177 |
| 76.55 | shadowsocks | 262.1 | 642.2 | 21.71 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 156.146.38.170 |
| 76.51 | shadowsocks | 264.0 | 609.3 | 21.67 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 156.146.38.168 |
| 76.51 | shadowsocks | 264.0 | 649.7 | 21.67 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 156.146.38.169 |
| 76.26 | shadowsocks | 254.9 | 624.9 | 21.88 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 156.146.38.167 |
| 73.01 | shadowsocks | 280.3 | 287.9 | 21.29 | 4.2 | 9.88 | 12.86 | 15.98 | Au1rxx-base64 | 149.22.87.204 |
| 72.39 | shadowsocks | 280.6 | 605.7 | 21.28 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 149.22.95.183 |
| 70.57 | shadowsocks | 301.6 | 340.3 | 20.8 | 2.24 | 9.9 | 12.86 | 15.98 | Au1rxx-base64 | 149.22.87.241 |
| 70.08 | shadowsocks | 310.2 | 578.8 | 20.6 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 173.244.56.9 |
| 69.6 | shadowsocks | 306.0 | 363.4 | 20.7 | 1.37 | 9.9 | 12.86 | 15.98 | Au1rxx-base64 | 149.22.87.240 |
| 69.5 | trojan | 318.4 | 745.0 | 20.41 | 0.0 | 10.0 | 10.05 | 14.54 | DeltaKronecker-all | 45.32.195.168 |
| 69.5 | shadowsocks | 344.7 | 707.6 | 19.8 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 173.244.56.6 |
| 68.91 | trojan | 317.2 | 731.9 | 20.44 | 0.0 | 10.0 | 10.05 | 14.54 | DeltaKronecker-all | 45.32.198.247 |
| 68.9 | shadowsocks | 360.8 | 733.3 | 19.43 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 37.19.198.236 |
| 68.73 | shadowsocks | 350.4 | 704.2 | 19.67 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 37.19.198.160 |
| 68.64 | shadowsocks | 356.0 | 752.6 | 19.54 | 0.0 | 10.0 | 12.86 | 16.08 | mheidari-all | 108.181.57.93 |
| 68.14 | trojan | 398.2 | 951.3 | 18.56 | 0.0 | 10.0 | 10.05 | 16.08 | mheidari-all | 64.94.95.118 |
| 67.97 | vless | 241.8 | 648.2 | 22.18 | 0.0 | 10.0 | 5.82 | 16.08 | mheidari-all | 107.173.237.146 |
| 67.8 | shadowsocks | 345.0 | 707.5 | 19.79 | 0.0 | 10.0 | 12.86 | 15.98 | Au1rxx-base64 | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.852 | 0.871 | 31 | 100 | prefer |
| Surfboard-tg-mixed | 0.697 | 0.62 | 92 | 6107 | observe |
| mheidari-all | 0.667 | 0.59 | 61 | 16429 | observe |
| DeltaKronecker-all | 0.604 | 0.524 | 82 | 7309 | observe |
| nscl5-all | 0.303 | 1.0 | 1 | 1189 | observe |
| tg-ConfigV2rayNG | 0.263 | 1.0 | 1 | 200 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 6997 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6970 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4528 | observe |
| barry-far-vless | 0.255 | None | 0 | 5100 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5366 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 30 |
| 204 | ProxyError | - | 24 |
| 204 | ClientOSError | - | 12 |
| geo | TimeoutError | - | 10 |
| cn-block | TimeoutError | - | 10 |
| speed | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 202 | - |
| global | False | 300 | 208 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
