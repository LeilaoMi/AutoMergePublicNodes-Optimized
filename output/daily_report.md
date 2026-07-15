# AutoNodes 每日报告

生成时间：2026-07-15 02:55:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76515 |
| 去重后节点数 | 23743 |
| TCP 可达数 | 3000 |
| 真测通过数 | 285 |
| verified 输出数 | 285 |
| global 输出数 | 293 |
| all 输出数 | 23743 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 30.2 |
| geo | 1.5 |
| probe | 43.2 |
| real_test | 82.5 |
| tcp | 33.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 59 | 52 | 7 | 88.1% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 177 | 167 | 10 | 94.4% |
| vless | 250 | 22 | 228 | 8.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 134 |
| geo:TimeoutError | 57 |
| geo:ClientOSError | 36 |
| speed:TimeoutError | 6 |
| cn-block:TimeoutError | 5 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| 204:ProxyError | 1 |
| 204:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4660 |
| ConnectionRefusedError | 654 |
| gaierror | 232 |
| OSError | 208 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.806 | prefer | 82 | 0.732 | 5500 |
| mheidari-all | 0.741 | prefer | 110 | 0.664 | 18109 |
| DeltaKronecker-all | 0.46 | observe | 298 | 0.379 | 6421 |
| Au1rxx-base64 | 0.317 | observe | 2 | 1.0 | 149 |
| nscl5-all | 0.26 | observe | 2 | 0.5 | 1300 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4019 |
| Epodonios-all | 0.255 | observe | 0 | None | 6322 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3968 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6061 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.379 | 113 | 185 | 298 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.664 | 73 | 37 | 110 |
| Surfboard-tg-mixed | 0.732 | 60 | 22 | 82 |
| Au1rxx-base64 | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18109 | yes | 4.19 | 0 |
| DeltaKronecker-all | 6421 | yes | 3.09 | 0 |
| Epodonios-all | 6322 | yes | 1.85 | 0 |
| SoliSpirit-all | 6061 | yes | 1.76 | 0 |
| Surfboard-tg-mixed | 5500 | yes | 2.66 | 0 |
| mahdibland-V2RayAggregator | 5187 | yes | 1.53 | 0 |
| barry-far-vless | 4653 | yes | 1.39 | 0 |
| Surfboard-tg-vless | 4205 | yes | 2.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 4019 | yes | 0.7 | 0 |
| MatinGhanbari-all-sub | 3968 | yes | 1.05 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.088 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 140 |
| geo | 93 |
| cn-block | 9 |
| 204 | 5 |
