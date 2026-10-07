# AutoNodes 每日报告

生成时间：2026-10-07 13:11:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 98660 |
| 去重后节点数 | 27302 |
| TCP 可达数 | 3000 |
| 真测通过数 | 406 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27302 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 78.8 |
| geo | 1.3 |
| probe | 272.6 |
| real_test | 160.2 |
| tcp | 45.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 1 | 4 | 20.0% |
| http | 17 | 7 | 10 | 41.2% |
| hysteria2 | 26 | 22 | 4 | 84.6% |
| shadowsocks | 152 | 138 | 14 | 90.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 95 | 83 | 12 | 87.4% |
| vless | 203 | 154 | 49 | 75.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 23 |
| cn-block:TimeoutError | 22 |
| 204:TimeoutError | 21 |
| speed:ClientOSError | 9 |
| geo:ClientOSError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| speed:TimeoutError | 2 |
| cn-block:ClientOSError | 2 |
| geo:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6226 |
| ConnectionRefusedError | 1032 |
| gaierror | 462 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | prefer | 334 | 0.898 | 1830 |
| mheidari-all | 0.873 | prefer | 56 | 0.804 | 23381 |
| Surfboard-tg-mixed | 0.678 | observe | 85 | 0.6 | 7069 |
| ermaozi | 0.447 | observe | 18 | 0.444 | 664 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5138 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5344 |
| Epodonios-all | 0.255 | observe | 0 | None | 7480 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9550 |

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
| downweight | ermaozi-get_subscribe | 0.169 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| ermaozi | 0.444 | 8 | 10 | 18 |
| Surfboard-tg-mixed | 0.6 | 51 | 34 | 85 |
| mheidari-all | 0.804 | 45 | 11 | 56 |
| Au1rxx-base64 | 0.898 | 300 | 34 | 334 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23381 | yes | 3.56 | 0 |
| SoliSpirit-all | 9550 | yes | 1.06 | 0 |
| Epodonios-all | 7480 | yes | 2.09 | 0 |
| Surfboard-tg-mixed | 7069 | yes | 2.83 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.21 | 0 |
| barry-far-vless | 5861 | yes | 0.55 | 0 |
| Surfboard-tg-vless | 5616 | yes | 2.63 | 0 |
| DeltaKronecker-all | 5344 | yes | 3.12 | 0 |
| 10ium-ScrapeCategorize-Vless | 5138 | yes | 0.43 | 0 |
| mahdibland-V2RayAggregator | 4418 | yes | 2.13 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 48 |
| cn-block | 26 |
| speed | 11 |
| geo | 9 |
