# AutoNodes 每日报告

生成时间：2026-08-09 02:10:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 82844 |
| 去重后节点数 | 23635 |
| TCP 可达数 | 3000 |
| 真测通过数 | 579 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23635 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 27.7 |
| geo | 1.4 |
| probe | 52.5 |
| real_test | 142.3 |
| tcp | 35.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 25 | 24 | 1 | 96.0% |
| shadowsocks | 160 | 150 | 10 | 93.8% |
| socks | 3 | 3 | 0 | 100.0% |
| trojan | 149 | 130 | 19 | 87.2% |
| vless | 433 | 249 | 184 | 57.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 69 |
| speed:TimeoutError | 41 |
| cn-block:TimeoutError | 29 |
| geo:ClientOSError | 26 |
| speed:ClientOSError | 18 |
| 204:TimeoutError | 16 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 2 |
| geo:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4938 |
| ConnectionRefusedError | 831 |
| gaierror | 320 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 357 | 0.952 | 1540 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.755 | prefer | 155 | 0.677 | 6454 |
| mheidari-all | 0.61 | observe | 200 | 0.53 | 17775 |
| tg-oneclickvpnkeys | 0.316 | observe | 2 | 1.0 | 123 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5450 |
| Epodonios-all | 0.255 | observe | 0 | None | 7127 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| DeltaKronecker-all | 0.168 | downweight | 55 | 0.073 | 0 | 5347 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.168 | 55 | 0.073 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.073 | 4 | 51 | 55 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.53 | 106 | 94 | 200 |
| Surfboard-tg-mixed | 0.677 | 105 | 50 | 155 |
| Au1rxx-base64 | 0.952 | 340 | 17 | 357 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17775 | yes | 4.1 | 0 |
| SoliSpirit-all | 7538 | yes | 2.51 | 0 |
| Epodonios-all | 7127 | yes | 1.54 | 0 |
| Surfboard-tg-mixed | 6454 | yes | 2.92 | 0 |
| barry-far-vless | 5532 | yes | 2.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 5450 | yes | 1.94 | 0 |
| DeltaKronecker-all | 5347 | yes | 4.18 | 0 |
| Surfboard-tg-vless | 5209 | yes | 2.65 | 0 |
| mahdibland-V2RayAggregator | 5127 | yes | 1.37 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 96 |
| speed | 59 |
| cn-block | 34 |
| 204 | 25 |
