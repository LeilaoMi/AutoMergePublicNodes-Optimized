# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-01 14:52:16 |
| 运行耗时 | 236.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 76903 |
| 去重后节点 | 23340 |
| TCP 可达 | 3000 |
| 真实可用 | 400 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23340 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 31.0 |
| probe | 49.0 |
| real_test | 100.7 |
| generate | 49.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43883 |
| trojan | 12871 |
| vmess | 10255 |
| shadowsocks | 9287 |
| hysteria2 | 253 |
| shadowsocksr | 158 |
| http | 135 |
| socks | 54 |
| hysteria | 6 |
| tuic | 1 |

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
| 74.58 | shadowsocks | 233.5 | 638.5 | 22.37 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 37.19.198.236 |
| 74.51 | shadowsocks | 236.5 | 650.7 | 22.3 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 37.19.198.160 |
| 74.41 | shadowsocks | 241.1 | 652.7 | 22.2 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 37.19.198.244 |
| 73.64 | shadowsocks | 230.9 | 635.1 | 22.43 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 37.19.198.243 |
| 71.51 | shadowsocks | 344.5 | 957.9 | 19.8 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 108.181.57.93 |
| 71.43 | shadowsocks | 218.3 | 585.2 | 22.72 | 0.0 | 10.0 | 11.93 | 10.78 | mheidari-all | 198.98.53.130 |
| 71.25 | shadowsocks | 278.3 | 639.1 | 21.34 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 156.146.38.169 |
| 71.18 | vless | 311.0 | 855.7 | 20.58 | 0.0 | 10.0 | 7.12 | 13.48 | Surfboard-tg-mixed | 137.184.218.169 |
| 70.67 | shadowsocks | 281.3 | 641.1 | 21.27 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 156.146.38.168 |
| 70.56 | shadowsocks | 284.3 | 665.4 | 21.2 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 156.146.38.167 |
| 70.37 | shadowsocks | 276.3 | 641.4 | 21.38 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 156.146.38.170 |
| 69.66 | vless | 259.8 | 728.0 | 21.76 | 0.0 | 10.0 | 7.12 | 10.78 | mheidari-all | 47.253.226.114 |
| 68.72 | vmess | 290.0 | 797.9 | 21.06 | 0.0 | 10.0 | 12.86 | 10.3 | DeltaKronecker-all | 67.220.85.46 |
| 68.14 | shadowsocks | 360.4 | 979.4 | 19.43 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 172.234.202.34 |
| 66.71 | vless | 322.5 | 820.8 | 20.31 | 0.0 | 10.0 | 7.12 | 14.28 | Au1rxx-base64 | 159.89.87.21 |
| 66.62 | vless | 291.9 | 834.2 | 21.02 | 0.0 | 10.0 | 7.12 | 13.48 | Surfboard-tg-mixed | 54.91.34.214 |
| 66.39 | shadowsocks | 346.6 | 654.0 | 19.76 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 149.22.95.183 |
| 65.69 | shadowsocks | 339.7 | 675.2 | 19.91 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 108.181.118.10 |
| 65.31 | shadowsocks | 389.3 | 782.9 | 18.77 | 0.0 | 10.0 | 11.93 | 14.28 | Au1rxx-base64 | 108.181.0.177 |
| 64.85 | http | 627.8 | 959.2 | 13.24 | 0.0 | 9.84 | 14.25 | 19.04 | snakem982 | 193.176.84.31 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.846 | 0.855 | 55 | 96 | prefer |
| Surfboard-tg-mixed | 0.686 | 0.607 | 275 | 5849 | observe |
| mheidari-all | 0.575 | 0.495 | 212 | 15660 | observe |
| DeltaKronecker-all | 0.493 | 0.411 | 107 | 7631 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4308 | observe |
| Epodonios-all | 0.255 | None | 0 | 6803 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6937 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4351 | observe |
| barry-far-vless | 0.255 | None | 0 | 4908 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5331 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 169 |
| geo | TimeoutError | - | 22 |
| 204 | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 15 |
| 204 | ClientOSError | - | 15 |
| geo | ClientOSError | - | 14 |
| 204 | ProxyError | - | 11 |
| cn-block | ProxyError | - | 5 |
| speed | TimeoutError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
