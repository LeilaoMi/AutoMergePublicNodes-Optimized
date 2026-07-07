# AutoNodes 每日报告

生成时间：2026-07-07 09:55:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84945 |
| 去重后节点数 | 24815 |
| TCP 可达数 | 3000 |
| 真测通过数 | 326 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24815 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 22.4 |
| geo | 1.4 |
| probe | 49.4 |
| real_test | 88.9 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 4 | 1 | 80.0% |
| shadowsocks | 127 | 106 | 21 | 83.5% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 190 | 157 | 33 | 82.6% |
| vless | 93 | 14 | 79 | 15.1% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 63 |
| geo:TimeoutError | 20 |
| geo:ClientOSError | 11 |
| 204:ProxyError | 11 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 8 |
| geo:ProxyError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| speed:TimeoutError | 3 |
| cn-block:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4659 |
| ConnectionRefusedError | 819 |
| OSError | 168 |
| gaierror | 75 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.846 | prefer | 42 | 0.857 | 118 |
| mheidari-all | 0.812 | prefer | 95 | 0.737 | 18158 |
| Surfboard-tg-mixed | 0.781 | prefer | 125 | 0.704 | 6102 |
| DeltaKronecker-all | 0.664 | observe | 159 | 0.585 | 8472 |
| xiaoji235-airport-v2ray-all | 0.4 | observe | 4 | 0.75 | 3626 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4700 |
| Epodonios-all | 0.255 | observe | 0 | None | 7013 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7353 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.585 | 93 | 66 | 159 |
| Surfboard-tg-mixed | 0.704 | 88 | 37 | 125 |
| mheidari-all | 0.737 | 70 | 25 | 95 |
| xiaoji235-airport-v2ray-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.857 | 36 | 6 | 42 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18158 | yes | 4.04 | 0 |
| DeltaKronecker-all | 8472 | yes | 3.28 | 0 |
| SoliSpirit-all | 7353 | yes | 1.98 | 0 |
| Epodonios-all | 7013 | yes | 1.68 | 0 |
| Surfboard-tg-mixed | 6102 | yes | 1.93 | 0 |
| mahdibland-V2RayAggregator | 5338 | yes | 1.51 | 0 |
| barry-far-vless | 5256 | yes | 1.37 | 0 |
| 10ium-ScrapeCategorize-Vless | 4700 | yes | 1.13 | 0 |
| Surfboard-tg-vless | 4575 | yes | 2.63 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 1.21 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 66 |
| geo | 35 |
| 204 | 27 |
| cn-block | 9 |
