# AutoNodes 每日报告

生成时间：2026-08-06 03:16:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 88953 |
| 去重后节点数 | 24594 |
| TCP 可达数 | 3000 |
| 真测通过数 | 511 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24594 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.7 |
| generate | 27.5 |
| geo | 1.4 |
| probe | 53.6 |
| real_test | 116.5 |
| tcp | 37.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 15 | 15 | 0 | 100.0% |
| hysteria2 | 21 | 21 | 0 | 100.0% |
| shadowsocks | 161 | 150 | 11 | 93.2% |
| socks | 18 | 15 | 3 | 83.3% |
| trojan | 183 | 163 | 20 | 89.1% |
| vless | 358 | 145 | 213 | 40.5% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 120 |
| speed:TimeoutError | 34 |
| speed:ClientOSError | 31 |
| geo:ClientOSError | 25 |
| cn-block:TimeoutError | 19 |
| 204:TimeoutError | 11 |
| cn-block:ProxyError | 2 |
| 204:ProxyError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 1 |
| geo:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5165 |
| ConnectionRefusedError | 814 |
| gaierror | 266 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 368 | 0.954 | 1385 |
| zhangkai | 0.789 | prefer | 15 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.655 | observe | 191 | 0.576 | 5908 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 5214 |
| mheidari-all | 0.271 | observe | 134 | 0.187 | 21048 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5260 |
| Epodonios-all | 0.255 | observe | 0 | None | 6515 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7399 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.247 | 40 | 0.15 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.15 | 6 | 34 | 40 |
| mheidari-all | 0.187 | 25 | 109 | 134 |
| nscl5-all | 0.25 | 1 | 3 | 4 |
| Surfboard-tg-mixed | 0.576 | 110 | 81 | 191 |
| Au1rxx-base64 | 0.954 | 351 | 17 | 368 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 15 | 0 | 15 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21048 | yes | 4.13 | 0 |
| SoliSpirit-all | 7399 | yes | 3.74 | 0 |
| Epodonios-all | 6515 | yes | 3.56 | 0 |
| Surfboard-tg-mixed | 5908 | yes | 2.51 | 0 |
| DeltaKronecker-all | 5316 | yes | 4.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 5260 | yes | 2.06 | 0 |
| xiaoji235-airport-v2ray-all | 5214 | yes | 2.34 | 0 |
| mahdibland-V2RayAggregator | 5206 | yes | 2.32 | 0 |
| barry-far-vless | 5104 | yes | 2.69 | 0 |
| Surfboard-tg-vless | 4791 | yes | 3.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 146 |
| speed | 65 |
| cn-block | 22 |
| 204 | 15 |
