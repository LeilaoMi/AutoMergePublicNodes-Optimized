# AutoNodes 每日报告

生成时间：2026-09-24 04:26:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/2 |
| 清理建议：优先/观察 | 2/103 |
| 原始节点数 | 96874 |
| 去重后节点数 | 26610 |
| TCP 可达数 | 3000 |
| 真测通过数 | 554 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26610 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| generate | 75.8 |
| geo | 1.4 |
| probe | 352.9 |
| real_test | 549.5 |
| tcp | 43.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 32 | 17 | 15 | 53.1% |
| hysteria2 | 25 | 25 | 0 | 100.0% |
| shadowsocks | 170 | 161 | 9 | 94.7% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 44 | 28 | 16 | 63.6% |
| vless | 802 | 314 | 488 | 39.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 215 |
| speed:TimeoutError | 82 |
| cn-block:ClientOSError | 54 |
| geo:ClientOSError | 53 |
| speed:ClientOSError | 38 |
| 204:TimeoutError | 32 |
| 204:ProxyError | 29 |
| cn-block:TimeoutError | 20 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| speed:ClientPayloadError | 1 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5971 |
| ConnectionRefusedError | 953 |
| gaierror | 341 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | prefer | 255 | 0.906 | 1648 |
| Surfboard-tg-mixed | 0.862 | prefer | 99 | 0.788 | 7099 |
| ermaozi | 0.6 | observe | 27 | 0.593 | 339 |
| mheidari-all | 0.409 | observe | 681 | 0.329 | 22298 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4332 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5131 |
| Epodonios-all | 0.255 | observe | 0 | None | 7563 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8881 |

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
| downweight | ermaozi-get_subscribe | 0.161 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.193 | 10 | 0.1 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.1 | 1 | 9 | 10 |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| mheidari-all | 0.329 | 224 | 457 | 681 |
| ninja-vless | 0.333 | 1 | 2 | 3 |
| ermaozi | 0.593 | 16 | 11 | 27 |
| Surfboard-tg-mixed | 0.788 | 78 | 21 | 99 |
| Au1rxx-base64 | 0.906 | 231 | 24 | 255 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22298 | yes | 3.46 | 0 |
| SoliSpirit-all | 8881 | yes | 1.57 | 0 |
| Epodonios-all | 7563 | yes | 1.62 | 0 |
| Surfboard-tg-mixed | 7099 | yes | 2.2 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.24 | 0 |
| DeltaKronecker-all | 6471 | yes | 2.85 | 0 |
| barry-far-vless | 5948 | yes | 0.76 | 0 |
| Surfboard-tg-vless | 5729 | yes | 2.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 5131 | yes | 0.63 | 0 |
| mahdibland-V2RayAggregator | 4332 | yes | 1.35 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 269 |
| speed | 121 |
| cn-block | 76 |
| 204 | 63 |
