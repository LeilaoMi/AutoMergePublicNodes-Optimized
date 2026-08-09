# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-09 02:10:25 |
| 运行耗时 | 264.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 82844 |
| 去重后节点 | 23635 |
| TCP 可达 | 3000 |
| 真实可用 | 579 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23635 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 35.2 |
| probe | 52.5 |
| real_test | 142.3 |
| generate | 27.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48567 |
| vmess | 13156 |
| trojan | 9878 |
| shadowsocks | 9737 |
| hysteria2 | 1307 |
| shadowsocksr | 70 |
| socks | 68 |
| http | 40 |
| hysteria | 13 |
| tuic | 8 |

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
| 84.03 | hysteria2 | 248.6 | 670.7 | 22.02 | 0.0 | 10.0 | 13.33 | 19.78 | Au1rxx-base64 | 159.223.157.129 |
| 83.99 | hysteria2 | 254.8 | 687.5 | 21.88 | 0.0 | 10.0 | 13.33 | 19.78 | Au1rxx-base64 | 138.124.68.188 |
| 83.85 | hysteria2 | 251.7 | 686.0 | 21.95 | 0.0 | 9.79 | 13.33 | 19.78 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.45 | shadowsocks | 237.0 | 634.1 | 22.29 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 37.19.198.160 |
| 81.38 | shadowsocks | 240.2 | 646.9 | 22.22 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 37.19.198.236 |
| 80.97 | shadowsocks | 257.6 | 687.5 | 21.81 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 37.19.198.244 |
| 80.27 | shadowsocks | 244.9 | 659.7 | 22.11 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 37.19.198.243 |
| 79.5 | vless | 303.9 | 687.2 | 20.74 | 0.0 | 10.0 | 10.63 | 19.78 | Au1rxx-base64 | 67.220.73.204 |
| 78.91 | shadowsocks | 274.2 | 628.6 | 21.43 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 156.146.38.167 |
| 78.52 | vless | 327.1 | 910.0 | 20.21 | 0.0 | 10.0 | 10.63 | 19.78 | Au1rxx-base64 | 45.138.100.226 |
| 78.22 | vless | 390.6 | 998.9 | 18.74 | 0.0 | 10.0 | 10.63 | 19.78 | Au1rxx-base64 | 128.254.207.163 |
| 77.34 | vless | 252.5 | 693.8 | 21.93 | 0.0 | 10.0 | 10.63 | 19.78 | Au1rxx-base64 | 47.253.226.114 |
| 77.3 | shadowsocks | 288.3 | 663.4 | 21.1 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 156.146.38.168 |
| 76.85 | shadowsocks | 230.4 | 604.9 | 22.45 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 198.98.53.130 |
| 76.84 | vless | 295.7 | 790.8 | 20.93 | 0.0 | 10.0 | 10.63 | 19.78 | Au1rxx-base64 | 104.18.43.174 |
| 76.83 | vless | 335.3 | 879.6 | 20.02 | 0.0 | 10.0 | 10.63 | 16.8 | mheidari-all | 169.40.42.192 |
| 76.8 | shadowsocks | 326.2 | 786.5 | 20.23 | 0.0 | 10.0 | 13.38 | 19.78 | Au1rxx-base64 | 156.146.38.170 |
| 76.71 | vless | 367.1 | 929.2 | 19.28 | 0.0 | 10.0 | 10.63 | 16.8 | mheidari-all | 169.40.42.133 |
| 76.3 | vless | 384.7 | 903.8 | 18.87 | 0.0 | 10.0 | 10.63 | 16.8 | mheidari-all | 169.40.42.184 |
| 76.23 | hysteria2 | 359.7 | 676.0 | 19.45 | 0.0 | 10.0 | 13.33 | 19.78 | Au1rxx-base64 | 31.76.113.32 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.952 | 357 | 1540 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.755 | 0.677 | 155 | 6454 | prefer |
| mheidari-all | 0.61 | 0.53 | 200 | 17775 | observe |
| tg-oneclickvpnkeys | 0.316 | 1.0 | 2 | 123 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5450 | observe |
| Epodonios-all | 0.255 | None | 0 | 7127 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7538 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5209 | observe |
| barry-far-vless | 0.255 | None | 0 | 5532 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5127 | observe |
| Au1rxx-clash | 0.237 | None | 0 | 1540 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 69 |
| speed | TimeoutError | - | 41 |
| cn-block | TimeoutError | - | 29 |
| geo | ClientOSError | - | 26 |
| speed | ClientOSError | - | 18 |
| 204 | TimeoutError | - | 16 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 2 |
| geo | status | 403 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
