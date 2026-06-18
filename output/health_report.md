# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-18 05:06:50 |
| 运行耗时 | 234.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 107 |
| 原始节点 | 70294 |
| 去重后节点 | 22593 |
| TCP 可达 | 786 |
| 真实可用 | 636 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22593 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 58.4 |
| probe | 100.0 |
| real_test | 37.0 |
| generate | 33.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 38486 |
| trojan | 10528 |
| shadowsocks | 10504 |
| vmess | 10229 |
| hysteria2 | 226 |
| shadowsocksr | 160 |
| http | 107 |
| socks | 46 |
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
| 78.36 | shadowsocks | 225.1 | 603.6 | 22.57 | 0.0 | 10.0 | 14.09 | 17.2 | mheidari-all | 198.98.53.130 |
| 78.2 | shadowsocks | 227.4 | 620.7 | 22.51 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 37.19.198.160 |
| 78.09 | shadowsocks | 232.5 | 633.2 | 22.4 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 37.19.198.243 |
| 77.95 | shadowsocks | 238.3 | 643.9 | 22.26 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 37.19.198.244 |
| 77.8 | trojan | 256.1 | 650.7 | 21.85 | 0.0 | 10.0 | 12.95 | 19.0 | Surfboard-tg-mixed | 207.126.167.150 |
| 77.02 | shadowsocks | 278.5 | 770.7 | 21.33 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 37.19.198.236 |
| 74.95 | shadowsocks | 281.3 | 645.7 | 21.27 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 156.146.38.167 |
| 74.69 | trojan | 334.8 | 885.8 | 20.03 | 0.0 | 10.0 | 12.95 | 19.0 | Surfboard-tg-mixed | 45.61.52.243 |
| 74.66 | shadowsocks | 353.2 | 833.0 | 19.6 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 107.172.250.161 |
| 73.58 | shadowsocks | 318.3 | 767.4 | 20.41 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 156.146.38.170 |
| 73.45 | shadowsocks | 318.8 | 765.1 | 20.4 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 149.28.255.6 |
| 73.32 | shadowsocks | 278.3 | 644.0 | 21.34 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 156.146.38.169 |
| 72.62 | shadowsocks | 316.6 | 756.5 | 20.45 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 156.146.38.168 |
| 72.6 | vless | 302.9 | 843.6 | 20.77 | 0.0 | 10.0 | 10.33 | 19.0 | Surfboard-tg-mixed | 137.184.218.169 |
| 71.57 | trojan | 382.8 | 899.2 | 18.92 | 0.0 | 10.0 | 12.95 | 17.2 | mheidari-all | 207.126.167.241 |
| 71.25 | vless | 361.1 | 919.2 | 19.42 | 0.0 | 10.0 | 10.33 | 19.0 | Surfboard-tg-mixed | 37.1.212.241 |
| 70.99 | shadowsocks | 249.5 | 653.2 | 22.0 | 0.0 | 10.0 | 14.09 | 10.4 | DeltaKronecker-all | 108.181.57.93 |
| 70.88 | vless | 294.9 | 815.8 | 20.95 | 0.0 | 10.0 | 10.33 | 17.1 | Au1rxx-base64 | 159.89.87.21 |
| 70.85 | vless | 347.0 | 896.3 | 19.75 | 0.0 | 10.0 | 10.33 | 17.2 | mheidari-all | 185.156.47.96 |
| 70.39 | shadowsocks | 330.3 | 595.9 | 20.13 | 0.0 | 10.0 | 14.09 | 17.1 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.985 | 0.907 | 344 | 4586 | prefer |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| Au1rxx-base64 | 0.866 | 0.87 | 77 | 126 | prefer |
| mheidari-all | 0.856 | 0.778 | 212 | 13927 | prefer |
| DeltaKronecker-all | 0.608 | 0.529 | 121 | 7763 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.289 | 1.0 | 1 | 847 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4274 | observe |
| Epodonios-all | 0.255 | None | 0 | 6401 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3977 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 5959 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3590 | observe |
| barry-far-vless | 0.255 | None | 0 | 4240 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 53 |
| speed | ClientOSError | - | 36 |
| general | unknown | - | 27 |
| geo | ClientOSError | - | 13 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |
| 204 | ProxyError | - | 4 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
