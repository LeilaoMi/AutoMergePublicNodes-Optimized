# AutoNodes 每日报告

生成时间：2026-07-31 14:25:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 79052 |
| 去重后节点数 | 22809 |
| TCP 可达数 | 3000 |
| 真测通过数 | 438 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22809 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| generate | 41.7 |
| geo | 1.4 |
| probe | 50.4 |
| real_test | 110.5 |
| tcp | 33.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 80 | 80 | 0 | 100.0% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 134 | 106 | 28 | 79.1% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 30 | 24 | 6 | 80.0% |
| vless | 279 | 212 | 67 | 76.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 21 |
| geo:ClientOSError | 17 |
| cn-block:TimeoutError | 17 |
| speed:TimeoutError | 13 |
| 204:ProxyError | 12 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 7 |
| speed:ClientOSError | 5 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4709 |
| ConnectionRefusedError | 748 |
| OSError | 221 |
| gaierror | 171 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 80 | 1.0 | 110 |
| Au1rxx-base64 | 0.877 | prefer | 395 | 0.818 | 1533 |
| mheidari-all | 0.735 | prefer | 27 | 0.667 | 16815 |
| DeltaKronecker-all | 0.563 | observe | 27 | 0.481 | 5144 |
| Surfboard-tg-mixed | 0.324 | observe | 8 | 0.375 | 5429 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 48 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5507 |
| Epodonios-all | 0.255 | observe | 0 | None | 5989 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3966 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7049 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.375 | 3 | 5 | 8 |
| DeltaKronecker-all | 0.481 | 13 | 14 | 27 |
| mheidari-all | 0.667 | 18 | 9 | 27 |
| Au1rxx-base64 | 0.818 | 323 | 72 | 395 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 80 | 0 | 80 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16815 | yes | 2.99 | 0 |
| SoliSpirit-all | 7049 | yes | 2.75 | 0 |
| Epodonios-all | 5989 | yes | 1.67 | 0 |
| 10ium-ScrapeCategorize-Vless | 5507 | yes | 1.19 | 0 |
| Surfboard-tg-mixed | 5429 | yes | 2.29 | 0 |
| DeltaKronecker-all | 5144 | yes | 2.47 | 0 |
| mahdibland-V2RayAggregator | 5074 | yes | 1.72 | 0 |
| barry-far-vless | 4528 | yes | 2.11 | 0 |
| Surfboard-tg-vless | 4260 | yes | 1.98 | 0 |
| MatinGhanbari-all-sub | 3966 | yes | 2.37 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 38 |
| 204 | 27 |
| cn-block | 20 |
| speed | 18 |
