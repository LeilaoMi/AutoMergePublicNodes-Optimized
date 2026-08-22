# AutoNodes 每日报告

生成时间：2026-08-22 06:53:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 91263 |
| 去重后节点数 | 23609 |
| TCP 可达数 | 3000 |
| 真测通过数 | 777 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23609 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.6 |
| generate | 34.4 |
| geo | 1.4 |
| probe | 53.8 |
| real_test | 163.5 |
| tcp | 39.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 21 | 18 | 3 | 85.7% |
| shadowsocks | 209 | 193 | 16 | 92.3% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 177 | 171 | 6 | 96.6% |
| vless | 538 | 281 | 257 | 52.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 101 |
| geo:ClientOSError | 86 |
| speed:TimeoutError | 35 |
| speed:ClientOSError | 15 |
| 204:TimeoutError | 15 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 8 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5338 |
| ConnectionRefusedError | 931 |
| gaierror | 647 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | prefer | 112 | 1.0 | 144 |
| Au1rxx-base64 | 0.992 | prefer | 446 | 0.942 | 1299 |
| Surfboard-tg-mixed | 0.855 | prefer | 171 | 0.778 | 6140 |
| mheidari-all | 0.444 | observe | 295 | 0.363 | 21732 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 3321 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 151 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5096 |
| Epodonios-all | 0.255 | observe | 0 | None | 6729 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3992 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7142 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.198 | 32 | 0.094 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.094 | 3 | 29 | 32 |
| mheidari-all | 0.363 | 107 | 188 | 295 |
| Surfboard-tg-mixed | 0.778 | 133 | 38 | 171 |
| Au1rxx-base64 | 0.942 | 420 | 26 | 446 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 112 | 0 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21732 | yes | 4.14 | 0 |
| SoliSpirit-all | 7142 | yes | 2.34 | 0 |
| Epodonios-all | 6729 | yes | 5.18 | 0 |
| Surfboard-tg-mixed | 6140 | yes | 2.83 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.41 | 0 |
| barry-far-vless | 5261 | yes | 0.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 5096 | yes | 0.99 | 0 |
| DeltaKronecker-all | 5015 | yes | 4.34 | 0 |
| Surfboard-tg-vless | 4954 | yes | 2.57 | 0 |
| mahdibland-V2RayAggregator | 4074 | yes | 0.94 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 188 |
| speed | 50 |
| 204 | 25 |
| cn-block | 21 |
