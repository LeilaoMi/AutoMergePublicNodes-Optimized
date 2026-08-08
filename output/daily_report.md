# AutoNodes 每日报告

生成时间：2026-08-08 07:05:49

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 82085 |
| 去重后节点数 | 23445 |
| TCP 可达数 | 3000 |
| 真测通过数 | 465 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23445 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 36.7 |
| geo | 1.5 |
| probe | 54.6 |
| real_test | 108.5 |
| tcp | 36.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 26 | 24 | 2 | 92.3% |
| shadowsocks | 159 | 146 | 13 | 91.8% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 149 | 130 | 19 | 87.2% |
| vless | 245 | 140 | 105 | 57.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 49 |
| geo:ClientOSError | 28 |
| 204:TimeoutError | 26 |
| cn-block:TimeoutError | 12 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| 204:ProxyError | 3 |
| cn-block:ClientOSError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5014 |
| ConnectionRefusedError | 778 |
| gaierror | 255 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.994 | prefer | 358 | 0.941 | 1368 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.609 | observe | 117 | 0.53 | 6419 |
| DeltaKronecker-all | 0.543 | observe | 80 | 0.463 | 5347 |
| mheidari-all | 0.356 | observe | 27 | 0.259 | 17696 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5450 |
| Epodonios-all | 0.255 | observe | 0 | None | 6914 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.259 | 7 | 20 | 27 |
| DeltaKronecker-all | 0.463 | 37 | 43 | 80 |
| Surfboard-tg-mixed | 0.53 | 62 | 55 | 117 |
| Au1rxx-base64 | 0.941 | 337 | 21 | 358 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17696 | yes | 4.06 | 0 |
| SoliSpirit-all | 7402 | yes | 2.37 | 0 |
| Epodonios-all | 6914 | yes | 4.27 | 0 |
| Surfboard-tg-mixed | 6419 | yes | 3.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 5450 | yes | 1.05 | 0 |
| barry-far-vless | 5409 | yes | 0.76 | 0 |
| DeltaKronecker-all | 5347 | yes | 4.45 | 0 |
| Surfboard-tg-vless | 5218 | yes | 2.75 | 0 |
| mahdibland-V2RayAggregator | 5162 | yes | 2.56 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.34 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 77 |
| 204 | 33 |
| speed | 15 |
| cn-block | 15 |
