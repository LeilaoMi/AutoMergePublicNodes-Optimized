# AutoNodes 每日报告

生成时间：2026-07-24 08:40:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83120 |
| 去重后节点数 | 22640 |
| TCP 可达数 | 3000 |
| 真测通过数 | 856 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22640 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 33.7 |
| geo | 1.3 |
| probe | 62.5 |
| real_test | 185.6 |
| tcp | 32.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 142 | 128 | 14 | 90.1% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 603 | 563 | 40 | 93.4% |
| vless | 394 | 124 | 270 | 31.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 133 |
| geo:ClientOSError | 41 |
| speed:ClientOSError | 38 |
| cn-block:TimeoutError | 37 |
| 204:ProxyError | 30 |
| speed:TimeoutError | 23 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 3 |
| speed:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4119 |
| ConnectionRefusedError | 685 |
| gaierror | 444 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.96 | prefer | 457 | 0.882 | 19618 |
| Au1rxx-base64 | 0.909 | prefer | 136 | 0.897 | 432 |
| Surfboard-tg-mixed | 0.662 | observe | 194 | 0.582 | 5319 |
| DeltaKronecker-all | 0.591 | observe | 354 | 0.511 | 5559 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 3847 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4588 |
| Epodonios-all | 0.255 | observe | 0 | None | 6546 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6796 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.511 | 181 | 173 | 354 |
| Surfboard-tg-mixed | 0.582 | 113 | 81 | 194 |
| mheidari-all | 0.882 | 403 | 54 | 457 |
| Au1rxx-base64 | 0.897 | 122 | 14 | 136 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19618 | yes | 4.42 | 0 |
| SoliSpirit-all | 6796 | yes | 2.55 | 0 |
| Epodonios-all | 6546 | yes | 1.1 | 0 |
| DeltaKronecker-all | 5559 | yes | 3.03 | 0 |
| Surfboard-tg-mixed | 5319 | yes | 2.39 | 0 |
| mahdibland-V2RayAggregator | 5027 | yes | 2.01 | 0 |
| barry-far-vless | 4836 | yes | 2.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4588 | yes | 1.93 | 0 |
| Surfboard-tg-vless | 4227 | yes | 2.19 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 2.02 | 0 |

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
| geo | 177 |
| speed | 64 |
| 204 | 43 |
| cn-block | 43 |
