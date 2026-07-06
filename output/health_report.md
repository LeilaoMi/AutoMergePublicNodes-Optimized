# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-06 15:48:22 |
| 运行耗时 | 179.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 79704 |
| 去重后节点 | 24484 |
| TCP 可达 | 3000 |
| 真实可用 | 375 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24484 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.3 |
| tcp | 31.0 |
| probe | 42.9 |
| real_test | 73.9 |
| generate | 26.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46285 |
| trojan | 12680 |
| vmess | 10482 |
| shadowsocks | 9433 |
| hysteria2 | 465 |
| shadowsocksr | 148 |
| http | 139 |
| socks | 55 |
| tuic | 11 |
| hysteria | 6 |

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
| 78.33 | shadowsocks | 262.6 | 658.7 | 21.7 | 0.0 | 10.0 | 12.91 | 18.22 | mheidari-all | 108.181.57.93 |
| 78.21 | shadowsocks | 235.6 | 630.6 | 22.32 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 37.19.198.243 |
| 78.09 | shadowsocks | 241.2 | 646.4 | 22.2 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 37.19.198.160 |
| 74.74 | shadowsocks | 271.5 | 617.2 | 21.49 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 156.146.38.167 |
| 74.57 | shadowsocks | 284.2 | 650.1 | 21.2 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 156.146.38.168 |
| 74.37 | shadowsocks | 281.0 | 647.5 | 21.27 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 156.146.38.169 |
| 74.29 | trojan | 321.8 | 756.8 | 20.33 | 0.0 | 10.0 | 12.68 | 15.84 | DeltaKronecker-all | 149.28.241.235 |
| 74.28 | trojan | 323.2 | 768.1 | 20.3 | 0.0 | 10.0 | 12.68 | 15.84 | DeltaKronecker-all | 45.32.195.168 |
| 74.13 | shadowsocks | 341.6 | 822.5 | 19.87 | 0.0 | 10.0 | 12.91 | 18.22 | mheidari-all | 185.196.61.82 |
| 74.07 | trojan | 317.7 | 746.2 | 20.42 | 0.0 | 10.0 | 12.68 | 15.84 | DeltaKronecker-all | 45.32.198.247 |
| 72.1 | shadowsocks | 236.0 | 616.3 | 22.32 | 0.0 | 10.0 | 12.91 | 18.22 | mheidari-all | 198.98.53.130 |
| 71.37 | trojan | 401.0 | 903.5 | 18.5 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 64.94.95.118 |
| 71.14 | shadowsocks | 323.8 | 769.4 | 20.28 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 156.146.38.170 |
| 70.02 | trojan | 457.1 | 780.9 | 17.2 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 104.17.131.88 |
| 69.78 | trojan | 464.9 | 793.7 | 17.02 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 199.181.197.36 |
| 69.75 | trojan | 467.0 | 801.8 | 16.97 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 104.17.121.71 |
| 69.57 | trojan | 473.4 | 777.7 | 16.82 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 104.18.7.147 |
| 69.35 | shadowsocks | 339.5 | 581.9 | 19.92 | 0.0 | 10.0 | 12.91 | 16.98 | Au1rxx-base64 | 216.105.168.18 |
| 69.26 | trojan | 468.4 | 789.2 | 16.94 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 199.181.197.143 |
| 69.25 | trojan | 470.6 | 801.5 | 16.88 | 0.0 | 10.0 | 12.68 | 18.22 | mheidari-all | 104.20.42.250 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.887 | 0.813 | 107 | 5986 | prefer |
| DeltaKronecker-all | 0.852 | 0.775 | 187 | 8330 | prefer |
| mheidari-all | 0.796 | 0.719 | 114 | 16268 | prefer |
| Au1rxx-base64 | 0.753 | 0.773 | 22 | 84 | prefer |
| nscl5-all | 0.424 | 1.0 | 3 | 1651 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| ermaozi | 0.256 | 1.0 | 1 | 26 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4358 | observe |
| Epodonios-all | 0.255 | None | 0 | 6989 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7108 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4436 | observe |
| barry-far-vless | 0.255 | None | 0 | 5099 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 22 |
| speed | ClientOSError | - | 17 |
| 204 | ProxyError | - | 11 |
| 204 | TimeoutError | - | 11 |
| geo | TimeoutError | - | 9 |
| speed | ProxyError | - | 8 |
| geo | ClientOSError | - | 5 |
| geo | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| speed | TimeoutError | - | 3 |
| cn-block | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
