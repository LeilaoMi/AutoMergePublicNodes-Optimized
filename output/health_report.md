# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-21 23:14:41 |
| 运行耗时 | 252.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 73540 |
| 去重后节点 | 22011 |
| TCP 可达 | 3000 |
| 真实可用 | 752 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22011 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.3 |
| tcp | 29.2 |
| probe | 52.2 |
| real_test | 138.0 |
| generate | 27.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43137 |
| trojan | 9968 |
| shadowsocks | 9926 |
| vmess | 9851 |
| hysteria2 | 250 |
| http | 182 |
| shadowsocksr | 163 |
| socks | 55 |
| hysteria | 6 |
| tuic | 2 |

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
| 73.1 | shadowsocks | 239.4 | 590.1 | 22.24 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 156.146.38.169 |
| 72.64 | shadowsocks | 259.0 | 642.9 | 21.78 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 156.146.38.167 |
| 71.67 | shadowsocks | 301.1 | 777.6 | 20.81 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 156.146.38.170 |
| 70.83 | vless | 271.0 | 558.9 | 21.51 | 0.0 | 10.0 | 11.24 | 16.36 | mheidari-all | 64.23.143.23 |
| 70.1 | vless | 296.5 | 557.9 | 20.92 | 0.0 | 9.68 | 11.24 | 17.7 | Au1rxx-base64 | a.cflive.top |
| 69.35 | vless | 343.3 | 787.0 | 19.83 | 0.0 | 10.0 | 11.24 | 16.36 | mheidari-all | 47.253.226.114 |
| 69.27 | vless | 345.0 | 736.8 | 19.79 | 0.0 | 10.0 | 11.24 | 17.7 | Au1rxx-base64 | 137.184.218.169 |
| 69.24 | shadowsocks | 321.1 | 763.5 | 20.34 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 107.172.250.161 |
| 68.6 | shadowsocks | 299.5 | 689.1 | 20.85 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 37.19.198.160 |
| 68.5 | shadowsocks | 306.0 | 705.8 | 20.69 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 37.19.198.236 |
| 68.49 | shadowsocks | 326.4 | 748.7 | 20.22 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 37.19.198.243 |
| 68.35 | shadowsocks | 288.6 | 584.3 | 21.1 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 173.244.56.9 |
| 68.07 | shadowsocks | 327.4 | 757.8 | 20.2 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 67.89 | shadowsocks | 273.4 | 605.0 | 21.45 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 167.160.90.51 |
| 67.59 | shadowsocks | 266.1 | 561.0 | 21.62 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 216.105.168.18 |
| 67.43 | shadowsocks | 363.3 | 870.0 | 19.37 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 37.19.198.244 |
| 67.21 | vless | 422.1 | 935.1 | 18.01 | 0.0 | 10.0 | 11.24 | 17.7 | Au1rxx-base64 | 15.204.97.219 |
| 67.1 | vless | 413.6 | 887.0 | 18.2 | 0.0 | 10.0 | 11.24 | 17.7 | Au1rxx-base64 | 15.204.97.214 |
| 66.9 | vless | 410.8 | 865.1 | 18.27 | 0.0 | 10.0 | 11.24 | 17.7 | Au1rxx-base64 | 34.213.172.16 |
| 66.56 | shadowsocks | 321.6 | 713.0 | 20.33 | 0.0 | 10.0 | 12.16 | 17.7 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | 1.0 | 69 | 131 | prefer |
| mheidari-all | 0.98 | 0.903 | 329 | 15086 | prefer |
| Au1rxx-base64 | 0.902 | 0.906 | 85 | 135 | prefer |
| Surfboard-tg-mixed | 0.894 | 0.816 | 305 | 4776 | prefer |
| DeltaKronecker-all | 0.686 | 0.608 | 97 | 6748 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4494 | observe |
| Epodonios-all | 0.255 | None | 0 | 7271 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6970 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3678 | observe |
| barry-far-vless | 0.255 | None | 0 | 4628 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4505 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.223 | None | 0 | 1204 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 52 |
| geo | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| speed | TimeoutError | - | 13 |
| geo | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 8 |
| 204 | ProxyError | - | 8 |
| 204 | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
