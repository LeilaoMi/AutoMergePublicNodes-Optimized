# AutoNodes 每日报告

生成时间：2026-08-19 01:43:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 82111 |
| 去重后节点数 | 22333 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1440 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22333 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 27.2 |
| geo | 0.6 |
| probe | 76.9 |
| real_test | 248.3 |
| tcp | 33.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 158 | 153 | 5 | 96.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 889 | 874 | 15 | 98.3% |
| vless | 382 | 261 | 121 | 68.3% |
| vmess | 4 | 3 | 1 | 75.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 64 |
| speed:TimeoutError | 24 |
| geo:ClientOSError | 23 |
| speed:ClientOSError | 13 |
| cn-block:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| 204:TimeoutError | 3 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4149 |
| ConnectionRefusedError | 898 |
| gaierror | 388 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 817 | 0.991 | 1745 |
| mheidari-all | 1.0 | prefer | 265 | 0.936 | 16675 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.889 | prefer | 296 | 0.811 | 6344 |
| nscl5-all | 0.519 | observe | 5 | 1.0 | 3330 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5068 |
| Epodonios-all | 0.255 | observe | 0 | None | 6993 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7254 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.217 | 71 | 0.127 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.127 | 9 | 62 | 71 |
| Surfboard-tg-mixed | 0.811 | 240 | 56 | 296 |
| mheidari-all | 0.936 | 248 | 17 | 265 |
| Au1rxx-base64 | 0.991 | 810 | 7 | 817 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 5 | 0 | 5 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16675 | yes | 4.4 | 0 |
| SoliSpirit-all | 7254 | yes | 3.31 | 0 |
| Epodonios-all | 6993 | yes | 2.89 | 0 |
| Surfboard-tg-mixed | 6344 | yes | 3.75 | 0 |
| DeltaKronecker-all | 5725 | yes | 4.95 | 0 |
| barry-far-vless | 5142 | yes | 2.53 | 0 |
| 10ium-ScrapeCategorize-Vless | 5068 | yes | 2.11 | 0 |
| Surfboard-tg-vless | 4847 | yes | 3.25 | 0 |
| mahdibland-V2RayAggregator | 4035 | yes | 1.51 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 1.9 | 0 |

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
| geo | 87 |
| speed | 38 |
| cn-block | 10 |
| 204 | 9 |
