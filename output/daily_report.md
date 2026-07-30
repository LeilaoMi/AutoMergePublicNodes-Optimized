# AutoNodes 每日报告

生成时间：2026-07-30 19:46:29

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78433 |
| 去重后节点数 | 23046 |
| TCP 可达数 | 3000 |
| 真测通过数 | 511 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23046 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 33.8 |
| geo | 1.3 |
| probe | 70.1 |
| real_test | 148.8 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 11 | 9 | 2 | 81.8% |
| shadowsocks | 132 | 103 | 29 | 78.0% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 30 | 24 | 6 | 80.0% |
| vless | 501 | 260 | 241 | 51.9% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 75 |
| cn-block:TimeoutError | 55 |
| geo:TimeoutError | 42 |
| 204:TimeoutError | 24 |
| speed:TimeoutError | 19 |
| geo:ClientOSError | 19 |
| cn-block:ProxyError | 19 |
| geo:ProxyError | 9 |
| speed:ClientOSError | 7 |
| 204:ClientOSError | 5 |
| speed:ProxyError | 5 |
| cn-block:ClientOSError | 2 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4706 |
| ConnectionRefusedError | 733 |
| OSError | 226 |
| gaierror | 200 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | prefer | 113 | 1.0 | 129 |
| Au1rxx-base64 | 0.866 | prefer | 265 | 0.811 | 1430 |
| Surfboard-tg-mixed | 0.535 | observe | 20 | 0.45 | 5387 |
| DeltaKronecker-all | 0.519 | observe | 381 | 0.438 | 5759 |
| ninja-vless | 0.457 | observe | 7 | 0.714 | 1791 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 6090 |
| mheidari-all | 0.259 | observe | 3 | 0.333 | 16222 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5342 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6594 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.333 | 1 | 2 | 3 |
| DeltaKronecker-all | 0.438 | 167 | 214 | 381 |
| Surfboard-tg-mixed | 0.45 | 9 | 11 | 20 |
| ninja-vless | 0.714 | 5 | 2 | 7 |
| Au1rxx-base64 | 0.811 | 215 | 50 | 265 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16222 | yes | 3.71 | 0 |
| SoliSpirit-all | 6594 | yes | 3.13 | 0 |
| Epodonios-all | 6090 | yes | 3.85 | 0 |
| DeltaKronecker-all | 5759 | yes | 4.27 | 0 |
| Surfboard-tg-mixed | 5387 | yes | 2.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 5342 | yes | 1.54 | 0 |
| mahdibland-V2RayAggregator | 5047 | yes | 1.96 | 0 |
| barry-far-vless | 4589 | yes | 1.34 | 0 |
| Surfboard-tg-vless | 4264 | yes | 2.68 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 2.32 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 104 |
| cn-block | 76 |
| geo | 71 |
| speed | 31 |
