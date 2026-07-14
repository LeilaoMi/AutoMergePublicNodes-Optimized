# AutoNodes 每日报告

生成时间：2026-07-14 19:29:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 81121 |
| 去重后节点数 | 24269 |
| TCP 可达数 | 3000 |
| 真测通过数 | 165 |
| verified 输出数 | 165 |
| global 输出数 | 173 |
| all 输出数 | 24269 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 16.0 |
| geo | 1.3 |
| probe | 44.8 |
| real_test | 49.5 |
| tcp | 32.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 58 | 44 | 14 | 75.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 80 | 61 | 19 | 76.2% |
| vless | 57 | 13 | 44 | 22.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 28 |
| speed:ClientOSError | 16 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 5 |
| geo:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| speed:TimeoutError | 3 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4580 |
| ConnectionRefusedError | 664 |
| gaierror | 280 |
| OSError | 202 |
| UnicodeError | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.772 | prefer | 50 | 0.7 | 7942 |
| Surfboard-tg-mixed | 0.665 | observe | 51 | 0.588 | 5623 |
| mheidari-all | 0.653 | observe | 94 | 0.574 | 18091 |
| Au1rxx-base64 | 0.494 | observe | 8 | 0.875 | 139 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3836 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4019 |
| Epodonios-all | 0.255 | observe | 0 | None | 6538 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.574 | 54 | 40 | 94 |
| Surfboard-tg-mixed | 0.588 | 30 | 21 | 51 |
| DeltaKronecker-all | 0.7 | 35 | 15 | 50 |
| Au1rxx-base64 | 0.875 | 7 | 1 | 8 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18091 | yes | 2.13 | 0 |
| DeltaKronecker-all | 7942 | yes | 2.42 | 0 |
| Epodonios-all | 6538 | yes | 0.59 | 0 |
| SoliSpirit-all | 6320 | yes | 1.62 | 0 |
| Surfboard-tg-mixed | 5623 | yes | 1.44 | 0 |
| mahdibland-V2RayAggregator | 5187 | yes | 1.22 | 0 |
| barry-far-vless | 4852 | yes | 0.86 | 0 |
| Surfboard-tg-vless | 4338 | yes | 1.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 4019 | yes | 0.95 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 1.27 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 33 |
| speed | 21 |
| 204 | 15 |
| cn-block | 9 |
