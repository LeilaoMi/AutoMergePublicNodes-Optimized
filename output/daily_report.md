# AutoNodes 每日报告

生成时间：2026-10-06 13:15:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 97839 |
| 去重后节点数 | 26950 |
| TCP 可达数 | 3000 |
| 真测通过数 | 423 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26950 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| generate | 94.1 |
| geo | 1.5 |
| probe | 201.7 |
| real_test | 162.0 |
| tcp | 45.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 77 | 28 | 49 | 36.4% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 133 | 121 | 12 | 91.0% |
| socks | 5 | 1 | 4 | 20.0% |
| trojan | 76 | 71 | 5 | 93.4% |
| vless | 229 | 186 | 43 | 81.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 42 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 13 |
| geo:ClientOSError | 9 |
| speed:ClientOSError | 8 |
| 204:ProxyConnectionError | 6 |
| cn-block:ClientOSError | 5 |
| geo:TimeoutError | 5 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5899 |
| ConnectionRefusedError | 1021 |
| gaierror | 462 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 298 | 0.95 | 1805 |
| Surfboard-tg-mixed | 0.798 | prefer | 140 | 0.721 | 7050 |
| mheidari-all | 0.57 | observe | 11 | 0.727 | 23204 |
| ermaozi | 0.399 | observe | 79 | 0.367 | 708 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4990 |
| Epodonios-all | 0.255 | observe | 0 | None | 7553 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9571 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5573 |
| barry-far-vless | 0.255 | observe | 0 | None | 5839 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.226 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.2 | 1 | 4 | 5 |
| ermaozi | 0.367 | 29 | 50 | 79 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.721 | 101 | 39 | 140 |
| mheidari-all | 0.727 | 8 | 3 | 11 |
| Au1rxx-base64 | 0.95 | 283 | 15 | 298 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23204 | yes | 6.75 | 0 |
| SoliSpirit-all | 9571 | yes | 2.49 | 0 |
| Epodonios-all | 7553 | yes | 3.83 | 0 |
| Surfboard-tg-mixed | 7050 | yes | 4.1 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.16 | 0 |
| barry-far-vless | 5839 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 5573 | yes | 4.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 1.43 | 0 |
| DeltaKronecker-all | 4889 | yes | 5.76 | 0 |
| mahdibland-V2RayAggregator | 4373 | yes | 3.45 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 66 |
| cn-block | 20 |
| geo | 15 |
| speed | 13 |
