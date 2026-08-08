# AutoNodes 每日报告

生成时间：2026-08-08 18:49:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83469 |
| 去重后节点数 | 23607 |
| TCP 可达数 | 3000 |
| 真测通过数 | 401 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23607 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 44.3 |
| geo | 1.4 |
| probe | 45.7 |
| real_test | 85.8 |
| tcp | 35.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 25 | 23 | 2 | 92.0% |
| shadowsocks | 146 | 131 | 15 | 89.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 139 | 131 | 8 | 94.2% |
| vless | 132 | 94 | 38 | 71.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 22 |
| cn-block:TimeoutError | 14 |
| speed:TimeoutError | 8 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 4 |
| geo:ClientOSError | 3 |
| geo:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4951 |
| ConnectionRefusedError | 817 |
| gaierror | 309 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.989 | prefer | 341 | 0.93 | 1540 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| mheidari-all | 0.84 | prefer | 17 | 0.882 | 17642 |
| Surfboard-tg-mixed | 0.68 | observe | 78 | 0.603 | 6620 |
| DeltaKronecker-all | 0.255 | observe | 9 | 0.222 | 5347 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5450 |
| Epodonios-all | 0.255 | observe | 0 | None | 7201 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7604 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5385 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.222 | 2 | 7 | 9 |
| Surfboard-tg-mixed | 0.603 | 47 | 31 | 78 |
| mheidari-all | 0.882 | 15 | 2 | 17 |
| Au1rxx-base64 | 0.93 | 317 | 24 | 341 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17642 | yes | 3.68 | 0 |
| SoliSpirit-all | 7604 | yes | 3.01 | 0 |
| Epodonios-all | 7201 | yes | 4.02 | 0 |
| Surfboard-tg-mixed | 6620 | yes | 3.21 | 0 |
| barry-far-vless | 5666 | yes | 1.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 5450 | yes | 1.63 | 0 |
| Surfboard-tg-vless | 5385 | yes | 2.55 | 0 |
| DeltaKronecker-all | 5347 | yes | 3.54 | 0 |
| mahdibland-V2RayAggregator | 5127 | yes | 2.12 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.69 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 31 |
| cn-block | 19 |
| speed | 9 |
| geo | 6 |
