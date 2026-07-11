# AutoNodes 每日报告

生成时间：2026-07-11 19:15:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75703 |
| 去重后节点数 | 24094 |
| TCP 可达数 | 3000 |
| 真测通过数 | 280 |
| verified 输出数 | 280 |
| global 输出数 | 296 |
| all 输出数 | 24094 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 36.3 |
| geo | 1.4 |
| probe | 51.5 |
| real_test | 76.7 |
| tcp | 31.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 1 | 1 | 0 | 100.0% |
| shadowsocks | 112 | 90 | 22 | 80.4% |
| socks | 8 | 4 | 4 | 50.0% |
| trojan | 154 | 82 | 72 | 53.2% |
| vless | 169 | 61 | 108 | 36.1% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 76 |
| 204:ProxyError | 32 |
| 204:TimeoutError | 24 |
| cn-block:ClientOSError | 16 |
| geo:TimeoutError | 15 |
| cn-block:ProxyError | 13 |
| geo:ClientOSError | 7 |
| speed:ProxyError | 6 |
| 204:ClientOSError | 5 |
| cn-block:TimeoutError | 5 |
| geo:ProxyError | 4 |
| speed:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4245 |
| ConnectionRefusedError | 667 |
| gaierror | 239 |
| OSError | 190 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.89 | prefer | 33 | 0.909 | 96 |
| mheidari-all | 0.739 | prefer | 80 | 0.662 | 16311 |
| Surfboard-tg-mixed | 0.58 | observe | 234 | 0.5 | 5315 |
| DeltaKronecker-all | 0.5 | observe | 98 | 0.418 | 7969 |
| nscl5-all | 0.36 | observe | 2 | 1.0 | 1207 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3953 |
| Epodonios-all | 0.255 | observe | 0 | None | 6185 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6553 |

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
| DeltaKronecker-all | 0.418 | 41 | 57 | 98 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.5 | 117 | 117 | 234 |
| mheidari-all | 0.662 | 53 | 27 | 80 |
| Au1rxx-base64 | 0.909 | 30 | 3 | 33 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16311 | yes | 3.29 | 0 |
| DeltaKronecker-all | 7969 | yes | 3.23 | 0 |
| SoliSpirit-all | 6553 | yes | 2.27 | 0 |
| Epodonios-all | 6185 | yes | 1.48 | 0 |
| mahdibland-V2RayAggregator | 5416 | yes | 0.69 | 0 |
| Surfboard-tg-mixed | 5315 | yes | 2.11 | 0 |
| barry-far-vless | 4681 | yes | 1.53 | 0 |
| Surfboard-tg-vless | 4082 | yes | 2.25 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.36 | 0 |
| 10ium-ScrapeCategorize-Vless | 3953 | yes | 1.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 85 |
| 204 | 61 |
| cn-block | 34 |
| geo | 26 |
