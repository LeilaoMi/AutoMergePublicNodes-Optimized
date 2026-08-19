# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-19 13:02:11 |
| 运行耗时 | 340.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82409 |
| 去重后节点 | 22576 |
| TCP 可达 | 3000 |
| 真实可用 | 1142 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22576 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.1 |
| tcp | 35.6 |
| probe | 63.2 |
| real_test | 189.2 |
| generate | 45.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44757 |
| trojan | 17703 |
| shadowsocks | 9987 |
| vmess | 8500 |
| hysteria2 | 1062 |
| http | 165 |
| socks | 122 |
| shadowsocksr | 94 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 4 |

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
| 82.8 | trojan | 253.0 | 529.3 | 21.92 | 0.0 | 10.0 | 14.76 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 82.27 | shadowsocks | 198.4 | 480.5 | 23.19 | 0.0 | 10.0 | 13.58 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 82.2 | shadowsocks | 201.3 | 492.2 | 23.12 | 0.0 | 10.0 | 13.58 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 81.82 | shadowsocks | 239.2 | 581.7 | 22.24 | 0.0 | 10.0 | 13.58 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 81.04 | shadowsocks | 273.1 | 648.3 | 21.46 | 0.0 | 10.0 | 13.58 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 80.49 | trojan | 257.4 | 568.3 | 21.82 | 0.0 | 10.0 | 14.76 | 17.74 | mheidari-all | 35.92.245.6 |
| 80.16 | trojan | 268.4 | 564.9 | 21.57 | 0.0 | 10.0 | 14.76 | 17.74 | mheidari-all | 35.90.27.143 |
| 80.0 | http | 200.3 | 514.0 | 23.14 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.198 |
| 79.82 | vless | 253.6 | 675.8 | 21.91 | 0.0 | 10.0 | 7.91 | 20.0 | Au1rxx-base64 | 70.39.197.13 |
| 79.66 | trojan | 296.7 | 696.3 | 20.91 | 0.0 | 10.0 | 14.76 | 17.74 | mheidari-all | 44.249.55.18 |
| 79.58 | shadowsocks | 239.6 | 502.1 | 22.23 | 0.0 | 10.0 | 13.58 | 20.0 | Au1rxx-base64 | 70.39.198.35 |
| 79.57 | trojan | 294.5 | 670.8 | 20.96 | 0.0 | 10.0 | 14.76 | 17.74 | mheidari-all | 54.213.46.211 |
| 79.37 | http | 227.7 | 583.7 | 22.51 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.216 |
| 79.35 | trojan | 286.9 | 659.8 | 21.14 | 0.0 | 10.0 | 14.76 | 17.74 | mheidari-all | 34.222.243.142 |
| 79.32 | trojan | 269.1 | 593.5 | 21.55 | 0.0 | 10.0 | 14.76 | 17.34 | Surfboard-tg-mixed | 54.185.164.73 |
| 79.14 | trojan | 298.0 | 662.7 | 20.88 | 0.0 | 10.0 | 14.76 | 17.34 | Surfboard-tg-mixed | 100.22.163.167 |
| 79.03 | trojan | 296.2 | 683.5 | 20.92 | 0.0 | 10.0 | 14.76 | 17.74 | mheidari-all | 34.210.213.17 |
| 78.7 | vless | 215.4 | 549.3 | 22.79 | 0.0 | 10.0 | 7.91 | 20.0 | Au1rxx-base64 | 154.29.155.211 |
| 78.45 | vless | 226.3 | 594.2 | 22.54 | 0.0 | 10.0 | 7.91 | 20.0 | Au1rxx-base64 | 38.244.21.216 |
| 78.36 | vless | 186.9 | 484.0 | 23.45 | 0.0 | 10.0 | 7.91 | 20.0 | Au1rxx-base64 | 66.112.214.26 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.976 | 619 | 1765 | prefer |
| zhangkai | 0.997 | 1.0 | 112 | 144 | prefer |
| Surfboard-tg-mixed | 0.954 | 0.879 | 173 | 6304 | prefer |
| mheidari-all | 0.946 | 0.869 | 312 | 16605 | prefer |
| nscl5-all | 0.349 | 0.667 | 3 | 3330 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5067 | observe |
| Epodonios-all | 0.255 | None | 0 | 7081 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7049 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4858 | observe |
| barry-far-vless | 0.255 | None | 0 | 5240 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3995 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1765 | observe |
| DeltaKronecker-all | 0.24 | 0.25 | 4 | 6390 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 13 |
| geo | ClientOSError | - | 11 |
| 204 | ProxyError | - | 9 |
| cn-block | TimeoutError | - | 9 |
| geo | TimeoutError | - | 9 |
| speed | TimeoutError | - | 8 |
| speed | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
