# AutoNodes 每日报告

生成时间：2026-08-08 02:04:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 82250 |
| 去重后节点数 | 23593 |
| TCP 可达数 | 3000 |
| 真测通过数 | 740 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23593 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 43.0 |
| geo | 1.2 |
| probe | 64.7 |
| real_test | 197.3 |
| tcp | 35.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 24 | 24 | 0 | 100.0% |
| shadowsocks | 159 | 151 | 8 | 95.0% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 160 | 146 | 14 | 91.2% |
| vless | 911 | 394 | 517 | 43.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 255 |
| cn-block:TimeoutError | 95 |
| geo:ClientOSError | 76 |
| speed:ClientOSError | 48 |
| speed:TimeoutError | 42 |
| 204:ProxyError | 8 |
| 204:TimeoutError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:30483: bind: address already in use | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4847 |
| ConnectionRefusedError | 818 |
| gaierror | 305 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 439 | 0.952 | 1365 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.747 | prefer | 25 | 0.68 | 6471 |
| mheidari-all | 0.544 | observe | 26 | 0.462 | 17687 |
| DeltaKronecker-all | 0.436 | observe | 765 | 0.356 | 5326 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7081 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7469 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5179 |

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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.356 | 272 | 493 | 765 |
| mheidari-all | 0.462 | 12 | 14 | 26 |
| Surfboard-tg-mixed | 0.68 | 17 | 8 | 25 |
| Au1rxx-base64 | 0.952 | 418 | 21 | 439 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17687 | yes | 3.6 | 0 |
| SoliSpirit-all | 7469 | yes | 2.05 | 0 |
| Epodonios-all | 7081 | yes | 3.79 | 0 |
| Surfboard-tg-mixed | 6471 | yes | 3.03 | 0 |
| barry-far-vless | 5509 | yes | 0.49 | 0 |
| DeltaKronecker-all | 5326 | yes | 4.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 5282 | yes | 0.84 | 0 |
| Surfboard-tg-vless | 5179 | yes | 2.63 | 0 |
| mahdibland-V2RayAggregator | 5175 | yes | 2.16 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 332 |
| cn-block | 99 |
| speed | 90 |
| 204 | 19 |
| sing-box exited 1 | 1 |
