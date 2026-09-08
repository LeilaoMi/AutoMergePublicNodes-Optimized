# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-08 04:05:38 |
| 运行耗时 | 395.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 91631 |
| 去重后节点 | 25396 |
| TCP 可达 | 3000 |
| 真实可用 | 694 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25396 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.6 |
| tcp | 41.1 |
| probe | 99.0 |
| real_test | 197.1 |
| generate | 50.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57483 |
| vmess | 12274 |
| shadowsocks | 10306 |
| trojan | 9059 |
| hysteria2 | 1780 |
| http | 503 |
| shadowsocksr | 127 |
| socks | 50 |
| anytls | 20 |
| hysteria | 16 |
| tuic | 13 |

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
| 83.55 | vless | 284.7 | 702.9 | 21.19 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 82.71 | vless | 295.9 | 710.6 | 20.93 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 167.17.69.171 |
| 82.34 | vless | 254.7 | 723.6 | 21.88 | 0.0 | 10.0 | 12.36 | 18.1 | mheidari-all | 67.220.73.204 |
| 82.23 | vless | 335.6 | 700.9 | 20.01 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.163 |
| 81.87 | vless | 333.4 | 775.6 | 20.06 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.90 |
| 81.73 | vless | 340.7 | 727.1 | 19.89 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.235 |
| 81.51 | shadowsocks | 274.9 | 707.8 | 21.41 | 0.0 | 10.0 | 14.1 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.08 | vless | 295.5 | 664.9 | 20.94 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.35 |
| 80.91 | vless | 396.2 | 895.4 | 18.61 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.52 |
| 80.72 | vless | 407.0 | 921.8 | 18.36 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.182 |
| 80.26 | hysteria2 | 283.6 | 677.1 | 21.21 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 80.25 | vless | 310.9 | 636.8 | 20.58 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.225 |
| 80.09 | shadowsocks | 254.4 | 621.2 | 21.89 | 0.0 | 10.0 | 14.1 | 18.1 | mheidari-all | 156.146.38.169 |
| 80.03 | vless | 318.0 | 715.0 | 20.42 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.212 |
| 79.98 | shadowsocks | 259.2 | 655.1 | 21.78 | 0.0 | 10.0 | 14.1 | 18.1 | mheidari-all | 37.19.198.244 |
| 79.66 | vless | 398.8 | 900.1 | 18.55 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.231 |
| 79.48 | vless | 350.9 | 761.2 | 19.66 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.173 |
| 79.45 | vless | 364.2 | 910.1 | 19.35 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.133 |
| 79.08 | vless | 379.7 | 834.6 | 18.99 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 169.40.42.74 |
| 78.91 | vless | 307.9 | 813.2 | 20.65 | 0.0 | 10.0 | 12.36 | 20.0 | Au1rxx-base64 | 130.94.115.231 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.994 | 1.0 | 40 | 450 | prefer |
| Au1rxx-base64 | 0.985 | 0.914 | 360 | 1833 | prefer |
| ermaozi-get_subscribe | 0.94 | 1.0 | 19 | 470 | prefer |
| Surfboard-tg-mixed | 0.919 | 0.847 | 85 | 7392 | prefer |
| DeltaKronecker-all | 0.457 | 0.373 | 59 | 6417 | observe |
| mheidari-all | 0.389 | 0.308 | 672 | 22287 | observe |
| tg-oneclickvpnkeys | 0.313 | 0.5 | 8 | 196 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7885 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8682 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6186 | observe |
| barry-far-vless | 0.255 | None | 0 | 6444 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4218 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1833 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 190 |
| speed | TimeoutError | - | 85 |
| geo | ClientOSError | - | 81 |
| speed | ClientOSError | - | 56 |
| cn-block | ClientOSError | - | 53 |
| 204 | TimeoutError | - | 24 |
| cn-block | TimeoutError | - | 24 |
| 204 | ProxyError | - | 22 |
| 204 | ClientOSError | - | 16 |
| 204 | ProxyConnectionError | - | 1 |
| cn-block | ProxyError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
