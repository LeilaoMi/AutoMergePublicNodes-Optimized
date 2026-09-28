# AutoNodes 每日报告

生成时间：2026-09-28 23:13:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 97528 |
| 去重后节点数 | 27021 |
| TCP 可达数 | 3000 |
| 真测通过数 | 410 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27021 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.2 |
| generate | 32.9 |
| geo | 1.5 |
| probe | 170.7 |
| real_test | 132.9 |
| tcp | 44.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 35 | 17 | 18 | 48.6% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 144 | 140 | 4 | 97.2% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 9 | 8 | 1 | 88.9% |
| vless | 279 | 220 | 59 | 78.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 30 |
| 204:ProxyError | 25 |
| cn-block:TimeoutError | 8 |
| speed:TimeoutError | 5 |
| geo:TimeoutError | 5 |
| 204:TimeoutError | 4 |
| 204:ProxyConnectionError | 2 |
| cn-block:ClientOSError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6010 |
| ConnectionRefusedError | 1012 |
| gaierror | 467 |
| OSError | 238 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.931 | prefer | 343 | 0.866 | 1674 |
| mheidari-all | 0.903 | prefer | 94 | 0.83 | 22856 |
| Surfboard-tg-mixed | 0.749 | prefer | 13 | 0.923 | 7142 |
| ermaozi | 0.562 | observe | 29 | 0.552 | 344 |
| DeltaKronecker-all | 0.446 | observe | 8 | 0.625 | 5428 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 121 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5326 |
| Epodonios-all | 0.255 | observe | 0 | None | 7535 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9706 |

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
| downweight | ermaozi-get_subscribe | 0.151 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.167 | 1 | 5 | 6 |
| ermaozi | 0.552 | 16 | 13 | 29 |
| DeltaKronecker-all | 0.625 | 5 | 3 | 8 |
| mheidari-all | 0.83 | 78 | 16 | 94 |
| Au1rxx-base64 | 0.866 | 297 | 46 | 343 |
| Surfboard-tg-mixed | 0.923 | 12 | 1 | 13 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22856 | yes | 6.14 | 0 |
| SoliSpirit-all | 9706 | yes | 2.41 | 0 |
| Epodonios-all | 7535 | yes | 3.78 | 0 |
| Surfboard-tg-mixed | 7142 | yes | 3.58 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.0 | 0 |
| barry-far-vless | 6027 | yes | 1.33 | 0 |
| Surfboard-tg-vless | 5799 | yes | 4.03 | 0 |
| DeltaKronecker-all | 5428 | yes | 6.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 5326 | yes | 6.91 | 0 |
| mahdibland-V2RayAggregator | 4237 | yes | 3.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 35 |
| 204 | 33 |
| cn-block | 11 |
| geo | 6 |
