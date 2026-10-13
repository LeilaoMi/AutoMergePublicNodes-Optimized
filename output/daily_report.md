# AutoNodes 每日报告

生成时间：2026-10-13 14:09:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 99026 |
| 去重后节点数 | 27337 |
| TCP 可达数 | 3000 |
| 真测通过数 | 430 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27337 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| generate | 89.6 |
| geo | 1.5 |
| probe | 338.3 |
| real_test | 330.8 |
| tcp | 47.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 5 | 0 | 100.0% |
| http | 28 | 11 | 17 | 39.3% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 150 | 130 | 20 | 86.7% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 119 | 97 | 22 | 81.5% |
| vless | 228 | 173 | 55 | 75.9% |
| vmess | 1 | 0 | 1 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 30 |
| 204:TimeoutError | 26 |
| 204:ProxyError | 16 |
| geo:ClientOSError | 11 |
| geo:TimeoutError | 11 |
| cn-block:ClientOSError | 7 |
| speed:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| speed:TimeoutError | 3 |
| 204:ProxyConnectionError | 2 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6759 |
| ConnectionRefusedError | 1023 |
| gaierror | 343 |
| OSError | 239 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.944 | prefer | 323 | 0.876 | 1754 |
| mheidari-all | 0.847 | prefer | 41 | 0.78 | 24075 |
| Surfboard-tg-mixed | 0.76 | prefer | 120 | 0.683 | 7201 |
| DeltaKronecker-all | 0.642 | observe | 30 | 0.567 | 5076 |
| zhangkai | 0.587 | observe | 12 | 0.833 | 144 |
| ermaozi-get_subscribe | 0.34 | observe | 20 | 0.3 | 534 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5086 |
| Epodonios-all | 0.255 | observe | 0 | None | 7717 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9931 |

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
| tg-oneclickvpnkeys | 0.0 | 0 | 2 | 2 |
| ermaozi-get_subscribe | 0.3 | 6 | 14 | 20 |
| DeltaKronecker-all | 0.567 | 17 | 13 | 30 |
| Surfboard-tg-mixed | 0.683 | 82 | 38 | 120 |
| mheidari-all | 0.78 | 32 | 9 | 41 |
| zhangkai | 0.833 | 10 | 2 | 12 |
| Au1rxx-base64 | 0.876 | 283 | 40 | 323 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24075 | yes | 7.18 | 0 |
| SoliSpirit-all | 9931 | yes | 2.38 | 0 |
| Epodonios-all | 7717 | yes | 6.3 | 0 |
| Surfboard-tg-mixed | 7201 | yes | 4.11 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.02 | 0 |
| barry-far-vless | 5973 | yes | 1.2 | 0 |
| Surfboard-tg-vless | 5723 | yes | 4.32 | 0 |
| 10ium-ScrapeCategorize-Vless | 5086 | yes | 0.98 | 0 |
| DeltaKronecker-all | 5076 | yes | 6.42 | 0 |
| mahdibland-V2RayAggregator | 4312 | yes | 3.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| vmess | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 46 |
| cn-block | 41 |
| geo | 23 |
| speed | 9 |
