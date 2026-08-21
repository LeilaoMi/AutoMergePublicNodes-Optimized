# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-21 07:01:24 |
| 运行耗时 | 358.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 94128 |
| 去重后节点 | 24576 |
| TCP 可达 | 3000 |
| 真实可用 | 1153 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24576 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 0.8 |
| tcp | 38.6 |
| probe | 68.1 |
| real_test | 206.8 |
| generate | 38.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52081 |
| trojan | 18264 |
| vmess | 10862 |
| shadowsocks | 10744 |
| hysteria2 | 1626 |
| shadowsocksr | 201 |
| http | 166 |
| socks | 125 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 12 |

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
| 82.89 | shadowsocks | 241.4 | 674.6 | 22.19 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 82.52 | shadowsocks | 257.2 | 719.7 | 21.82 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 82.46 | shadowsocks | 259.9 | 727.1 | 21.76 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.33 | shadowsocks | 298.1 | 781.8 | 20.88 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 155.138.136.240 |
| 80.55 | shadowsocks | 321.1 | 900.1 | 20.35 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 38.180.135.156 |
| 80.19 | shadowsocks | 241.4 | 672.2 | 22.19 | 0.0 | 10.0 | 14.7 | 19.3 | Surfboard-tg-mixed | 37.19.198.243 |
| 79.92 | shadowsocks | 286.0 | 649.0 | 21.16 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 79.6 | shadowsocks | 282.6 | 659.9 | 21.24 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 79.39 | shadowsocks | 252.1 | 695.3 | 21.94 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 162.243.36.19 |
| 79.28 | hysteria2 | 336.9 | 298.0 | 19.98 | 3.82 | 9.19 | 14.56 | 20.0 | Au1rxx-base64 | 45.32.252.144 |
| 78.7 | shadowsocks | 323.3 | 772.3 | 20.29 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 78.46 | vless | 242.0 | 659.1 | 22.18 | 0.0 | 10.0 | 6.28 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 78.38 | vless | 245.3 | 665.9 | 22.1 | 0.0 | 10.0 | 6.28 | 20.0 | Au1rxx-base64 | 79.127.243.217 |
| 78.29 | shadowsocks | 331.7 | 782.7 | 20.1 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 77.96 | vless | 263.5 | 629.6 | 21.68 | 0.0 | 10.0 | 6.28 | 20.0 | Au1rxx-base64 | 169.40.42.90 |
| 77.96 | shadowsocks | 314.4 | 712.1 | 20.5 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 108.181.57.93 |
| 77.64 | shadowsocks | 303.0 | 658.6 | 20.77 | 0.0 | 10.0 | 14.7 | 20.0 | Au1rxx-base64 | 23.150.248.20 |
| 77.61 | vless | 252.6 | 658.7 | 21.93 | 0.0 | 10.0 | 6.28 | 20.0 | Au1rxx-base64 | 169.40.42.179 |
| 77.55 | vless | 281.0 | 685.4 | 21.27 | 0.0 | 10.0 | 6.28 | 20.0 | Au1rxx-base64 | 169.40.42.184 |
| 77.5 | vless | 283.3 | 693.7 | 21.22 | 0.0 | 10.0 | 6.28 | 20.0 | Au1rxx-base64 | 216.152.147.28 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.952 | 640 | 1607 | prefer |
| zhangkai | 0.988 | 0.991 | 112 | 144 | prefer |
| mheidari-all | 0.894 | 0.816 | 305 | 21864 | prefer |
| Surfboard-tg-mixed | 0.83 | 0.752 | 230 | 6368 | prefer |
| nscl5-all | 0.391 | 1.0 | 2 | 3031 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| DeltaKronecker-all | 0.296 | 0.2 | 35 | 6250 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5148 | observe |
| Epodonios-all | 0.255 | None | 0 | 7077 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7024 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5051 | observe |
| barry-far-vless | 0.255 | None | 0 | 5415 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4647 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 52 |
| speed | TimeoutError | - | 30 |
| geo | ClientOSError | - | 26 |
| 204 | TimeoutError | - | 21 |
| cn-block | TimeoutError | - | 19 |
| 204 | ProxyError | - | 10 |
| speed | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
