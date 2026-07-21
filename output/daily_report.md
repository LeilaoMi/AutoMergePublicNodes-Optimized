# AutoNodes 每日报告

生成时间：2026-07-21 08:42:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 81900 |
| 去重后节点数 | 22899 |
| TCP 可达数 | 3000 |
| 真测通过数 | 558 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22899 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 33.2 |
| geo | 1.4 |
| probe | 66.2 |
| real_test | 174.3 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 133 | 106 | 27 | 79.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 457 | 349 | 108 | 76.4% |
| vless | 581 | 63 | 518 | 10.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 275 |
| geo:TimeoutError | 200 |
| cn-block:TimeoutError | 67 |
| geo:ClientOSError | 36 |
| 204:TimeoutError | 18 |
| 204:ProxyError | 17 |
| speed:TimeoutError | 14 |
| cn-block:ProxyError | 9 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| speed:ProxyError | 4 |
| geo:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4470 |
| ConnectionRefusedError | 662 |
| gaierror | 244 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.769 | prefer | 252 | 0.69 | 19339 |
| Au1rxx-base64 | 0.695 | observe | 168 | 0.685 | 314 |
| Surfboard-tg-mixed | 0.674 | observe | 227 | 0.595 | 5412 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 4304 |
| DeltaKronecker-all | 0.266 | observe | 524 | 0.185 | 5415 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4482 |
| Epodonios-all | 0.255 | observe | 0 | None | 6403 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6715 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.185 | 97 | 427 | 524 |
| Surfboard-tg-mixed | 0.595 | 135 | 92 | 227 |
| Au1rxx-base64 | 0.685 | 115 | 53 | 168 |
| mheidari-all | 0.69 | 174 | 78 | 252 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19339 | yes | 3.56 | 0 |
| SoliSpirit-all | 6715 | yes | 2.19 | 0 |
| Epodonios-all | 6403 | yes | 1.93 | 0 |
| DeltaKronecker-all | 5415 | yes | 3.63 | 0 |
| Surfboard-tg-mixed | 5412 | yes | 3.1 | 0 |
| mahdibland-V2RayAggregator | 5247 | yes | 2.37 | 0 |
| barry-far-vless | 4688 | yes | 1.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4482 | yes | 1.12 | 0 |
| xiaoji235-airport-v2ray-all | 4304 | yes | 0.96 | 0 |
| Surfboard-tg-vless | 4142 | yes | 2.09 | 0 |

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
| speed | 293 |
| geo | 239 |
| cn-block | 82 |
| 204 | 40 |
