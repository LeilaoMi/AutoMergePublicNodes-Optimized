# AutoNodes 每日报告

生成时间：2026-08-21 01:47:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 95323 |
| 去重后节点数 | 25209 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1206 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25209 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 36.2 |
| geo | 1.2 |
| probe | 73.9 |
| real_test | 233.3 |
| tcp | 40.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 110 | 110 | 0 | 100.0% |
| hysteria2 | 32 | 32 | 0 | 100.0% |
| shadowsocks | 195 | 192 | 3 | 98.5% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 621 | 606 | 15 | 97.6% |
| vless | 619 | 259 | 360 | 41.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 140 |
| geo:ClientOSError | 112 |
| speed:TimeoutError | 72 |
| speed:ClientOSError | 24 |
| cn-block:TimeoutError | 13 |
| cn-block:ClientOSError | 5 |
| 204:TimeoutError | 4 |
| 204:ProxyError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5153 |
| ConnectionRefusedError | 958 |
| gaierror | 531 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 555 | 0.995 | 1663 |
| zhangkai | 0.997 | prefer | 111 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.965 | prefer | 59 | 0.898 | 6412 |
| mheidari-all | 0.686 | observe | 792 | 0.606 | 21987 |
| nscl5-all | 0.349 | observe | 3 | 0.667 | 3031 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4958 |
| Epodonios-all | 0.255 | observe | 0 | None | 7184 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7304 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.207 | 61 | 0.115 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.115 | 7 | 54 | 61 |
| mheidari-all | 0.606 | 480 | 312 | 792 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.898 | 53 | 6 | 59 |
| Au1rxx-base64 | 0.995 | 552 | 3 | 555 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 111 | 0 | 111 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21987 | yes | 8.76 | 0 |
| SoliSpirit-all | 7304 | yes | 3.65 | 0 |
| Epodonios-all | 7184 | yes | 3.82 | 0 |
| DeltaKronecker-all | 6781 | yes | 4.21 | 0 |
| Surfboard-tg-mixed | 6412 | yes | 3.06 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.35 | 0 |
| barry-far-vless | 5451 | yes | 2.18 | 0 |
| Surfboard-tg-vless | 5053 | yes | 3.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 4958 | yes | 2.46 | 0 |
| mahdibland-V2RayAggregator | 4586 | yes | 0.82 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 252 |
| speed | 96 |
| cn-block | 19 |
| 204 | 12 |
