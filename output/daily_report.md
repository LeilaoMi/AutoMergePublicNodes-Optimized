# AutoNodes 每日报告

生成时间：2026-07-13 19:39:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77315 |
| 去重后节点数 | 23920 |
| TCP 可达数 | 3000 |
| 真测通过数 | 205 |
| verified 输出数 | 205 |
| global 输出数 | 214 |
| all 输出数 | 23920 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 35.6 |
| geo | 1.3 |
| probe | 43.6 |
| real_test | 68.8 |
| tcp | 32.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 81 | 67 | 14 | 82.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 122 | 81 | 41 | 66.4% |
| vless | 57 | 15 | 42 | 26.3% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 27 |
| speed:ClientOSError | 20 |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 8 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 6 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 2 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4607 |
| ConnectionRefusedError | 659 |
| gaierror | 213 |
| OSError | 191 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.771 | prefer | 53 | 0.698 | 16297 |
| DeltaKronecker-all | 0.723 | prefer | 96 | 0.646 | 7926 |
| Surfboard-tg-mixed | 0.673 | observe | 116 | 0.595 | 5561 |
| Au1rxx-base64 | 0.259 | observe | 1 | 1.0 | 91 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3897 |
| Epodonios-all | 0.255 | observe | 0 | None | 6496 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6673 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4279 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.595 | 69 | 47 | 116 |
| DeltaKronecker-all | 0.646 | 62 | 34 | 96 |
| mheidari-all | 0.698 | 37 | 16 | 53 |
| Au1rxx-base64 | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16297 | yes | 3.63 | 0 |
| DeltaKronecker-all | 7926 | yes | 3.81 | 0 |
| SoliSpirit-all | 6673 | yes | 2.53 | 0 |
| Epodonios-all | 6496 | yes | 1.56 | 0 |
| Surfboard-tg-mixed | 5561 | yes | 2.6 | 0 |
| mahdibland-V2RayAggregator | 5454 | yes | 1.71 | 0 |
| barry-far-vless | 4810 | yes | 1.5 | 0 |
| Surfboard-tg-vless | 4279 | yes | 2.1 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 2.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 3897 | yes | 1.67 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 31 |
| 204 | 27 |
| speed | 23 |
| cn-block | 17 |
