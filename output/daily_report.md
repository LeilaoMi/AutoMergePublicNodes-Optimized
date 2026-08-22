# AutoNodes 每日报告

生成时间：2026-08-22 01:39:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 92902 |
| 去重后节点数 | 23044 |
| TCP 可达数 | 3000 |
| 真测通过数 | 865 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23044 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 25.4 |
| geo | 1.4 |
| probe | 64.2 |
| real_test | 191.7 |
| tcp | 39.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 174 | 168 | 6 | 96.6% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 192 | 180 | 12 | 93.8% |
| vless | 729 | 378 | 351 | 51.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 130 |
| geo:ClientOSError | 91 |
| speed:TimeoutError | 90 |
| speed:ClientOSError | 27 |
| cn-block:TimeoutError | 8 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |
| geo:parse | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5122 |
| ConnectionRefusedError | 942 |
| gaierror | 767 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 326 | 0.939 | 1933 |
| zhangkai | 0.997 | prefer | 113 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.918 | prefer | 115 | 0.843 | 6361 |
| mheidari-all | 0.598 | observe | 666 | 0.518 | 21889 |
| nscl5-all | 0.287 | observe | 2 | 0.5 | 3321 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 162 |
| Pawdroid | 0.256 | observe | 1 | 1.0 | 20 |
| Epodonios-all | 0.255 | observe | 0 | None | 7089 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3985 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7133 |

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
| downweight | DeltaKronecker-all | 0.197 | 9 | 0.111 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.111 | 1 | 8 | 9 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.518 | 345 | 321 | 666 |
| Surfboard-tg-mixed | 0.843 | 97 | 18 | 115 |
| Au1rxx-base64 | 0.939 | 306 | 20 | 326 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21889 | yes | 4.59 | 0 |
| SoliSpirit-all | 7133 | yes | 3.76 | 0 |
| Epodonios-all | 7089 | yes | 4.9 | 0 |
| Surfboard-tg-mixed | 6361 | yes | 3.11 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.59 | 0 |
| barry-far-vless | 5449 | yes | 2.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 5148 | yes | 1.77 | 0 |
| Surfboard-tg-vless | 5127 | yes | 2.72 | 0 |
| DeltaKronecker-all | 4245 | yes | 4.63 | 0 |
| mahdibland-V2RayAggregator | 4091 | yes | 0.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 223 |
| speed | 118 |
| 204 | 16 |
| cn-block | 15 |
