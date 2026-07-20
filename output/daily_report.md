# AutoNodes 每日报告

生成时间：2026-07-20 09:30:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 85581 |
| 去重后节点数 | 24016 |
| TCP 可达数 | 3000 |
| 真测通过数 | 482 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24016 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 23.3 |
| geo | 1.1 |
| probe | 55.6 |
| real_test | 150.7 |
| tcp | 33.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 135 | 117 | 18 | 86.7% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 317 | 269 | 48 | 84.9% |
| vless | 475 | 55 | 420 | 11.6% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 240 |
| speed:ClientOSError | 133 |
| cn-block:TimeoutError | 56 |
| speed:TimeoutError | 15 |
| geo:ClientOSError | 14 |
| 204:TimeoutError | 10 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 5 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4610 |
| ConnectionRefusedError | 678 |
| gaierror | 426 |
| OSError | 215 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.911 | prefer | 242 | 0.872 | 1064 |
| DeltaKronecker-all | 0.623 | observe | 221 | 0.543 | 5962 |
| Surfboard-tg-mixed | 0.606 | observe | 36 | 0.528 | 5183 |
| mheidari-all | 0.299 | observe | 432 | 0.218 | 20095 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4714 |
| Epodonios-all | 0.255 | observe | 0 | None | 6441 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6860 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.218 | 94 | 338 | 432 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.528 | 19 | 17 | 36 |
| DeltaKronecker-all | 0.543 | 120 | 101 | 221 |
| Au1rxx-base64 | 0.872 | 211 | 31 | 242 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20095 | yes | 3.98 | 0 |
| SoliSpirit-all | 6860 | yes | 2.55 | 0 |
| Epodonios-all | 6441 | yes | 4.18 | 0 |
| DeltaKronecker-all | 5962 | yes | 4.59 | 0 |
| mahdibland-V2RayAggregator | 5193 | yes | 2.07 | 0 |
| Surfboard-tg-mixed | 5183 | yes | 2.87 | 0 |
| xiaoji235-airport-v2ray-all | 5035 | yes | 0.64 | 0 |
| barry-far-vless | 4852 | yes | 1.47 | 0 |
| 10ium-ScrapeCategorize-Vless | 4714 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4032 | yes | 2.7 | 0 |

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
| geo | 254 |
| speed | 149 |
| cn-block | 65 |
| 204 | 21 |
