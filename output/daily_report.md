# AutoNodes 每日报告

生成时间：2026-08-03 03:37:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 81081 |
| 去重后节点数 | 22634 |
| TCP 可达数 | 3000 |
| 真测通过数 | 876 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22634 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 46.9 |
| geo | 1.5 |
| probe | 64.0 |
| real_test | 200.2 |
| tcp | 34.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 143 | 143 | 0 | 100.0% |
| hysteria2 | 19 | 17 | 2 | 89.5% |
| shadowsocks | 166 | 153 | 13 | 92.2% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 42 | 32 | 10 | 76.2% |
| vless | 788 | 529 | 259 | 67.1% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 87 |
| geo:TimeoutError | 70 |
| speed:TimeoutError | 41 |
| speed:ClientOSError | 31 |
| geo:ClientOSError | 21 |
| 204:TimeoutError | 19 |
| 204:ClientOSError | 7 |
| 204:ProxyError | 6 |
| geo:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4764 |
| ConnectionRefusedError | 760 |
| gaierror | 267 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 143 | 1.0 | 344 |
| Au1rxx-base64 | 0.939 | prefer | 586 | 0.875 | 1632 |
| DeltaKronecker-all | 0.629 | observe | 284 | 0.549 | 3437 |
| Surfboard-tg-mixed | 0.623 | observe | 90 | 0.544 | 5182 |
| mheidari-all | 0.349 | observe | 50 | 0.26 | 18808 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 3833 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 56 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5486 |
| Epodonios-all | 0.255 | observe | 0 | None | 5849 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| nscl5-all | 0.137 | observe | 4 | 0.0 | 0 | 1431 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 4 | 4 |
| mheidari-all | 0.26 | 13 | 37 | 50 |
| Surfboard-tg-mixed | 0.544 | 49 | 41 | 90 |
| DeltaKronecker-all | 0.549 | 156 | 128 | 284 |
| Au1rxx-base64 | 0.875 | 513 | 73 | 586 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18808 | yes | 5.47 | 0 |
| SoliSpirit-all | 6871 | yes | 4.02 | 0 |
| Epodonios-all | 5849 | yes | 4.92 | 0 |
| 10ium-ScrapeCategorize-Vless | 5486 | yes | 2.05 | 0 |
| mahdibland-V2RayAggregator | 5208 | yes | 3.15 | 0 |
| Surfboard-tg-mixed | 5182 | yes | 3.45 | 0 |
| barry-far-vless | 4560 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 4109 | yes | 3.62 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.17 | 0 |
| xiaoji235-airport-v2ray-all | 3833 | yes | 1.6 | 0 |

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
| geo | 93 |
| cn-block | 90 |
| speed | 72 |
| 204 | 32 |
