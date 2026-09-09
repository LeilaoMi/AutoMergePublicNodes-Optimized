# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-09 16:29:56 |
| 运行耗时 | 657.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 84876 |
| 去重后节点 | 22038 |
| TCP 可达 | 3000 |
| 真实可用 | 402 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22038 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 36.9 |
| probe | 271.3 |
| real_test | 261.7 |
| generate | 79.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51926 |
| vmess | 12415 |
| shadowsocks | 9945 |
| trojan | 7995 |
| hysteria2 | 1831 |
| http | 560 |
| shadowsocksr | 133 |
| socks | 52 |
| hysteria | 9 |
| tuic | 8 |
| anytls | 2 |

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
| 84.48 | hysteria2 | 206.9 | 528.7 | 22.99 | 0.0 | 10.0 | 12.75 | 19.74 | Au1rxx-base64 | 66.94.121.46 |
| 84.27 | vless | 229.7 | 595.4 | 22.46 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 172.233.139.46 |
| 83.86 | vless | 247.5 | 483.3 | 22.05 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 172.235.38.85 |
| 83.35 | vless | 269.4 | 553.9 | 21.54 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 38.209.125.45 |
| 82.67 | vless | 298.9 | 781.8 | 20.86 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 15.204.97.216 |
| 79.26 | shadowsocks | 230.8 | 557.5 | 22.43 | 0.0 | 10.0 | 13.89 | 16.94 | mheidari-all | 173.244.56.9 |
| 78.57 | vless | 260.0 | 641.2 | 21.76 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 31.58.50.200 |
| 78.45 | vless | 481.1 | 1269.4 | 16.64 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 51.81.203.63 |
| 78.43 | shadowsocks | 245.5 | 634.7 | 22.1 | 0.0 | 10.0 | 13.89 | 16.94 | mheidari-all | 108.181.118.10 |
| 78.35 | shadowsocks | 237.4 | 572.6 | 22.28 | 0.0 | 10.0 | 13.89 | 17.26 | Surfboard-tg-mixed | 149.22.95.183 |
| 78.02 | vless | 251.1 | 626.7 | 21.96 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 38.246.229.58 |
| 77.96 | shadowsocks | 287.1 | 706.3 | 21.13 | 0.0 | 10.0 | 13.89 | 16.94 | mheidari-all | 173.244.56.6 |
| 77.3 | vless | 323.8 | 853.8 | 20.28 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 15.204.97.198 |
| 77.04 | vless | 328.3 | 333.5 | 20.18 | 2.49 | 9.94 | 12.07 | 19.74 | Au1rxx-base64 | 154.31.114.248 |
| 76.67 | vless | 333.3 | 337.3 | 20.06 | 2.35 | 9.94 | 12.07 | 19.74 | Au1rxx-base64 | 13.114.124.85 |
| 76.31 | vless | 339.0 | 341.5 | 19.93 | 2.19 | 9.94 | 12.07 | 19.74 | Au1rxx-base64 | 13.230.66.70 |
| 76.22 | vless | 341.2 | 344.3 | 19.88 | 2.09 | 9.94 | 12.07 | 19.74 | Au1rxx-base64 | 13.231.7.104 |
| 76.2 | vless | 250.8 | 630.7 | 21.97 | 0.0 | 10.0 | 12.07 | 19.74 | Au1rxx-base64 | 38.244.20.152 |
| 76.2 | vless | 338.9 | 343.6 | 19.93 | 2.11 | 9.9 | 12.07 | 19.74 | Au1rxx-base64 | 13.231.19.51 |
| 76.18 | vless | 339.5 | 347.4 | 19.92 | 1.97 | 9.93 | 12.07 | 19.74 | Au1rxx-base64 | 3.112.131.211 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.916 | 0.853 | 225 | 1634 | prefer |
| Surfboard-tg-mixed | 0.82 | 0.743 | 148 | 7428 | prefer |
| DeltaKronecker-all | 0.749 | 0.923 | 13 | 5187 | prefer |
| mheidari-all | 0.662 | 0.583 | 120 | 16618 | observe |
| ermaozi | 0.609 | 0.6 | 25 | 410 | observe |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 205 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4795 | observe |
| Epodonios-all | 0.255 | None | 0 | 7926 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9327 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6118 | observe |
| barry-far-vless | 0.255 | None | 0 | 6336 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4219 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1634 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 39 |
| cn-block | TimeoutError | - | 27 |
| 204 | ProxyError | - | 23 |
| 204 | TimeoutError | - | 19 |
| cn-block | ClientOSError | - | 10 |
| 204 | ProxyConnectionError | - | 6 |
| geo | TimeoutError | - | 5 |
| speed | TimeoutError | - | 4 |
| speed | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
