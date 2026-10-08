# AutoNodes 每日报告

生成时间：2026-10-08 13:21:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 98623 |
| 去重后节点数 | 27533 |
| TCP 可达数 | 3000 |
| 真测通过数 | 457 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27533 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 83.8 |
| geo | 1.4 |
| probe | 343.7 |
| real_test | 257.7 |
| tcp | 46.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 34 | 22 | 12 | 64.7% |
| hysteria2 | 20 | 18 | 2 | 90.0% |
| shadowsocks | 169 | 148 | 21 | 87.6% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 87 | 72 | 15 | 82.8% |
| vless | 254 | 196 | 58 | 77.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 22 |
| cn-block:TimeoutError | 21 |
| 204:ProxyError | 17 |
| speed:ClientOSError | 10 |
| cn-block:ClientOSError | 10 |
| speed:TimeoutError | 8 |
| geo:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6726 |
| ConnectionRefusedError | 1014 |
| gaierror | 338 |
| OSError | 237 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.962 | prefer | 21 | 1.0 | 144 |
| Au1rxx-base64 | 0.96 | prefer | 352 | 0.889 | 1824 |
| mheidari-all | 0.858 | prefer | 43 | 0.791 | 23417 |
| Surfboard-tg-mixed | 0.73 | prefer | 115 | 0.652 | 7320 |
| ermaozi | 0.452 | observe | 7 | 0.857 | 66 |
| DeltaKronecker-all | 0.344 | observe | 12 | 0.333 | 5197 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 178 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5081 |
| Epodonios-all | 0.255 | observe | 0 | None | 7669 |

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
| downweight | ermaozi-get_subscribe | 0.125 | 13 | 0.077 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.077 | 1 | 12 | 13 |
| DeltaKronecker-all | 0.333 | 4 | 8 | 12 |
| Surfboard-tg-mixed | 0.652 | 75 | 40 | 115 |
| mheidari-all | 0.791 | 34 | 9 | 43 |
| ermaozi | 0.857 | 6 | 1 | 7 |
| Au1rxx-base64 | 0.889 | 313 | 39 | 352 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 21 | 0 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23417 | yes | 3.0 | 0 |
| SoliSpirit-all | 9655 | yes | 2.08 | 0 |
| Epodonios-all | 7669 | yes | 2.33 | 0 |
| Surfboard-tg-mixed | 7320 | yes | 2.62 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.64 | 0 |
| barry-far-vless | 5968 | yes | 0.46 | 0 |
| Surfboard-tg-vless | 5776 | yes | 3.79 | 0 |
| DeltaKronecker-all | 5197 | yes | 4.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 5081 | yes | 1.25 | 0 |
| mahdibland-V2RayAggregator | 4431 | yes | 2.13 | 0 |

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
| 204 | 45 |
| cn-block | 34 |
| speed | 18 |
| geo | 13 |
