# AutoNodes 每日报告

生成时间：2026-10-07 23:03:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 98461 |
| 去重后节点数 | 27482 |
| TCP 可达数 | 3000 |
| 真测通过数 | 428 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27482 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 26.1 |
| geo | 1.4 |
| probe | 189.0 |
| real_test | 140.9 |
| tcp | 46.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 9 | 2 | 7 | 22.2% |
| http | 39 | 24 | 15 | 61.5% |
| hysteria2 | 25 | 24 | 1 | 96.0% |
| shadowsocks | 119 | 111 | 8 | 93.3% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 73 | 72 | 1 | 98.6% |
| vless | 246 | 193 | 53 | 78.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 19 |
| speed:TimeoutError | 16 |
| 204:ClientOSError | 9 |
| speed:ClientOSError | 9 |
| cn-block:TimeoutError | 9 |
| geo:ClientOSError | 7 |
| 204:TimeoutError | 6 |
| geo:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6407 |
| ConnectionRefusedError | 1025 |
| gaierror | 426 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.94 | prefer | 352 | 0.869 | 1824 |
| mheidari-all | 0.925 | prefer | 101 | 0.851 | 23169 |
| ermaozi | 0.636 | observe | 39 | 0.615 | 664 |
| Surfboard-tg-mixed | 0.529 | observe | 7 | 0.857 | 7189 |
| DeltaKronecker-all | 0.32 | observe | 4 | 0.5 | 5344 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5138 |
| Epodonios-all | 0.255 | observe | 0 | None | 7553 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| downweight | ermaozi-get_subscribe | 0.198 | 9 | 0.222 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.222 | 2 | 7 | 9 |
| DeltaKronecker-all | 0.5 | 2 | 2 | 4 |
| ermaozi | 0.615 | 24 | 15 | 39 |
| mheidari-all | 0.851 | 86 | 15 | 101 |
| Surfboard-tg-mixed | 0.857 | 6 | 1 | 7 |
| Au1rxx-base64 | 0.869 | 306 | 46 | 352 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23169 | yes | 3.76 | 0 |
| SoliSpirit-all | 9262 | yes | 2.9 | 0 |
| Epodonios-all | 7553 | yes | 2.08 | 0 |
| Surfboard-tg-mixed | 7189 | yes | 2.64 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.14 | 0 |
| barry-far-vless | 5859 | yes | 1.98 | 0 |
| Surfboard-tg-vless | 5706 | yes | 2.53 | 0 |
| DeltaKronecker-all | 5344 | yes | 3.3 | 0 |
| 10ium-ScrapeCategorize-Vless | 5138 | yes | 1.88 | 0 |
| mahdibland-V2RayAggregator | 4431 | yes | 0.39 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 34 |
| speed | 25 |
| cn-block | 15 |
| geo | 13 |
