# AutoNodes 每日报告

生成时间：2026-08-20 18:53:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 95001 |
| 去重后节点数 | 25247 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1089 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25247 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 31.1 |
| geo | 0.9 |
| probe | 67.0 |
| real_test | 194.9 |
| tcp | 40.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 111 | 111 | 0 | 100.0% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 172 | 161 | 11 | 93.6% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 591 | 587 | 4 | 99.3% |
| vless | 287 | 217 | 70 | 75.6% |
| vmess | 3 | 1 | 2 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 19 |
| 204:TimeoutError | 18 |
| geo:TimeoutError | 16 |
| geo:ClientOSError | 11 |
| 204:ProxyError | 6 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| speed:ClientOSError | 4 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5645 |
| ConnectionRefusedError | 958 |
| gaierror | 404 |
| OSError | 224 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 571 | 0.953 | 1789 |
| mheidari-all | 1.0 | prefer | 251 | 0.936 | 22064 |
| zhangkai | 0.988 | prefer | 112 | 0.991 | 144 |
| Surfboard-tg-mixed | 0.911 | prefer | 234 | 0.833 | 6440 |
| DeltaKronecker-all | 0.372 | observe | 9 | 0.444 | 6781 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4958 |
| Epodonios-all | 0.255 | observe | 0 | None | 7181 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7349 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5117 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.444 | 4 | 5 | 9 |
| Surfboard-tg-mixed | 0.833 | 195 | 39 | 234 |
| mheidari-all | 0.936 | 235 | 16 | 251 |
| Au1rxx-base64 | 0.953 | 544 | 27 | 571 |
| zhangkai | 0.991 | 111 | 1 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22064 | yes | 4.09 | 0 |
| SoliSpirit-all | 7349 | yes | 2.37 | 0 |
| Epodonios-all | 7181 | yes | 4.26 | 0 |
| DeltaKronecker-all | 6781 | yes | 4.54 | 0 |
| Surfboard-tg-mixed | 6440 | yes | 3.02 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.27 | 0 |
| barry-far-vless | 5501 | yes | 1.42 | 0 |
| Surfboard-tg-vless | 5117 | yes | 2.6 | 0 |
| 10ium-ScrapeCategorize-Vless | 4958 | yes | 0.68 | 0 |
| mahdibland-V2RayAggregator | 4586 | yes | 2.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 28 |
| geo | 27 |
| cn-block | 25 |
| speed | 10 |
