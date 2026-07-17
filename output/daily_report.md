# AutoNodes 每日报告

生成时间：2026-07-17 08:23:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 98/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79278 |
| 去重后节点数 | 24796 |
| TCP 可达数 | 3000 |
| 真测通过数 | 562 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24796 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 41.4 |
| geo | 1.1 |
| probe | 54.5 |
| real_test | 127.5 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 137 | 109 | 28 | 79.6% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 434 | 400 | 34 | 92.2% |
| vless | 133 | 9 | 124 | 6.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 83 |
| speed:ClientOSError | 40 |
| 204:ProxyError | 17 |
| speed:TimeoutError | 9 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 8 |
| cn-block:TimeoutError | 7 |
| 204:TimeoutError | 5 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 3 |
| speed:ProxyError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4320 |
| ConnectionRefusedError | 661 |
| gaierror | 292 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.978 | prefer | 105 | 0.981 | 149 |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.964 | prefer | 145 | 0.89 | 16487 |
| Surfboard-tg-mixed | 0.826 | prefer | 124 | 0.75 | 5351 |
| DeltaKronecker-all | 0.674 | observe | 333 | 0.595 | 8967 |
| nscl5-all | 0.328 | observe | 1 | 1.0 | 1821 |
| xiaoji235-airport-v2ray-all | 0.322 | observe | 1 | 1.0 | 1680 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6542 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.595 | 198 | 135 | 333 |
| Surfboard-tg-mixed | 0.75 | 93 | 31 | 124 |
| mheidari-all | 0.89 | 129 | 16 | 145 |
| Au1rxx-base64 | 0.981 | 103 | 2 | 105 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16487 | yes | 3.54 | 0 |
| DeltaKronecker-all | 8967 | yes | 3.79 | 0 |
| SoliSpirit-all | 6827 | yes | 2.28 | 0 |
| Epodonios-all | 6542 | yes | 1.0 | 0 |
| Surfboard-tg-mixed | 5351 | yes | 1.78 | 0 |
| mahdibland-V2RayAggregator | 5208 | yes | 1.09 | 0 |
| barry-far-vless | 4764 | yes | 1.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 4428 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 4142 | yes | 2.36 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.62 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.068 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 88 |
| speed | 51 |
| 204 | 30 |
| cn-block | 18 |
