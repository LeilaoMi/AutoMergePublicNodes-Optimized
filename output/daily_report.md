# AutoNodes 每日报告

生成时间：2026-08-20 13:04:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 94317 |
| 去重后节点数 | 25202 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1105 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25202 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| generate | 38.5 |
| geo | 0.6 |
| probe | 62.8 |
| real_test | 211.9 |
| tcp | 37.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 111 | 111 | 0 | 100.0% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 88 | 83 | 5 | 94.3% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 654 | 645 | 9 | 98.6% |
| vless | 351 | 244 | 107 | 69.5% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 40 |
| geo:TimeoutError | 23 |
| 204:TimeoutError | 18 |
| cn-block:TimeoutError | 14 |
| speed:TimeoutError | 9 |
| cn-block:ClientOSError | 8 |
| speed:ClientOSError | 5 |
| 204:ProxyError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4466 |
| ConnectionRefusedError | 980 |
| gaierror | 750 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 565 | 0.973 | 1789 |
| zhangkai | 0.988 | prefer | 112 | 0.991 | 144 |
| Surfboard-tg-mixed | 0.957 | prefer | 79 | 0.886 | 6453 |
| mheidari-all | 0.871 | prefer | 471 | 0.792 | 21209 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 6781 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4958 |
| Epodonios-all | 0.255 | observe | 0 | None | 7150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7279 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5135 |

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
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.792 | 373 | 98 | 471 |
| Surfboard-tg-mixed | 0.886 | 70 | 9 | 79 |
| Au1rxx-base64 | 0.973 | 550 | 15 | 565 |
| zhangkai | 0.991 | 111 | 1 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21209 | yes | 5.02 | 0 |
| SoliSpirit-all | 7279 | yes | 2.61 | 0 |
| Epodonios-all | 7150 | yes | 5.5 | 0 |
| DeltaKronecker-all | 6781 | yes | 5.29 | 0 |
| Surfboard-tg-mixed | 6453 | yes | 3.5 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.22 | 0 |
| barry-far-vless | 5460 | yes | 1.41 | 0 |
| Surfboard-tg-vless | 5135 | yes | 3.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4958 | yes | 1.67 | 0 |
| mahdibland-V2RayAggregator | 4586 | yes | 2.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 63 |
| 204 | 24 |
| cn-block | 24 |
| speed | 14 |
