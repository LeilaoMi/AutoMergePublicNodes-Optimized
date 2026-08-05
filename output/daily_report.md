# AutoNodes 每日报告

生成时间：2026-08-05 19:47:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 87804 |
| 去重后节点数 | 24105 |
| TCP 可达数 | 3000 |
| 真测通过数 | 449 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24105 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 29.0 |
| geo | 1.2 |
| probe | 49.6 |
| real_test | 99.5 |
| tcp | 36.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 21 | 17 | 4 | 81.0% |
| shadowsocks | 140 | 124 | 16 | 88.6% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 163 | 158 | 5 | 96.9% |
| vless | 189 | 127 | 62 | 67.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 25 |
| 204:TimeoutError | 19 |
| geo:ClientOSError | 14 |
| 204:ProxyError | 8 |
| cn-block:TimeoutError | 7 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 1 |
| speed:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4748 |
| ConnectionRefusedError | 815 |
| gaierror | 328 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.981 | prefer | 401 | 0.92 | 1563 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.607 | observe | 89 | 0.528 | 5930 |
| mheidari-all | 0.46 | observe | 17 | 0.412 | 20396 |
| DeltaKronecker-all | 0.43 | observe | 9 | 0.556 | 5316 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5260 |
| Epodonios-all | 0.255 | observe | 0 | None | 6540 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7160 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.412 | 7 | 10 | 17 |
| Surfboard-tg-mixed | 0.528 | 47 | 42 | 89 |
| DeltaKronecker-all | 0.556 | 5 | 4 | 9 |
| Au1rxx-base64 | 0.92 | 369 | 32 | 401 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20396 | yes | 5.23 | 0 |
| SoliSpirit-all | 7160 | yes | 3.1 | 0 |
| Epodonios-all | 6540 | yes | 4.63 | 0 |
| Surfboard-tg-mixed | 5930 | yes | 3.01 | 0 |
| DeltaKronecker-all | 5316 | yes | 5.14 | 0 |
| 10ium-ScrapeCategorize-Vless | 5260 | yes | 2.19 | 0 |
| mahdibland-V2RayAggregator | 5206 | yes | 2.41 | 0 |
| barry-far-vless | 5072 | yes | 1.88 | 0 |
| Surfboard-tg-vless | 4758 | yes | 2.61 | 0 |
| xiaoji235-airport-v2ray-all | 4655 | yes | 2.79 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 39 |
| 204 | 32 |
| cn-block | 11 |
| speed | 8 |
