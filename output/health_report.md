# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-29 06:40:11 |
| 运行耗时 | 261.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 76898 |
| 去重后节点 | 20895 |
| TCP 可达 | 3000 |
| 真实可用 | 630 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 20895 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.5 |
| tcp | 35.1 |
| probe | 58.6 |
| real_test | 130.6 |
| generate | 29.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47452 |
| vmess | 10683 |
| shadowsocks | 10513 |
| trojan | 6300 |
| hysteria2 | 1582 |
| http | 174 |
| shadowsocksr | 128 |
| socks | 56 |
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
| 83.88 | vless | 266.2 | 686.0 | 21.62 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 166.88.186.151 |
| 83.85 | trojan | 202.2 | 512.7 | 23.1 | 0.0 | 10.0 | 13.75 | 20.0 | Au1rxx-base64 | 107.150.105.84 |
| 83.04 | vless | 216.1 | 524.1 | 22.78 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 64.23.229.123 |
| 83.0 | vless | 260.9 | 639.3 | 21.74 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 192.220.9.89 |
| 82.12 | shadowsocks | 240.3 | 582.8 | 22.22 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 81.84 | shadowsocks | 230.7 | 575.5 | 22.44 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 81.66 | http | 300.4 | 826.7 | 20.82 | 0.0 | 10.0 | 14.5 | 19.34 | zhangkai | 138.199.35.216 |
| 81.53 | http | 306.4 | 841.2 | 20.69 | 0.0 | 10.0 | 14.5 | 19.34 | zhangkai | 138.199.35.198 |
| 81.23 | vless | 284.7 | 775.5 | 21.19 | 0.0 | 10.0 | 12.26 | 17.78 | DeltaKronecker-all | 108.186.202.51 |
| 80.99 | trojan | 251.5 | 670.9 | 21.96 | 0.0 | 10.0 | 13.75 | 17.78 | DeltaKronecker-all | 34.94.125.227 |
| 80.81 | shadowsocks | 253.2 | 623.3 | 21.92 | 0.0 | 9.53 | 13.9 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 80.63 | shadowsocks | 260.2 | 597.5 | 21.75 | 0.0 | 10.0 | 13.9 | 18.98 | mheidari-all | 156.146.38.170 |
| 80.49 | trojan | 217.8 | 507.7 | 22.74 | 0.0 | 10.0 | 13.75 | 20.0 | Au1rxx-base64 | us01.duotg.top |
| 80.47 | vless | 197.2 | 509.8 | 23.21 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 172.235.43.210 |
| 80.45 | vless | 340.9 | 823.1 | 19.89 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 15.204.97.206 |
| 80.45 | vless | 350.2 | 851.6 | 19.67 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 15.204.97.195 |
| 80.44 | vless | 198.5 | 515.6 | 23.18 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 172.239.67.231 |
| 80.39 | vless | 200.8 | 525.7 | 23.13 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 172.235.38.85 |
| 80.33 | vless | 203.4 | 520.3 | 23.07 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 172.233.139.46 |
| 80.25 | vless | 354.9 | 839.9 | 19.56 | 0.0 | 10.0 | 12.26 | 20.0 | Au1rxx-base64 | 15.204.97.197 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Au1rxx-base64 | 0.959 | 0.889 | 379 | 1789 | prefer |
| mheidari-all | 0.852 | 0.778 | 99 | 14598 | prefer |
| DeltaKronecker-all | 0.801 | 0.724 | 170 | 4065 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.719 | 89 | 6733 | prefer |
| tg-oneclickvpnkeys | 0.326 | 0.75 | 4 | 139 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7084 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7191 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5530 | observe |
| barry-far-vless | 0.255 | None | 0 | 5694 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4093 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 26 |
| geo | ClientOSError | - | 25 |
| cn-block | TimeoutError | - | 21 |
| 204 | TimeoutError | - | 16 |
| geo | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 11 |
| 204 | ProxyError | - | 9 |
| cn-block | ProxyError | - | 6 |
| speed | ClientOSError | - | 6 |
| geo | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
