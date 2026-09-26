# AutoNodes 每日报告

生成时间：2026-09-26 04:43:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 96568 |
| 去重后节点数 | 26493 |
| TCP 可达数 | 3000 |
| 真测通过数 | 531 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26493 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| generate | 88.2 |
| geo | 1.5 |
| probe | 334.5 |
| real_test | 540.3 |
| tcp | 43.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 3 | 0 | 100.0% |
| http | 43 | 13 | 30 | 30.2% |
| hysteria2 | 18 | 16 | 2 | 88.9% |
| shadowsocks | 172 | 157 | 15 | 91.3% |
| socks | 10 | 5 | 5 | 50.0% |
| trojan | 49 | 30 | 19 | 61.2% |
| vless | 768 | 306 | 462 | 39.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 204 |
| speed:TimeoutError | 116 |
| geo:ClientOSError | 59 |
| 204:ProxyError | 45 |
| cn-block:ClientOSError | 35 |
| 204:TimeoutError | 28 |
| speed:ClientOSError | 25 |
| cn-block:TimeoutError | 15 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5562 |
| ConnectionRefusedError | 965 |
| gaierror | 483 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.924 | prefer | 284 | 0.863 | 1594 |
| Surfboard-tg-mixed | 0.845 | prefer | 79 | 0.772 | 7217 |
| mheidari-all | 0.403 | observe | 649 | 0.322 | 22526 |
| ermaozi | 0.357 | observe | 33 | 0.333 | 352 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.272 | observe | 13 | 0.308 | 375 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5293 |
| Epodonios-all | 0.255 | observe | 0 | None | 7682 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8923 |

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
| DeltaKronecker-all | 0.0 | 0 | 4 | 4 |
| ermaozi-get_subscribe | 0.308 | 4 | 9 | 13 |
| mheidari-all | 0.322 | 209 | 440 | 649 |
| ermaozi | 0.333 | 11 | 22 | 33 |
| Surfboard-tg-mixed | 0.772 | 61 | 18 | 79 |
| Au1rxx-base64 | 0.863 | 245 | 39 | 284 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22526 | yes | 6.27 | 0 |
| SoliSpirit-all | 8923 | yes | 2.18 | 0 |
| Epodonios-all | 7682 | yes | 5.58 | 0 |
| Surfboard-tg-mixed | 7217 | yes | 4.28 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.4 | 0 |
| barry-far-vless | 6063 | yes | 1.09 | 0 |
| Surfboard-tg-vless | 5837 | yes | 3.45 | 0 |
| DeltaKronecker-all | 5452 | yes | 6.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5293 | yes | 1.37 | 0 |
| mahdibland-V2RayAggregator | 4304 | yes | 3.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 263 |
| speed | 141 |
| 204 | 77 |
| cn-block | 52 |
