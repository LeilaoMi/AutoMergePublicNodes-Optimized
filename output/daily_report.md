# AutoNodes 每日报告

生成时间：2026-07-12 19:16:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77366 |
| 去重后节点数 | 24159 |
| TCP 可达数 | 3000 |
| 真测通过数 | 266 |
| verified 输出数 | 266 |
| global 输出数 | 294 |
| all 输出数 | 24159 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 42.0 |
| geo | 1.3 |
| probe | 45.8 |
| real_test | 78.8 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 1 | 1 | 0 | 100.0% |
| shadowsocks | 114 | 88 | 26 | 77.2% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 164 | 114 | 50 | 69.5% |
| vless | 53 | 19 | 34 | 35.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 27 |
| cn-block:TimeoutError | 21 |
| cn-block:ClientOSError | 15 |
| 204:TimeoutError | 10 |
| geo:TimeoutError | 9 |
| 204:ProxyError | 8 |
| 204:ClientOSError | 7 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 4 |
| geo:ProxyError | 3 |
| geo:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4357 |
| ConnectionRefusedError | 661 |
| gaierror | 289 |
| OSError | 202 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.833 | prefer | 68 | 0.838 | 115 |
| mheidari-all | 0.77 | prefer | 69 | 0.696 | 16307 |
| Surfboard-tg-mixed | 0.737 | prefer | 97 | 0.66 | 5587 |
| DeltaKronecker-all | 0.646 | observe | 104 | 0.567 | 8141 |
| xiaoji235-airport-v2ray-all | 0.315 | observe | 1 | 1.0 | 1508 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4003 |
| Epodonios-all | 0.255 | observe | 0 | None | 6616 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.567 | 59 | 45 | 104 |
| Surfboard-tg-mixed | 0.66 | 64 | 33 | 97 |
| mheidari-all | 0.696 | 48 | 21 | 69 |
| Au1rxx-base64 | 0.838 | 57 | 11 | 68 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16307 | yes | 3.13 | 0 |
| DeltaKronecker-all | 8141 | yes | 3.27 | 0 |
| Epodonios-all | 6616 | yes | 1.83 | 0 |
| SoliSpirit-all | 6361 | yes | 2.43 | 0 |
| Surfboard-tg-mixed | 5587 | yes | 0.49 | 0 |
| mahdibland-V2RayAggregator | 5438 | yes | 1.59 | 0 |
| barry-far-vless | 4906 | yes | 2.06 | 0 |
| Surfboard-tg-vless | 4317 | yes | 2.06 | 0 |
| 10ium-ScrapeCategorize-Vless | 4003 | yes | 2.22 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.84 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 41 |
| speed | 32 |
| 204 | 25 |
| geo | 13 |
