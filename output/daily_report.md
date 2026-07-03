# AutoNodes 每日报告

生成时间：2026-07-03 09:32:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77356 |
| 去重后节点数 | 22732 |
| TCP 可达数 | 3000 |
| 真测通过数 | 437 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22732 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 47.5 |
| geo | 1.4 |
| probe | 51.4 |
| real_test | 106.8 |
| tcp | 30.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 126 | 103 | 23 | 81.7% |
| socks | 25 | 22 | 3 | 88.0% |
| trojan | 136 | 103 | 33 | 75.7% |
| vless | 377 | 166 | 211 | 44.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 121 |
| geo:TimeoutError | 62 |
| 204:TimeoutError | 16 |
| geo:ClientOSError | 15 |
| 204:ProxyError | 14 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4284 |
| ConnectionRefusedError | 695 |
| OSError | 153 |
| gaierror | 148 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.766 | prefer | 103 | 0.689 | 6997 |
| Au1rxx-base64 | 0.741 | prefer | 40 | 0.75 | 80 |
| Surfboard-tg-mixed | 0.74 | prefer | 283 | 0.661 | 6013 |
| mheidari-all | 0.537 | observe | 243 | 0.457 | 16051 |
| nscl5-all | 0.356 | observe | 2 | 1.0 | 1114 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4368 |
| Epodonios-all | 0.255 | observe | 0 | None | 6902 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3977 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6954 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.457 | 111 | 132 | 243 |
| Surfboard-tg-mixed | 0.661 | 187 | 96 | 283 |
| DeltaKronecker-all | 0.689 | 71 | 32 | 103 |
| Au1rxx-base64 | 0.75 | 30 | 10 | 40 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16051 | yes | 3.56 | 0 |
| DeltaKronecker-all | 6997 | yes | 4.26 | 0 |
| SoliSpirit-all | 6954 | yes | 1.92 | 0 |
| Epodonios-all | 6902 | yes | 1.58 | 0 |
| Surfboard-tg-mixed | 6013 | yes | 2.16 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 1.87 | 0 |
| barry-far-vless | 5055 | yes | 1.36 | 0 |
| Surfboard-tg-vless | 4518 | yes | 2.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 4368 | yes | 1.56 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 1.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 129 |
| geo | 79 |
| 204 | 36 |
| cn-block | 26 |
