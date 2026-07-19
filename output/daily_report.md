# AutoNodes 每日报告

生成时间：2026-07-19 19:18:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 86198 |
| 去重后节点数 | 23804 |
| TCP 可达数 | 3000 |
| 真测通过数 | 429 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23804 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 41.3 |
| geo | 0.5 |
| probe | 62.8 |
| real_test | 150.1 |
| tcp | 34.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 35 | 34 | 1 | 97.1% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 139 | 118 | 21 | 84.9% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 197 | 152 | 45 | 77.2% |
| vless | 542 | 113 | 429 | 20.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 293 |
| geo:TimeoutError | 80 |
| cn-block:TimeoutError | 45 |
| 204:TimeoutError | 22 |
| geo:ClientOSError | 20 |
| cn-block:ClientOSError | 9 |
| 204:ProxyError | 8 |
| speed:TimeoutError | 8 |
| 204:ClientOSError | 8 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:43742: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4883 |
| ConnectionRefusedError | 678 |
| gaierror | 406 |
| OSError | 215 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.948 | prefer | 35 | 0.971 | 61 |
| Au1rxx-base64 | 0.87 | prefer | 234 | 0.829 | 1082 |
| Surfboard-tg-mixed | 0.644 | observe | 53 | 0.566 | 5340 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 4642 |
| mheidari-all | 0.387 | observe | 487 | 0.306 | 19340 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 2755 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4478 |
| Epodonios-all | 0.255 | observe | 0 | None | 6712 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.232 | 110 | 0.145 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.145 | 16 | 94 | 110 |
| mheidari-all | 0.306 | 149 | 338 | 487 |
| Surfboard-tg-mixed | 0.566 | 30 | 23 | 53 |
| Au1rxx-base64 | 0.829 | 194 | 40 | 234 |
| zhangkai | 0.971 | 34 | 1 | 35 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19340 | yes | 4.19 | 0 |
| SoliSpirit-all | 7186 | yes | 4.09 | 0 |
| Epodonios-all | 6712 | yes | 1.55 | 0 |
| DeltaKronecker-all | 6235 | yes | 4.56 | 0 |
| Surfboard-tg-mixed | 5340 | yes | 2.67 | 0 |
| mahdibland-V2RayAggregator | 5229 | yes | 1.63 | 0 |
| barry-far-vless | 4995 | yes | 2.2 | 0 |
| xiaoji235-airport-v2ray-all | 4642 | yes | 1.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 4478 | yes | 2.02 | 0 |
| Surfboard-tg-vless | 4216 | yes | 2.81 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 301 |
| geo | 100 |
| cn-block | 57 |
| 204 | 38 |
| sing-box exited 1 | 1 |
