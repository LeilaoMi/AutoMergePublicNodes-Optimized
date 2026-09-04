# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-04 16:10:52 |
| 运行耗时 | 324.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 84288 |
| 去重后节点 | 23436 |
| TCP 可达 | 3000 |
| 真实可用 | 595 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23436 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.2 |
| tcp | 37.2 |
| probe | 91.0 |
| real_test | 145.6 |
| generate | 42.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53565 |
| vmess | 11419 |
| shadowsocks | 9598 |
| trojan | 7954 |
| hysteria2 | 1388 |
| http | 144 |
| shadowsocksr | 131 |
| socks | 63 |
| tuic | 15 |
| hysteria | 10 |
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
| 83.63 | vless | 196.1 | 513.2 | 23.24 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 172.235.38.85 |
| 83.38 | vless | 206.8 | 501.3 | 22.99 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 172.233.139.46 |
| 83.24 | vless | 212.9 | 513.1 | 22.85 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 31.58.50.200 |
| 81.29 | shadowsocks | 233.6 | 550.5 | 22.37 | 0.0 | 10.0 | 13.6 | 19.32 | Au1rxx-base64 | 173.244.56.9 |
| 81.26 | http | 202.7 | 493.9 | 23.09 | 0.0 | 10.0 | 13.45 | 17.72 | zhangkai | 138.199.35.216 |
| 81.26 | shadowsocks | 213.4 | 521.3 | 22.84 | 0.0 | 10.0 | 13.6 | 19.32 | Au1rxx-base64 | 108.181.118.10 |
| 81.24 | shadowsocks | 235.6 | 527.6 | 22.32 | 0.0 | 10.0 | 13.6 | 19.32 | Au1rxx-base64 | 173.244.56.6 |
| 80.95 | http | 216.0 | 547.3 | 22.78 | 0.0 | 10.0 | 13.45 | 17.72 | zhangkai | 138.199.35.198 |
| 80.91 | vless | 313.4 | 820.2 | 20.52 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 15.204.97.216 |
| 80.78 | vless | 319.0 | 835.0 | 20.39 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 15.204.97.197 |
| 79.75 | vless | 233.9 | 597.9 | 22.36 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 38.127.121.44 |
| 79.11 | vless | 196.9 | 525.6 | 23.22 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 204.44.127.222 |
| 78.43 | vless | 204.7 | 524.9 | 23.04 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 23.94.227.94 |
| 78.28 | vless | 232.9 | 500.7 | 22.39 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 104.18.34.14 |
| 78.07 | vless | 241.8 | 586.3 | 22.18 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 172.64.158.146 |
| 77.81 | vless | 231.4 | 580.7 | 22.42 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 38.209.125.45 |
| 77.8 | shadowsocks | 236.5 | 561.3 | 22.3 | 0.0 | 10.0 | 13.6 | 15.9 | mheidari-all | 149.22.95.183 |
| 76.8 | vless | 264.9 | 298.6 | 21.65 | 3.8 | 9.92 | 11.07 | 16.76 | Surfboard-tg-mixed | 31.76.91.72 |
| 76.4 | shadowsocks | 303.7 | 667.2 | 20.75 | 0.0 | 10.0 | 13.6 | 19.32 | Au1rxx-base64 | 156.146.38.168 |
| 76.29 | vless | 232.2 | 488.6 | 22.4 | 0.0 | 10.0 | 11.07 | 19.32 | Au1rxx-base64 | 172.64.32.103 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.986 | 0.919 | 356 | 1751 | prefer |
| mheidari-all | 0.848 | 0.772 | 149 | 15927 | prefer |
| zhangkai | 0.806 | 0.826 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.801 | 0.724 | 163 | 7209 | prefer |
| DeltaKronecker-all | 0.661 | 0.833 | 12 | 7089 | observe |
| tg-oneclickvpnkeys | 0.443 | 1.0 | 5 | 104 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4810 | observe |
| Epodonios-all | 0.255 | None | 0 | 7667 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8718 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6091 | observe |
| barry-far-vless | 0.255 | None | 0 | 6339 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4123 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 30 |
| cn-block | TimeoutError | - | 19 |
| cn-block | ClientOSError | - | 14 |
| 204 | ProxyError | - | 12 |
| speed | TimeoutError | - | 10 |
| geo | ClientOSError | - | 10 |
| 204 | ProxyConnectionError | - | 8 |
| speed | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
