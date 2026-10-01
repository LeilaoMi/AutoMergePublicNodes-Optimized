# AutoNodes 每日报告

生成时间：2026-10-01 22:40:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 98426 |
| 去重后节点数 | 27512 |
| TCP 可达数 | 3000 |
| 真测通过数 | 335 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27512 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| generate | 74.3 |
| geo | 1.5 |
| probe | 227.2 |
| real_test | 126.2 |
| tcp | 45.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 21 | 16 | 5 | 76.2% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 154 | 141 | 13 | 91.6% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 20 | 18 | 2 | 90.0% |
| vless | 164 | 140 | 24 | 85.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 9 |
| 204:ProxyConnectionError | 8 |
| cn-block:TimeoutError | 8 |
| 204:ProxyError | 5 |
| speed:TimeoutError | 4 |
| speed:ClientOSError | 4 |
| geo:ClientOSError | 3 |
| geo:TimeoutError | 3 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6045 |
| ConnectionRefusedError | 1044 |
| gaierror | 476 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.994 | prefer | 214 | 0.925 | 1818 |
| mheidari-all | 0.907 | prefer | 96 | 0.833 | 22987 |
| Surfboard-tg-mixed | 0.906 | prefer | 44 | 0.841 | 7183 |
| zhangkai | 0.745 | prefer | 21 | 0.762 | 144 |
| DeltaKronecker-all | 0.446 | observe | 5 | 0.8 | 5603 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5324 |
| Epodonios-all | 0.255 | observe | 0 | None | 7711 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9539 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5811 |

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
| zhangkai | 0.762 | 16 | 5 | 21 |
| DeltaKronecker-all | 0.8 | 4 | 1 | 5 |
| mheidari-all | 0.833 | 80 | 16 | 96 |
| Surfboard-tg-mixed | 0.841 | 37 | 7 | 44 |
| Au1rxx-base64 | 0.925 | 198 | 16 | 214 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22987 | yes | 6.17 | 0 |
| SoliSpirit-all | 9539 | yes | 5.69 | 0 |
| Epodonios-all | 7711 | yes | 3.96 | 0 |
| Surfboard-tg-mixed | 7183 | yes | 3.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.12 | 0 |
| barry-far-vless | 6097 | yes | 3.32 | 0 |
| Surfboard-tg-vless | 5811 | yes | 4.85 | 0 |
| DeltaKronecker-all | 5603 | yes | 7.0 | 0 |
| 10ium-ScrapeCategorize-Vless | 5324 | yes | 3.73 | 0 |
| mahdibland-V2RayAggregator | 4310 | yes | 3.69 | 0 |

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
| 204 | 24 |
| cn-block | 8 |
| speed | 8 |
| geo | 6 |
