# AutoNodes 每日报告

生成时间：2026-07-25 08:19:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78921 |
| 去重后节点数 | 22393 |
| TCP 可达数 | 3000 |
| 真测通过数 | 842 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22393 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 42.2 |
| geo | 1.3 |
| probe | 61.9 |
| real_test | 177.8 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 135 | 112 | 23 | 83.0% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 604 | 554 | 50 | 91.7% |
| vless | 377 | 136 | 241 | 36.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 132 |
| speed:ClientOSError | 55 |
| cn-block:TimeoutError | 29 |
| 204:ProxyError | 26 |
| geo:ClientOSError | 24 |
| 204:TimeoutError | 18 |
| speed:TimeoutError | 14 |
| cn-block:ClientOSError | 7 |
| cn-block:ProxyError | 6 |
| geo:ProxyError | 4 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4016 |
| ConnectionRefusedError | 691 |
| gaierror | 368 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.861 | prefer | 132 | 0.848 | 432 |
| mheidari-all | 0.845 | prefer | 479 | 0.766 | 17378 |
| DeltaKronecker-all | 0.779 | prefer | 227 | 0.7 | 5838 |
| Surfboard-tg-mixed | 0.675 | observe | 282 | 0.596 | 5473 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4879 |
| Epodonios-all | 0.255 | observe | 0 | None | 6614 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6346 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4256 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.596 | 168 | 114 | 282 |
| DeltaKronecker-all | 0.7 | 159 | 68 | 227 |
| mheidari-all | 0.766 | 367 | 112 | 479 |
| Au1rxx-base64 | 0.848 | 112 | 20 | 132 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17378 | yes | 3.64 | 0 |
| Epodonios-all | 6614 | yes | 3.85 | 0 |
| SoliSpirit-all | 6346 | yes | 3.62 | 0 |
| DeltaKronecker-all | 5838 | yes | 4.15 | 0 |
| Surfboard-tg-mixed | 5473 | yes | 3.11 | 0 |
| mahdibland-V2RayAggregator | 5009 | yes | 1.76 | 0 |
| barry-far-vless | 4927 | yes | 2.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4879 | yes | 1.73 | 0 |
| Surfboard-tg-vless | 4256 | yes | 2.64 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 2.38 | 0 |

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
| geo | 160 |
| speed | 69 |
| 204 | 46 |
| cn-block | 42 |
