# AutoNodes 每日报告

生成时间：2026-07-28 19:43:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 80840 |
| 去重后节点数 | 22955 |
| TCP 可达数 | 3000 |
| 真测通过数 | 346 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22955 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 32.4 |
| geo | 1.4 |
| probe | 47.2 |
| real_test | 87.7 |
| tcp | 32.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 186 | 135 | 51 | 72.6% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 57 | 42 | 15 | 73.7% |
| vless | 214 | 155 | 59 | 72.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 27 |
| 204:TimeoutError | 23 |
| cn-block:TimeoutError | 22 |
| 204:ProxyError | 19 |
| geo:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 6 |
| speed:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4181 |
| ConnectionRefusedError | 757 |
| gaierror | 344 |
| OSError | 220 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.858 | prefer | 270 | 0.807 | 1312 |
| mheidari-all | 0.717 | prefer | 133 | 0.639 | 17378 |
| DeltaKronecker-all | 0.69 | observe | 39 | 0.615 | 5965 |
| Surfboard-tg-mixed | 0.661 | observe | 29 | 0.586 | 5820 |
| 10ium-ScrapeCategorize-Vless | 0.349 | observe | 3 | 0.667 | 4972 |
| Epodonios-all | 0.255 | observe | 0 | None | 6834 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6507 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4597 |
| barry-far-vless | 0.255 | observe | 0 | None | 5117 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.586 | 17 | 12 | 29 |
| DeltaKronecker-all | 0.615 | 24 | 15 | 39 |
| mheidari-all | 0.639 | 85 | 48 | 133 |
| 10ium-ScrapeCategorize-Vless | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.807 | 218 | 52 | 270 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17378 | yes | 4.12 | 0 |
| Epodonios-all | 6834 | yes | 3.63 | 0 |
| SoliSpirit-all | 6507 | yes | 3.66 | 0 |
| DeltaKronecker-all | 5965 | yes | 4.69 | 0 |
| Surfboard-tg-mixed | 5820 | yes | 2.7 | 0 |
| barry-far-vless | 5117 | yes | 0.96 | 0 |
| mahdibland-V2RayAggregator | 5059 | yes | 2.19 | 0 |
| 10ium-ScrapeCategorize-Vless | 4972 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 4597 | yes | 2.87 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.32 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 48 |
| geo | 37 |
| cn-block | 30 |
| speed | 14 |
