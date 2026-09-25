# AutoNodes 每日报告

生成时间：2026-09-25 11:42:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 96970 |
| 去重后节点数 | 26327 |
| TCP 可达数 | 3000 |
| 真测通过数 | 290 |
| verified 输出数 | 290 |
| global 输出数 | 300 |
| all 输出数 | 26327 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 81.0 |
| geo | 1.5 |
| probe | 263.1 |
| real_test | 121.0 |
| tcp | 42.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 0 | 2 | 0.0% |
| http | 46 | 26 | 20 | 56.5% |
| hysteria2 | 22 | 11 | 11 | 50.0% |
| shadowsocks | 136 | 125 | 11 | 91.9% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 13 | 5 | 8 | 38.5% |
| vless | 156 | 122 | 34 | 78.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyConnectionError | 25 |
| 204:ProxyError | 15 |
| 204:TimeoutError | 15 |
| cn-block:TimeoutError | 11 |
| geo:TimeoutError | 6 |
| speed:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 4 |
| speed:ClientOSError | 2 |
| geo:ProxyError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5668 |
| ConnectionRefusedError | 971 |
| gaierror | 435 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.925 | prefer | 191 | 0.864 | 1624 |
| mheidari-all | 0.886 | prefer | 60 | 0.817 | 22444 |
| Surfboard-tg-mixed | 0.737 | prefer | 68 | 0.662 | 7280 |
| ermaozi | 0.576 | observe | 46 | 0.565 | 338 |
| DeltaKronecker-all | 0.372 | observe | 9 | 0.444 | 5452 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5293 |
| Epodonios-all | 0.255 | observe | 0 | None | 7869 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9069 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.444 | 4 | 5 | 9 |
| ermaozi | 0.565 | 26 | 20 | 46 |
| Surfboard-tg-mixed | 0.662 | 45 | 23 | 68 |
| mheidari-all | 0.817 | 49 | 11 | 60 |
| Au1rxx-base64 | 0.864 | 165 | 26 | 191 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22444 | yes | 5.72 | 0 |
| SoliSpirit-all | 9069 | yes | 3.72 | 0 |
| Epodonios-all | 7869 | yes | 3.09 | 0 |
| Surfboard-tg-mixed | 7280 | yes | 3.89 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.19 | 0 |
| barry-far-vless | 6140 | yes | 1.29 | 0 |
| Surfboard-tg-vless | 5801 | yes | 3.62 | 0 |
| DeltaKronecker-all | 5452 | yes | 4.85 | 0 |
| 10ium-ScrapeCategorize-Vless | 5293 | yes | 1.53 | 0 |
| mahdibland-V2RayAggregator | 4324 | yes | 3.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 59 |
| cn-block | 15 |
| geo | 8 |
| speed | 7 |
