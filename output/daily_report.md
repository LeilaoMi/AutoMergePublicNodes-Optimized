# AutoNodes 每日报告

生成时间：2026-07-12 13:42:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77498 |
| 去重后节点数 | 24183 |
| TCP 可达数 | 3000 |
| 真测通过数 | 284 |
| verified 输出数 | 284 |
| global 输出数 | 300 |
| all 输出数 | 24183 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 44.0 |
| geo | 1.3 |
| probe | 45.8 |
| real_test | 74.7 |
| tcp | 32.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 1 | 1 | 0 | 100.0% |
| shadowsocks | 116 | 95 | 21 | 81.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 173 | 136 | 37 | 78.6% |
| vless | 41 | 10 | 31 | 24.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 15 |
| speed:ClientOSError | 14 |
| geo:TimeoutError | 13 |
| cn-block:ClientOSError | 9 |
| geo:ClientOSError | 9 |
| cn-block:TimeoutError | 9 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 3 |
| speed:TimeoutError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4478 |
| ConnectionRefusedError | 656 |
| gaierror | 262 |
| OSError | 202 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.907 | prefer | 39 | 0.923 | 105 |
| Surfboard-tg-mixed | 0.833 | prefer | 87 | 0.759 | 5528 |
| mheidari-all | 0.778 | prefer | 84 | 0.702 | 16247 |
| DeltaKronecker-all | 0.757 | prefer | 125 | 0.68 | 8141 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 6473 |
| xiaoji235-airport-v2ray-all | 0.315 | observe | 1 | 1.0 | 1508 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4003 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6883 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.68 | 85 | 40 | 125 |
| mheidari-all | 0.702 | 59 | 25 | 84 |
| Surfboard-tg-mixed | 0.759 | 66 | 21 | 87 |
| Au1rxx-base64 | 0.923 | 36 | 3 | 39 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16247 | yes | 3.69 | 0 |
| DeltaKronecker-all | 8141 | yes | 3.85 | 0 |
| SoliSpirit-all | 6883 | yes | 2.04 | 0 |
| Epodonios-all | 6473 | yes | 1.91 | 0 |
| Surfboard-tg-mixed | 5528 | yes | 1.62 | 0 |
| mahdibland-V2RayAggregator | 5416 | yes | 1.71 | 0 |
| barry-far-vless | 4831 | yes | 1.48 | 0 |
| Surfboard-tg-vless | 4291 | yes | 2.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 4003 | yes | 1.67 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.76 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 26 |
| geo | 25 |
| cn-block | 21 |
| speed | 19 |
