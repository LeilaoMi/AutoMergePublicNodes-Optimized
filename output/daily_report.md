# AutoNodes 每日报告

生成时间：2026-07-29 14:26:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78926 |
| 去重后节点数 | 22704 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22704 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.0 |
| generate | 34.2 |
| geo | 1.4 |
| probe | 55.1 |
| real_test | 119.6 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 70 | 70 | 0 | 100.0% |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 194 | 170 | 24 | 87.6% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 54 | 45 | 9 | 83.3% |
| vless | 297 | 170 | 127 | 57.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 56 |
| cn-block:TimeoutError | 30 |
| speed:TimeoutError | 28 |
| 204:TimeoutError | 24 |
| 204:ProxyError | 8 |
| speed:ClientOSError | 5 |
| geo:ClientOSError | 5 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4311 |
| ConnectionRefusedError | 746 |
| gaierror | 302 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 70 | 1.0 | 84 |
| Au1rxx-base64 | 0.87 | prefer | 291 | 0.818 | 1352 |
| Surfboard-tg-mixed | 0.677 | observe | 147 | 0.599 | 5803 |
| DeltaKronecker-all | 0.67 | observe | 103 | 0.592 | 5519 |
| mheidari-all | 0.594 | observe | 18 | 0.556 | 16071 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 5118 |
| xiaoji235-airport-v2ray-all | 0.329 | observe | 1 | 1.0 | 1861 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6469 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.556 | 10 | 8 | 18 |
| DeltaKronecker-all | 0.592 | 61 | 42 | 103 |
| Surfboard-tg-mixed | 0.599 | 88 | 59 | 147 |
| Au1rxx-base64 | 0.818 | 238 | 53 | 291 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 70 | 0 | 70 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16071 | yes | 3.87 | 0 |
| Epodonios-all | 6469 | yes | 1.53 | 0 |
| SoliSpirit-all | 6373 | yes | 2.11 | 0 |
| Surfboard-tg-mixed | 5803 | yes | 2.35 | 0 |
| DeltaKronecker-all | 5519 | yes | 3.89 | 0 |
| 10ium-ScrapeCategorize-Vless | 5118 | yes | 1.17 | 0 |
| mahdibland-V2RayAggregator | 5089 | yes | 1.69 | 0 |
| barry-far-vless | 4964 | yes | 1.31 | 0 |
| Surfboard-tg-vless | 4538 | yes | 2.84 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.52 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 61 |
| cn-block | 35 |
| 204 | 34 |
| speed | 33 |
