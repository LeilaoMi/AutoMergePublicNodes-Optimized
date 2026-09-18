# AutoNodes 每日报告

生成时间：2026-09-18 04:23:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84088 |
| 去重后节点数 | 23179 |
| TCP 可达数 | 3000 |
| 真测通过数 | 607 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23179 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 33.1 |
| geo | 1.5 |
| probe | 354.4 |
| real_test | 544.8 |
| tcp | 39.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 22 | 6 | 78.6% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 183 | 177 | 6 | 96.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 79 | 52 | 27 | 65.8% |
| vless | 748 | 334 | 414 | 44.7% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 211 |
| speed:ClientOSError | 78 |
| geo:ClientOSError | 68 |
| speed:TimeoutError | 53 |
| cn-block:TimeoutError | 18 |
| 204:ProxyError | 13 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5551 |
| ConnectionRefusedError | 836 |
| gaierror | 292 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.947 | prefer | 286 | 0.885 | 1618 |
| Surfboard-tg-mixed | 0.834 | prefer | 120 | 0.758 | 7282 |
| ermaozi | 0.765 | prefer | 26 | 0.769 | 378 |
| mheidari-all | 0.517 | observe | 110 | 0.436 | 15863 |
| DeltaKronecker-all | 0.455 | observe | 513 | 0.374 | 5931 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4261 |
| ermaozi-get_subscribe | 0.285 | observe | 3 | 0.667 | 402 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5093 |
| Epodonios-all | 0.255 | observe | 0 | None | 7966 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.374 | 192 | 321 | 513 |
| mheidari-all | 0.436 | 48 | 62 | 110 |
| ermaozi-get_subscribe | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.758 | 91 | 29 | 120 |
| ermaozi | 0.769 | 20 | 6 | 26 |
| Au1rxx-base64 | 0.885 | 253 | 33 | 286 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15863 | yes | 2.83 | 0 |
| SoliSpirit-all | 9011 | yes | 2.8 | 0 |
| Epodonios-all | 7966 | yes | 2.03 | 0 |
| Surfboard-tg-mixed | 7282 | yes | 2.21 | 0 |
| barry-far-vless | 6180 | yes | 0.66 | 0 |
| DeltaKronecker-all | 5931 | yes | 3.06 | 0 |
| Surfboard-tg-vless | 5769 | yes | 2.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 5093 | yes | 0.79 | 0 |
| mahdibland-V2RayAggregator | 4261 | yes | 1.8 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 279 |
| speed | 132 |
| cn-block | 25 |
| 204 | 18 |
