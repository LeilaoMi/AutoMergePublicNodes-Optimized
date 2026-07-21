# AutoNodes 每日报告

生成时间：2026-07-21 14:11:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 82302 |
| 去重后节点数 | 22942 |
| TCP 可达数 | 3000 |
| 真测通过数 | 496 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22942 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 47.6 |
| geo | 1.3 |
| probe | 68.6 |
| real_test | 158.5 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 125 | 103 | 22 | 82.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 341 | 267 | 74 | 78.3% |
| vless | 386 | 85 | 301 | 22.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 156 |
| speed:ClientOSError | 107 |
| cn-block:TimeoutError | 71 |
| 204:TimeoutError | 16 |
| geo:ClientOSError | 15 |
| speed:TimeoutError | 11 |
| cn-block:ClientOSError | 9 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4233 |
| ConnectionRefusedError | 672 |
| gaierror | 304 |
| OSError | 217 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.766 | prefer | 116 | 0.69 | 5491 |
| Au1rxx-base64 | 0.68 | observe | 183 | 0.667 | 388 |
| mheidari-all | 0.562 | observe | 513 | 0.481 | 19167 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4304 |
| DeltaKronecker-all | 0.297 | observe | 44 | 0.205 | 5415 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4482 |
| Epodonios-all | 0.255 | observe | 0 | None | 6557 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6824 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.205 | 9 | 35 | 44 |
| mheidari-all | 0.481 | 247 | 266 | 513 |
| Au1rxx-base64 | 0.667 | 122 | 61 | 183 |
| Surfboard-tg-mixed | 0.69 | 80 | 36 | 116 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19167 | yes | 3.81 | 0 |
| SoliSpirit-all | 6824 | yes | 2.41 | 0 |
| Epodonios-all | 6557 | yes | 1.77 | 0 |
| Surfboard-tg-mixed | 5491 | yes | 2.14 | 0 |
| DeltaKronecker-all | 5415 | yes | 3.94 | 0 |
| mahdibland-V2RayAggregator | 5247 | yes | 2.34 | 0 |
| barry-far-vless | 4794 | yes | 1.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 4482 | yes | 1.63 | 0 |
| xiaoji235-airport-v2ray-all | 4304 | yes | 1.44 | 0 |
| Surfboard-tg-vless | 4162 | yes | 1.96 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 171 |
| speed | 118 |
| cn-block | 84 |
| 204 | 26 |
