# AutoNodes 每日报告

生成时间：2026-08-02 08:36:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 77331 |
| 去重后节点数 | 22731 |
| TCP 可达数 | 3000 |
| 真测通过数 | 695 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22731 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 36.4 |
| geo | 1.4 |
| probe | 60.8 |
| real_test | 153.0 |
| tcp | 34.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 143 | 143 | 0 | 100.0% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 151 | 114 | 37 | 75.5% |
| socks | 16 | 11 | 5 | 68.8% |
| trojan | 41 | 29 | 12 | 70.7% |
| vless | 546 | 378 | 168 | 69.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 66 |
| speed:TimeoutError | 55 |
| 204:TimeoutError | 28 |
| cn-block:TimeoutError | 18 |
| speed:ClientOSError | 14 |
| geo:ClientOSError | 14 |
| 204:ProxyError | 12 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:49596: bind: address already in use | 1 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4689 |
| ConnectionRefusedError | 779 |
| gaierror | 251 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | prefer | 219 | 0.986 | 344 |
| Au1rxx-base64 | 0.802 | prefer | 524 | 0.739 | 1604 |
| Surfboard-tg-mixed | 0.678 | observe | 115 | 0.6 | 5167 |
| DeltaKronecker-all | 0.48 | observe | 43 | 0.395 | 4549 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 5764 |
| xiaoji235-airport-v2ray-all | 0.329 | observe | 1 | 1.0 | 1861 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| chromego_merge | 0.258 | observe | 1 | 1.0 | 70 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 57 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3969 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | mheidari-all | 0.208 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.143 | 1 | 6 | 7 |
| DeltaKronecker-all | 0.395 | 17 | 26 | 43 |
| Surfboard-tg-mixed | 0.6 | 69 | 46 | 115 |
| Au1rxx-base64 | 0.739 | 387 | 137 | 524 |
| zhangkai | 0.986 | 216 | 3 | 219 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16553 | yes | 5.28 | 0 |
| SoliSpirit-all | 6688 | yes | 2.98 | 0 |
| Epodonios-all | 5764 | yes | 2.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 5486 | yes | 2.36 | 0 |
| Surfboard-tg-mixed | 5167 | yes | 3.39 | 0 |
| mahdibland-V2RayAggregator | 5071 | yes | 2.79 | 0 |
| DeltaKronecker-all | 4549 | yes | 4.18 | 0 |
| barry-far-vless | 4406 | yes | 1.89 | 0 |
| Surfboard-tg-vless | 3990 | yes | 3.11 | 0 |
| MatinGhanbari-all-sub | 3969 | yes | 2.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 81 |
| speed | 69 |
| 204 | 48 |
| cn-block | 25 |
| sing-box exited 1 | 1 |
