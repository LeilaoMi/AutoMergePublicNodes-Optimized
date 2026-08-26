# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-26 01:47:07 |
| 运行耗时 | 360.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 79196 |
| 去重后节点 | 22570 |
| TCP 可达 | 3000 |
| 真实可用 | 550 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22570 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.4 |
| tcp | 36.4 |
| probe | 78.0 |
| real_test | 195.1 |
| generate | 43.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49693 |
| shadowsocks | 10725 |
| vmess | 10476 |
| trojan | 6546 |
| hysteria2 | 1387 |
| http | 167 |
| shadowsocksr | 124 |
| socks | 68 |
| hysteria | 7 |
| tuic | 3 |

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
| 83.16 | http | 229.7 | 592.9 | 22.46 | 0.0 | 10.0 | 14.38 | 19.32 | zhangkai | 138.199.35.198 |
| 83.04 | http | 235.0 | 596.8 | 22.34 | 0.0 | 10.0 | 14.38 | 19.32 | zhangkai | 138.199.35.216 |
| 82.79 | vless | 231.7 | 571.3 | 22.41 | 0.0 | 10.0 | 11.52 | 18.86 | DeltaKronecker-all | 15.204.97.209 |
| 81.76 | shadowsocks | 215.4 | 492.1 | 22.79 | 0.0 | 10.0 | 14.11 | 18.86 | DeltaKronecker-all | 62.146.171.57 |
| 81.11 | shadowsocks | 232.6 | 576.6 | 22.39 | 0.0 | 10.0 | 14.11 | 18.86 | DeltaKronecker-all | 94.72.127.58 |
| 81.04 | trojan | 197.0 | 513.3 | 23.22 | 0.0 | 10.0 | 13.78 | 18.04 | Au1rxx-base64 | us01.duotg.top |
| 80.78 | shadowsocks | 227.5 | 566.7 | 22.51 | 0.0 | 10.0 | 14.11 | 18.16 | Surfboard-tg-mixed | 94.72.127.55 |
| 80.69 | shadowsocks | 209.7 | 463.8 | 22.92 | 0.0 | 10.0 | 14.11 | 18.16 | Surfboard-tg-mixed | 108.181.0.177 |
| 80.27 | vless | 242.5 | 280.1 | 22.16 | 4.49 | 9.93 | 11.52 | 18.16 | Surfboard-tg-mixed | 31.76.91.72 |
| 80.17 | trojan | 276.0 | 663.2 | 21.39 | 0.0 | 10.0 | 13.78 | 18.04 | Au1rxx-base64 | 35.91.251.124 |
| 80.12 | shadowsocks | 239.9 | 559.1 | 22.22 | 0.0 | 10.0 | 14.11 | 18.04 | Au1rxx-base64 | 154.53.60.212 |
| 80.1 | shadowsocks | 251.7 | 575.3 | 21.95 | 0.0 | 10.0 | 14.11 | 18.04 | Au1rxx-base64 | 149.22.95.183 |
| 79.41 | vless | 291.4 | 779.6 | 21.03 | 0.0 | 10.0 | 11.52 | 18.86 | DeltaKronecker-all | 166.88.186.151 |
| 79.33 | shadowsocks | 251.0 | 536.7 | 21.97 | 0.0 | 10.0 | 14.11 | 18.16 | Surfboard-tg-mixed | 154.53.63.33 |
| 79.3 | vless | 210.0 | 511.0 | 22.92 | 0.0 | 10.0 | 11.52 | 18.86 | DeltaKronecker-all | 104.16.180.203 |
| 79.16 | shadowsocks | 219.6 | 537.2 | 22.69 | 0.0 | 10.0 | 14.11 | 16.86 | mheidari-all | 108.181.118.10 |
| 79.06 | vless | 263.4 | 658.0 | 21.68 | 0.0 | 10.0 | 11.52 | 18.86 | DeltaKronecker-all | 104.24.88.105 |
| 78.85 | trojan | 196.0 | 496.5 | 23.24 | 0.0 | 10.0 | 13.78 | 18.04 | Au1rxx-base64 | 14.1.28.76 |
| 78.2 | shadowsocks | 228.9 | 545.0 | 22.48 | 0.0 | 10.0 | 14.11 | 16.86 | mheidari-all | 173.244.56.9 |
| 77.39 | shadowsocks | 217.5 | 515.5 | 22.74 | 0.0 | 10.0 | 14.11 | 18.04 | Au1rxx-base64 | 129.146.166.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.983 | 115 | 1944 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.873 | 0.798 | 114 | 6470 | prefer |
| mheidari-all | 0.856 | 0.787 | 47 | 14587 | prefer |
| DeltaKronecker-all | 0.391 | 0.31 | 912 | 6340 | observe |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 191 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 7017 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7048 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5307 | observe |
| barry-far-vless | 0.255 | None | 0 | 5579 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4119 | observe |
| Au1rxx-clash | 0.253 | None | 0 | 1946 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 392 |
| speed | ClientOSError | - | 115 |
| geo | ClientOSError | - | 72 |
| speed | TimeoutError | - | 37 |
| cn-block | TimeoutError | - | 16 |
| 204 | ProxyError | - | 12 |
| 204 | TimeoutError | - | 12 |
| geo | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
