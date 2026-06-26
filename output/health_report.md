# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-26 09:42:28 |
| 运行耗时 | 261.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 82588 |
| 去重后节点 | 22700 |
| TCP 可达 | 3000 |
| 真实可用 | 351 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22700 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.3 |
| tcp | 30.4 |
| probe | 64.6 |
| real_test | 117.1 |
| generate | 42.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45846 |
| trojan | 14718 |
| vmess | 11320 |
| shadowsocks | 10080 |
| hysteria2 | 256 |
| shadowsocksr | 158 |
| http | 129 |
| socks | 73 |
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
| 77.83 | trojan | 316.6 | 857.8 | 20.45 | 0.0 | 10.0 | 12.76 | 17.12 | Surfboard-tg-mixed | 207.126.167.150 |
| 77.24 | shadowsocks | 198.4 | 487.9 | 23.18 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 108.181.118.10 |
| 77.02 | shadowsocks | 229.7 | 520.3 | 22.46 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 173.244.56.9 |
| 76.94 | shadowsocks | 211.7 | 524.4 | 22.88 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 108.181.0.177 |
| 76.72 | shadowsocks | 242.7 | 579.3 | 22.16 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 149.22.95.183 |
| 76.12 | shadowsocks | 268.8 | 680.2 | 21.56 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 173.244.56.6 |
| 72.99 | trojan | 390.9 | 997.1 | 18.73 | 0.0 | 10.0 | 12.76 | 15.18 | Au1rxx-base64 | 45.61.52.243 |
| 71.49 | vless | 303.3 | 799.5 | 20.76 | 0.0 | 10.0 | 5.55 | 15.18 | Au1rxx-base64 | 15.204.97.219 |
| 70.65 | vless | 279.9 | 664.8 | 21.3 | 0.0 | 10.0 | 5.55 | 13.8 | mheidari-all | 34.213.172.16 |
| 70.16 | vless | 228.3 | 565.4 | 22.49 | 0.0 | 10.0 | 5.55 | 17.12 | Surfboard-tg-mixed | 38.244.21.213 |
| 69.83 | shadowsocks | 298.6 | 356.4 | 20.87 | 1.64 | 9.9 | 13.38 | 15.18 | Au1rxx-base64 | 149.22.87.241 |
| 69.69 | shadowsocks | 318.2 | 661.1 | 20.41 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 156.146.38.167 |
| 69.63 | shadowsocks | 299.4 | 359.5 | 20.85 | 1.52 | 9.91 | 13.38 | 15.18 | Au1rxx-base64 | 149.22.87.240 |
| 68.92 | vless | 303.7 | 423.2 | 20.75 | 0.0 | 10.0 | 5.55 | 17.12 | Surfboard-tg-mixed | 141.193.154.182 |
| 68.73 | shadowsocks | 347.3 | 725.3 | 19.74 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 156.146.38.168 |
| 67.9 | vless | 458.3 | 1264.8 | 17.17 | 0.0 | 10.0 | 5.55 | 15.18 | Au1rxx-base64 | 15.204.97.214 |
| 67.81 | shadowsocks | 378.3 | 736.7 | 19.02 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 37.19.198.160 |
| 67.78 | shadowsocks | 386.0 | 797.2 | 18.84 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 37.19.198.243 |
| 67.74 | trojan | 399.9 | 690.5 | 18.52 | 0.0 | 10.0 | 12.76 | 15.18 | Au1rxx-base64 | 207.126.167.162 |
| 66.86 | shadowsocks | 419.2 | 894.9 | 18.07 | 0.0 | 10.0 | 13.38 | 15.18 | Au1rxx-base64 | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Au1rxx-base64 | 0.89 | 0.905 | 42 | 96 | prefer |
| mheidari-all | 0.729 | 0.651 | 189 | 16243 | prefer |
| Surfboard-tg-mixed | 0.661 | 0.582 | 189 | 5153 | observe |
| DeltaKronecker-all | 0.605 | 0.526 | 78 | 12590 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1175 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4567 | observe |
| Epodonios-all | 0.255 | None | 0 | 7806 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3985 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7302 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3827 | observe |
| barry-far-vless | 0.255 | None | 0 | 4575 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5185 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 73 |
| 204 | TimeoutError | - | 38 |
| cn-block | TimeoutError | - | 23 |
| geo | TimeoutError | - | 13 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 9 |
| geo | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
