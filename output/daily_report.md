# AutoNodes 每日报告

生成时间：2026-10-06 06:01:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 98384 |
| 去重后节点数 | 27441 |
| TCP 可达数 | 3000 |
| 真测通过数 | 531 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27441 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| generate | 74.6 |
| geo | 1.5 |
| probe | 282.3 |
| real_test | 355.7 |
| tcp | 48.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 2 | 4 | 33.3% |
| http | 59 | 34 | 25 | 57.6% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 172 | 156 | 16 | 90.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 113 | 106 | 7 | 93.8% |
| vless | 409 | 213 | 196 | 52.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 113 |
| speed:TimeoutError | 36 |
| 204:ProxyError | 25 |
| geo:ClientOSError | 20 |
| 204:TimeoutError | 14 |
| cn-block:TimeoutError | 14 |
| speed:ClientOSError | 8 |
| 204:ProxyConnectionError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6924 |
| ConnectionRefusedError | 1023 |
| gaierror | 280 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 356 | 0.935 | 1801 |
| Surfboard-tg-mixed | 0.797 | prefer | 143 | 0.72 | 7083 |
| ermaozi | 0.601 | observe | 59 | 0.576 | 691 |
| mheidari-all | 0.351 | observe | 201 | 0.269 | 23039 |
| DeltaKronecker-all | 0.337 | observe | 13 | 0.308 | 5300 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 53 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5111 |
| Epodonios-all | 0.255 | observe | 0 | None | 7631 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9601 |

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
| downweight | ermaozi-get_subscribe | 0.227 | 6 | 0.333 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.269 | 54 | 147 | 201 |
| DeltaKronecker-all | 0.308 | 4 | 9 | 13 |
| ermaozi-get_subscribe | 0.333 | 2 | 4 | 6 |
| ermaozi | 0.576 | 34 | 25 | 59 |
| Surfboard-tg-mixed | 0.72 | 103 | 40 | 143 |
| Au1rxx-base64 | 0.935 | 333 | 23 | 356 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23039 | yes | 5.63 | 0 |
| SoliSpirit-all | 9601 | yes | 6.15 | 0 |
| Epodonios-all | 7631 | yes | 5.01 | 0 |
| Surfboard-tg-mixed | 7083 | yes | 5.93 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.94 | 0 |
| barry-far-vless | 5876 | yes | 3.93 | 0 |
| Surfboard-tg-vless | 5600 | yes | 4.2 | 0 |
| DeltaKronecker-all | 5300 | yes | 7.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 5111 | yes | 3.64 | 0 |
| mahdibland-V2RayAggregator | 4375 | yes | 3.72 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 133 |
| 204 | 50 |
| speed | 44 |
| cn-block | 21 |
