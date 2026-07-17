# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-17 03:19:52 |
| 运行耗时 | 213.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 79372 |
| 去重后节点 | 24584 |
| TCP 可达 | 3000 |
| 真实可用 | 614 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24584 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.1 |
| tcp | 33.0 |
| probe | 47.7 |
| real_test | 106.3 |
| generate | 20.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45696 |
| trojan | 12553 |
| vmess | 10871 |
| shadowsocks | 9715 |
| hysteria2 | 271 |
| shadowsocksr | 128 |
| http | 97 |
| socks | 29 |
| hysteria | 8 |
| tuic | 4 |

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
| 78.57 | shadowsocks | 252.2 | 608.0 | 21.94 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 156.146.38.169 |
| 78.41 | shadowsocks | 259.0 | 631.1 | 21.78 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 156.146.38.168 |
| 78.4 | shadowsocks | 259.7 | 639.3 | 21.77 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 156.146.38.170 |
| 78.19 | shadowsocks | 268.5 | 673.6 | 21.56 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 37.19.198.236 |
| 77.91 | shadowsocks | 259.2 | 649.5 | 21.78 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 185.196.61.82 |
| 77.51 | shadowsocks | 273.3 | 672.6 | 21.45 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 37.19.198.243 |
| 77.43 | shadowsocks | 258.3 | 640.6 | 21.8 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 156.146.38.167 |
| 76.47 | shadowsocks | 321.4 | 877.9 | 20.34 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 50.114.177.235 |
| 75.23 | shadowsocks | 335.8 | 851.2 | 20.0 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 68.168.222.210 |
| 73.27 | vmess | 400.3 | 1090.5 | 18.51 | 0.0 | 10.0 | 12.0 | 17.26 | mheidari-all | 67.220.95.3 |
| 73.11 | shadowsocks | 272.1 | 678.2 | 21.48 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 37.19.198.244 |
| 72.97 | shadowsocks | 287.0 | 570.9 | 21.13 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 173.244.56.9 |
| 72.86 | shadowsocks | 290.8 | 580.4 | 21.05 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 173.244.56.6 |
| 72.04 | shadowsocks | 303.1 | 628.0 | 20.76 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 149.22.95.183 |
| 71.9 | shadowsocks | 288.3 | 710.7 | 21.1 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 108.181.57.93 |
| 71.75 | shadowsocks | 321.0 | 621.4 | 20.35 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 108.181.0.177 |
| 71.62 | shadowsocks | 314.6 | 568.0 | 20.5 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 108.181.118.10 |
| 69.64 | shadowsocks | 275.2 | 663.7 | 21.41 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 69.64 | shadowsocks | 357.3 | 346.8 | 19.51 | 1.99 | 9.53 | 12.13 | 18.5 | Au1rxx-base64 | 149.22.87.240 |
| 68.73 | shadowsocks | 271.8 | 551.0 | 21.48 | 0.0 | 10.0 | 12.13 | 18.5 | Au1rxx-base64 | 216.105.168.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.975 | 1.0 | 35 | 61 | prefer |
| mheidari-all | 0.97 | 0.895 | 152 | 16574 | prefer |
| Surfboard-tg-mixed | 0.932 | 0.856 | 153 | 5396 | prefer |
| Au1rxx-base64 | 0.928 | 0.932 | 88 | 149 | prefer |
| DeltaKronecker-all | 0.796 | 0.717 | 318 | 8462 | prefer |
| xiaoji235-airport-v2ray-all | 0.322 | 1.0 | 1 | 1680 | observe |
| nscl5-all | 0.28 | 0.5 | 2 | 1821 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4470 | observe |
| Epodonios-all | 0.255 | None | 0 | 6574 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6961 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4171 | observe |
| barry-far-vless | 0.255 | None | 0 | 4857 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5260 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 48 |
| geo | TimeoutError | - | 39 |
| speed | TimeoutError | - | 13 |
| geo | ClientOSError | - | 12 |
| cn-block | TimeoutError | - | 11 |
| 204 | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
