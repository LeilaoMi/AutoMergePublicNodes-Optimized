# AutoNodes 每日报告

生成时间：2026-08-04 19:47:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 86001 |
| 去重后节点数 | 24515 |
| TCP 可达数 | 3000 |
| 真测通过数 | 509 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24515 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 41.0 |
| geo | 0.8 |
| probe | 52.6 |
| real_test | 105.8 |
| tcp | 36.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 53 | 53 | 0 | 100.0% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 110 | 98 | 12 | 89.1% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 163 | 158 | 5 | 96.9% |
| vless | 251 | 177 | 74 | 70.5% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 21 |
| 204:TimeoutError | 16 |
| geo:TimeoutError | 14 |
| cn-block:TimeoutError | 10 |
| geo:ClientOSError | 10 |
| speed:TimeoutError | 8 |
| 204:ClientOSError | 7 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4671 |
| ConnectionRefusedError | 849 |
| gaierror | 298 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.985 | prefer | 53 | 1.0 | 72 |
| Au1rxx-base64 | 0.965 | prefer | 418 | 0.904 | 1560 |
| DeltaKronecker-all | 0.654 | observe | 106 | 0.575 | 5788 |
| Surfboard-tg-mixed | 0.595 | observe | 13 | 0.692 | 5570 |
| mheidari-all | 0.53 | observe | 10 | 0.7 | 19967 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 58 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5251 |
| Epodonios-all | 0.255 | observe | 0 | None | 6154 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6965 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 177 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.575 | 61 | 45 | 106 |
| Surfboard-tg-mixed | 0.692 | 9 | 4 | 13 |
| mheidari-all | 0.7 | 7 | 3 | 10 |
| Au1rxx-base64 | 0.904 | 378 | 40 | 418 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 53 | 0 | 53 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19967 | yes | 4.24 | 0 |
| SoliSpirit-all | 6965 | yes | 4.55 | 0 |
| Epodonios-all | 6154 | yes | 4.38 | 0 |
| DeltaKronecker-all | 5788 | yes | 4.58 | 0 |
| Surfboard-tg-mixed | 5570 | yes | 2.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 5251 | yes | 1.52 | 0 |
| mahdibland-V2RayAggregator | 5141 | yes | 0.15 | 0 |
| barry-far-vless | 4787 | yes | 1.26 | 0 |
| xiaoji235-airport-v2ray-all | 4655 | yes | 1.52 | 0 |
| Surfboard-tg-vless | 4451 | yes | 2.76 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 44 |
| geo | 24 |
| cn-block | 18 |
| speed | 9 |
