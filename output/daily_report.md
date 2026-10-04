# AutoNodes 每日报告

生成时间：2026-10-04 05:32:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 99314 |
| 去重后节点数 | 27386 |
| TCP 可达数 | 3000 |
| 真测通过数 | 429 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27386 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| generate | 37.0 |
| geo | 1.2 |
| probe | 327.6 |
| real_test | 452.0 |
| tcp | 47.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 24 | 18 | 6 | 75.0% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 136 | 124 | 12 | 91.2% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 80 | 58 | 22 | 72.5% |
| vless | 522 | 217 | 305 | 41.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 152 |
| speed:TimeoutError | 81 |
| geo:ClientOSError | 33 |
| 204:TimeoutError | 18 |
| cn-block:TimeoutError | 15 |
| 204:ProxyConnectionError | 14 |
| 204:ProxyError | 14 |
| speed:ClientOSError | 13 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6724 |
| ConnectionRefusedError | 1177 |
| gaierror | 431 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.977 | prefer | 284 | 0.908 | 1782 |
| ermaozi | 0.73 | prefer | 25 | 0.72 | 646 |
| Surfboard-tg-mixed | 0.715 | prefer | 72 | 0.639 | 7318 |
| mheidari-all | 0.355 | observe | 384 | 0.273 | 23371 |
| DeltaKronecker-all | 0.263 | observe | 8 | 0.25 | 5207 |
| Epodonios-all | 0.255 | observe | 0 | None | 7797 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3995 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9571 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5909 |
| barry-far-vless | 0.255 | observe | 0 | None | 6122 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.25 | 2 | 6 | 8 |
| mheidari-all | 0.273 | 105 | 279 | 384 |
| Surfboard-tg-mixed | 0.639 | 46 | 26 | 72 |
| ermaozi | 0.72 | 18 | 7 | 25 |
| Au1rxx-base64 | 0.908 | 258 | 26 | 284 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23371 | yes | 6.89 | 0 |
| SoliSpirit-all | 9571 | yes | 1.45 | 0 |
| Epodonios-all | 7797 | yes | 3.67 | 0 |
| Surfboard-tg-mixed | 7318 | yes | 4.39 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.88 | 0 |
| barry-far-vless | 6122 | yes | 0.74 | 0 |
| Surfboard-tg-vless | 5909 | yes | 5.26 | 0 |
| DeltaKronecker-all | 5207 | yes | 5.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 5192 | yes | 1.71 | 0 |
| mahdibland-V2RayAggregator | 4285 | yes | 3.39 | 0 |

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
| geo | 185 |
| speed | 94 |
| 204 | 47 |
| cn-block | 22 |
