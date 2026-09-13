# AutoNodes 每日报告

生成时间：2026-09-13 05:14:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 94336 |
| 去重后节点数 | 25332 |
| TCP 可达数 | 3000 |
| 真测通过数 | 537 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25332 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 93.7 |
| geo | 1.4 |
| probe | 385.2 |
| real_test | 584.8 |
| tcp | 42.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 29 | 18 | 11 | 62.1% |
| hysteria2 | 21 | 19 | 2 | 90.5% |
| shadowsocks | 126 | 121 | 5 | 96.0% |
| socks | 6 | 2 | 4 | 33.3% |
| trojan | 17 | 7 | 10 | 41.2% |
| vless | 929 | 366 | 563 | 39.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 211 |
| geo:ClientOSError | 109 |
| speed:ClientOSError | 107 |
| speed:TimeoutError | 70 |
| cn-block:ClientOSError | 51 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 8 |
| 204:ProxyConnectionError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5757 |
| ConnectionRefusedError | 956 |
| gaierror | 450 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.911 | prefer | 372 | 0.847 | 1653 |
| ermaozi | 0.71 | prefer | 24 | 0.708 | 436 |
| Surfboard-tg-mixed | 0.633 | observe | 19 | 0.579 | 7432 |
| mheidari-all | 0.353 | observe | 511 | 0.272 | 20709 |
| DeltaKronecker-all | 0.349 | observe | 195 | 0.267 | 5970 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5301 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 127 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4793 |
| Epodonios-all | 0.255 | observe | 0 | None | 7895 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.155 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.167 | 1 | 5 | 6 |
| DeltaKronecker-all | 0.267 | 52 | 143 | 195 |
| mheidari-all | 0.272 | 139 | 372 | 511 |
| Surfboard-tg-mixed | 0.579 | 11 | 8 | 19 |
| ermaozi | 0.708 | 17 | 7 | 24 |
| Au1rxx-base64 | 0.847 | 315 | 57 | 372 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20709 | yes | 5.81 | 0 |
| SoliSpirit-all | 8737 | yes | 2.44 | 0 |
| Epodonios-all | 7895 | yes | 3.63 | 0 |
| Surfboard-tg-mixed | 7432 | yes | 4.05 | 0 |
| barry-far-vless | 6259 | yes | 1.63 | 0 |
| Surfboard-tg-vless | 6027 | yes | 3.82 | 0 |
| DeltaKronecker-all | 5970 | yes | 5.85 | 0 |
| xiaoji235-airport-v2ray-all | 5301 | yes | 2.15 | 0 |
| 10ium-ScrapeCategorize-Vless | 4793 | yes | 0.64 | 0 |
| mahdibland-V2RayAggregator | 4295 | yes | 2.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 323 |
| speed | 179 |
| cn-block | 67 |
| 204 | 26 |
