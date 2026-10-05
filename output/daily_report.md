# AutoNodes 每日报告

生成时间：2026-10-05 05:15:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 98824 |
| 去重后节点数 | 27507 |
| TCP 可达数 | 3000 |
| 真测通过数 | 548 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27507 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| generate | 77.1 |
| geo | 1.5 |
| probe | 269.8 |
| real_test | 415.2 |
| tcp | 46.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 1 | 5 | 16.7% |
| http | 58 | 25 | 33 | 43.1% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 152 | 143 | 9 | 94.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 92 | 87 | 5 | 94.6% |
| vless | 550 | 272 | 278 | 49.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 128 |
| speed:TimeoutError | 59 |
| geo:ClientOSError | 39 |
| 204:ProxyError | 33 |
| cn-block:TimeoutError | 20 |
| 204:ProxyConnectionError | 19 |
| 204:TimeoutError | 16 |
| speed:ClientOSError | 10 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6362 |
| ConnectionRefusedError | 1028 |
| gaierror | 427 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | prefer | 363 | 0.887 | 1883 |
| Surfboard-tg-mixed | 0.931 | prefer | 72 | 0.861 | 7178 |
| ermaozi | 0.468 | observe | 57 | 0.439 | 694 |
| mheidari-all | 0.45 | observe | 366 | 0.369 | 23195 |
| DeltaKronecker-all | 0.332 | observe | 14 | 0.286 | 5267 |
| Epodonios-all | 0.255 | observe | 0 | None | 7673 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9258 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5736 |
| barry-far-vless | 0.255 | observe | 0 | None | 6057 |

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
| downweight | ermaozi-get_subscribe | 0.096 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 5 | 5 |
| DeltaKronecker-all | 0.286 | 4 | 10 | 14 |
| mheidari-all | 0.369 | 135 | 231 | 366 |
| ermaozi | 0.439 | 25 | 32 | 57 |
| Surfboard-tg-mixed | 0.861 | 62 | 10 | 72 |
| Au1rxx-base64 | 0.887 | 322 | 41 | 363 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23195 | yes | 7.81 | 0 |
| SoliSpirit-all | 9258 | yes | 2.95 | 0 |
| Epodonios-all | 7673 | yes | 4.16 | 0 |
| Surfboard-tg-mixed | 7178 | yes | 6.0 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.33 | 0 |
| barry-far-vless | 6057 | yes | 1.56 | 0 |
| Surfboard-tg-vless | 5736 | yes | 4.44 | 0 |
| DeltaKronecker-all | 5267 | yes | 6.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 5173 | yes | 1.35 | 0 |
| mahdibland-V2RayAggregator | 4365 | yes | 3.57 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 167 |
| 204 | 71 |
| speed | 70 |
| cn-block | 23 |
