# AutoNodes 每日报告

生成时间：2026-07-10 19:43:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76205 |
| 去重后节点数 | 23865 |
| TCP 可达数 | 3000 |
| 真测通过数 | 280 |
| verified 输出数 | 280 |
| global 输出数 | 294 |
| all 输出数 | 23865 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| generate | 29.3 |
| geo | 1.3 |
| probe | 46.0 |
| real_test | 70.4 |
| tcp | 32.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 118 | 105 | 13 | 89.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 151 | 80 | 71 | 53.0% |
| vless | 123 | 50 | 73 | 40.7% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 52 |
| 204:ProxyError | 29 |
| 204:TimeoutError | 16 |
| geo:TimeoutError | 13 |
| cn-block:ProxyError | 11 |
| 204:ClientOSError | 10 |
| cn-block:ClientOSError | 7 |
| cn-block:TimeoutError | 6 |
| geo:ProxyError | 6 |
| speed:ProxyError | 4 |
| geo:ClientOSError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4512 |
| ConnectionRefusedError | 678 |
| gaierror | 221 |
| OSError | 193 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.895 | prefer | 71 | 0.901 | 123 |
| Surfboard-tg-mixed | 0.806 | prefer | 82 | 0.732 | 5583 |
| DeltaKronecker-all | 0.585 | observe | 107 | 0.505 | 7600 |
| mheidari-all | 0.552 | observe | 140 | 0.471 | 16338 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4165 |
| Epodonios-all | 0.255 | observe | 0 | None | 6378 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6475 |
| barry-far-vless | 0.255 | observe | 0 | None | 4674 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.471 | 66 | 74 | 140 |
| DeltaKronecker-all | 0.505 | 54 | 53 | 107 |
| Surfboard-tg-mixed | 0.732 | 60 | 22 | 82 |
| Au1rxx-base64 | 0.901 | 64 | 7 | 71 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16338 | yes | 2.93 | 0 |
| DeltaKronecker-all | 7600 | yes | 2.82 | 0 |
| SoliSpirit-all | 6475 | yes | 2.59 | 0 |
| Epodonios-all | 6378 | yes | 2.51 | 0 |
| Surfboard-tg-mixed | 5583 | yes | 1.68 | 0 |
| mahdibland-V2RayAggregator | 5415 | yes | 1.4 | 0 |
| barry-far-vless | 4674 | yes | 0.81 | 0 |
| Surfboard-tg-vless | 4208 | yes | 1.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 4165 | yes | 1.05 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 0.89 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 56 |
| 204 | 55 |
| cn-block | 24 |
| geo | 23 |
