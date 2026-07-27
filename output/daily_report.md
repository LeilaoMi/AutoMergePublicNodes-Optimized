# AutoNodes 每日报告

生成时间：2026-07-27 03:44:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 83507 |
| 去重后节点数 | 22089 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1052 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22089 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 21.5 |
| geo | 1.2 |
| probe | 71.8 |
| real_test | 225.3 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 6 | 0 | 100.0% |
| http | 76 | 76 | 0 | 100.0% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 148 | 138 | 10 | 93.2% |
| socks | 28 | 23 | 5 | 82.1% |
| trojan | 543 | 521 | 22 | 95.9% |
| vless | 716 | 275 | 441 | 38.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 188 |
| speed:ClientOSError | 155 |
| speed:TimeoutError | 54 |
| geo:ClientOSError | 34 |
| cn-block:TimeoutError | 23 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 5 |
| 204:TimeoutError | 4 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4428 |
| ConnectionRefusedError | 714 |
| OSError | 219 |
| gaierror | 187 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.991 | prefer | 555 | 0.933 | 1476 |
| zhangkai | 0.991 | prefer | 76 | 1.0 | 86 |
| DeltaKronecker-all | 0.815 | prefer | 153 | 0.739 | 4320 |
| Surfboard-tg-mixed | 0.747 | prefer | 64 | 0.672 | 5483 |
| mheidari-all | 0.519 | observe | 666 | 0.438 | 19312 |
| tg-oneclickvpnkeys | 0.483 | observe | 6 | 1.0 | 149 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 3959 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 6493 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.145 | downweight | 5 | 0.0 | 0 | 1791 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ninja-vless | 0.145 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 5 | 5 |
| mheidari-all | 0.438 | 292 | 374 | 666 |
| Surfboard-tg-mixed | 0.672 | 43 | 21 | 64 |
| DeltaKronecker-all | 0.739 | 113 | 40 | 153 |
| Au1rxx-base64 | 0.933 | 518 | 37 | 555 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |
| tg-oneclickvpnkeys | 1.0 | 6 | 0 | 6 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19312 | yes | 4.41 | 0 |
| Epodonios-all | 6493 | yes | 2.43 | 0 |
| SoliSpirit-all | 6284 | yes | 1.86 | 0 |
| Surfboard-tg-mixed | 5483 | yes | 4.58 | 0 |
| mahdibland-V2RayAggregator | 5003 | yes | 2.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 1.03 | 0 |
| barry-far-vless | 4841 | yes | 0.66 | 0 |
| DeltaKronecker-all | 4320 | yes | 4.58 | 0 |
| Surfboard-tg-vless | 4173 | yes | 2.87 | 0 |
| MatinGhanbari-all-sub | 3963 | yes | 1.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 223 |
| speed | 211 |
| cn-block | 30 |
| 204 | 15 |
