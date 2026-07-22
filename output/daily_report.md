# AutoNodes 每日报告

生成时间：2026-07-22 19:39:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 81866 |
| 去重后节点数 | 22606 |
| TCP 可达数 | 3000 |
| 真测通过数 | 565 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22606 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 25.6 |
| geo | 1.2 |
| probe | 59.2 |
| real_test | 139.3 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 35 | 1 | 97.2% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 123 | 97 | 26 | 78.9% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 401 | 354 | 47 | 88.3% |
| vless | 270 | 71 | 199 | 26.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 83 |
| speed:ClientOSError | 68 |
| cn-block:TimeoutError | 44 |
| geo:ClientOSError | 31 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 9 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 8 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 5 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4582 |
| ConnectionRefusedError | 693 |
| OSError | 219 |
| gaierror | 122 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | prefer | 36 | 0.972 | 61 |
| Au1rxx-base64 | 0.805 | prefer | 186 | 0.79 | 432 |
| mheidari-all | 0.709 | prefer | 523 | 0.629 | 19265 |
| DeltaKronecker-all | 0.705 | prefer | 78 | 0.628 | 5212 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4246 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4613 |
| Epodonios-all | 0.255 | observe | 0 | None | 6453 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6754 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | Surfboard-tg-mixed | 0.239 | 12 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.167 | 2 | 10 | 12 |
| DeltaKronecker-all | 0.628 | 49 | 29 | 78 |
| mheidari-all | 0.629 | 329 | 194 | 523 |
| Au1rxx-base64 | 0.79 | 147 | 39 | 186 |
| zhangkai | 0.972 | 35 | 1 | 36 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19265 | yes | 2.19 | 0 |
| SoliSpirit-all | 6754 | yes | 2.32 | 0 |
| Epodonios-all | 6453 | yes | 2.3 | 0 |
| Surfboard-tg-mixed | 5342 | yes | 1.22 | 0 |
| DeltaKronecker-all | 5212 | yes | 2.49 | 0 |
| mahdibland-V2RayAggregator | 4954 | yes | 1.41 | 0 |
| barry-far-vless | 4789 | yes | 0.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 4613 | yes | 1.05 | 0 |
| xiaoji235-airport-v2ray-all | 4246 | yes | 0.7 | 0 |
| Surfboard-tg-vless | 4192 | yes | 1.57 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 114 |
| speed | 75 |
| cn-block | 57 |
| 204 | 28 |
