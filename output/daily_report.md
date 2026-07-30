# AutoNodes 每日报告

生成时间：2026-07-30 08:41:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78173 |
| 去重后节点数 | 22773 |
| TCP 可达数 | 3000 |
| 真测通过数 | 507 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22773 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 36.0 |
| geo | 1.3 |
| probe | 55.3 |
| real_test | 143.7 |
| tcp | 31.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 118 | 118 | 0 | 100.0% |
| hysteria2 | 16 | 12 | 4 | 75.0% |
| shadowsocks | 218 | 179 | 39 | 82.1% |
| socks | 8 | 6 | 2 | 75.0% |
| trojan | 72 | 62 | 10 | 86.1% |
| vless | 267 | 129 | 138 | 48.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 66 |
| cn-block:TimeoutError | 29 |
| 204:TimeoutError | 23 |
| speed:TimeoutError | 21 |
| speed:ClientOSError | 17 |
| 204:ProxyError | 12 |
| geo:ClientOSError | 10 |
| 204:ClientOSError | 7 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4312 |
| ConnectionRefusedError | 713 |
| gaierror | 302 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.998 | prefer | 118 | 1.0 | 157 |
| Au1rxx-base64 | 0.88 | prefer | 266 | 0.835 | 1201 |
| Surfboard-tg-mixed | 0.645 | observe | 168 | 0.565 | 5473 |
| DeltaKronecker-all | 0.637 | observe | 95 | 0.558 | 5759 |
| mheidari-all | 0.455 | observe | 46 | 0.37 | 16105 |
| xiaoji235-airport-v2ray-all | 0.329 | observe | 1 | 1.0 | 1861 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5342 |
| Epodonios-all | 0.255 | observe | 0 | None | 6219 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.37 | 17 | 29 | 46 |
| DeltaKronecker-all | 0.558 | 53 | 42 | 95 |
| Surfboard-tg-mixed | 0.565 | 95 | 73 | 168 |
| Au1rxx-base64 | 0.835 | 222 | 44 | 266 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 118 | 0 | 118 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16105 | yes | 4.32 | 0 |
| SoliSpirit-all | 6833 | yes | 2.61 | 0 |
| Epodonios-all | 6219 | yes | 2.5 | 0 |
| DeltaKronecker-all | 5759 | yes | 5.35 | 0 |
| Surfboard-tg-mixed | 5473 | yes | 3.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 5342 | yes | 1.77 | 0 |
| mahdibland-V2RayAggregator | 5029 | yes | 2.34 | 0 |
| barry-far-vless | 4657 | yes | 1.52 | 0 |
| Surfboard-tg-vless | 4282 | yes | 3.21 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.35 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 77 |
| 204 | 42 |
| speed | 38 |
| cn-block | 36 |
