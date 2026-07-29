# AutoNodes 每日报告

生成时间：2026-07-29 08:54:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 77964 |
| 去重后节点数 | 22464 |
| TCP 可达数 | 3000 |
| 真测通过数 | 606 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22464 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| generate | 33.0 |
| geo | 1.3 |
| probe | 72.6 |
| real_test | 202.7 |
| tcp | 31.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 95 | 95 | 0 | 100.0% |
| hysteria2 | 12 | 9 | 3 | 75.0% |
| shadowsocks | 173 | 151 | 22 | 87.3% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 46 | 39 | 7 | 84.8% |
| vless | 844 | 309 | 535 | 36.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 215 |
| speed:ClientOSError | 91 |
| 204:ProxyError | 65 |
| speed:TimeoutError | 64 |
| geo:ClientOSError | 46 |
| cn-block:TimeoutError | 29 |
| cn-block:ProxyError | 20 |
| 204:TimeoutError | 19 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 6 |
| geo:ProxyError | 6 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4473 |
| ConnectionRefusedError | 707 |
| gaierror | 243 |
| OSError | 224 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | prefer | 95 | 1.0 | 167 |
| Au1rxx-base64 | 0.887 | prefer | 257 | 0.84 | 1232 |
| Surfboard-tg-mixed | 0.446 | observe | 8 | 0.625 | 5706 |
| DeltaKronecker-all | 0.436 | observe | 801 | 0.356 | 5519 |
| mheidari-all | 0.305 | observe | 10 | 0.3 | 15942 |
| xiaoji235-airport-v2ray-all | 0.282 | observe | 2 | 0.5 | 1861 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6451 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6039 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.3 | 3 | 7 | 10 |
| DeltaKronecker-all | 0.356 | 285 | 516 | 801 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.625 | 5 | 3 | 8 |
| Au1rxx-base64 | 0.84 | 216 | 41 | 257 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 95 | 0 | 95 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15942 | yes | 2.84 | 0 |
| Epodonios-all | 6451 | yes | 1.76 | 0 |
| SoliSpirit-all | 6039 | yes | 2.32 | 0 |
| Surfboard-tg-mixed | 5706 | yes | 1.64 | 0 |
| DeltaKronecker-all | 5519 | yes | 2.86 | 0 |
| 10ium-ScrapeCategorize-Vless | 5118 | yes | 2.11 | 0 |
| mahdibland-V2RayAggregator | 5089 | yes | 1.32 | 0 |
| barry-far-vless | 4902 | yes | 1.31 | 0 |
| Surfboard-tg-vless | 4505 | yes | 2.41 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 1.62 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 267 |
| speed | 158 |
| 204 | 90 |
| cn-block | 55 |
