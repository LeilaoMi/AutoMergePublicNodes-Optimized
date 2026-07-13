# AutoNodes 每日报告

生成时间：2026-07-13 14:50:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 77707 |
| 去重后节点数 | 23895 |
| TCP 可达数 | 3000 |
| 真测通过数 | 208 |
| verified 输出数 | 208 |
| global 输出数 | 222 |
| all 输出数 | 23895 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| generate | 47.3 |
| geo | 1.3 |
| probe | 44.3 |
| real_test | 97.1 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 62 | 49 | 13 | 79.0% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 179 | 102 | 77 | 57.0% |
| vless | 70 | 11 | 59 | 15.7% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 45 |
| speed:ClientOSError | 25 |
| 204:ProxyError | 19 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 13 |
| cn-block:ProxyError | 6 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 6 |
| geo:ProxyError | 6 |
| speed:ProxyError | 5 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4459 |
| ConnectionRefusedError | 657 |
| gaierror | 263 |
| OSError | 191 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.708 | prefer | 76 | 0.632 | 5596 |
| mheidari-all | 0.637 | observe | 86 | 0.558 | 16239 |
| DeltaKronecker-all | 0.545 | observe | 155 | 0.465 | 7926 |
| Au1rxx-base64 | 0.317 | observe | 2 | 1.0 | 134 |
| xiaoji235-airport-v2ray-all | 0.273 | observe | 2 | 0.5 | 1647 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3897 |
| Epodonios-all | 0.255 | observe | 0 | None | 6473 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.465 | 72 | 83 | 155 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.558 | 48 | 38 | 86 |
| Surfboard-tg-mixed | 0.632 | 48 | 28 | 76 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Au1rxx-base64 | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16239 | yes | 1.89 | 0 |
| DeltaKronecker-all | 7926 | yes | 2.23 | 0 |
| SoliSpirit-all | 6904 | yes | 1.1 | 0 |
| Epodonios-all | 6473 | yes | 0.62 | 0 |
| Surfboard-tg-mixed | 5596 | yes | 1.36 | 0 |
| mahdibland-V2RayAggregator | 5412 | yes | 0.91 | 0 |
| barry-far-vless | 4964 | yes | 0.57 | 0 |
| Surfboard-tg-vless | 4341 | yes | 1.43 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 3897 | yes | 0.66 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 52 |
| 204 | 38 |
| speed | 36 |
| cn-block | 25 |
