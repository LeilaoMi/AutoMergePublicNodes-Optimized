# AutoNodes 每日报告

生成时间：2026-07-07 20:07:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 84823 |
| 去重后节点数 | 24903 |
| TCP 可达数 | 3000 |
| 真测通过数 | 209 |
| verified 输出数 | 209 |
| global 输出数 | 217 |
| all 输出数 | 24903 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 41.2 |
| geo | 1.3 |
| probe | 45.3 |
| real_test | 65.3 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 4 | 1 | 80.0% |
| shadowsocks | 111 | 87 | 24 | 78.4% |
| socks | 8 | 7 | 1 | 87.5% |
| trojan | 122 | 65 | 57 | 53.3% |
| vless | 34 | 4 | 30 | 11.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 28 |
| 204:TimeoutError | 21 |
| geo:TimeoutError | 14 |
| speed:ClientOSError | 8 |
| 204:ClientOSError | 8 |
| cn-block:TimeoutError | 7 |
| geo:ClientOSError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 5 |
| geo:ProxyError | 5 |
| speed:ProxyError | 3 |
| speed:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4517 |
| ConnectionRefusedError | 829 |
| gaierror | 201 |
| OSError | 167 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.844 | prefer | 48 | 0.854 | 104 |
| mheidari-all | 0.655 | observe | 71 | 0.577 | 18207 |
| Surfboard-tg-mixed | 0.646 | observe | 74 | 0.568 | 6066 |
| DeltaKronecker-all | 0.597 | observe | 87 | 0.517 | 8472 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 3626 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 170 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4700 |
| Epodonios-all | 0.255 | observe | 0 | None | 7120 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.517 | 45 | 42 | 87 |
| Surfboard-tg-mixed | 0.568 | 42 | 32 | 74 |
| mheidari-all | 0.577 | 41 | 30 | 71 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.854 | 41 | 7 | 48 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18207 | yes | 3.11 | 0 |
| DeltaKronecker-all | 8472 | yes | 3.52 | 0 |
| Epodonios-all | 7120 | yes | 0.83 | 0 |
| SoliSpirit-all | 7035 | yes | 2.68 | 0 |
| Surfboard-tg-mixed | 6066 | yes | 1.71 | 0 |
| mahdibland-V2RayAggregator | 5339 | yes | 0.91 | 0 |
| barry-far-vless | 5281 | yes | 0.86 | 0 |
| 10ium-ScrapeCategorize-Vless | 4700 | yes | 1.43 | 0 |
| Surfboard-tg-vless | 4596 | yes | 2.42 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 57 |
| geo | 25 |
| cn-block | 18 |
| speed | 13 |
