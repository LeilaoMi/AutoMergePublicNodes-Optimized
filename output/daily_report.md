# AutoNodes 每日报告

生成时间：2026-08-20 01:42:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/2 |
| 清理建议：优先/观察 | 3/102 |
| 原始节点数 | 91151 |
| 去重后节点数 | 23547 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1275 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23547 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 37.6 |
| geo | 1.1 |
| probe | 77.3 |
| real_test | 242.2 |
| tcp | 37.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 100 | 99 | 1 | 99.0% |
| socks | 6 | 4 | 2 | 66.7% |
| trojan | 711 | 697 | 14 | 98.0% |
| vless | 670 | 343 | 327 | 51.2% |
| vmess | 4 | 3 | 1 | 75.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 128 |
| geo:ClientOSError | 85 |
| speed:TimeoutError | 75 |
| speed:ClientOSError | 19 |
| cn-block:TimeoutError | 14 |
| 204:TimeoutError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4380 |
| ConnectionRefusedError | 976 |
| gaierror | 587 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 680 | 0.991 | 1789 |
| zhangkai | 0.997 | prefer | 113 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.734 | prefer | 24 | 0.667 | 6430 |
| mheidari-all | 0.681 | observe | 784 | 0.601 | 20672 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5974 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5067 |
| Epodonios-all | 0.255 | observe | 0 | None | 7184 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7353 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5059 |

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
| ninja-vless | 0.136 | downweight | 7 | 0.0 | 0 | 1791 |
| nscl5-all | 0.148 | downweight | 6 | 0.0 | 0 | 2418 |
| DeltaKronecker-all | 0.16 | observe | 4 | 0.0 | 0 | 4713 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ninja-vless | 0.136 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.148 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 4 | 4 |
| nscl5-all | 0.0 | 0 | 6 | 6 |
| ninja-vless | 0.0 | 0 | 7 | 7 |
| mheidari-all | 0.601 | 471 | 313 | 784 |
| Surfboard-tg-mixed | 0.667 | 16 | 8 | 24 |
| Au1rxx-base64 | 0.991 | 674 | 6 | 680 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20672 | yes | 3.48 | 0 |
| SoliSpirit-all | 7353 | yes | 1.77 | 0 |
| Epodonios-all | 7184 | yes | 3.96 | 0 |
| Surfboard-tg-mixed | 6430 | yes | 2.24 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.11 | 0 |
| barry-far-vless | 5381 | yes | 0.78 | 0 |
| 10ium-ScrapeCategorize-Vless | 5067 | yes | 0.53 | 0 |
| Surfboard-tg-vless | 5059 | yes | 2.55 | 0 |
| DeltaKronecker-all | 4713 | yes | 3.45 | 0 |
| mahdibland-V2RayAggregator | 4086 | yes | 1.94 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 213 |
| speed | 94 |
| cn-block | 21 |
| 204 | 17 |
