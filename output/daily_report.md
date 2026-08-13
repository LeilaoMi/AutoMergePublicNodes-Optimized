# AutoNodes 每日报告

生成时间：2026-08-13 13:28:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79794 |
| 去重后节点数 | 22452 |
| TCP 可达数 | 3000 |
| 真测通过数 | 786 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22452 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 14.7 |
| generate | 37.0 |
| geo | 0.9 |
| probe | 64.7 |
| real_test | 166.1 |
| tcp | 32.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 17 | 14 | 3 | 82.4% |
| shadowsocks | 164 | 152 | 12 | 92.7% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 335 | 328 | 7 | 97.9% |
| vless | 223 | 161 | 62 | 72.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 15 |
| geo:ClientOSError | 14 |
| geo:TimeoutError | 14 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 9 |
| speed:ClientOSError | 8 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4019 |
| ConnectionRefusedError | 768 |
| gaierror | 367 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 534 | 0.961 | 1591 |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.828 | prefer | 113 | 0.752 | 5967 |
| mheidari-all | 0.774 | prefer | 70 | 0.7 | 17032 |
| DeltaKronecker-all | 0.503 | observe | 24 | 0.417 | 4878 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5203 |
| Epodonios-all | 0.255 | observe | 0 | None | 6610 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7410 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.417 | 10 | 14 | 24 |
| mheidari-all | 0.7 | 49 | 21 | 70 |
| Surfboard-tg-mixed | 0.752 | 85 | 28 | 113 |
| Au1rxx-base64 | 0.961 | 513 | 21 | 534 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17032 | yes | 4.27 | 0 |
| SoliSpirit-all | 7410 | yes | 2.99 | 0 |
| Epodonios-all | 6610 | yes | 3.64 | 0 |
| Surfboard-tg-mixed | 5967 | yes | 2.86 | 0 |
| 10ium-ScrapeCategorize-Vless | 5203 | yes | 2.16 | 0 |
| mahdibland-V2RayAggregator | 5197 | yes | 1.9 | 0 |
| barry-far-vless | 5031 | yes | 2.31 | 0 |
| DeltaKronecker-all | 4878 | yes | 3.8 | 0 |
| Surfboard-tg-vless | 4695 | yes | 3.39 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.53 | 0 |

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
| geo | 29 |
| 204 | 23 |
| cn-block | 20 |
| speed | 14 |
