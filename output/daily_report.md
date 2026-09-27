# AutoNodes 每日报告

生成时间：2026-09-27 04:58:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 95804 |
| 去重后节点数 | 26625 |
| TCP 可达数 | 3000 |
| 真测通过数 | 496 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26625 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| generate | 96.3 |
| geo | 1.6 |
| probe | 281.0 |
| real_test | 377.5 |
| tcp | 44.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 38 | 22 | 16 | 57.9% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 175 | 150 | 25 | 85.7% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 48 | 34 | 14 | 70.8% |
| vless | 551 | 269 | 282 | 48.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 133 |
| speed:TimeoutError | 61 |
| geo:ClientOSError | 41 |
| cn-block:ClientOSError | 21 |
| 204:ProxyError | 20 |
| speed:ClientOSError | 17 |
| cn-block:TimeoutError | 16 |
| 204:ProxyConnectionError | 14 |
| 204:TimeoutError | 14 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6345 |
| ConnectionRefusedError | 946 |
| gaierror | 335 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.926 | prefer | 279 | 0.867 | 1536 |
| Surfboard-tg-mixed | 0.801 | prefer | 195 | 0.723 | 7113 |
| ermaozi | 0.585 | observe | 33 | 0.576 | 338 |
| mheidari-all | 0.361 | observe | 308 | 0.279 | 22408 |
| ermaozi-get_subscribe | 0.335 | observe | 7 | 0.571 | 361 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 149 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5242 |
| Epodonios-all | 0.255 | observe | 0 | None | 7583 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

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
| downweight | DeltaKronecker-all | 0.243 | 11 | 0.182 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.182 | 2 | 9 | 11 |
| mheidari-all | 0.279 | 86 | 222 | 308 |
| ermaozi-get_subscribe | 0.571 | 4 | 3 | 7 |
| ermaozi | 0.576 | 19 | 14 | 33 |
| Surfboard-tg-mixed | 0.723 | 141 | 54 | 195 |
| Au1rxx-base64 | 0.867 | 242 | 37 | 279 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22408 | yes | 6.23 | 0 |
| SoliSpirit-all | 8902 | yes | 4.62 | 0 |
| Epodonios-all | 7583 | yes | 3.25 | 0 |
| Surfboard-tg-mixed | 7113 | yes | 4.91 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.59 | 0 |
| barry-far-vless | 5907 | yes | 3.68 | 0 |
| Surfboard-tg-vless | 5686 | yes | 4.68 | 0 |
| DeltaKronecker-all | 5512 | yes | 6.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 5242 | yes | 2.88 | 0 |
| mahdibland-V2RayAggregator | 4355 | yes | 2.99 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 174 |
| speed | 78 |
| 204 | 52 |
| cn-block | 38 |
