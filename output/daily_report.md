# AutoNodes 每日报告

生成时间：2026-07-14 08:21:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78847 |
| 去重后节点数 | 23657 |
| TCP 可达数 | 3000 |
| 真测通过数 | 278 |
| verified 输出数 | 278 |
| global 输出数 | 290 |
| all 输出数 | 23657 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| generate | 25.7 |
| geo | 1.3 |
| probe | 45.1 |
| real_test | 85.0 |
| tcp | 30.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 102 | 77 | 25 | 75.5% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 186 | 148 | 38 | 79.6% |
| vless | 76 | 9 | 67 | 11.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 51 |
| speed:TimeoutError | 17 |
| 204:TimeoutError | 15 |
| speed:ClientOSError | 14 |
| geo:ClientOSError | 8 |
| cn-block:ClientOSError | 8 |
| 204:ProxyError | 5 |
| cn-block:TimeoutError | 5 |
| 204:ClientOSError | 5 |
| geo:status | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4106 |
| ConnectionRefusedError | 639 |
| gaierror | 311 |
| OSError | 196 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.796 | prefer | 107 | 0.72 | 5561 |
| DeltaKronecker-all | 0.733 | prefer | 148 | 0.655 | 7942 |
| mheidari-all | 0.638 | observe | 111 | 0.559 | 18314 |
| Au1rxx-base64 | 0.404 | observe | 4 | 1.0 | 103 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3836 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4019 |
| Epodonios-all | 0.255 | observe | 0 | None | 6471 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6406 |

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

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.559 | 62 | 49 | 111 |
| DeltaKronecker-all | 0.655 | 97 | 51 | 148 |
| Surfboard-tg-mixed | 0.72 | 77 | 30 | 107 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| Au1rxx-base64 | 1.0 | 4 | 0 | 4 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18314 | yes | 3.75 | 0 |
| DeltaKronecker-all | 7942 | yes | 7.06 | 0 |
| Epodonios-all | 6471 | yes | 1.32 | 0 |
| SoliSpirit-all | 6406 | yes | 1.87 | 0 |
| Surfboard-tg-mixed | 5561 | yes | 1.77 | 0 |
| mahdibland-V2RayAggregator | 5405 | yes | 1.87 | 0 |
| barry-far-vless | 4826 | yes | 1.2 | 0 |
| Surfboard-tg-vless | 4279 | yes | 2.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 4019 | yes | 1.66 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 0.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 60 |
| speed | 32 |
| 204 | 25 |
| cn-block | 14 |
