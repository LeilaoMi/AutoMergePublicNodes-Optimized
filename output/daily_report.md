# AutoNodes 每日报告

生成时间：2026-07-19 13:42:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 86572 |
| 去重后节点数 | 23745 |
| TCP 可达数 | 3000 |
| 真测通过数 | 444 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23745 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 44.6 |
| geo | 0.8 |
| probe | 66.4 |
| real_test | 178.5 |
| tcp | 34.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 148 | 120 | 28 | 81.1% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 261 | 203 | 58 | 77.8% |
| vless | 726 | 74 | 652 | 10.2% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 408 |
| speed:ClientOSError | 154 |
| geo:ClientOSError | 75 |
| cn-block:TimeoutError | 34 |
| 204:TimeoutError | 21 |
| 204:ProxyError | 17 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 5 |
| geo:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4678 |
| ConnectionRefusedError | 674 |
| gaierror | 518 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.868 | prefer | 213 | 0.826 | 1124 |
| mheidari-all | 0.756 | prefer | 109 | 0.679 | 20221 |
| Surfboard-tg-mixed | 0.463 | observe | 204 | 0.382 | 5306 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 4642 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4478 |
| Epodonios-all | 0.255 | observe | 0 | None | 6635 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6812 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.204 | 617 | 0.123 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.123 | 76 | 541 | 617 |
| Surfboard-tg-mixed | 0.382 | 78 | 126 | 204 |
| mheidari-all | 0.679 | 74 | 35 | 109 |
| Au1rxx-base64 | 0.826 | 176 | 37 | 213 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20221 | yes | 4.54 | 0 |
| SoliSpirit-all | 6812 | yes | 2.22 | 0 |
| Epodonios-all | 6635 | yes | 2.21 | 0 |
| DeltaKronecker-all | 6235 | yes | 4.06 | 0 |
| mahdibland-V2RayAggregator | 5355 | yes | 2.02 | 0 |
| Surfboard-tg-mixed | 5306 | yes | 2.6 | 0 |
| barry-far-vless | 4858 | yes | 1.74 | 0 |
| xiaoji235-airport-v2ray-all | 4642 | yes | 1.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 4478 | yes | 1.42 | 0 |
| Surfboard-tg-vless | 4184 | yes | 2.75 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 486 |
| speed | 163 |
| 204 | 46 |
| cn-block | 45 |
