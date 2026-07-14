# AutoNodes 每日报告

生成时间：2026-07-14 14:00:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80389 |
| 去重后节点数 | 23994 |
| TCP 可达数 | 3000 |
| 真测通过数 | 251 |
| verified 输出数 | 251 |
| global 输出数 | 261 |
| all 输出数 | 23994 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 30.9 |
| geo | 1.3 |
| probe | 44.1 |
| real_test | 69.6 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 102 | 82 | 20 | 80.4% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 154 | 122 | 32 | 79.2% |
| vless | 42 | 2 | 40 | 4.8% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 32 |
| speed:ClientOSError | 16 |
| cn-block:ClientOSError | 10 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 7 |
| speed:TimeoutError | 7 |
| 204:ProxyError | 5 |
| geo:ClientOSError | 3 |
| cn-block:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4485 |
| ConnectionRefusedError | 673 |
| gaierror | 227 |
| OSError | 201 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.796 | prefer | 100 | 0.72 | 17504 |
| Surfboard-tg-mixed | 0.781 | prefer | 115 | 0.704 | 5621 |
| DeltaKronecker-all | 0.732 | prefer | 87 | 0.655 | 7942 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3836 |
| Au1rxx-base64 | 0.362 | observe | 3 | 1.0 | 97 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4019 |
| Epodonios-all | 0.255 | observe | 0 | None | 6477 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6376 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.655 | 57 | 30 | 87 |
| Surfboard-tg-mixed | 0.704 | 81 | 34 | 115 |
| mheidari-all | 0.72 | 72 | 28 | 100 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| Au1rxx-base64 | 1.0 | 3 | 0 | 3 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17504 | yes | 3.34 | 0 |
| DeltaKronecker-all | 7942 | yes | 3.32 | 0 |
| Epodonios-all | 6477 | yes | 1.44 | 0 |
| SoliSpirit-all | 6376 | yes | 2.22 | 0 |
| Surfboard-tg-mixed | 5621 | yes | 2.26 | 0 |
| mahdibland-V2RayAggregator | 5405 | yes | 1.53 | 0 |
| barry-far-vless | 4832 | yes | 1.56 | 0 |
| Surfboard-tg-vless | 4172 | yes | 1.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 4019 | yes | 1.21 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.048 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 36 |
| speed | 24 |
| 204 | 19 |
| cn-block | 15 |
