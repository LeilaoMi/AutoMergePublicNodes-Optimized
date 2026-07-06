# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-06 04:07:54 |
| 运行耗时 | 180.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78913 |
| 去重后节点 | 24116 |
| TCP 可达 | 3000 |
| 真实可用 | 448 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24116 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.3 |
| tcp | 31.1 |
| probe | 42.6 |
| real_test | 79.2 |
| generate | 21.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45238 |
| trojan | 13001 |
| vmess | 10424 |
| shadowsocks | 9438 |
| hysteria2 | 460 |
| shadowsocksr | 155 |
| http | 135 |
| socks | 48 |
| tuic | 8 |
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
| 78.21 | shadowsocks | 225.2 | 623.0 | 22.57 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 37.19.198.160 |
| 78.12 | shadowsocks | 229.0 | 634.7 | 22.48 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 37.19.198.244 |
| 78.1 | shadowsocks | 229.9 | 637.7 | 22.46 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 37.19.198.236 |
| 78.07 | shadowsocks | 230.8 | 637.0 | 22.43 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 37.19.198.243 |
| 77.44 | shadowsocks | 225.5 | 598.3 | 22.56 | 0.0 | 10.0 | 13.14 | 15.74 | mheidari-all | 198.98.53.130 |
| 76.61 | shadowsocks | 239.9 | 637.4 | 22.23 | 0.0 | 10.0 | 13.14 | 15.74 | mheidari-all | 108.181.57.93 |
| 74.33 | shadowsocks | 297.4 | 647.0 | 20.89 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 156.146.38.169 |
| 73.74 | shadowsocks | 288.3 | 658.7 | 21.1 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 156.146.38.167 |
| 73.7 | shadowsocks | 276.5 | 625.9 | 21.38 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 156.146.38.168 |
| 73.53 | shadowsocks | 352.2 | 885.7 | 19.62 | 0.0 | 10.0 | 13.14 | 15.74 | mheidari-all | 185.196.61.82 |
| 73.4 | shadowsocks | 295.6 | 815.9 | 20.94 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 71.39 | hysteria2 | 353.8 | 690.0 | 19.59 | 0.0 | 9.98 | 12.0 | 16.5 | Au1rxx-base64 | 62.210.124.146 |
| 71.07 | trojan | 332.9 | 764.8 | 20.07 | 0.0 | 10.0 | 10.79 | 15.42 | DeltaKronecker-all | 149.28.241.235 |
| 70.85 | trojan | 343.2 | 802.8 | 19.83 | 0.0 | 10.0 | 10.79 | 15.42 | DeltaKronecker-all | 45.32.195.168 |
| 70.76 | vless | 268.2 | 667.8 | 21.57 | 0.0 | 10.0 | 4.77 | 15.42 | DeltaKronecker-all | 104.25.161.29 |
| 70.4 | shadowsocks | 321.8 | 601.6 | 20.33 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 149.22.95.183 |
| 70.18 | shadowsocks | 305.3 | 563.5 | 20.71 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 108.181.0.177 |
| 69.67 | shadowsocks | 287.6 | 662.3 | 21.12 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 156.146.38.170 |
| 69.19 | shadowsocks | 356.9 | 669.1 | 19.52 | 0.0 | 10.0 | 13.14 | 16.5 | Au1rxx-base64 | 108.181.118.10 |
| 68.94 | trojan | 411.7 | 1009.5 | 18.25 | 0.0 | 10.0 | 10.79 | 15.42 | DeltaKronecker-all | 45.32.198.247 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.987 | 0.913 | 127 | 5914 | prefer |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.969 | 0.897 | 97 | 16346 | prefer |
| Au1rxx-base64 | 0.831 | 0.841 | 44 | 133 | prefer |
| DeltaKronecker-all | 0.77 | 0.691 | 243 | 7739 | prefer |
| nscl5-all | 0.321 | 1.0 | 1 | 1651 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Pawdroid | 0.256 | 1.0 | 1 | 20 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4662 | observe |
| Epodonios-all | 0.255 | None | 0 | 7009 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6809 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4330 | observe |
| barry-far-vless | 0.255 | None | 0 | 5045 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 34 |
| speed | ClientOSError | - | 27 |
| geo | ClientOSError | - | 16 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 8 |
| speed | TimeoutError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 278 | 300 | - |
| global | False | 292 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
