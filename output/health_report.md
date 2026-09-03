# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-03 11:03:07 |
| 运行耗时 | 299.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82567 |
| 去重后节点 | 22929 |
| TCP 可达 | 3000 |
| 真实可用 | 553 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22929 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.5 |
| tcp | 37.8 |
| probe | 89.6 |
| real_test | 126.3 |
| generate | 38.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51705 |
| vmess | 11434 |
| shadowsocks | 9815 |
| trojan | 7658 |
| hysteria2 | 1587 |
| http | 138 |
| shadowsocksr | 125 |
| socks | 84 |
| tuic | 11 |
| hysteria | 10 |

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
| 81.61 | shadowsocks | 265.7 | 611.0 | 21.63 | 0.0 | 10.0 | 14.52 | 19.46 | Au1rxx-base64 | 156.146.38.170 |
| 81.56 | vless | 189.9 | 487.2 | 23.38 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.233.156.118 |
| 81.5 | vless | 192.6 | 502.7 | 23.32 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.236.252.35 |
| 81.4 | vless | 197.0 | 507.1 | 23.22 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.233.139.46 |
| 81.37 | vless | 198.1 | 518.4 | 23.19 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.235.43.210 |
| 81.37 | shadowsocks | 263.1 | 642.0 | 21.69 | 0.0 | 10.0 | 14.52 | 19.46 | Au1rxx-base64 | 156.146.38.169 |
| 81.34 | vless | 199.4 | 509.3 | 23.16 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.233.156.123 |
| 81.31 | vless | 200.9 | 524.1 | 23.13 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.239.67.156 |
| 81.19 | vless | 206.0 | 537.7 | 23.01 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.239.67.231 |
| 81.0 | hysteria2 | 411.7 | 1073.0 | 18.25 | 0.0 | 10.0 | 14.29 | 19.46 | Au1rxx-base64 | 66.94.121.46 |
| 80.97 | vless | 215.3 | 521.4 | 22.79 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 172.235.38.85 |
| 80.95 | vless | 216.4 | 515.3 | 22.77 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 45.79.103.108 |
| 80.95 | vless | 216.5 | 511.6 | 22.77 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 45.33.107.237 |
| 79.86 | vless | 263.5 | 627.5 | 21.68 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 74.207.245.124 |
| 79.79 | vless | 266.3 | 649.1 | 21.61 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 192.155.87.188 |
| 79.33 | http | 398.4 | 1108.7 | 18.55 | 0.0 | 10.0 | 14.44 | 19.34 | zhangkai | 138.199.35.216 |
| 79.3 | http | 400.0 | 1114.6 | 18.52 | 0.0 | 10.0 | 14.44 | 19.34 | zhangkai | 138.199.35.198 |
| 78.51 | shadowsocks | 269.7 | 494.5 | 21.53 | 0.0 | 10.0 | 14.52 | 19.46 | Au1rxx-base64 | 173.244.56.9 |
| 76.74 | vless | 259.5 | 629.6 | 21.77 | 0.0 | 10.0 | 8.72 | 19.46 | Au1rxx-base64 | 50.116.9.184 |
| 76.46 | shadowsocks | 331.4 | 727.2 | 20.11 | 0.0 | 10.0 | 14.52 | 19.46 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | 0.909 | 329 | 1751 | prefer |
| zhangkai | 0.922 | 0.955 | 22 | 144 | prefer |
| mheidari-all | 0.84 | 0.764 | 123 | 16145 | prefer |
| Surfboard-tg-mixed | 0.82 | 0.743 | 171 | 7139 | prefer |
| DeltaKronecker-all | 0.684 | 0.786 | 14 | 6335 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 87 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4671 | observe |
| Epodonios-all | 0.255 | None | 0 | 7527 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8132 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6006 | observe |
| barry-far-vless | 0.255 | None | 0 | 6217 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4081 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 22 |
| 204 | TimeoutError | - | 20 |
| geo | ClientOSError | - | 19 |
| speed | TimeoutError | - | 13 |
| 204 | ProxyError | - | 9 |
| geo | TimeoutError | - | 5 |
| speed | ClientOSError | - | 5 |
| 204 | ProxyConnectionError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
