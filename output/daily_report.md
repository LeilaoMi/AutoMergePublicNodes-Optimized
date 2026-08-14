# AutoNodes 每日报告

生成时间：2026-08-14 02:28:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 79423 |
| 去重后节点数 | 21338 |
| TCP 可达数 | 3000 |
| 真测通过数 | 997 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21338 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 34.7 |
| geo | 1.0 |
| probe | 63.4 |
| real_test | 204.8 |
| tcp | 33.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 17 | 15 | 2 | 88.2% |
| shadowsocks | 166 | 154 | 12 | 92.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 386 | 377 | 9 | 97.7% |
| vless | 508 | 321 | 187 | 63.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 68 |
| cn-block:TimeoutError | 39 |
| speed:TimeoutError | 39 |
| geo:ClientOSError | 20 |
| speed:ClientOSError | 18 |
| 204:TimeoutError | 10 |
| 204:ProxyError | 7 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4288 |
| ConnectionRefusedError | 777 |
| gaierror | 295 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 711 | 0.948 | 1965 |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.772 | prefer | 170 | 0.694 | 5918 |
| DeltaKronecker-all | 0.671 | observe | 15 | 0.733 | 3656 |
| mheidari-all | 0.443 | observe | 169 | 0.361 | 16929 |
| 10ium-ScrapeCategorize-Vless | 0.373 | observe | 5 | 0.6 | 5203 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6600 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7655 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | nscl5-all | 0.207 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.167 | 1 | 5 | 6 |
| mheidari-all | 0.361 | 61 | 108 | 169 |
| 10ium-ScrapeCategorize-Vless | 0.6 | 3 | 2 | 5 |
| Surfboard-tg-mixed | 0.694 | 118 | 52 | 170 |
| DeltaKronecker-all | 0.733 | 11 | 4 | 15 |
| Au1rxx-base64 | 0.948 | 674 | 37 | 711 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16929 | yes | 3.9 | 0 |
| SoliSpirit-all | 7655 | yes | 3.57 | 0 |
| Epodonios-all | 6600 | yes | 4.61 | 0 |
| Surfboard-tg-mixed | 5918 | yes | 3.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 5203 | yes | 2.36 | 0 |
| mahdibland-V2RayAggregator | 5197 | yes | 2.79 | 0 |
| barry-far-vless | 5003 | yes | 2.16 | 0 |
| Surfboard-tg-vless | 4638 | yes | 4.04 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.66 | 0 |
| DeltaKronecker-all | 3656 | yes | 4.01 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 88 |
| speed | 58 |
| cn-block | 44 |
| 204 | 21 |
