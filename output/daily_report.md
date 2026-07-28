# AutoNodes 每日报告

生成时间：2026-07-28 08:49:30

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 86095 |
| 去重后节点数 | 23310 |
| TCP 可达数 | 3000 |
| 真测通过数 | 679 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23310 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 44.0 |
| geo | 1.3 |
| probe | 62.7 |
| real_test | 188.4 |
| tcp | 32.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 151 | 127 | 24 | 84.1% |
| socks | 8 | 5 | 3 | 62.5% |
| trojan | 374 | 325 | 49 | 86.9% |
| vless | 319 | 141 | 178 | 44.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 91 |
| cn-block:TimeoutError | 30 |
| speed:ClientOSError | 27 |
| 204:TimeoutError | 21 |
| speed:TimeoutError | 21 |
| 204:ProxyError | 20 |
| geo:ClientOSError | 19 |
| cn-block:ProxyError | 8 |
| cn-block:ClientOSError | 6 |
| geo:ProxyError | 6 |
| 204:ClientOSError | 4 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4305 |
| ConnectionRefusedError | 747 |
| gaierror | 324 |
| OSError | 223 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 69 | 1.0 | 81 |
| Au1rxx-base64 | 0.961 | prefer | 408 | 0.909 | 1345 |
| DeltaKronecker-all | 0.637 | observe | 104 | 0.558 | 5965 |
| Surfboard-tg-mixed | 0.636 | observe | 43 | 0.558 | 5743 |
| mheidari-all | 0.593 | observe | 300 | 0.513 | 18776 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.259 | observe | 3 | 0.333 | 3959 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4972 |
| Epodonios-all | 0.255 | observe | 0 | None | 6749 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 2 | 2 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.333 | 1 | 2 | 3 |
| mheidari-all | 0.513 | 154 | 146 | 300 |
| Surfboard-tg-mixed | 0.558 | 24 | 19 | 43 |
| DeltaKronecker-all | 0.558 | 58 | 46 | 104 |
| Au1rxx-base64 | 0.909 | 371 | 37 | 408 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 69 | 0 | 69 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18776 | yes | 3.82 | 0 |
| Epodonios-all | 6749 | yes | 3.3 | 0 |
| SoliSpirit-all | 6579 | yes | 2.87 | 0 |
| DeltaKronecker-all | 5965 | yes | 5.11 | 0 |
| Surfboard-tg-mixed | 5743 | yes | 3.99 | 0 |
| barry-far-vless | 5112 | yes | 1.4 | 0 |
| mahdibland-V2RayAggregator | 4991 | yes | 1.55 | 0 |
| 10ium-ScrapeCategorize-Vless | 4972 | yes | 1.63 | 0 |
| Surfboard-tg-vless | 4586 | yes | 1.97 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 2.61 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 116 |
| speed | 50 |
| 204 | 45 |
| cn-block | 44 |
