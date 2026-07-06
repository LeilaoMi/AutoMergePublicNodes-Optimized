# AutoNodes 每日报告

生成时间：2026-07-06 10:52:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79147 |
| 去重后节点数 | 24406 |
| TCP 可达数 | 3000 |
| 真测通过数 | 338 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24406 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| generate | 35.7 |
| geo | 1.3 |
| probe | 43.3 |
| real_test | 81.8 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 120 | 104 | 16 | 86.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 211 | 179 | 32 | 84.8% |
| vless | 55 | 11 | 44 | 20.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 26 |
| geo:TimeoutError | 23 |
| 204:ClientOSError | 12 |
| geo:ClientOSError | 6 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 6 |
| speed:TimeoutError | 5 |
| 204:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4520 |
| ConnectionRefusedError | 760 |
| OSError | 158 |
| gaierror | 87 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.911 | prefer | 87 | 0.839 | 16255 |
| Au1rxx-base64 | 0.849 | prefer | 30 | 0.867 | 120 |
| Surfboard-tg-mixed | 0.841 | prefer | 115 | 0.765 | 5925 |
| DeltaKronecker-all | 0.792 | prefer | 158 | 0.715 | 8330 |
| nscl5-all | 0.321 | observe | 1 | 1.0 | 1651 |
| ermaozi | 0.256 | observe | 1 | 1.0 | 27 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4358 |
| Epodonios-all | 0.255 | observe | 0 | None | 6980 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.715 | 113 | 45 | 158 |
| Surfboard-tg-mixed | 0.765 | 88 | 27 | 115 |
| mheidari-all | 0.839 | 73 | 14 | 87 |
| Au1rxx-base64 | 0.867 | 26 | 4 | 30 |
| ermaozi | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16255 | yes | 3.01 | 0 |
| DeltaKronecker-all | 8330 | yes | 3.51 | 0 |
| Epodonios-all | 6980 | yes | 1.32 | 0 |
| SoliSpirit-all | 6861 | yes | 3.1 | 0 |
| Surfboard-tg-mixed | 5925 | yes | 2.25 | 0 |
| mahdibland-V2RayAggregator | 5349 | yes | 1.13 | 0 |
| barry-far-vless | 5043 | yes | 1.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4358 | yes | 1.81 | 0 |
| Surfboard-tg-vless | 4334 | yes | 2.46 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.15 | 0 |

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
| geo | 31 |
| speed | 31 |
| 204 | 21 |
| cn-block | 10 |
