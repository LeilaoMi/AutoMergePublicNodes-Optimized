# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-22 01:39:37 |
| 运行耗时 | 327.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 92902 |
| 去重后节点 | 23044 |
| TCP 可达 | 3000 |
| 真实可用 | 865 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23044 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.4 |
| tcp | 39.1 |
| probe | 64.2 |
| real_test | 191.7 |
| generate | 25.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50861 |
| trojan | 19043 |
| shadowsocks | 10577 |
| vmess | 10294 |
| hysteria2 | 1570 |
| shadowsocksr | 207 |
| http | 167 |
| socks | 123 |
| anytls | 32 |
| hysteria | 15 |
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
| 84.33 | vless | 251.9 | 646.7 | 21.95 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.90 |
| 84.17 | vless | 259.1 | 622.1 | 21.78 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 195.211.99.49 |
| 84.12 | vless | 261.7 | 631.4 | 21.72 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.74 |
| 84.1 | vless | 262.6 | 681.0 | 21.7 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.104 |
| 83.68 | vless | 280.6 | 680.5 | 21.28 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.52 |
| 83.63 | vless | 282.7 | 618.8 | 21.23 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.179 |
| 83.52 | hysteria2 | 255.3 | 665.3 | 21.87 | 0.0 | 10.0 | 12.95 | 19.8 | mheidari-all | 159.223.157.129 |
| 83.45 | vless | 290.5 | 649.7 | 21.05 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.133 |
| 83.26 | vless | 290.4 | 649.6 | 21.06 | 0.0 | 10.0 | 12.4 | 19.8 | mheidari-all | 169.40.42.182 |
| 82.81 | vless | 318.5 | 845.3 | 20.41 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.231 |
| 82.62 | vless | 326.3 | 827.2 | 20.22 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.16 |
| 82.55 | vless | 329.4 | 770.2 | 20.15 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.35 |
| 82.5 | vless | 245.2 | 658.2 | 22.1 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 179.255.185.74 |
| 82.49 | vless | 288.8 | 639.7 | 21.09 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.229 |
| 82.27 | shadowsocks | 230.0 | 630.0 | 22.45 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 82.25 | shadowsocks | 230.9 | 642.2 | 22.43 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 82.24 | vless | 342.8 | 874.0 | 19.84 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.225 |
| 82.15 | vless | 342.1 | 861.9 | 19.86 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 216.152.147.28 |
| 82.13 | vless | 338.8 | 558.2 | 19.93 | 0.0 | 10.0 | 12.4 | 19.8 | mheidari-all | 195.211.99.45 |
| 82.11 | vless | 348.5 | 889.9 | 19.71 | 0.0 | 10.0 | 12.4 | 20.0 | Au1rxx-base64 | 169.40.42.223 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.939 | 326 | 1933 | prefer |
| zhangkai | 0.997 | 1.0 | 113 | 144 | prefer |
| Surfboard-tg-mixed | 0.918 | 0.843 | 115 | 6361 | prefer |
| mheidari-all | 0.598 | 0.518 | 666 | 21889 | observe |
| nscl5-all | 0.287 | 0.5 | 2 | 3321 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 162 | observe |
| Pawdroid | 0.256 | 1.0 | 1 | 20 | observe |
| Epodonios-all | 0.255 | None | 0 | 7089 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3985 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7133 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5127 | observe |
| barry-far-vless | 0.255 | None | 0 | 5449 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4091 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |
| Au1rxx-clash | 0.252 | None | 0 | 1933 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 130 |
| geo | ClientOSError | - | 91 |
| speed | TimeoutError | - | 90 |
| speed | ClientOSError | - | 27 |
| cn-block | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| geo | parse | TimeoutError | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
