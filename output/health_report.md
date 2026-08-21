# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-21 01:46:44 |
| 运行耗时 | 390.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 95323 |
| 去重后节点 | 25209 |
| TCP 可达 | 3000 |
| 真实可用 | 1206 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25209 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.2 |
| tcp | 40.0 |
| probe | 73.9 |
| real_test | 233.3 |
| generate | 36.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51241 |
| trojan | 19312 |
| shadowsocks | 11362 |
| vmess | 10415 |
| hysteria2 | 2456 |
| shadowsocksr | 192 |
| http | 164 |
| socks | 124 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 10 |

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
| 82.92 | vless | 266.4 | 685.9 | 21.61 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 167.17.69.171 |
| 81.81 | shadowsocks | 256.6 | 676.7 | 21.84 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 81.67 | shadowsocks | 262.5 | 708.0 | 21.7 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 81.57 | vless | 324.9 | 847.1 | 20.26 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 169.40.42.35 |
| 81.51 | shadowsocks | 269.4 | 730.1 | 21.54 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.44 | shadowsocks | 253.5 | 635.1 | 21.91 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 155.138.136.240 |
| 81.09 | hysteria2 | 250.4 | 683.9 | 21.98 | 0.0 | 9.36 | 13.85 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 80.62 | vless | 365.2 | 924.6 | 19.32 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 216.152.147.28 |
| 80.54 | shadowsocks | 311.5 | 822.5 | 20.57 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 142.4.216.225 |
| 80.14 | vless | 383.9 | 896.9 | 18.89 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 169.40.42.231 |
| 80.05 | vless | 390.2 | 915.2 | 18.74 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 169.40.42.182 |
| 80.03 | hysteria2 | 288.2 | 547.4 | 21.11 | 0.0 | 9.36 | 13.85 | 20.0 | Au1rxx-base64 | 150.241.102.127 |
| 79.58 | vless | 275.9 | 640.0 | 21.39 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 195.211.99.49 |
| 79.5 | shadowsocks | 226.8 | 590.2 | 22.53 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 198.98.53.130 |
| 79.26 | shadowsocks | 345.2 | 964.6 | 19.79 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 15.204.246.132 |
| 78.94 | vless | 424.1 | 1095.2 | 17.96 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 209.200.246.86 |
| 78.91 | shadowsocks | 289.6 | 676.1 | 21.08 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 78.65 | shadowsocks | 289.0 | 675.4 | 21.09 | 0.0 | 10.0 | 13.97 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 78.6 | vless | 351.7 | 799.7 | 19.64 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 169.40.42.90 |
| 78.45 | vless | 404.4 | 992.2 | 18.42 | 0.0 | 10.0 | 11.31 | 20.0 | mheidari-all | 130.107.73.148 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.995 | 555 | 1663 | prefer |
| zhangkai | 0.997 | 1.0 | 111 | 144 | prefer |
| Surfboard-tg-mixed | 0.965 | 0.898 | 59 | 6412 | prefer |
| mheidari-all | 0.686 | 0.606 | 792 | 21987 | observe |
| nscl5-all | 0.349 | 0.667 | 3 | 3031 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4958 | observe |
| Epodonios-all | 0.255 | None | 0 | 7184 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7304 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5053 | observe |
| barry-far-vless | 0.255 | None | 0 | 5451 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4586 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1663 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 140 |
| geo | ClientOSError | - | 112 |
| speed | TimeoutError | - | 72 |
| speed | ClientOSError | - | 24 |
| cn-block | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 4 |
| 204 | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
