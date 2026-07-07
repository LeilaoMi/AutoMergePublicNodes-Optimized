# AutoNodes 每日报告

生成时间：2026-07-07 14:53:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 85387 |
| 去重后节点数 | 24893 |
| TCP 可达数 | 3000 |
| 真测通过数 | 284 |
| verified 输出数 | 284 |
| global 输出数 | 293 |
| all 输出数 | 24893 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| generate | 43.5 |
| geo | 1.4 |
| probe | 42.5 |
| real_test | 73.3 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 120 | 99 | 21 | 82.5% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 167 | 121 | 46 | 72.5% |
| vless | 39 | 13 | 26 | 33.3% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 17 |
| geo:ClientOSError | 13 |
| speed:ClientOSError | 10 |
| 204:ClientOSError | 9 |
| cn-block:TimeoutError | 8 |
| 204:TimeoutError | 7 |
| geo:TimeoutError | 7 |
| speed:ProxyError | 6 |
| geo:ProxyError | 5 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4635 |
| ConnectionRefusedError | 828 |
| OSError | 168 |
| gaierror | 111 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.807 | prefer | 108 | 0.731 | 8472 |
| Au1rxx-base64 | 0.799 | prefer | 66 | 0.803 | 123 |
| Surfboard-tg-mixed | 0.772 | prefer | 89 | 0.697 | 6181 |
| mheidari-all | 0.755 | prefer | 75 | 0.68 | 18192 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3626 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4700 |
| Epodonios-all | 0.255 | observe | 0 | None | 7142 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3965 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.68 | 51 | 24 | 75 |
| Surfboard-tg-mixed | 0.697 | 62 | 27 | 89 |
| DeltaKronecker-all | 0.731 | 79 | 29 | 108 |
| Au1rxx-base64 | 0.803 | 53 | 13 | 66 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18192 | yes | 4.08 | 0 |
| DeltaKronecker-all | 8472 | yes | 4.32 | 0 |
| SoliSpirit-all | 7271 | yes | 2.31 | 0 |
| Epodonios-all | 7142 | yes | 1.1 | 0 |
| Surfboard-tg-mixed | 6181 | yes | 3.56 | 0 |
| barry-far-vless | 5363 | yes | 2.74 | 0 |
| mahdibland-V2RayAggregator | 5338 | yes | 2.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 4700 | yes | 2.55 | 0 |
| Surfboard-tg-vless | 4677 | yes | 2.45 | 0 |
| MatinGhanbari-all-sub | 3965 | yes | 2.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 33 |
| geo | 25 |
| speed | 20 |
| cn-block | 16 |
