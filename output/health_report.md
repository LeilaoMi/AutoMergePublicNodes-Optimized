# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-04 08:51:45 |
| 运行耗时 | 290.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 85567 |
| 去重后节点 | 24255 |
| TCP 可达 | 3000 |
| 真实可用 | 548 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24255 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.4 |
| tcp | 36.9 |
| probe | 65.4 |
| real_test | 152.9 |
| generate | 27.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52325 |
| vmess | 13001 |
| shadowsocks | 10047 |
| trojan | 8931 |
| hysteria2 | 1002 |
| http | 76 |
| shadowsocksr | 74 |
| socks | 72 |
| hysteria | 19 |
| tuic | 10 |
| anytls | 10 |

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
| 82.31 | shadowsocks | 197.0 | 529.3 | 23.22 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 149.22.95.183 |
| 81.39 | hysteria2 | 236.5 | 285.0 | 22.3 | 4.31 | 10.0 | 14.32 | 18.82 | Au1rxx-base64 | 45.76.202.45 |
| 78.89 | shadowsocks | 257.6 | 266.7 | 21.81 | 5.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 149.22.87.204 |
| 78.14 | hysteria2 | 351.8 | 759.3 | 19.63 | 0.0 | 10.0 | 14.32 | 18.82 | Au1rxx-base64 | 138.124.68.188 |
| 77.84 | vless | 267.4 | 675.3 | 21.59 | 0.0 | 10.0 | 7.43 | 18.82 | Au1rxx-base64 | 52.43.158.158 |
| 77.06 | shadowsocks | 285.9 | 625.6 | 21.16 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 108.181.0.177 |
| 76.87 | vless | 300.2 | 737.9 | 20.83 | 0.0 | 10.0 | 7.43 | 18.82 | Au1rxx-base64 | 66.175.217.170 |
| 76.54 | hysteria2 | 408.3 | 891.9 | 18.33 | 0.0 | 10.0 | 14.32 | 18.82 | Au1rxx-base64 | 159.223.157.129 |
| 75.98 | shadowsocks | 280.4 | 331.8 | 21.29 | 2.56 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 149.22.87.240 |
| 75.95 | shadowsocks | 279.0 | 334.4 | 21.32 | 2.46 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 149.22.87.241 |
| 75.95 | shadowsocks | 294.8 | 654.2 | 20.95 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 108.181.118.10 |
| 75.71 | shadowsocks | 306.5 | 639.3 | 20.68 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 156.146.38.168 |
| 75.71 | vless | 316.2 | 796.6 | 20.46 | 0.0 | 10.0 | 7.43 | 18.82 | Au1rxx-base64 | 64.49.38.6 |
| 75.56 | vless | 240.3 | 508.0 | 22.21 | 0.0 | 10.0 | 7.43 | 18.82 | Au1rxx-base64 | 70.39.198.183 |
| 75.27 | shadowsocks | 325.9 | 679.9 | 20.23 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 156.146.38.167 |
| 74.86 | vless | 253.1 | 554.6 | 21.92 | 0.0 | 10.0 | 7.43 | 18.82 | Au1rxx-base64 | 192.204.50.220 |
| 74.58 | shadowsocks | 317.8 | 664.2 | 20.42 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 156.146.38.169 |
| 73.79 | shadowsocks | 320.9 | 602.1 | 20.35 | 0.0 | 10.0 | 14.27 | 18.82 | Au1rxx-base64 | 173.244.56.6 |
| 73.68 | trojan | 330.4 | 667.8 | 20.13 | 0.0 | 10.0 | 12.99 | 18.82 | Au1rxx-base64 | 163.245.196.68 |
| 73.49 | vless | 255.3 | 549.0 | 21.87 | 0.0 | 10.0 | 7.43 | 18.82 | Au1rxx-base64 | 70.39.197.13 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 67 | 92 | prefer |
| Au1rxx-base64 | 0.81 | 0.744 | 589 | 1672 | prefer |
| DeltaKronecker-all | 0.423 | 0.333 | 33 | 5788 | observe |
| mheidari-all | 0.393 | 0.3 | 30 | 20242 | observe |
| Surfboard-tg-mixed | 0.353 | 0.267 | 75 | 5211 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 6811 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 178 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 57 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5251 | observe |
| Epodonios-all | 0.255 | None | 0 | 5819 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4191 | observe |
| barry-far-vless | 0.255 | None | 0 | 4536 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5110 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5127 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 129 |
| speed | TimeoutError | - | 44 |
| 204 | TimeoutError | - | 23 |
| speed | ClientOSError | - | 12 |
| 204 | ProxyError | - | 11 |
| 204 | ClientOSError | - | 10 |
| cn-block | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
