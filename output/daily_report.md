# AutoNodes 每日报告

生成时间：2026-07-03 19:41:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77772 |
| 去重后节点数 | 23173 |
| TCP 可达数 | 3000 |
| 真测通过数 | 267 |
| verified 输出数 | 267 |
| global 输出数 | 274 |
| all 输出数 | 23173 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 37.5 |
| geo | 1.4 |
| probe | 49.4 |
| real_test | 72.9 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 127 | 109 | 18 | 85.8% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 159 | 101 | 58 | 63.5% |
| vless | 48 | 10 | 38 | 20.8% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 36 |
| speed:ClientOSError | 18 |
| geo:TimeoutError | 18 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 8 |
| cn-block:ProxyError | 7 |
| cn-block:ClientOSError | 7 |
| cn-block:TimeoutError | 5 |
| geo:ClientOSError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4418 |
| ConnectionRefusedError | 680 |
| OSError | 153 |
| gaierror | 121 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.791 | prefer | 95 | 0.716 | 6062 |
| Au1rxx-base64 | 0.717 | prefer | 33 | 0.727 | 79 |
| DeltaKronecker-all | 0.715 | prefer | 113 | 0.637 | 6997 |
| mheidari-all | 0.711 | prefer | 101 | 0.634 | 16169 |
| nscl5-all | 0.356 | observe | 2 | 1.0 | 1114 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4368 |
| Epodonios-all | 0.255 | observe | 0 | None | 7138 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6834 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 12 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.634 | 64 | 37 | 101 |
| DeltaKronecker-all | 0.637 | 72 | 41 | 113 |
| Surfboard-tg-mixed | 0.716 | 68 | 27 | 95 |
| Au1rxx-base64 | 0.727 | 24 | 9 | 33 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16169 | yes | 3.59 | 0 |
| Epodonios-all | 7138 | yes | 1.73 | 0 |
| DeltaKronecker-all | 6997 | yes | 3.01 | 0 |
| SoliSpirit-all | 6834 | yes | 2.13 | 0 |
| Surfboard-tg-mixed | 6062 | yes | 2.58 | 0 |
| mahdibland-V2RayAggregator | 5333 | yes | 0.85 | 0 |
| barry-far-vless | 5164 | yes | 1.38 | 0 |
| Surfboard-tg-vless | 4562 | yes | 2.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 4368 | yes | 1.17 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 52 |
| geo | 24 |
| speed | 21 |
| cn-block | 19 |
