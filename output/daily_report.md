# AutoNodes 每日报告

生成时间：2026-07-26 13:46:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 81669 |
| 去重后节点数 | 22638 |
| TCP 可达数 | 3000 |
| 真测通过数 | 761 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22638 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 38.2 |
| geo | 1.3 |
| probe | 65.7 |
| real_test | 172.9 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 7 | 7 | 0 | 100.0% |
| http | 75 | 75 | 0 | 100.0% |
| hysteria2 | 9 | 7 | 2 | 77.8% |
| shadowsocks | 141 | 114 | 27 | 80.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 485 | 460 | 25 | 94.8% |
| vless | 246 | 97 | 149 | 39.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 73 |
| speed:ClientOSError | 43 |
| cn-block:TimeoutError | 23 |
| speed:TimeoutError | 15 |
| geo:ClientOSError | 14 |
| 204:TimeoutError | 14 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4283 |
| ConnectionRefusedError | 701 |
| gaierror | 293 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.99 | prefer | 75 | 1.0 | 86 |
| Au1rxx-base64 | 0.98 | prefer | 460 | 0.924 | 1458 |
| DeltaKronecker-all | 0.81 | prefer | 146 | 0.733 | 5950 |
| Surfboard-tg-mixed | 0.709 | prefer | 68 | 0.632 | 5591 |
| mheidari-all | 0.582 | observe | 205 | 0.502 | 17236 |
| tg-oneclickvpnkeys | 0.519 | observe | 7 | 1.0 | 149 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 6731 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.502 | 103 | 102 | 205 |
| Surfboard-tg-mixed | 0.632 | 43 | 25 | 68 |
| DeltaKronecker-all | 0.733 | 107 | 39 | 146 |
| Au1rxx-base64 | 0.924 | 425 | 35 | 460 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 7 | 0 | 7 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17236 | yes | 3.54 | 0 |
| Epodonios-all | 6731 | yes | 0.65 | 0 |
| SoliSpirit-all | 6620 | yes | 2.85 | 0 |
| DeltaKronecker-all | 5950 | yes | 3.14 | 0 |
| Surfboard-tg-mixed | 5591 | yes | 2.45 | 0 |
| barry-far-vless | 5039 | yes | 1.72 | 0 |
| mahdibland-V2RayAggregator | 4980 | yes | 1.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 2.36 | 0 |
| Surfboard-tg-vless | 4351 | yes | 2.71 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 1.81 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 88 |
| speed | 58 |
| cn-block | 32 |
| 204 | 27 |
