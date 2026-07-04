# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-04 03:42:44 |
| 运行耗时 | 190.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 78050 |
| 去重后节点 | 23076 |
| TCP 可达 | 3000 |
| 真实可用 | 418 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23076 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.3 |
| tcp | 31.0 |
| probe | 41.7 |
| real_test | 71.3 |
| generate | 41.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45301 |
| trojan | 12448 |
| vmess | 10487 |
| shadowsocks | 9150 |
| hysteria2 | 289 |
| shadowsocksr | 155 |
| http | 135 |
| socks | 77 |
| hysteria | 6 |
| tuic | 1 |
| anytls | 1 |

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
| 74.97 | shadowsocks | 256.6 | 626.4 | 21.84 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 156.146.38.167 |
| 74.65 | shadowsocks | 270.5 | 673.5 | 21.52 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 37.19.198.236 |
| 74.63 | shadowsocks | 248.7 | 610.9 | 22.02 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 156.146.38.169 |
| 74.4 | shadowsocks | 276.1 | 690.6 | 21.39 | 0.0 | 10.0 | 12.79 | 14.22 | mheidari-all | 198.98.53.130 |
| 74.39 | trojan | 289.8 | 621.7 | 21.07 | 0.0 | 10.0 | 9.5 | 15.82 | Surfboard-tg-mixed | 94.140.0.40 |
| 74.22 | shadowsocks | 259.9 | 643.0 | 21.76 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 37.19.198.160 |
| 73.42 | shadowsocks | 250.5 | 616.1 | 21.98 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 156.146.38.170 |
| 73.19 | shadowsocks | 247.1 | 606.3 | 22.06 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 156.146.38.168 |
| 72.97 | shadowsocks | 264.8 | 653.4 | 21.65 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 37.19.198.243 |
| 71.5 | shadowsocks | 371.0 | 963.2 | 19.19 | 0.0 | 10.0 | 12.79 | 14.22 | mheidari-all | 108.181.57.93 |
| 71.29 | vmess | 391.7 | 1050.6 | 18.71 | 0.0 | 10.0 | 12.86 | 14.22 | mheidari-all | 67.220.95.3 |
| 71.23 | trojan | 299.6 | 730.3 | 20.84 | 0.0 | 10.0 | 9.5 | 14.3 | DeltaKronecker-all | 64.94.95.114 |
| 69.91 | shadowsocks | 259.1 | 647.3 | 21.78 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 37.19.198.244 |
| 69.74 | trojan | 299.6 | 728.3 | 20.84 | 0.0 | 10.0 | 9.5 | 14.3 | DeltaKronecker-all | 64.94.95.117 |
| 69.61 | trojan | 295.3 | 726.8 | 20.94 | 0.0 | 10.0 | 9.5 | 14.3 | DeltaKronecker-all | 64.94.95.115 |
| 69.1 | shadowsocks | 323.5 | 596.1 | 20.29 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 149.22.95.183 |
| 68.64 | shadowsocks | 297.8 | 570.7 | 20.88 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 108.181.118.10 |
| 68.63 | shadowsocks | 325.9 | 666.4 | 20.23 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 108.181.0.177 |
| 68.08 | trojan | 308.1 | 551.5 | 20.65 | 0.0 | 10.0 | 9.5 | 14.3 | DeltaKronecker-all | 104.17.148.22 |
| 67.98 | shadowsocks | 297.9 | 637.9 | 20.88 | 0.0 | 10.0 | 12.79 | 14.34 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.877 | 0.801 | 141 | 6191 | prefer |
| mheidari-all | 0.864 | 0.79 | 100 | 16050 | prefer |
| Au1rxx-base64 | 0.849 | 0.875 | 24 | 82 | prefer |
| DeltaKronecker-all | 0.819 | 0.741 | 220 | 6997 | prefer |
| nscl5-all | 0.359 | 1.0 | 2 | 1189 | observe |
| tg-ConfigV2rayNG | 0.319 | 1.0 | 2 | 200 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7108 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6859 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4665 | observe |
| barry-far-vless | 0.255 | None | 0 | 5259 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5333 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 44 |
| speed | ClientOSError | - | 27 |
| cn-block | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 9 |
| geo | ClientOSError | - | 7 |
| speed | TimeoutError | - | 7 |
| 204 | ProxyError | - | 3 |
| 204 | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 267 | 300 | - |
| global | False | 274 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
