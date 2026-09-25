# AutoNodes 每日报告

生成时间：2026-09-25 04:34:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 97834 |
| 去重后节点数 | 26576 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26576 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 77.7 |
| geo | 1.6 |
| probe | 265.0 |
| real_test | 356.8 |
| tcp | 43.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 33 | 17 | 16 | 51.5% |
| hysteria2 | 21 | 21 | 0 | 100.0% |
| shadowsocks | 177 | 171 | 6 | 96.6% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 50 | 33 | 17 | 66.0% |
| vless | 482 | 209 | 273 | 43.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 128 |
| speed:TimeoutError | 49 |
| geo:ClientOSError | 36 |
| cn-block:ClientOSError | 28 |
| speed:ClientOSError | 22 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 8 |
| 204:ProxyConnectionError | 7 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |
| speed:ClientPayloadError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6296 |
| ConnectionRefusedError | 961 |
| gaierror | 328 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.975 | prefer | 266 | 0.91 | 1702 |
| Surfboard-tg-mixed | 0.791 | prefer | 185 | 0.714 | 7399 |
| ermaozi | 0.514 | observe | 26 | 0.5 | 338 |
| DeltaKronecker-all | 0.352 | observe | 11 | 0.364 | 5845 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4405 |
| mheidari-all | 0.304 | observe | 270 | 0.222 | 22554 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 80 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5307 |
| Epodonios-all | 0.255 | observe | 0 | None | 7876 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| downweight | ermaozi-get_subscribe | 0.234 | 5 | 0.4 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.222 | 60 | 210 | 270 |
| DeltaKronecker-all | 0.364 | 4 | 7 | 11 |
| ermaozi-get_subscribe | 0.4 | 2 | 3 | 5 |
| ermaozi | 0.5 | 13 | 13 | 26 |
| Surfboard-tg-mixed | 0.714 | 132 | 53 | 185 |
| Au1rxx-base64 | 0.91 | 242 | 24 | 266 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22554 | yes | 4.79 | 0 |
| SoliSpirit-all | 9018 | yes | 4.0 | 0 |
| Epodonios-all | 7876 | yes | 2.6 | 0 |
| Surfboard-tg-mixed | 7399 | yes | 3.39 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.76 | 0 |
| barry-far-vless | 6091 | yes | 1.75 | 0 |
| Surfboard-tg-vless | 5862 | yes | 3.14 | 0 |
| DeltaKronecker-all | 5845 | yes | 4.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 5307 | yes | 3.01 | 0 |
| mahdibland-V2RayAggregator | 4405 | yes | 1.3 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 167 |
| speed | 72 |
| cn-block | 45 |
| 204 | 31 |
