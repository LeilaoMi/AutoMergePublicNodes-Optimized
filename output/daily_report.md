# AutoNodes 每日报告

生成时间：2026-09-23 21:29:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 96813 |
| 去重后节点数 | 26642 |
| TCP 可达数 | 3000 |
| 真测通过数 | 406 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26642 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 79.6 |
| geo | 1.5 |
| probe | 247.2 |
| real_test | 158.3 |
| tcp | 43.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 36 | 25 | 11 | 69.4% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 170 | 148 | 22 | 87.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 29 | 26 | 3 | 89.7% |
| vless | 235 | 188 | 47 | 80.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 11 |
| cn-block:ClientOSError | 11 |
| 204:TimeoutError | 10 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 7 |
| 204:ProxyConnectionError | 6 |
| 204:ClientOSError | 5 |
| speed:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6111 |
| ConnectionRefusedError | 954 |
| gaierror | 373 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.959 | prefer | 252 | 0.897 | 1635 |
| mheidari-all | 0.885 | prefer | 85 | 0.812 | 22531 |
| Surfboard-tg-mixed | 0.802 | prefer | 113 | 0.726 | 7072 |
| ermaozi | 0.793 | prefer | 30 | 0.8 | 291 |
| DeltaKronecker-all | 0.438 | observe | 3 | 1.0 | 6471 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4332 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5131 |
| Epodonios-all | 0.255 | observe | 0 | None | 7534 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8842 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.148 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.167 | 1 | 5 | 6 |
| Surfboard-tg-mixed | 0.726 | 82 | 31 | 113 |
| ermaozi | 0.8 | 24 | 6 | 30 |
| mheidari-all | 0.812 | 69 | 16 | 85 |
| Au1rxx-base64 | 0.897 | 226 | 26 | 252 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22531 | yes | 6.43 | 0 |
| SoliSpirit-all | 8842 | yes | 4.62 | 0 |
| Epodonios-all | 7534 | yes | 0.22 | 0 |
| Surfboard-tg-mixed | 7072 | yes | 4.38 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.46 | 0 |
| DeltaKronecker-all | 6471 | yes | 4.37 | 0 |
| barry-far-vless | 5930 | yes | 4.04 | 0 |
| Surfboard-tg-vless | 5711 | yes | 5.31 | 0 |
| 10ium-ScrapeCategorize-Vless | 5131 | yes | 2.37 | 0 |
| mahdibland-V2RayAggregator | 4332 | yes | 1.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 34 |
| 204 | 32 |
| speed | 11 |
| geo | 9 |
