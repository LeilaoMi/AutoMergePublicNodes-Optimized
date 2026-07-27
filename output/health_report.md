# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-27 10:07:05 |
| 运行耗时 | 370.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 84235 |
| 去重后节点 | 22876 |
| TCP 可达 | 3000 |
| 真实可用 | 733 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22876 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.5 |
| tcp | 32.2 |
| probe | 78.1 |
| real_test | 212.2 |
| generate | 40.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46872 |
| trojan | 15553 |
| shadowsocks | 10521 |
| vmess | 10340 |
| hysteria2 | 622 |
| shadowsocksr | 103 |
| socks | 93 |
| http | 84 |
| anytls | 22 |
| hysteria | 13 |
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
| 83.0 | trojan | 258.0 | 679.2 | 21.81 | 0.0 | 10.0 | 14.37 | 19.82 | Au1rxx-base64 | 153.75.250.171 |
| 82.02 | shadowsocks | 236.7 | 637.3 | 22.3 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 37.19.198.244 |
| 81.79 | shadowsocks | 246.6 | 667.4 | 22.07 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 37.19.198.160 |
| 80.93 | hysteria2 | 245.7 | 652.7 | 22.09 | 0.0 | 10.0 | 13.12 | 19.82 | Au1rxx-base64 | 159.223.157.129 |
| 80.84 | shadowsocks | 287.8 | 778.2 | 21.12 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 198.98.53.130 |
| 79.47 | shadowsocks | 284.1 | 653.5 | 21.2 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 156.146.38.168 |
| 79.16 | shadowsocks | 276.3 | 633.8 | 21.38 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 156.146.38.170 |
| 79.11 | shadowsocks | 273.1 | 637.2 | 21.46 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 185.196.61.82 |
| 79.04 | shadowsocks | 236.0 | 633.9 | 22.32 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 37.19.198.243 |
| 78.92 | shadowsocks | 282.3 | 658.7 | 21.24 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 156.146.38.169 |
| 78.14 | trojan | 300.8 | 646.9 | 20.81 | 0.0 | 10.0 | 14.37 | 19.82 | Au1rxx-base64 | 163.245.196.68 |
| 77.12 | trojan | 350.5 | 876.1 | 19.66 | 0.0 | 10.0 | 14.37 | 16.3 | DeltaKronecker-all | 64.74.163.118 |
| 76.99 | shadowsocks | 316.8 | 715.5 | 20.45 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 108.181.57.93 |
| 76.31 | trojan | 364.7 | 856.1 | 19.34 | 0.0 | 10.0 | 14.37 | 19.82 | Au1rxx-base64 | 64.94.95.118 |
| 76.17 | trojan | 477.8 | 1223.0 | 16.72 | 0.0 | 10.0 | 14.37 | 19.82 | Au1rxx-base64 | 148.72.168.35 |
| 75.96 | shadowsocks | 250.4 | 674.8 | 21.98 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 37.19.198.236 |
| 75.78 | hysteria2 | 355.6 | 691.9 | 19.55 | 0.0 | 10.0 | 13.12 | 19.82 | Au1rxx-base64 | 62.210.124.146 |
| 75.54 | shadowsocks | 282.1 | 649.2 | 21.25 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 156.146.38.167 |
| 74.95 | shadowsocks | 313.2 | 580.0 | 20.53 | 0.0 | 10.0 | 13.9 | 19.82 | Au1rxx-base64 | 173.244.56.6 |
| 74.77 | trojan | 293.1 | 637.7 | 20.99 | 0.0 | 10.0 | 14.37 | 19.82 | Au1rxx-base64 | 64.94.95.114 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.991 | 1.0 | 76 | 86 | prefer |
| Au1rxx-base64 | 0.975 | 0.92 | 426 | 1407 | prefer |
| Surfboard-tg-mixed | 0.705 | 0.63 | 54 | 5483 | prefer |
| tg-oneclickvpnkeys | 0.445 | 1.0 | 5 | 132 | observe |
| mheidari-all | 0.413 | 0.327 | 52 | 19339 | observe |
| DeltaKronecker-all | 0.369 | 0.289 | 714 | 5643 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 3959 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 174 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4831 | observe |
| Epodonios-all | 0.255 | None | 0 | 6410 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6188 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4173 | observe |
| barry-far-vless | 0.255 | None | 0 | 4692 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 202 |
| speed | ClientOSError | - | 177 |
| 204 | ProxyError | - | 54 |
| geo | ClientOSError | - | 50 |
| cn-block | TimeoutError | - | 34 |
| 204 | TimeoutError | - | 26 |
| speed | TimeoutError | - | 25 |
| cn-block | ProxyError | - | 15 |
| cn-block | ClientOSError | - | 9 |
| geo | ProxyError | - | 5 |
| 204 | ClientOSError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
