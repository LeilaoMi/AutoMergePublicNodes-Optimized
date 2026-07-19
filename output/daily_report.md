# AutoNodes 每日报告

生成时间：2026-07-19 03:30:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 88550 |
| 去重后节点数 | 23429 |
| TCP 可达数 | 3000 |
| 真测通过数 | 804 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23429 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 27.3 |
| geo | 1.0 |
| probe | 59.1 |
| real_test | 172.8 |
| tcp | 33.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 139 | 131 | 8 | 94.2% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 546 | 514 | 32 | 94.1% |
| vless | 603 | 114 | 489 | 18.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 280 |
| geo:TimeoutError | 89 |
| geo:ClientOSError | 78 |
| speed:TimeoutError | 30 |
| cn-block:TimeoutError | 23 |
| 204:ProxyError | 13 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:44792: bind: address already in use | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4626 |
| ConnectionRefusedError | 683 |
| gaierror | 355 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.711 | prefer | 76 | 0.711 | 149 |
| mheidari-all | 0.694 | observe | 653 | 0.614 | 20126 |
| Surfboard-tg-mixed | 0.682 | observe | 350 | 0.603 | 5442 |
| DeltaKronecker-all | 0.544 | observe | 209 | 0.464 | 9946 |
| xiaoji235-airport-v2ray-all | 0.372 | observe | 9 | 0.444 | 4642 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4371 |
| Epodonios-all | 0.255 | observe | 0 | None | 6663 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.444 | 4 | 5 | 9 |
| DeltaKronecker-all | 0.464 | 97 | 112 | 209 |
| Surfboard-tg-mixed | 0.603 | 211 | 139 | 350 |
| mheidari-all | 0.614 | 401 | 252 | 653 |
| Au1rxx-base64 | 0.711 | 54 | 22 | 76 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20126 | yes | 3.62 | 0 |
| DeltaKronecker-all | 9946 | yes | 4.14 | 0 |
| SoliSpirit-all | 7072 | yes | 2.34 | 0 |
| Epodonios-all | 6663 | yes | 0.45 | 0 |
| Surfboard-tg-mixed | 5442 | yes | 2.25 | 0 |
| mahdibland-V2RayAggregator | 5340 | yes | 1.82 | 0 |
| barry-far-vless | 4859 | yes | 1.43 | 0 |
| xiaoji235-airport-v2ray-all | 4642 | yes | 1.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 4371 | yes | 0.97 | 0 |
| Surfboard-tg-vless | 4204 | yes | 1.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 311 |
| geo | 167 |
| cn-block | 31 |
| 204 | 22 |
| sing-box exited 1 | 1 |
