# AutoNodes 每日报告

生成时间：2026-07-31 19:47:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78935 |
| 去重后节点数 | 22858 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22858 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 42.6 |
| geo | 1.4 |
| probe | 62.7 |
| real_test | 138.3 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 80 | 80 | 0 | 100.0% |
| hysteria2 | 16 | 12 | 4 | 75.0% |
| shadowsocks | 129 | 103 | 26 | 79.8% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 38 | 25 | 13 | 65.8% |
| vless | 401 | 248 | 153 | 61.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 61 |
| 204:TimeoutError | 34 |
| speed:TimeoutError | 26 |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 20 |
| speed:ClientOSError | 15 |
| geo:ClientOSError | 9 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4640 |
| ConnectionRefusedError | 766 |
| gaierror | 257 |
| OSError | 223 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 80 | 1.0 | 110 |
| Au1rxx-base64 | 0.763 | prefer | 508 | 0.697 | 1685 |
| mheidari-all | 0.569 | observe | 43 | 0.488 | 16449 |
| DeltaKronecker-all | 0.447 | observe | 28 | 0.357 | 5144 |
| Surfboard-tg-mixed | 0.373 | observe | 5 | 0.6 | 5433 |
| xiaoji235-airport-v2ray-all | 0.329 | observe | 1 | 1.0 | 1861 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 51 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5507 |
| Epodonios-all | 0.255 | observe | 0 | None | 6115 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.357 | 10 | 18 | 28 |
| mheidari-all | 0.488 | 21 | 22 | 43 |
| Surfboard-tg-mixed | 0.6 | 3 | 2 | 5 |
| Au1rxx-base64 | 0.697 | 354 | 154 | 508 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 80 | 0 | 80 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16449 | yes | 4.88 | 0 |
| SoliSpirit-all | 6602 | yes | 4.19 | 0 |
| Epodonios-all | 6115 | yes | 5.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 5507 | yes | 3.44 | 0 |
| Surfboard-tg-mixed | 5433 | yes | 3.91 | 0 |
| DeltaKronecker-all | 5144 | yes | 5.27 | 0 |
| mahdibland-V2RayAggregator | 5081 | yes | 1.15 | 0 |
| barry-far-vless | 4677 | yes | 3.07 | 0 |
| Surfboard-tg-vless | 4317 | yes | 3.07 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 3.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 70 |
| 204 | 59 |
| speed | 41 |
| cn-block | 28 |
