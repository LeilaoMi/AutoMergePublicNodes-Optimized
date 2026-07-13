# AutoNodes 每日报告

生成时间：2026-07-13 03:35:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77721 |
| 去重后节点数 | 24189 |
| TCP 可达数 | 3000 |
| 真测通过数 | 461 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24189 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 21.2 |
| geo | 1.3 |
| probe | 42.4 |
| real_test | 82.2 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 1 | 1 | 50.0% |
| shadowsocks | 137 | 125 | 12 | 91.2% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 262 | 249 | 13 | 95.0% |
| vless | 131 | 43 | 88 | 32.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 43 |
| speed:ClientOSError | 27 |
| geo:ClientOSError | 15 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 7 |
| cn-block:TimeoutError | 6 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4210 |
| ConnectionRefusedError | 675 |
| gaierror | 333 |
| OSError | 205 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.996 | prefer | 129 | 0.922 | 5535 |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.878 | prefer | 92 | 0.804 | 16437 |
| DeltaKronecker-all | 0.802 | prefer | 246 | 0.724 | 8141 |
| Au1rxx-base64 | 0.745 | prefer | 71 | 0.746 | 127 |
| xiaoji235-airport-v2ray-all | 0.321 | observe | 1 | 1.0 | 1647 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4003 |
| Epodonios-all | 0.255 | observe | 0 | None | 6591 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6553 |

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
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.724 | 178 | 68 | 246 |
| Au1rxx-base64 | 0.746 | 53 | 18 | 71 |
| mheidari-all | 0.804 | 74 | 18 | 92 |
| Surfboard-tg-mixed | 0.922 | 119 | 10 | 129 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16437 | yes | 3.34 | 0 |
| DeltaKronecker-all | 8141 | yes | 3.46 | 0 |
| Epodonios-all | 6591 | yes | 0.66 | 0 |
| SoliSpirit-all | 6553 | yes | 2.55 | 0 |
| Surfboard-tg-mixed | 5535 | yes | 2.63 | 0 |
| mahdibland-V2RayAggregator | 5438 | yes | 1.13 | 0 |
| barry-far-vless | 4867 | yes | 1.11 | 0 |
| Surfboard-tg-vless | 4183 | yes | 2.78 | 0 |
| 10ium-ScrapeCategorize-Vless | 4003 | yes | 1.3 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 58 |
| speed | 35 |
| cn-block | 14 |
| 204 | 9 |
