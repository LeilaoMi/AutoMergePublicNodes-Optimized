# AutoNodes 每日报告

生成时间：2026-07-06 20:09:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80258 |
| 去重后节点数 | 24589 |
| TCP 可达数 | 3000 |
| 真测通过数 | 284 |
| verified 输出数 | 284 |
| global 输出数 | 300 |
| all 输出数 | 24589 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 34.3 |
| geo | 1.3 |
| probe | 48.2 |
| real_test | 72.9 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 124 | 100 | 24 | 80.6% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 173 | 126 | 47 | 72.8% |
| vless | 38 | 9 | 29 | 23.7% |
| vmess | 6 | 5 | 1 | 83.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 30 |
| 204:ClientOSError | 13 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 10 |
| 204:ProxyError | 9 |
| cn-block:ClientOSError | 9 |
| geo:TimeoutError | 7 |
| cn-block:ProxyError | 4 |
| speed:ProxyError | 3 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 2 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4494 |
| ConnectionRefusedError | 783 |
| OSError | 158 |
| gaierror | 149 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.805 | prefer | 58 | 0.81 | 121 |
| Surfboard-tg-mixed | 0.794 | prefer | 110 | 0.718 | 6111 |
| DeltaKronecker-all | 0.793 | prefer | 120 | 0.717 | 8330 |
| mheidari-all | 0.661 | observe | 60 | 0.583 | 16332 |
| nscl5-all | 0.321 | observe | 1 | 1.0 | 1651 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4358 |
| Epodonios-all | 0.255 | observe | 0 | None | 7090 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7234 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.583 | 35 | 25 | 60 |
| DeltaKronecker-all | 0.717 | 86 | 34 | 120 |
| Surfboard-tg-mixed | 0.718 | 79 | 31 | 110 |
| Au1rxx-base64 | 0.81 | 47 | 11 | 58 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16332 | yes | 3.89 | 0 |
| DeltaKronecker-all | 8330 | yes | 3.91 | 0 |
| SoliSpirit-all | 7234 | yes | 2.74 | 0 |
| Epodonios-all | 7090 | yes | 0.66 | 0 |
| Surfboard-tg-mixed | 6111 | yes | 2.72 | 0 |
| mahdibland-V2RayAggregator | 5338 | yes | 1.01 | 0 |
| barry-far-vless | 5174 | yes | 1.99 | 0 |
| Surfboard-tg-vless | 4506 | yes | 1.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 4358 | yes | 1.5 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 35 |
| 204 | 34 |
| cn-block | 23 |
| geo | 10 |
