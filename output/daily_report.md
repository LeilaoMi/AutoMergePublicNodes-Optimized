# AutoNodes 每日报告

生成时间：2026-10-09 22:40:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 97854 |
| 去重后节点数 | 27601 |
| TCP 可达数 | 3000 |
| 真测通过数 | 441 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27601 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| generate | 76.7 |
| geo | 1.5 |
| probe | 251.9 |
| real_test | 293.2 |
| tcp | 46.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 29 | 21 | 8 | 72.4% |
| hysteria2 | 20 | 20 | 0 | 100.0% |
| shadowsocks | 132 | 117 | 15 | 88.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 99 | 99 | 0 | 100.0% |
| vless | 224 | 182 | 42 | 81.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 20 |
| speed:ClientOSError | 10 |
| 204:ProxyError | 9 |
| geo:TimeoutError | 7 |
| 204:TimeoutError | 7 |
| speed:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ClientOSError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6560 |
| ConnectionRefusedError | 1021 |
| gaierror | 409 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | prefer | 367 | 0.913 | 1805 |
| zhangkai | 0.962 | prefer | 21 | 1.0 | 144 |
| mheidari-all | 0.88 | prefer | 68 | 0.809 | 23076 |
| Surfboard-tg-mixed | 0.783 | prefer | 35 | 0.714 | 7025 |
| DeltaKronecker-all | 0.259 | observe | 3 | 0.333 | 5154 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4984 |
| Epodonios-all | 0.255 | observe | 0 | None | 7582 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9986 |

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
| downweight | ermaozi-get_subscribe | 0.241 | 11 | 0.273 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.273 | 3 | 8 | 11 |
| DeltaKronecker-all | 0.333 | 1 | 2 | 3 |
| Surfboard-tg-mixed | 0.714 | 25 | 10 | 35 |
| mheidari-all | 0.809 | 55 | 13 | 68 |
| Au1rxx-base64 | 0.913 | 335 | 32 | 367 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 21 | 0 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23076 | yes | 7.29 | 0 |
| SoliSpirit-all | 9986 | yes | 2.68 | 0 |
| Epodonios-all | 7582 | yes | 4.13 | 0 |
| Surfboard-tg-mixed | 7025 | yes | 4.72 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.22 | 0 |
| barry-far-vless | 5812 | yes | 0.73 | 0 |
| Surfboard-tg-vless | 5553 | yes | 4.97 | 0 |
| DeltaKronecker-all | 5154 | yes | 7.6 | 0 |
| 10ium-ScrapeCategorize-Vless | 4984 | yes | 1.47 | 0 |
| mahdibland-V2RayAggregator | 4346 | yes | 3.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 25 |
| 204 | 16 |
| speed | 15 |
| geo | 10 |
