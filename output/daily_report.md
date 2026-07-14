# AutoNodes 每日报告

生成时间：2026-07-14 02:56:49

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 77090 |
| 去重后节点数 | 23680 |
| TCP 可达数 | 3000 |
| 真测通过数 | 359 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23680 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 15.7 |
| geo | 1.4 |
| probe | 40.5 |
| real_test | 74.9 |
| tcp | 31.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 108 | 104 | 4 | 96.3% |
| trojan | 212 | 191 | 21 | 90.1% |
| vless | 142 | 21 | 121 | 14.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 72 |
| speed:ClientOSError | 35 |
| speed:TimeoutError | 16 |
| geo:ClientOSError | 15 |
| cn-block:ClientOSError | 2 |
| 204:ClientOSError | 2 |
| cn-block:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| 204:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4345 |
| ConnectionRefusedError | 637 |
| gaierror | 264 |
| OSError | 196 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.932 | prefer | 113 | 0.858 | 5561 |
| DeltaKronecker-all | 0.75 | prefer | 228 | 0.671 | 7926 |
| mheidari-all | 0.658 | observe | 114 | 0.579 | 16374 |
| Au1rxx-base64 | 0.482 | observe | 6 | 1.0 | 119 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 3836 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3897 |
| Epodonios-all | 0.255 | observe | 0 | None | 6563 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3978 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6467 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-Ahmedhamoomi_Servers | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-BESTFORBEST66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CryptoGuardVPN | 0.025 | observe | 0 | None | 1 | 0 |
| tg-DarkVPNpro | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ninja-vless | 0.14 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 6 | 6 |
| mheidari-all | 0.579 | 66 | 48 | 114 |
| DeltaKronecker-all | 0.671 | 153 | 75 | 228 |
| Surfboard-tg-mixed | 0.858 | 97 | 16 | 113 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Au1rxx-base64 | 1.0 | 6 | 0 | 6 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16374 | yes | 2.48 | 0 |
| DeltaKronecker-all | 7926 | yes | 2.63 | 0 |
| Epodonios-all | 6563 | yes | 1.05 | 0 |
| SoliSpirit-all | 6467 | yes | 1.68 | 0 |
| Surfboard-tg-mixed | 5561 | yes | 2.13 | 0 |
| mahdibland-V2RayAggregator | 5454 | yes | 1.77 | 0 |
| barry-far-vless | 4885 | yes | 0.87 | 0 |
| Surfboard-tg-vless | 4279 | yes | 1.31 | 0 |
| MatinGhanbari-all-sub | 3978 | yes | 1.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 3897 | yes | 0.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 87 |
| speed | 51 |
| cn-block | 5 |
| 204 | 3 |
