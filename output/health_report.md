# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-24 19:58:15 |
| 运行耗时 | 248.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76862 |
| 去重后节点 | 22607 |
| TCP 可达 | 3000 |
| 真实可用 | 396 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22607 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 29.7 |
| probe | 55.8 |
| real_test | 112.1 |
| generate | 44.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45372 |
| trojan | 10850 |
| vmess | 10232 |
| shadowsocks | 9807 |
| hysteria2 | 234 |
| shadowsocksr | 164 |
| http | 129 |
| socks | 66 |
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
| 77.37 | shadowsocks | 235.8 | 635.9 | 22.32 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 37.19.198.244 |
| 77.27 | shadowsocks | 239.9 | 645.4 | 22.22 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 37.19.198.243 |
| 77.19 | shadowsocks | 243.6 | 649.4 | 22.14 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 37.19.198.160 |
| 74.35 | shadowsocks | 271.1 | 627.6 | 21.5 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 156.146.38.168 |
| 74.09 | shadowsocks | 355.7 | 970.0 | 19.54 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 108.181.57.93 |
| 74.08 | shadowsocks | 277.5 | 636.8 | 21.36 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 156.146.38.170 |
| 73.76 | shadowsocks | 278.0 | 639.5 | 21.34 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 156.146.38.169 |
| 73.72 | vless | 276.0 | 664.9 | 21.39 | 0.0 | 10.0 | 9.91 | 16.42 | Surfboard-tg-mixed | 104.16.9.20 |
| 73.42 | shadowsocks | 282.6 | 653.1 | 21.24 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 156.146.38.167 |
| 70.79 | shadowsocks | 251.4 | 667.0 | 21.96 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 198.98.53.130 |
| 70.79 | vless | 496.0 | 1276.5 | 16.3 | 0.0 | 10.0 | 9.91 | 16.42 | Surfboard-tg-mixed | 15.223.121.250 |
| 70.01 | shadowsocks | 319.1 | 597.1 | 20.39 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 173.244.56.9 |
| 69.83 | shadowsocks | 302.7 | 578.4 | 20.77 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 173.244.56.6 |
| 68.83 | shadowsocks | 353.1 | 650.9 | 19.6 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 149.22.95.183 |
| 67.99 | shadowsocks | 403.4 | 1066.0 | 18.44 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 172.234.202.34 |
| 67.34 | vless | 285.2 | 670.2 | 21.18 | 0.0 | 10.0 | 9.91 | 13.54 | DeltaKronecker-all | 162.159.252.15 |
| 67.09 | shadowsocks | 312.5 | 848.5 | 20.54 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 66.98 | trojan | 397.4 | 758.1 | 18.58 | 0.0 | 10.0 | 10.52 | 16.1 | Au1rxx-base64 | 45.61.52.243 |
| 66.95 | shadowsocks | 290.3 | 782.6 | 21.06 | 0.0 | 10.0 | 12.95 | 16.1 | Au1rxx-base64 | 147.90.234.133 |
| 66.45 | vless | 322.5 | 646.4 | 20.31 | 0.0 | 10.0 | 9.91 | 16.42 | Surfboard-tg-mixed | 92.223.71.246 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Au1rxx-base64 | 0.801 | 0.806 | 62 | 114 | prefer |
| Surfboard-tg-mixed | 0.744 | 0.665 | 233 | 5375 | prefer |
| mheidari-all | 0.731 | 0.652 | 187 | 15681 | prefer |
| DeltaKronecker-all | 0.558 | 0.477 | 65 | 6644 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1140 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4745 | observe |
| Epodonios-all | 0.255 | None | 0 | 8092 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3985 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7510 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4084 | observe |
| barry-far-vless | 0.255 | None | 0 | 4852 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4710 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 71 |
| 204 | TimeoutError | - | 31 |
| cn-block | TimeoutError | - | 27 |
| geo | TimeoutError | - | 12 |
| 204 | ProxyError | - | 11 |
| 204 | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 8 |
| geo | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
