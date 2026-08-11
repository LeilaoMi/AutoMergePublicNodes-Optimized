# AutoNodes 每日报告

生成时间：2026-08-11 02:10:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 85365 |
| 去重后节点数 | 24753 |
| TCP 可达数 | 3000 |
| 真测通过数 | 635 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24753 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 37.0 |
| geo | 1.4 |
| probe | 60.3 |
| real_test | 165.2 |
| tcp | 37.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 49 | 49 | 0 | 100.0% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 166 | 157 | 9 | 94.6% |
| socks | 12 | 10 | 2 | 83.3% |
| trojan | 129 | 118 | 11 | 91.5% |
| tuic | 1 | 1 | 0 | 100.0% |
| vless | 698 | 282 | 416 | 40.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 176 |
| speed:TimeoutError | 86 |
| geo:ClientOSError | 80 |
| speed:ClientOSError | 43 |
| cn-block:TimeoutError | 19 |
| 204:ProxyError | 13 |
| 204:TimeoutError | 12 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4849 |
| ConnectionRefusedError | 829 |
| gaierror | 320 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.983 | prefer | 49 | 1.0 | 67 |
| Au1rxx-base64 | 0.938 | prefer | 404 | 0.881 | 1463 |
| Surfboard-tg-mixed | 0.713 | prefer | 28 | 0.643 | 6329 |
| mheidari-all | 0.459 | observe | 534 | 0.378 | 20211 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 6946 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7525 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.152 | observe | 4 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.25 | 51 | 0.157 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.157 | 8 | 43 | 51 |
| mheidari-all | 0.378 | 202 | 332 | 534 |
| Surfboard-tg-mixed | 0.643 | 18 | 10 | 28 |
| Au1rxx-base64 | 0.881 | 356 | 48 | 404 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 49 | 0 | 49 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20211 | yes | 4.31 | 0 |
| SoliSpirit-all | 7525 | yes | 1.8 | 0 |
| Epodonios-all | 6946 | yes | 2.38 | 0 |
| Surfboard-tg-mixed | 6329 | yes | 3.42 | 0 |
| DeltaKronecker-all | 5881 | yes | 4.38 | 0 |
| barry-far-vless | 5506 | yes | 1.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 0.89 | 0 |
| mahdibland-V2RayAggregator | 5191 | yes | 2.53 | 0 |
| Surfboard-tg-vless | 5163 | yes | 2.99 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 256 |
| speed | 130 |
| 204 | 29 |
| cn-block | 23 |
