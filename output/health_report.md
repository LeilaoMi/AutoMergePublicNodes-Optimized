# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-23 04:07:04 |
| 运行耗时 | 295.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 78328 |
| 去重后节点 | 22742 |
| TCP 可达 | 3000 |
| 真实可用 | 432 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22742 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.3 |
| tcp | 30.7 |
| probe | 68.6 |
| real_test | 149.2 |
| generate | 40.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47400 |
| trojan | 10607 |
| shadowsocks | 9927 |
| vmess | 9743 |
| hysteria2 | 245 |
| http | 171 |
| shadowsocksr | 163 |
| socks | 63 |
| hysteria | 6 |
| tuic | 2 |
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
| 80.43 | shadowsocks | 188.6 | 483.0 | 23.41 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 216.105.168.18 |
| 80.14 | vless | 181.5 | 474.9 | 23.58 | 0.0 | 10.0 | 11.32 | 15.24 | DeltaKronecker-all | 64.23.143.23 |
| 79.77 | vless | 294.0 | 705.0 | 20.97 | 0.0 | 10.0 | 11.32 | 18.38 | mheidari-all | 34.213.172.16 |
| 79.32 | shadowsocks | 214.9 | 530.6 | 22.8 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 108.181.0.177 |
| 79.0 | vless | 316.9 | 839.4 | 20.44 | 0.0 | 10.0 | 11.32 | 17.24 | Au1rxx-base64 | 15.204.97.219 |
| 78.97 | shadowsocks | 230.0 | 584.1 | 22.45 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 108.181.118.10 |
| 78.89 | vless | 321.7 | 842.4 | 20.33 | 0.0 | 10.0 | 11.32 | 17.24 | Au1rxx-base64 | 15.204.97.214 |
| 77.42 | shadowsocks | 228.4 | 524.2 | 22.49 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 149.22.95.183 |
| 76.79 | vless | 196.6 | 477.4 | 23.23 | 0.0 | 10.0 | 11.32 | 15.24 | DeltaKronecker-all | 144.34.235.155 |
| 75.38 | shadowsocks | 288.1 | 646.9 | 21.11 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 156.146.38.169 |
| 75.13 | shadowsocks | 288.6 | 647.8 | 21.1 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 156.146.38.170 |
| 74.71 | trojan | 351.7 | 956.1 | 19.64 | 0.0 | 10.0 | 10.33 | 17.24 | Au1rxx-base64 | 45.61.52.243 |
| 73.84 | trojan | 389.3 | 878.8 | 18.77 | 0.0 | 10.0 | 10.33 | 17.24 | Au1rxx-base64 | 207.126.167.241 |
| 73.69 | shadowsocks | 347.9 | 830.4 | 19.72 | 0.0 | 10.0 | 13.78 | 17.24 | Au1rxx-base64 | 156.146.38.168 |
| 72.75 | shadowsocks | 296.7 | 342.7 | 20.91 | 2.15 | 9.91 | 13.78 | 17.24 | Au1rxx-base64 | 149.22.87.204 |
| 72.53 | shadowsocks | 298.7 | 348.3 | 20.86 | 1.94 | 9.9 | 13.78 | 17.24 | Au1rxx-base64 | 149.22.87.241 |
| 72.21 | vless | 271.9 | 586.3 | 21.48 | 0.0 | 10.0 | 11.32 | 15.24 | DeltaKronecker-all | 209.141.46.141 |
| 71.79 | vless | 325.9 | 845.1 | 20.23 | 0.0 | 10.0 | 11.32 | 15.24 | DeltaKronecker-all | 15.204.91.171 |
| 71.39 | vless | 191.3 | 484.0 | 23.35 | 0.0 | 10.0 | 11.32 | 15.24 | DeltaKronecker-all | 172.252.125.77 |
| 71.06 | vless | 163.1 | 442.8 | 24.0 | 0.0 | 10.0 | 11.32 | 15.24 | DeltaKronecker-all | 92.223.71.246 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.987 | 1.0 | 58 | 95 | prefer |
| Surfboard-tg-mixed | 0.819 | 0.933 | 15 | 5421 | prefer |
| Au1rxx-base64 | 0.734 | 0.733 | 90 | 145 | prefer |
| mheidari-all | 0.64 | 0.561 | 173 | 15546 | observe |
| DeltaKronecker-all | 0.334 | 0.254 | 769 | 7452 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4466 | observe |
| Epodonios-all | 0.255 | None | 0 | 8267 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7417 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4156 | observe |
| barry-far-vless | 0.255 | None | 0 | 5190 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4547 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.237 | None | 0 | 1559 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 293 |
| geo | TimeoutError | - | 180 |
| 204 | TimeoutError | - | 52 |
| geo | ClientOSError | - | 48 |
| 204 | ProxyError | - | 42 |
| speed | TimeoutError | - | 31 |
| cn-block | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| geo | status | 403 | 1 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
