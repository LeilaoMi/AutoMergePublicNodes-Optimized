# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-01 03:33:14 |
| 运行耗时 | 255.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78571 |
| 去重后节点 | 22863 |
| TCP 可达 | 3000 |
| 真实可用 | 619 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22863 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.4 |
| tcp | 34.2 |
| probe | 53.6 |
| real_test | 129.6 |
| generate | 30.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46761 |
| vmess | 12053 |
| shadowsocks | 10145 |
| trojan | 8777 |
| hysteria2 | 567 |
| http | 87 |
| shadowsocksr | 75 |
| socks | 60 |
| anytls | 26 |
| hysteria | 14 |
| tuic | 6 |

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
| 85.04 | http | 190.0 | 495.9 | 23.38 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.202 |
| 85.02 | http | 190.7 | 495.7 | 23.36 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.217 |
| 84.98 | http | 192.6 | 495.7 | 23.32 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.218 |
| 84.96 | http | 193.4 | 496.3 | 23.3 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.205 |
| 84.89 | http | 196.5 | 505.4 | 23.23 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.209 |
| 84.53 | http | 212.2 | 536.1 | 22.87 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.207 |
| 84.43 | http | 216.4 | 571.3 | 22.77 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.220 |
| 84.33 | http | 220.6 | 579.7 | 22.67 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.197 |
| 84.31 | http | 221.6 | 586.0 | 22.65 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.199 |
| 84.23 | http | 224.8 | 596.4 | 22.57 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.196 |
| 81.28 | http | 352.6 | 980.8 | 19.62 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.204 |
| 78.29 | http | 481.5 | 1354.3 | 16.63 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.198 |
| 78.28 | vless | 173.9 | 477.8 | 23.75 | 0.0 | 10.0 | 9.27 | 15.26 | Au1rxx-base64 | 64.23.143.23 |
| 78.09 | vless | 182.4 | 462.5 | 23.56 | 0.0 | 10.0 | 9.27 | 15.26 | Au1rxx-base64 | 70.39.198.183 |
| 76.89 | vless | 234.0 | 559.2 | 22.36 | 0.0 | 10.0 | 9.27 | 15.26 | Au1rxx-base64 | 70.39.178.231 |
| 76.45 | vless | 253.0 | 656.2 | 21.92 | 0.0 | 10.0 | 9.27 | 15.26 | Au1rxx-base64 | 192.204.50.220 |
| 76.26 | vless | 227.2 | 502.7 | 22.52 | 0.0 | 10.0 | 9.27 | 15.26 | Au1rxx-base64 | 52.43.158.158 |
| 75.34 | shadowsocks | 216.0 | 521.6 | 22.78 | 0.0 | 9.39 | 11.91 | 15.26 | Au1rxx-base64 | 173.244.56.9 |
| 75.1 | shadowsocks | 225.8 | 519.7 | 22.55 | 0.0 | 9.38 | 11.91 | 15.26 | Au1rxx-base64 | 149.22.95.183 |
| 74.84 | shadowsocks | 213.4 | 514.8 | 22.84 | 0.0 | 9.46 | 11.91 | 15.26 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 80 | 110 | prefer |
| Au1rxx-base64 | 0.938 | 0.873 | 529 | 1664 | prefer |
| Surfboard-tg-mixed | 0.573 | 0.6 | 15 | 5365 | observe |
| DeltaKronecker-all | 0.504 | 0.421 | 57 | 5144 | observe |
| mheidari-all | 0.406 | 0.323 | 127 | 16450 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 6122 | observe |
| nscl5-all | 0.305 | 1.0 | 1 | 1258 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5507 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6657 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4239 | observe |
| barry-far-vless | 0.255 | None | 0 | 4596 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5081 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1664 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 57 |
| geo | TimeoutError | - | 56 |
| speed | ClientOSError | - | 36 |
| geo | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 7 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
