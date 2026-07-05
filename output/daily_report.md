# AutoNodes 每日报告

生成时间：2026-07-05 09:17:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79402 |
| 去重后节点数 | 23931 |
| TCP 可达数 | 3000 |
| 真测通过数 | 367 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23931 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 37.4 |
| geo | 5.5 |
| probe | 49.2 |
| real_test | 75.6 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 131 | 109 | 22 | 83.2% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 236 | 205 | 31 | 86.9% |
| vless | 45 | 8 | 37 | 17.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 21 |
| 204:ProxyError | 18 |
| 204:ClientOSError | 15 |
| speed:ClientOSError | 11 |
| 204:TimeoutError | 11 |
| geo:ClientOSError | 6 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4383 |
| ConnectionRefusedError | 789 |
| gaierror | 166 |
| OSError | 155 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.913 | prefer | 82 | 0.841 | 16512 |
| Surfboard-tg-mixed | 0.893 | prefer | 105 | 0.819 | 6080 |
| DeltaKronecker-all | 0.818 | prefer | 200 | 0.74 | 7739 |
| Au1rxx-base64 | 0.804 | prefer | 33 | 0.818 | 109 |
| nscl5-all | 0.308 | observe | 1 | 1.0 | 1323 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4662 |
| Epodonios-all | 0.255 | observe | 0 | None | 7028 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6942 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.74 | 148 | 52 | 200 |
| Au1rxx-base64 | 0.818 | 27 | 6 | 33 |
| Surfboard-tg-mixed | 0.819 | 86 | 19 | 105 |
| mheidari-all | 0.841 | 69 | 13 | 82 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16512 | yes | 3.55 | 0 |
| DeltaKronecker-all | 7739 | yes | 3.26 | 0 |
| Epodonios-all | 7028 | yes | 2.05 | 0 |
| SoliSpirit-all | 6942 | yes | 2.42 | 0 |
| Surfboard-tg-mixed | 6080 | yes | 1.86 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 0.82 | 0 |
| barry-far-vless | 5158 | yes | 1.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 4662 | yes | 1.5 | 0 |
| Surfboard-tg-vless | 4554 | yes | 2.57 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 44 |
| geo | 29 |
| speed | 12 |
| cn-block | 8 |
