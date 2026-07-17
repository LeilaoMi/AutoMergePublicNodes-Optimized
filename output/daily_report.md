# AutoNodes 每日报告

生成时间：2026-07-17 03:20:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79372 |
| 去重后节点数 | 24584 |
| TCP 可达数 | 3000 |
| 真测通过数 | 614 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24584 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 20.4 |
| geo | 1.1 |
| probe | 47.7 |
| real_test | 106.3 |
| tcp | 33.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 35 | 35 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 168 | 151 | 17 | 89.9% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 420 | 407 | 13 | 96.9% |
| vless | 119 | 14 | 105 | 11.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 48 |
| geo:TimeoutError | 39 |
| speed:TimeoutError | 13 |
| geo:ClientOSError | 12 |
| cn-block:TimeoutError | 11 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4410 |
| ConnectionRefusedError | 665 |
| gaierror | 297 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.975 | prefer | 35 | 1.0 | 61 |
| mheidari-all | 0.97 | prefer | 152 | 0.895 | 16574 |
| Surfboard-tg-mixed | 0.932 | prefer | 153 | 0.856 | 5396 |
| Au1rxx-base64 | 0.928 | prefer | 88 | 0.932 | 149 |
| DeltaKronecker-all | 0.796 | prefer | 318 | 0.717 | 8462 |
| xiaoji235-airport-v2ray-all | 0.322 | observe | 1 | 1.0 | 1680 |
| nscl5-all | 0.28 | observe | 2 | 0.5 | 1821 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4470 |
| Epodonios-all | 0.255 | observe | 0 | None | 6574 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.717 | 228 | 90 | 318 |
| Surfboard-tg-mixed | 0.856 | 131 | 22 | 153 |
| mheidari-all | 0.895 | 136 | 16 | 152 |
| Au1rxx-base64 | 0.932 | 82 | 6 | 88 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 35 | 0 | 35 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16574 | yes | 2.97 | 0 |
| DeltaKronecker-all | 8462 | yes | 3.38 | 0 |
| SoliSpirit-all | 6961 | yes | 1.86 | 0 |
| Epodonios-all | 6574 | yes | 1.74 | 0 |
| Surfboard-tg-mixed | 5396 | yes | 1.58 | 0 |
| mahdibland-V2RayAggregator | 5260 | yes | 0.22 | 0 |
| barry-far-vless | 4857 | yes | 1.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 4470 | yes | 1.07 | 0 |
| Surfboard-tg-vless | 4171 | yes | 2.0 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.9 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 61 |
| geo | 51 |
| cn-block | 15 |
| 204 | 10 |
