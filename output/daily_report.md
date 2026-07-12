# AutoNodes 每日报告

生成时间：2026-07-12 03:33:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76600 |
| 去重后节点数 | 24228 |
| TCP 可达数 | 3000 |
| 真测通过数 | 508 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24228 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 43.7 |
| geo | 1.3 |
| probe | 53.1 |
| real_test | 118.6 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 1 | 1 | 0 | 100.0% |
| shadowsocks | 133 | 119 | 14 | 89.5% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 140 | 134 | 6 | 95.7% |
| vless | 549 | 211 | 338 | 38.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 155 |
| geo:TimeoutError | 82 |
| speed:TimeoutError | 37 |
| geo:ClientOSError | 29 |
| cn-block:ClientOSError | 14 |
| 204:ProxyError | 12 |
| 204:ClientOSError | 11 |
| cn-block:TimeoutError | 9 |
| 204:TimeoutError | 5 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4344 |
| ConnectionRefusedError | 658 |
| gaierror | 285 |
| OSError | 202 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.786 | prefer | 80 | 0.787 | 140 |
| Surfboard-tg-mixed | 0.724 | prefer | 332 | 0.645 | 5277 |
| mheidari-all | 0.577 | observe | 292 | 0.497 | 16401 |
| DeltaKronecker-all | 0.457 | observe | 120 | 0.375 | 7969 |
| nscl5-all | 0.378 | observe | 4 | 0.75 | 1439 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 3953 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6385 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3977 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.375 | 45 | 75 | 120 |
| mheidari-all | 0.497 | 145 | 147 | 292 |
| Surfboard-tg-mixed | 0.645 | 214 | 118 | 332 |
| nscl5-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.787 | 63 | 17 | 80 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16401 | yes | 3.6 | 0 |
| DeltaKronecker-all | 7969 | yes | 3.69 | 0 |
| SoliSpirit-all | 6662 | yes | 2.57 | 0 |
| Epodonios-all | 6385 | yes | 1.78 | 0 |
| mahdibland-V2RayAggregator | 5416 | yes | 0.67 | 0 |
| Surfboard-tg-mixed | 5277 | yes | 2.15 | 0 |
| barry-far-vless | 4725 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 4046 | yes | 2.29 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 1.31 | 0 |
| 10ium-ScrapeCategorize-Vless | 3953 | yes | 1.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 192 |
| geo | 114 |
| 204 | 28 |
| cn-block | 25 |
