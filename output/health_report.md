# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-01 08:33:10 |
| 运行耗时 | 309.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78775 |
| 去重后节点 | 23169 |
| TCP 可达 | 3000 |
| 真实可用 | 642 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23169 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.3 |
| tcp | 34.0 |
| probe | 60.2 |
| real_test | 168.6 |
| generate | 39.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47195 |
| vmess | 12309 |
| shadowsocks | 10135 |
| trojan | 8175 |
| hysteria2 | 601 |
| http | 173 |
| shadowsocksr | 76 |
| socks | 63 |
| anytls | 26 |
| hysteria | 14 |
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
| 83.83 | http | 242.0 | 638.0 | 22.17 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.5 |
| 83.48 | http | 257.5 | 672.4 | 21.82 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.7 |
| 83.43 | http | 259.7 | 694.5 | 21.77 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.8 |
| 83.21 | hysteria2 | 233.3 | 642.5 | 22.38 | 0.0 | 8.96 | 14.21 | 18.76 | Au1rxx-base64 | 159.223.157.129 |
| 82.92 | http | 238.4 | 632.9 | 22.26 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.23 |
| 82.84 | http | 241.7 | 639.8 | 22.18 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.50 |
| 82.66 | http | 249.7 | 669.2 | 22.0 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.21 |
| 82.54 | http | 254.6 | 681.0 | 21.88 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.20 |
| 82.38 | http | 261.5 | 677.3 | 21.72 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.25 |
| 82.17 | hysteria2 | 283.1 | 788.3 | 21.22 | 0.0 | 8.98 | 14.21 | 18.76 | Au1rxx-base64 | 138.124.68.188 |
| 81.82 | http | 242.8 | 637.0 | 22.16 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.33 |
| 81.69 | hysteria2 | 287.9 | 791.6 | 21.11 | 0.0 | 8.61 | 14.21 | 18.76 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.44 | http | 259.3 | 694.3 | 21.78 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.16 |
| 80.71 | shadowsocks | 226.0 | 628.2 | 22.55 | 0.0 | 9.05 | 14.35 | 18.76 | Au1rxx-base64 | 37.19.198.236 |
| 80.71 | shadowsocks | 226.3 | 622.5 | 22.54 | 0.0 | 9.06 | 14.35 | 18.76 | Au1rxx-base64 | 37.19.198.243 |
| 80.67 | vless | 241.3 | 645.4 | 22.19 | 0.0 | 10.0 | 9.72 | 18.76 | Au1rxx-base64 | 167.99.48.117 |
| 80.34 | vless | 255.6 | 675.9 | 21.86 | 0.0 | 10.0 | 9.72 | 18.76 | Au1rxx-base64 | 78.111.89.171 |
| 80.33 | shadowsocks | 242.1 | 676.9 | 22.17 | 0.0 | 9.05 | 14.35 | 18.76 | Au1rxx-base64 | 37.19.198.244 |
| 80.28 | vless | 258.1 | 628.0 | 21.8 | 0.0 | 10.0 | 9.72 | 18.76 | Au1rxx-base64 | 169.40.42.95 |
| 80.21 | vless | 261.2 | 644.6 | 21.73 | 0.0 | 10.0 | 9.72 | 18.76 | Au1rxx-base64 | 169.40.42.184 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 158 | 228 | prefer |
| Au1rxx-base64 | 0.796 | 0.731 | 461 | 1655 | prefer |
| Surfboard-tg-mixed | 0.62 | 0.541 | 85 | 5316 | observe |
| mheidari-all | 0.43 | 0.556 | 9 | 16723 | observe |
| DeltaKronecker-all | 0.389 | 0.307 | 309 | 5502 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5391 | observe |
| Epodonios-all | 0.255 | None | 0 | 5937 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6670 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4168 | observe |
| barry-far-vless | 0.255 | None | 0 | 4552 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5039 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1655 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 147 |
| speed | TimeoutError | - | 70 |
| geo | ClientOSError | - | 56 |
| speed | ClientOSError | - | 38 |
| 204 | TimeoutError | - | 25 |
| 204 | ProxyError | - | 18 |
| cn-block | TimeoutError | - | 10 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
