# AutoNodes 每日报告

生成时间：2026-07-11 13:42:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76522 |
| 去重后节点数 | 24023 |
| TCP 可达数 | 3000 |
| 真测通过数 | 295 |
| verified 输出数 | 295 |
| global 输出数 | 300 |
| all 输出数 | 24023 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 26.8 |
| geo | 1.4 |
| probe | 45.6 |
| real_test | 62.9 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 108 | 99 | 9 | 91.7% |
| socks | 7 | 6 | 1 | 85.7% |
| trojan | 216 | 142 | 74 | 65.7% |
| vless | 35 | 3 | 32 | 8.6% |
| vmess | 7 | 7 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 24 |
| geo:TimeoutError | 19 |
| speed:ClientOSError | 16 |
| cn-block:ProxyError | 13 |
| geo:ProxyError | 10 |
| geo:ClientOSError | 8 |
| cn-block:ClientOSError | 7 |
| speed:ProxyError | 7 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 4 |
| cn-block:TimeoutError | 3 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4318 |
| ConnectionRefusedError | 668 |
| gaierror | 293 |
| OSError | 188 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.904 | prefer | 100 | 0.83 | 5543 |
| Au1rxx-base64 | 0.804 | prefer | 28 | 0.821 | 103 |
| mheidari-all | 0.802 | prefer | 77 | 0.727 | 16510 |
| DeltaKronecker-all | 0.645 | observe | 166 | 0.566 | 7969 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.303 | observe | 1 | 1.0 | 1207 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3953 |
| Epodonios-all | 0.255 | observe | 0 | None | 6467 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3968 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.566 | 94 | 72 | 166 |
| mheidari-all | 0.727 | 56 | 21 | 77 |
| Au1rxx-base64 | 0.821 | 23 | 5 | 28 |
| Surfboard-tg-mixed | 0.83 | 83 | 17 | 100 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16510 | yes | 3.68 | 0 |
| DeltaKronecker-all | 7969 | yes | 3.65 | 0 |
| SoliSpirit-all | 6527 | yes | 1.5 | 0 |
| Epodonios-all | 6467 | yes | 0.57 | 0 |
| Surfboard-tg-mixed | 5543 | yes | 2.19 | 0 |
| mahdibland-V2RayAggregator | 5423 | yes | 1.66 | 0 |
| barry-far-vless | 4696 | yes | 1.05 | 0 |
| Surfboard-tg-vless | 4147 | yes | 1.91 | 0 |
| MatinGhanbari-all-sub | 3968 | yes | 1.59 | 0 |
| 10ium-ScrapeCategorize-Vless | 3953 | yes | 1.24 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.086 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 37 |
| 204 | 32 |
| speed | 24 |
| cn-block | 23 |
