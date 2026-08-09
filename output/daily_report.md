# AutoNodes 每日报告

生成时间：2026-08-09 07:08:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 82916 |
| 去重后节点数 | 23032 |
| TCP 可达数 | 3000 |
| 真测通过数 | 528 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23032 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 42.9 |
| geo | 1.4 |
| probe | 59.1 |
| real_test | 116.5 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 25 | 24 | 1 | 96.0% |
| shadowsocks | 153 | 141 | 12 | 92.2% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 131 | 128 | 3 | 97.7% |
| vless | 343 | 209 | 134 | 60.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 40 |
| 204:TimeoutError | 27 |
| cn-block:TimeoutError | 20 |
| speed:TimeoutError | 17 |
| speed:ClientOSError | 14 |
| 204:ProxyError | 13 |
| geo:ClientOSError | 11 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 1 |
| cn-block:ClientOSError | 1 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4624 |
| ConnectionRefusedError | 803 |
| gaierror | 340 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | prefer | 397 | 0.919 | 1640 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.78 | prefer | 88 | 0.705 | 6537 |
| mheidari-all | 0.625 | observe | 141 | 0.546 | 17626 |
| tg-oneclickvpnkeys | 0.318 | observe | 2 | 1.0 | 171 |
| Epodonios-all | 0.255 | observe | 0 | None | 7052 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7616 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5295 |
| barry-far-vless | 0.255 | observe | 0 | None | 5569 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.187 | 26 | 0.077 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.077 | 2 | 24 | 26 |
| mheidari-all | 0.546 | 77 | 64 | 141 |
| Surfboard-tg-mixed | 0.705 | 62 | 26 | 88 |
| Au1rxx-base64 | 0.919 | 365 | 32 | 397 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17626 | yes | 4.76 | 0 |
| SoliSpirit-all | 7616 | yes | 3.3 | 0 |
| Epodonios-all | 7052 | yes | 2.87 | 0 |
| Surfboard-tg-mixed | 6537 | yes | 3.77 | 0 |
| barry-far-vless | 5569 | yes | 2.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5505 | yes | 2.5 | 0 |
| Surfboard-tg-vless | 5295 | yes | 4.0 | 0 |
| mahdibland-V2RayAggregator | 5130 | yes | 2.96 | 0 |
| DeltaKronecker-all | 4998 | yes | 4.9 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.58 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 52 |
| 204 | 44 |
| speed | 32 |
| cn-block | 22 |
