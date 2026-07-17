# AutoNodes 每日报告

生成时间：2026-07-17 19:23:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 80102 |
| 去重后节点数 | 25151 |
| TCP 可达数 | 3000 |
| 真测通过数 | 531 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25151 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| generate | 29.8 |
| geo | 1.3 |
| probe | 61.4 |
| real_test | 138.9 |
| tcp | 34.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 123 | 97 | 26 | 78.9% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 386 | 342 | 44 | 88.6% |
| vless | 243 | 47 | 196 | 19.3% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 134 |
| speed:ClientOSError | 52 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 10 |
| 204:TimeoutError | 9 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 8 |
| geo:ClientOSError | 7 |
| cn-block:ProxyError | 5 |
| speed:ProxyError | 4 |
| geo:ProxyError | 2 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4810 |
| ConnectionRefusedError | 683 |
| OSError | 216 |
| gaierror | 193 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.876 | prefer | 136 | 0.875 | 150 |
| Surfboard-tg-mixed | 0.835 | prefer | 145 | 0.759 | 5558 |
| mheidari-all | 0.833 | prefer | 318 | 0.755 | 16753 |
| xiaoji235-airport-v2ray-all | 0.322 | observe | 1 | 1.0 | 1680 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4428 |
| Epodonios-all | 0.255 | observe | 0 | None | 6514 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6898 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.233 | 161 | 0.149 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.149 | 24 | 137 | 161 |
| mheidari-all | 0.755 | 240 | 78 | 318 |
| Surfboard-tg-mixed | 0.759 | 110 | 35 | 145 |
| Au1rxx-base64 | 0.875 | 119 | 17 | 136 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16753 | yes | 1.51 | 0 |
| DeltaKronecker-all | 8967 | yes | 2.55 | 0 |
| SoliSpirit-all | 6898 | yes | 1.81 | 0 |
| Epodonios-all | 6514 | yes | 1.78 | 0 |
| Surfboard-tg-mixed | 5558 | yes | 1.6 | 0 |
| mahdibland-V2RayAggregator | 5263 | yes | 0.95 | 0 |
| barry-far-vless | 4875 | yes | 0.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4428 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 4258 | yes | 1.17 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.54 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 143 |
| speed | 66 |
| cn-block | 30 |
| 204 | 29 |
