# AutoNodes 每日报告

生成时间：2026-07-18 19:18:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 88346 |
| 去重后节点数 | 23115 |
| TCP 可达数 | 3000 |
| 真测通过数 | 839 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23115 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| generate | 37.4 |
| geo | 0.8 |
| probe | 74.2 |
| real_test | 221.9 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 150 | 118 | 32 | 78.7% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 669 | 640 | 29 | 95.7% |
| vless | 387 | 38 | 349 | 9.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 180 |
| speed:ClientOSError | 101 |
| geo:ClientOSError | 53 |
| cn-block:TimeoutError | 34 |
| 204:TimeoutError | 21 |
| cn-block:ClientOSError | 8 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4398 |
| ConnectionRefusedError | 695 |
| gaierror | 258 |
| OSError | 217 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.917 | prefer | 121 | 0.917 | 150 |
| Surfboard-tg-mixed | 0.869 | prefer | 140 | 0.793 | 5696 |
| mheidari-all | 0.743 | prefer | 776 | 0.664 | 19946 |
| DeltaKronecker-all | 0.44 | observe | 173 | 0.358 | 9946 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 4321 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4371 |
| Epodonios-all | 0.255 | observe | 0 | None | 6883 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.358 | 62 | 111 | 173 |
| mheidari-all | 0.664 | 515 | 261 | 776 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.793 | 111 | 29 | 140 |
| Au1rxx-base64 | 0.917 | 111 | 10 | 121 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19946 | yes | 4.32 | 0 |
| DeltaKronecker-all | 9946 | yes | 4.32 | 0 |
| SoliSpirit-all | 7250 | yes | 3.01 | 0 |
| Epodonios-all | 6883 | yes | 2.1 | 0 |
| Surfboard-tg-mixed | 5696 | yes | 2.62 | 0 |
| mahdibland-V2RayAggregator | 5340 | yes | 0.5 | 0 |
| barry-far-vless | 4962 | yes | 2.34 | 0 |
| Surfboard-tg-vless | 4374 | yes | 1.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 4371 | yes | 2.13 | 0 |
| xiaoji235-airport-v2ray-all | 4321 | yes | 1.6 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.098 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 233 |
| speed | 107 |
| cn-block | 45 |
| 204 | 28 |
