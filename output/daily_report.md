# AutoNodes 每日报告

生成时间：2026-09-29 12:40:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 96889 |
| 去重后节点数 | 26969 |
| TCP 可达数 | 3000 |
| 真测通过数 | 449 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26969 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 75.8 |
| geo | 1.4 |
| probe | 281.4 |
| real_test | 198.0 |
| tcp | 45.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 31 | 27 | 4 | 87.1% |
| hysteria2 | 27 | 26 | 1 | 96.3% |
| shadowsocks | 181 | 155 | 26 | 85.6% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 16 | 10 | 6 | 62.5% |
| vless | 320 | 227 | 93 | 70.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 30 |
| 204:TimeoutError | 28 |
| cn-block:TimeoutError | 19 |
| 204:ProxyError | 15 |
| speed:TimeoutError | 11 |
| cn-block:ClientOSError | 9 |
| geo:TimeoutError | 9 |
| geo:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6283 |
| ConnectionRefusedError | 1004 |
| gaierror | 312 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.893 | prefer | 331 | 0.831 | 1598 |
| mheidari-all | 0.886 | prefer | 65 | 0.815 | 22883 |
| ermaozi | 0.795 | prefer | 35 | 0.8 | 291 |
| Surfboard-tg-mixed | 0.707 | prefer | 140 | 0.629 | 7053 |
| ermaozi-get_subscribe | 0.323 | observe | 2 | 1.0 | 293 |
| DeltaKronecker-all | 0.32 | observe | 4 | 0.5 | 5528 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5314 |
| Epodonios-all | 0.255 | observe | 0 | None | 7502 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.629 | 88 | 52 | 140 |
| ermaozi | 0.8 | 28 | 7 | 35 |
| mheidari-all | 0.815 | 53 | 12 | 65 |
| Au1rxx-base64 | 0.831 | 275 | 56 | 331 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22883 | yes | 3.86 | 0 |
| SoliSpirit-all | 9548 | yes | 2.0 | 0 |
| Epodonios-all | 7502 | yes | 2.02 | 0 |
| Surfboard-tg-mixed | 7053 | yes | 1.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.83 | 0 |
| barry-far-vless | 5869 | yes | 1.2 | 0 |
| Surfboard-tg-vless | 5690 | yes | 2.55 | 0 |
| DeltaKronecker-all | 5528 | yes | 3.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 5314 | yes | 0.95 | 0 |
| mahdibland-V2RayAggregator | 4338 | yes | 1.61 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 43 |
| speed | 42 |
| cn-block | 31 |
| geo | 15 |
