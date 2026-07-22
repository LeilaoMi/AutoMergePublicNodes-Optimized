# AutoNodes 每日报告

生成时间：2026-07-22 03:24:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 82651 |
| 去重后节点数 | 23277 |
| TCP 可达数 | 3000 |
| 真测通过数 | 696 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23277 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 47.7 |
| geo | 1.3 |
| probe | 70.7 |
| real_test | 209.6 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 153 | 139 | 14 | 90.8% |
| socks | 6 | 2 | 4 | 33.3% |
| trojan | 420 | 375 | 45 | 89.3% |
| vless | 625 | 140 | 485 | 22.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 238 |
| cn-block:TimeoutError | 106 |
| speed:ClientOSError | 94 |
| geo:ClientOSError | 42 |
| speed:TimeoutError | 38 |
| cn-block:ClientOSError | 10 |
| 204:TimeoutError | 10 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4313 |
| ConnectionRefusedError | 671 |
| gaierror | 316 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.953 | prefer | 108 | 0.88 | 5428 |
| Au1rxx-base64 | 0.8 | prefer | 214 | 0.785 | 432 |
| mheidari-all | 0.552 | observe | 811 | 0.472 | 19634 |
| xiaoji235-airport-v2ray-all | 0.4 | observe | 4 | 0.75 | 4246 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4482 |
| Epodonios-all | 0.255 | observe | 0 | None | 6487 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6978 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4091 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.249 | 69 | 0.159 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.159 | 11 | 58 | 69 |
| mheidari-all | 0.472 | 383 | 428 | 811 |
| xiaoji235-airport-v2ray-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.785 | 168 | 46 | 214 |
| Surfboard-tg-mixed | 0.88 | 95 | 13 | 108 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19634 | yes | 4.71 | 0 |
| SoliSpirit-all | 6978 | yes | 2.82 | 0 |
| Epodonios-all | 6487 | yes | 1.96 | 0 |
| Surfboard-tg-mixed | 5428 | yes | 2.62 | 0 |
| DeltaKronecker-all | 5415 | yes | 3.72 | 0 |
| mahdibland-V2RayAggregator | 5204 | yes | 2.04 | 0 |
| barry-far-vless | 4665 | yes | 1.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 4482 | yes | 1.35 | 0 |
| xiaoji235-airport-v2ray-all | 4246 | yes | 1.25 | 0 |
| Surfboard-tg-vless | 4091 | yes | 2.45 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 280 |
| speed | 133 |
| cn-block | 117 |
| 204 | 18 |
