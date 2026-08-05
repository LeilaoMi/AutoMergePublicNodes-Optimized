# AutoNodes 每日报告

生成时间：2026-08-05 08:48:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 85532 |
| 去重后节点数 | 23905 |
| TCP 可达数 | 3000 |
| 真测通过数 | 504 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23905 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 32.7 |
| geo | 1.1 |
| probe | 52.0 |
| real_test | 118.7 |
| tcp | 35.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 51 | 50 | 1 | 98.0% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 162 | 134 | 28 | 82.7% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 165 | 156 | 9 | 94.5% |
| vless | 228 | 143 | 85 | 62.7% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 39 |
| 204:ProxyError | 22 |
| 204:TimeoutError | 19 |
| speed:TimeoutError | 11 |
| cn-block:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| speed:ClientOSError | 8 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4791 |
| ConnectionRefusedError | 831 |
| gaierror | 292 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.965 | prefer | 405 | 0.911 | 1403 |
| zhangkai | 0.965 | prefer | 51 | 0.98 | 72 |
| Surfboard-tg-mixed | 0.628 | observe | 124 | 0.548 | 5560 |
| mheidari-all | 0.455 | observe | 30 | 0.367 | 20226 |
| DeltaKronecker-all | 0.361 | observe | 18 | 0.278 | 5316 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5260 |
| Epodonios-all | 0.255 | observe | 0 | None | 6163 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6818 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.278 | 5 | 13 | 18 |
| mheidari-all | 0.367 | 11 | 19 | 30 |
| Surfboard-tg-mixed | 0.548 | 68 | 56 | 124 |
| Au1rxx-base64 | 0.911 | 369 | 36 | 405 |
| zhangkai | 0.98 | 50 | 1 | 51 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20226 | yes | 4.85 | 0 |
| SoliSpirit-all | 6818 | yes | 3.36 | 0 |
| Epodonios-all | 6163 | yes | 3.37 | 0 |
| Surfboard-tg-mixed | 5560 | yes | 5.19 | 0 |
| DeltaKronecker-all | 5316 | yes | 5.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 5260 | yes | 1.89 | 0 |
| mahdibland-V2RayAggregator | 5147 | yes | 2.45 | 0 |
| barry-far-vless | 4823 | yes | 2.27 | 0 |
| xiaoji235-airport-v2ray-all | 4655 | yes | 2.11 | 0 |
| Surfboard-tg-vless | 4397 | yes | 3.0 | 0 |

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
| geo | 49 |
| 204 | 46 |
| speed | 19 |
| cn-block | 14 |
