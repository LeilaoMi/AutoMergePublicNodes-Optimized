# AutoNodes 每日报告

生成时间：2026-09-27 11:57:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 95691 |
| 去重后节点数 | 26593 |
| TCP 可达数 | 3000 |
| 真测通过数 | 418 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26593 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 93.9 |
| geo | 1.4 |
| probe | 273.1 |
| real_test | 178.0 |
| tcp | 43.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 71 | 32 | 39 | 45.1% |
| hysteria2 | 23 | 19 | 4 | 82.6% |
| shadowsocks | 174 | 151 | 23 | 86.8% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 31 | 25 | 6 | 80.6% |
| vless | 247 | 190 | 57 | 76.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 28 |
| 204:ProxyConnectionError | 20 |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 16 |
| speed:TimeoutError | 15 |
| geo:TimeoutError | 13 |
| cn-block:ClientOSError | 7 |
| speed:ClientOSError | 7 |
| cn-block:ProxyError | 2 |
| geo:ClientOSError | 2 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5798 |
| ConnectionRefusedError | 953 |
| gaierror | 386 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.936 | prefer | 281 | 0.875 | 1589 |
| Surfboard-tg-mixed | 0.849 | prefer | 106 | 0.774 | 7025 |
| mheidari-all | 0.734 | prefer | 76 | 0.658 | 22397 |
| ermaozi | 0.505 | observe | 57 | 0.491 | 338 |
| DeltaKronecker-all | 0.418 | observe | 10 | 0.5 | 5466 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| ermaozi-get_subscribe | 0.261 | observe | 15 | 0.267 | 361 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 149 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |

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
| ermaozi-get_subscribe | 0.267 | 4 | 11 | 15 |
| ermaozi | 0.491 | 28 | 29 | 57 |
| DeltaKronecker-all | 0.5 | 5 | 5 | 10 |
| mheidari-all | 0.658 | 50 | 26 | 76 |
| Surfboard-tg-mixed | 0.774 | 82 | 24 | 106 |
| Au1rxx-base64 | 0.875 | 246 | 35 | 281 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22397 | yes | 5.7 | 0 |
| SoliSpirit-all | 8971 | yes | 4.43 | 0 |
| Epodonios-all | 7510 | yes | 3.21 | 0 |
| Surfboard-tg-mixed | 7025 | yes | 4.14 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.15 | 0 |
| barry-far-vless | 5862 | yes | 1.97 | 0 |
| Surfboard-tg-vless | 5637 | yes | 3.61 | 0 |
| DeltaKronecker-all | 5466 | yes | 6.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 2.12 | 0 |
| mahdibland-V2RayAggregator | 4277 | yes | 3.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 68 |
| cn-block | 25 |
| speed | 23 |
| geo | 15 |
