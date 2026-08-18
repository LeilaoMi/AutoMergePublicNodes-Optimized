# AutoNodes 每日报告

生成时间：2026-08-18 13:02:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 91956 |
| 去重后节点数 | 24183 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1245 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24183 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 36.2 |
| geo | 1.4 |
| probe | 71.6 |
| real_test | 245.8 |
| tcp | 38.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 158 | 138 | 20 | 87.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 860 | 843 | 17 | 98.0% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 184 | 118 | 66 | 64.1% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 23 |
| cn-block:TimeoutError | 21 |
| geo:TimeoutError | 18 |
| geo:ClientOSError | 13 |
| speed:TimeoutError | 9 |
| speed:ClientOSError | 8 |
| 204:ProxyError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4732 |
| ConnectionRefusedError | 957 |
| gaierror | 294 |
| OSError | 228 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 563 | 0.931 | 1759 |
| mheidari-all | 1.0 | prefer | 447 | 0.96 | 21086 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.86 | prefer | 207 | 0.783 | 6253 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 2992 |
| DeltaKronecker-all | 0.272 | observe | 7 | 0.286 | 5725 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5068 |
| Epodonios-all | 0.255 | observe | 0 | None | 6795 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3984 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6898 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.286 | 2 | 5 | 7 |
| Surfboard-tg-mixed | 0.783 | 162 | 45 | 207 |
| Au1rxx-base64 | 0.931 | 524 | 39 | 563 |
| mheidari-all | 0.96 | 429 | 18 | 447 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21086 | yes | 5.06 | 0 |
| SoliSpirit-all | 6898 | yes | 3.21 | 0 |
| Epodonios-all | 6795 | yes | 2.59 | 0 |
| xiaoji235-airport-v2ray-all | 6329 | yes | 3.0 | 0 |
| Surfboard-tg-mixed | 6253 | yes | 3.66 | 0 |
| DeltaKronecker-all | 5725 | yes | 4.23 | 0 |
| barry-far-vless | 5206 | yes | 2.47 | 0 |
| 10ium-ScrapeCategorize-Vless | 5068 | yes | 2.17 | 0 |
| Surfboard-tg-vless | 4907 | yes | 3.26 | 0 |
| mahdibland-V2RayAggregator | 4045 | yes | 2.69 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 34 |
| geo | 31 |
| cn-block | 26 |
| speed | 17 |
