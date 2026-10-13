# AutoNodes 每日报告

生成时间：2026-10-13 00:46:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 1/105 |
| 原始节点数 | 100924 |
| 去重后节点数 | 27887 |
| TCP 可达数 | 3000 |
| 真测通过数 | 486 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27887 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 73.0 |
| geo | 1.6 |
| probe | 414.4 |
| real_test | 703.0 |
| tcp | 47.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 4 | 1 | 3 | 25.0% |
| http | 23 | 10 | 13 | 43.5% |
| hysteria2 | 17 | 16 | 1 | 94.1% |
| shadowsocks | 118 | 114 | 4 | 96.6% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 124 | 116 | 8 | 93.5% |
| vless | 638 | 224 | 414 | 35.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 217 |
| speed:TimeoutError | 111 |
| geo:ClientOSError | 37 |
| speed:ClientOSError | 34 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 4 |
| cn-block:ProxyError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6441 |
| ConnectionRefusedError | 1055 |
| gaierror | 373 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.991 | prefer | 348 | 0.92 | 1847 |
| Surfboard-tg-mixed | 0.593 | observe | 7 | 1.0 | 7208 |
| ermaozi | 0.471 | observe | 25 | 0.44 | 675 |
| mheidari-all | 0.351 | observe | 529 | 0.27 | 23897 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5028 |
| Epodonios-all | 0.255 | observe | 0 | None | 7736 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10536 |

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
| downweight | DeltaKronecker-all | 0.234 | 13 | 0.154 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.154 | 2 | 11 | 13 |
| ermaozi-get_subscribe | 0.25 | 1 | 3 | 4 |
| mheidari-all | 0.27 | 143 | 386 | 529 |
| ermaozi | 0.44 | 11 | 14 | 25 |
| Au1rxx-base64 | 0.92 | 320 | 28 | 348 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 7 | 0 | 7 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23897 | yes | 5.04 | 0 |
| SoliSpirit-all | 10536 | yes | 1.77 | 0 |
| Epodonios-all | 7736 | yes | 4.24 | 0 |
| Surfboard-tg-mixed | 7208 | yes | 0.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.2 | 0 |
| barry-far-vless | 6023 | yes | 0.68 | 0 |
| DeltaKronecker-all | 5701 | yes | 4.91 | 0 |
| Surfboard-tg-vless | 5678 | yes | 3.32 | 0 |
| 10ium-ScrapeCategorize-Vless | 5028 | yes | 0.38 | 0 |
| mahdibland-V2RayAggregator | 4314 | yes | 2.95 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 258 |
| speed | 146 |
| 204 | 21 |
| cn-block | 20 |
