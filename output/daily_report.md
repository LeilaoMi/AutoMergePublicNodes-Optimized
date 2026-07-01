# AutoNodes 每日报告

生成时间：2026-07-01 10:04:21

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 75612 |
| 去重后节点数 | 23077 |
| TCP 可达数 | 3000 |
| 真测通过数 | 326 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23077 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 43.4 |
| geo | 1.4 |
| probe | 55.2 |
| real_test | 113.0 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 38 | 37 | 1 | 97.4% |
| hysteria2 | 7 | 3 | 4 | 42.9% |
| shadowsocks | 120 | 96 | 24 | 80.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 183 | 82 | 101 | 44.8% |
| vless | 215 | 102 | 113 | 47.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 110 |
| 204:TimeoutError | 41 |
| geo:TimeoutError | 27 |
| 204:ProxyError | 12 |
| 204:ClientOSError | 12 |
| cn-block:TimeoutError | 12 |
| geo:ClientOSError | 11 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 7 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4347 |
| ConnectionRefusedError | 636 |
| gaierror | 165 |
| OSError | 144 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.952 | prefer | 38 | 0.974 | 61 |
| Au1rxx-base64 | 0.714 | prefer | 60 | 0.717 | 115 |
| Surfboard-tg-mixed | 0.674 | observe | 249 | 0.594 | 5595 |
| mheidari-all | 0.539 | observe | 72 | 0.458 | 15660 |
| DeltaKronecker-all | 0.515 | observe | 145 | 0.434 | 7631 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| ermaozi | 0.256 | observe | 1 | 1.0 | 28 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4308 |
| Epodonios-all | 0.255 | observe | 0 | None | 6487 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.132 | observe | 4 | 0.0 | 0 | 1298 |
| chromego_merge | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| peasoft-NoMoreWalls | 0.175 | observe | 0 | None | 0 | 3 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.434 | 63 | 82 | 145 |
| mheidari-all | 0.458 | 33 | 39 | 72 |
| Surfboard-tg-mixed | 0.594 | 148 | 101 | 249 |
| Au1rxx-base64 | 0.717 | 43 | 17 | 60 |
| snakem982 | 0.974 | 37 | 1 | 38 |
| ermaozi | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15660 | yes | 2.98 | 0 |
| DeltaKronecker-all | 7631 | yes | 3.38 | 0 |
| SoliSpirit-all | 6549 | yes | 2.09 | 0 |
| Epodonios-all | 6487 | yes | 1.56 | 0 |
| Surfboard-tg-mixed | 5595 | yes | 3.21 | 0 |
| mahdibland-V2RayAggregator | 5331 | yes | 1.67 | 0 |
| barry-far-vless | 4743 | yes | 1.13 | 0 |
| 10ium-ScrapeCategorize-Vless | 4308 | yes | 0.93 | 0 |
| Surfboard-tg-vless | 4151 | yes | 1.9 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.22 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 118 |
| 204 | 65 |
| geo | 39 |
| cn-block | 22 |
