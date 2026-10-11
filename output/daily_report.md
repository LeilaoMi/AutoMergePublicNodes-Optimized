# AutoNodes 每日报告

生成时间：2026-10-11 12:42:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 98718 |
| 去重后节点数 | 27554 |
| TCP 可达数 | 3000 |
| 真测通过数 | 514 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27554 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 76.9 |
| geo | 1.3 |
| probe | 345.5 |
| real_test | 394.8 |
| tcp | 47.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 2 | 4 | 33.3% |
| http | 18 | 8 | 10 | 44.4% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 156 | 130 | 26 | 83.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 177 | 171 | 6 | 96.6% |
| vless | 247 | 184 | 63 | 74.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 24 |
| 204:TimeoutError | 20 |
| 204:ProxyError | 13 |
| speed:ClientOSError | 11 |
| geo:ClientOSError | 9 |
| geo:TimeoutError | 8 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6525 |
| ConnectionRefusedError | 1023 |
| gaierror | 404 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.988 | prefer | 362 | 0.917 | 1835 |
| mheidari-all | 0.913 | prefer | 52 | 0.846 | 23631 |
| DeltaKronecker-all | 0.906 | prefer | 44 | 0.841 | 5372 |
| Surfboard-tg-mixed | 0.716 | prefer | 141 | 0.638 | 7157 |
| ermaozi | 0.493 | observe | 18 | 0.5 | 635 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5099 |
| Epodonios-all | 0.255 | observe | 0 | None | 7574 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9584 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5553 |

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
| downweight | ermaozi-get_subscribe | 0.225 | 6 | 0.333 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.333 | 2 | 4 | 6 |
| ermaozi | 0.5 | 9 | 9 | 18 |
| Surfboard-tg-mixed | 0.638 | 90 | 51 | 141 |
| DeltaKronecker-all | 0.841 | 37 | 7 | 44 |
| mheidari-all | 0.846 | 44 | 8 | 52 |
| Au1rxx-base64 | 0.917 | 332 | 30 | 362 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23631 | yes | 5.14 | 0 |
| SoliSpirit-all | 9584 | yes | 3.24 | 0 |
| Epodonios-all | 7574 | yes | 5.31 | 0 |
| Surfboard-tg-mixed | 7157 | yes | 3.0 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.86 | 0 |
| barry-far-vless | 5786 | yes | 2.81 | 0 |
| Surfboard-tg-vless | 5553 | yes | 3.63 | 0 |
| DeltaKronecker-all | 5372 | yes | 5.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 5099 | yes | 2.96 | 0 |
| mahdibland-V2RayAggregator | 4318 | yes | 1.13 | 0 |

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
| 204 | 37 |
| cn-block | 35 |
| speed | 20 |
| geo | 19 |
