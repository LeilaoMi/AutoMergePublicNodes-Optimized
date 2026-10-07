# AutoNodes 每日报告

生成时间：2026-10-07 05:34:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 97105 |
| 去重后节点数 | 27064 |
| TCP 可达数 | 3000 |
| 真测通过数 | 454 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27064 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| generate | 77.9 |
| geo | 1.6 |
| probe | 300.4 |
| real_test | 395.2 |
| tcp | 46.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 19 | 31 | 38.0% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 148 | 141 | 7 | 95.3% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 111 | 96 | 15 | 86.5% |
| vless | 427 | 180 | 247 | 42.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 122 |
| speed:TimeoutError | 57 |
| geo:ClientOSError | 31 |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 19 |
| 204:ProxyConnectionError | 15 |
| 204:TimeoutError | 15 |
| speed:ClientOSError | 13 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 3 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6425 |
| ConnectionRefusedError | 972 |
| gaierror | 360 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.968 | prefer | 305 | 0.898 | 1797 |
| Surfboard-tg-mixed | 0.742 | prefer | 69 | 0.667 | 7006 |
| mheidari-all | 0.435 | observe | 325 | 0.354 | 22990 |
| ermaozi | 0.414 | observe | 50 | 0.38 | 726 |
| Epodonios-all | 0.255 | observe | 0 | None | 7476 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9204 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5583 |
| barry-far-vless | 0.255 | observe | 0 | None | 5829 |
| mahdibland-V2RayAggregator | 0.255 | observe | 0 | None | 4373 |

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
| downweight | DeltaKronecker-all | 0.148 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 6 | 6 |
| mheidari-all | 0.354 | 115 | 210 | 325 |
| ermaozi | 0.38 | 19 | 31 | 50 |
| Surfboard-tg-mixed | 0.667 | 46 | 23 | 69 |
| Au1rxx-base64 | 0.898 | 274 | 31 | 305 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22990 | yes | 6.44 | 0 |
| SoliSpirit-all | 9204 | yes | 4.7 | 0 |
| Epodonios-all | 7476 | yes | 3.87 | 0 |
| Surfboard-tg-mixed | 7006 | yes | 4.62 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.88 | 0 |
| barry-far-vless | 5829 | yes | 1.89 | 0 |
| Surfboard-tg-vless | 5583 | yes | 4.87 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 3.36 | 0 |
| DeltaKronecker-all | 4889 | yes | 6.53 | 0 |
| mahdibland-V2RayAggregator | 4373 | yes | 2.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 156 |
| speed | 71 |
| 204 | 51 |
| cn-block | 26 |
