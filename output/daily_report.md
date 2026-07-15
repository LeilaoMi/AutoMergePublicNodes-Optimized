# AutoNodes 每日报告

生成时间：2026-07-15 19:23:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 76371 |
| 去重后节点数 | 23023 |
| TCP 可达数 | 3000 |
| 真测通过数 | 202 |
| verified 输出数 | 202 |
| global 输出数 | 212 |
| all 输出数 | 23023 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| generate | 42.1 |
| geo | 1.5 |
| probe | 49.9 |
| real_test | 57.3 |
| tcp | 32.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 66 | 52 | 14 | 78.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 119 | 91 | 28 | 76.5% |
| vless | 91 | 15 | 76 | 16.5% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 41 |
| speed:ClientOSError | 29 |
| 204:TimeoutError | 16 |
| 204:ProxyError | 9 |
| geo:ClientOSError | 8 |
| cn-block:TimeoutError | 7 |
| cn-block:ClientOSError | 5 |
| speed:TimeoutError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4677 |
| ConnectionRefusedError | 653 |
| gaierror | 219 |
| OSError | 210 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.739 | prefer | 86 | 0.663 | 5510 |
| mheidari-all | 0.614 | observe | 86 | 0.535 | 16638 |
| DeltaKronecker-all | 0.613 | observe | 103 | 0.534 | 6421 |
| Au1rxx-base64 | 0.494 | observe | 8 | 0.875 | 138 |
| Surfboard-tg-vless | 0.335 | observe | 1 | 1.0 | 4277 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3759 |
| Epodonios-all | 0.255 | observe | 0 | None | 6514 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3967 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6930 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.534 | 55 | 48 | 103 |
| mheidari-all | 0.535 | 46 | 40 | 86 |
| Surfboard-tg-mixed | 0.663 | 57 | 29 | 86 |
| Au1rxx-base64 | 0.875 | 7 | 1 | 8 |
| Surfboard-tg-vless | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16638 | yes | 2.76 | 0 |
| SoliSpirit-all | 6930 | yes | 1.27 | 0 |
| Epodonios-all | 6514 | yes | 3.11 | 0 |
| DeltaKronecker-all | 6421 | yes | 3.04 | 0 |
| Surfboard-tg-mixed | 5510 | yes | 1.84 | 0 |
| mahdibland-V2RayAggregator | 5183 | yes | 1.54 | 0 |
| barry-far-vless | 4862 | yes | 0.92 | 0 |
| Surfboard-tg-vless | 4277 | yes | 1.47 | 0 |
| MatinGhanbari-all-sub | 3967 | yes | 0.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 3759 | yes | 0.62 | 0 |

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
| geo | 49 |
| speed | 32 |
| 204 | 25 |
| cn-block | 13 |
