# AutoNodes 每日报告

生成时间：2026-07-08 03:25:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 83948 |
| 去重后节点数 | 24959 |
| TCP 可达数 | 3000 |
| 真测通过数 | 398 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24959 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 46.9 |
| geo | 1.3 |
| probe | 41.8 |
| real_test | 71.4 |
| tcp | 32.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 4 | 1 | 80.0% |
| shadowsocks | 136 | 127 | 9 | 93.4% |
| socks | 9 | 6 | 3 | 66.7% |
| trojan | 198 | 186 | 12 | 93.9% |
| vless | 142 | 33 | 109 | 23.2% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 59 |
| speed:ClientOSError | 31 |
| speed:TimeoutError | 18 |
| geo:ClientOSError | 10 |
| 204:ClientOSError | 6 |
| 204:TimeoutError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:TimeoutError | 2 |
| 204:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4600 |
| ConnectionRefusedError | 823 |
| OSError | 170 |
| gaierror | 149 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.984 | prefer | 102 | 0.912 | 5768 |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.788 | prefer | 166 | 0.711 | 8472 |
| Au1rxx-base64 | 0.745 | prefer | 75 | 0.747 | 125 |
| mheidari-all | 0.71 | prefer | 144 | 0.632 | 18232 |
| xiaoji235-airport-v2ray-all | 0.32 | observe | 4 | 0.5 | 3640 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 170 |
| Epodonios-all | 0.255 | observe | 0 | None | 6908 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6977 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 11 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 2 | 2 | 4 |
| mheidari-all | 0.632 | 91 | 53 | 144 |
| DeltaKronecker-all | 0.711 | 118 | 48 | 166 |
| Au1rxx-base64 | 0.747 | 56 | 19 | 75 |
| Surfboard-tg-mixed | 0.912 | 93 | 9 | 102 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18232 | yes | 2.06 | 0 |
| DeltaKronecker-all | 8472 | yes | 3.96 | 0 |
| SoliSpirit-all | 6977 | yes | 2.84 | 0 |
| Epodonios-all | 6908 | yes | 1.1 | 0 |
| Surfboard-tg-mixed | 5768 | yes | 2.9 | 0 |
| mahdibland-V2RayAggregator | 5339 | yes | 1.26 | 0 |
| barry-far-vless | 5099 | yes | 0.85 | 0 |
| 10ium-ScrapeCategorize-Vless | 4700 | yes | 2.44 | 0 |
| Surfboard-tg-vless | 4340 | yes | 1.43 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 1.4 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 69 |
| speed | 49 |
| 204 | 10 |
| cn-block | 6 |
