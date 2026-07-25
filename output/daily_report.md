# AutoNodes 每日报告

生成时间：2026-07-25 19:21:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80536 |
| 去重后节点数 | 22511 |
| TCP 可达数 | 3000 |
| 真测通过数 | 708 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22511 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| generate | 42.0 |
| geo | 1.3 |
| probe | 68.8 |
| real_test | 169.4 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 76 | 76 | 0 | 100.0% |
| hysteria2 | 8 | 8 | 0 | 100.0% |
| shadowsocks | 125 | 92 | 33 | 73.6% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 494 | 450 | 44 | 91.1% |
| vless | 193 | 81 | 112 | 42.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 59 |
| speed:ClientOSError | 32 |
| cn-block:TimeoutError | 31 |
| 204:ProxyError | 22 |
| 204:TimeoutError | 18 |
| speed:TimeoutError | 8 |
| geo:ClientOSError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4100 |
| ConnectionRefusedError | 708 |
| gaierror | 329 |
| OSError | 220 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 76 | 1.0 | 119 |
| Au1rxx-base64 | 0.908 | prefer | 427 | 0.862 | 1199 |
| mheidari-all | 0.782 | prefer | 253 | 0.704 | 17275 |
| Surfboard-tg-mixed | 0.747 | prefer | 49 | 0.673 | 5515 |
| DeltaKronecker-all | 0.65 | observe | 91 | 0.571 | 5838 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4879 |
| Epodonios-all | 0.255 | observe | 0 | None | 6622 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6305 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 183 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.571 | 52 | 39 | 91 |
| Surfboard-tg-mixed | 0.673 | 33 | 16 | 49 |
| mheidari-all | 0.704 | 178 | 75 | 253 |
| Au1rxx-base64 | 0.862 | 368 | 59 | 427 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 76 | 0 | 76 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17275 | yes | 4.29 | 0 |
| Epodonios-all | 6622 | yes | 2.61 | 0 |
| SoliSpirit-all | 6305 | yes | 2.85 | 0 |
| DeltaKronecker-all | 5838 | yes | 4.5 | 0 |
| Surfboard-tg-mixed | 5515 | yes | 3.02 | 0 |
| mahdibland-V2RayAggregator | 4980 | yes | 2.18 | 0 |
| barry-far-vless | 4959 | yes | 1.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 4879 | yes | 1.94 | 0 |
| Surfboard-tg-vless | 4371 | yes | 3.17 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 2.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 67 |
| 204 | 42 |
| speed | 41 |
| cn-block | 41 |
