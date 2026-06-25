# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-25 04:08:54 |
| 运行耗时 | 229.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 75444 |
| 去重后节点 | 22495 |
| TCP 可达 | 3000 |
| 真实可用 | 521 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22495 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 29.7 |
| probe | 50.1 |
| real_test | 114.1 |
| generate | 30.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44276 |
| trojan | 10757 |
| vmess | 9989 |
| shadowsocks | 9833 |
| hysteria2 | 232 |
| shadowsocksr | 153 |
| http | 129 |
| socks | 67 |
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
| 76.29 | shadowsocks | 249.8 | 620.2 | 22.0 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 198.98.53.130 |
| 76.06 | shadowsocks | 259.4 | 638.9 | 21.77 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 156.146.38.167 |
| 76.04 | shadowsocks | 260.4 | 643.2 | 21.75 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 37.19.198.244 |
| 76.02 | shadowsocks | 261.2 | 643.5 | 21.73 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 156.146.38.168 |
| 75.94 | shadowsocks | 264.7 | 660.5 | 21.65 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 156.146.38.169 |
| 74.8 | shadowsocks | 292.4 | 690.0 | 21.01 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 108.181.57.93 |
| 74.51 | shadowsocks | 255.7 | 622.4 | 21.86 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 156.146.38.170 |
| 72.47 | vless | 323.7 | 770.8 | 20.28 | 0.0 | 10.0 | 8.91 | 14.88 | Surfboard-tg-mixed | 15.223.121.250 |
| 71.98 | shadowsocks | 276.8 | 680.1 | 21.37 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 37.19.198.243 |
| 71.44 | shadowsocks | 275.2 | 686.1 | 21.41 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 37.19.198.160 |
| 71.06 | shadowsocks | 287.1 | 567.6 | 21.13 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 149.22.95.183 |
| 70.95 | shadowsocks | 329.2 | 964.5 | 20.16 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 172.234.202.34 |
| 70.76 | shadowsocks | 272.7 | 687.6 | 21.47 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 37.19.198.236 |
| 70.62 | shadowsocks | 290.0 | 579.0 | 21.07 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 173.244.56.9 |
| 70.29 | shadowsocks | 330.2 | 712.4 | 20.13 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 173.244.56.6 |
| 69.46 | trojan | 346.6 | 835.3 | 19.75 | 0.0 | 10.0 | 9.33 | 14.62 | mheidari-all | 64.94.95.118 |
| 69.43 | shadowsocks | 299.9 | 532.5 | 20.83 | 0.0 | 10.0 | 12.27 | 16.02 | Au1rxx-base64 | 108.181.0.177 |
| 69.33 | vless | 354.5 | 874.1 | 19.57 | 0.0 | 10.0 | 8.91 | 14.88 | Surfboard-tg-mixed | 137.184.218.169 |
| 69.1 | vless | 317.9 | 769.6 | 20.42 | 0.0 | 10.0 | 8.91 | 14.88 | Surfboard-tg-mixed | 104.16.9.20 |
| 69.07 | vless | 357.1 | 888.6 | 19.51 | 0.0 | 10.0 | 8.91 | 16.02 | Au1rxx-base64 | 159.89.87.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Surfboard-tg-mixed | 0.829 | 0.751 | 285 | 5184 | prefer |
| Au1rxx-base64 | 0.694 | 0.694 | 72 | 119 | observe |
| mheidari-all | 0.676 | 0.597 | 248 | 15443 | observe |
| DeltaKronecker-all | 0.631 | 0.552 | 125 | 6644 | observe |
| nscl5-all | 0.357 | 1.0 | 2 | 1136 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4745 | observe |
| Epodonios-all | 0.255 | None | 0 | 7785 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7191 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3909 | observe |
| barry-far-vless | 0.255 | None | 0 | 4704 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4710 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 107 |
| geo | TimeoutError | - | 63 |
| speed | TimeoutError | - | 25 |
| geo | ClientOSError | - | 18 |
| cn-block | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 5 |
| 204 | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |
| geo | status | 403 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
