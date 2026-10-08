# AutoNodes 每日报告

生成时间：2026-10-08 05:43:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 1/105 |
| 原始节点数 | 99165 |
| 去重后节点数 | 27686 |
| TCP 可达数 | 3000 |
| 真测通过数 | 415 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27686 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| generate | 76.0 |
| geo | 1.5 |
| probe | 299.9 |
| real_test | 411.4 |
| tcp | 46.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 8 | 0 | 8 | 0.0% |
| http | 60 | 31 | 29 | 51.7% |
| hysteria2 | 22 | 18 | 4 | 81.8% |
| shadowsocks | 124 | 117 | 7 | 94.4% |
| socks | 3 | 3 | 0 | 100.0% |
| trojan | 82 | 66 | 16 | 80.5% |
| vless | 487 | 180 | 307 | 37.0% |
| vmess | 2 | 0 | 2 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 157 |
| speed:TimeoutError | 58 |
| 204:ProxyError | 40 |
| geo:ClientOSError | 38 |
| speed:ClientOSError | 24 |
| 204:ProxyConnectionError | 21 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 15 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6525 |
| ConnectionRefusedError | 1011 |
| gaierror | 458 |
| OSError | 238 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | prefer | 303 | 0.908 | 1772 |
| ermaozi-get_subscribe | 0.539 | observe | 31 | 0.516 | 592 |
| Surfboard-tg-mixed | 0.446 | observe | 8 | 0.625 | 7193 |
| ermaozi | 0.433 | observe | 40 | 0.4 | 715 |
| mheidari-all | 0.342 | observe | 387 | 0.261 | 23407 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7663 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9552 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5725 |

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
| downweight | DeltaKronecker-all | 0.175 | 17 | 0.059 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.059 | 1 | 16 | 17 |
| mheidari-all | 0.261 | 101 | 286 | 387 |
| ermaozi | 0.4 | 16 | 24 | 40 |
| ermaozi-get_subscribe | 0.516 | 16 | 15 | 31 |
| Surfboard-tg-mixed | 0.625 | 5 | 3 | 8 |
| Au1rxx-base64 | 0.908 | 275 | 28 | 303 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23407 | yes | 6.67 | 0 |
| SoliSpirit-all | 9552 | yes | 2.6 | 0 |
| Epodonios-all | 7663 | yes | 3.81 | 0 |
| Surfboard-tg-mixed | 7193 | yes | 5.7 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.03 | 0 |
| barry-far-vless | 5963 | yes | 0.81 | 0 |
| Surfboard-tg-vless | 5725 | yes | 4.46 | 0 |
| DeltaKronecker-all | 5344 | yes | 7.02 | 0 |
| 10ium-ScrapeCategorize-Vless | 5138 | yes | 1.33 | 0 |
| mahdibland-V2RayAggregator | 4431 | yes | 3.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |
| vmess | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 195 |
| speed | 82 |
| 204 | 76 |
| cn-block | 20 |
