# AutoNodes 每日报告

生成时间：2026-10-03 11:34:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 98931 |
| 去重后节点数 | 27239 |
| TCP 可达数 | 3000 |
| 真测通过数 | 357 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27239 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 90.5 |
| geo | 1.5 |
| probe | 259.1 |
| real_test | 171.2 |
| tcp | 47.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 3 | 2 | 60.0% |
| http | 24 | 14 | 10 | 58.3% |
| hysteria2 | 17 | 15 | 2 | 88.2% |
| shadowsocks | 154 | 131 | 23 | 85.1% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 33 | 17 | 16 | 51.5% |
| vless | 228 | 177 | 51 | 77.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 37 |
| cn-block:TimeoutError | 18 |
| 204:ProxyConnectionError | 11 |
| 204:ProxyError | 10 |
| geo:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| speed:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| geo:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6863 |
| ConnectionRefusedError | 1158 |
| gaierror | 357 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.958 | prefer | 239 | 0.891 | 1754 |
| mheidari-all | 0.854 | prefer | 60 | 0.783 | 23264 |
| Surfboard-tg-mixed | 0.705 | prefer | 126 | 0.627 | 7251 |
| ermaozi | 0.603 | observe | 24 | 0.583 | 645 |
| ermaozi-get_subscribe | 0.313 | observe | 5 | 0.6 | 516 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5192 |
| Epodonios-all | 0.255 | observe | 0 | None | 7748 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9363 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5966 |

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
| downweight | DeltaKronecker-all | 0.216 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.167 | 1 | 5 | 6 |
| ermaozi | 0.583 | 14 | 10 | 24 |
| ermaozi-get_subscribe | 0.6 | 3 | 2 | 5 |
| Surfboard-tg-mixed | 0.627 | 79 | 47 | 126 |
| mheidari-all | 0.783 | 47 | 13 | 60 |
| Au1rxx-base64 | 0.891 | 213 | 26 | 239 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23264 | yes | 6.58 | 0 |
| SoliSpirit-all | 9363 | yes | 2.47 | 0 |
| Epodonios-all | 7748 | yes | 3.35 | 0 |
| Surfboard-tg-mixed | 7251 | yes | 4.35 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.16 | 0 |
| barry-far-vless | 6206 | yes | 0.77 | 0 |
| Surfboard-tg-vless | 5966 | yes | 4.07 | 0 |
| DeltaKronecker-all | 5207 | yes | 4.79 | 0 |
| 10ium-ScrapeCategorize-Vless | 5192 | yes | 0.98 | 0 |
| mahdibland-V2RayAggregator | 4335 | yes | 3.07 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 61 |
| cn-block | 24 |
| speed | 11 |
| geo | 10 |
