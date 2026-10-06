# AutoNodes 每日报告

生成时间：2026-10-06 22:40:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 97769 |
| 去重后节点数 | 27067 |
| TCP 可达数 | 3000 |
| 真测通过数 | 472 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27067 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| generate | 34.0 |
| geo | 1.5 |
| probe | 188.6 |
| real_test | 168.2 |
| tcp | 44.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 9 | 2 | 7 | 22.2% |
| http | 47 | 20 | 27 | 42.6% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 164 | 151 | 13 | 92.1% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 101 | 95 | 6 | 94.1% |
| vless | 207 | 179 | 28 | 86.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 27 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 9 |
| speed:ClientOSError | 6 |
| cn-block:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| 204:ProxyConnectionError | 5 |
| geo:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| geo:TimeoutError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5743 |
| ConnectionRefusedError | 1033 |
| gaierror | 541 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 326 | 0.951 | 1829 |
| mheidari-all | 0.942 | prefer | 63 | 0.873 | 23303 |
| Surfboard-tg-mixed | 0.856 | prefer | 105 | 0.781 | 7055 |
| ermaozi | 0.448 | observe | 48 | 0.417 | 708 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 4889 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4990 |
| Epodonios-all | 0.255 | observe | 0 | None | 7604 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9213 |

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
| downweight | ermaozi-get_subscribe | 0.199 | 9 | 0.222 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.222 | 2 | 7 | 9 |
| ermaozi | 0.417 | 20 | 28 | 48 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.781 | 82 | 23 | 105 |
| mheidari-all | 0.873 | 55 | 8 | 63 |
| Au1rxx-base64 | 0.951 | 310 | 16 | 326 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23303 | yes | 6.43 | 0 |
| SoliSpirit-all | 9213 | yes | 4.3 | 0 |
| Epodonios-all | 7604 | yes | 3.79 | 0 |
| Surfboard-tg-mixed | 7055 | yes | 6.68 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.32 | 0 |
| barry-far-vless | 5954 | yes | 0.86 | 0 |
| Surfboard-tg-vless | 5593 | yes | 4.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 1.29 | 0 |
| DeltaKronecker-all | 4889 | yes | 6.81 | 0 |
| mahdibland-V2RayAggregator | 4373 | yes | 3.53 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 48 |
| cn-block | 15 |
| speed | 12 |
| geo | 9 |
