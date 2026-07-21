# AutoNodes 每日报告

生成时间：2026-07-21 19:43:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 82288 |
| 去重后节点数 | 22983 |
| TCP 可达数 | 3000 |
| 真测通过数 | 533 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22983 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 41.4 |
| geo | 1.0 |
| probe | 58.4 |
| real_test | 140.9 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 35 | 1 | 97.2% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 130 | 99 | 31 | 76.2% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 375 | 332 | 43 | 88.5% |
| vless | 284 | 61 | 223 | 21.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 99 |
| geo:TimeoutError | 95 |
| cn-block:TimeoutError | 41 |
| 204:TimeoutError | 19 |
| 204:ProxyError | 15 |
| geo:ClientOSError | 10 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| speed:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4199 |
| ConnectionRefusedError | 682 |
| gaierror | 327 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | prefer | 36 | 0.972 | 61 |
| Au1rxx-base64 | 0.833 | prefer | 193 | 0.819 | 432 |
| mheidari-all | 0.684 | observe | 364 | 0.604 | 19482 |
| Surfboard-tg-mixed | 0.613 | observe | 210 | 0.533 | 5357 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4304 |
| DeltaKronecker-all | 0.302 | observe | 25 | 0.2 | 5415 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4482 |
| Epodonios-all | 0.255 | observe | 0 | None | 6463 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 6 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.2 | 5 | 20 | 25 |
| Surfboard-tg-mixed | 0.533 | 112 | 98 | 210 |
| mheidari-all | 0.604 | 220 | 144 | 364 |
| Au1rxx-base64 | 0.819 | 158 | 35 | 193 |
| zhangkai | 0.972 | 35 | 1 | 36 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19482 | yes | 3.62 | 0 |
| SoliSpirit-all | 6710 | yes | 3.11 | 0 |
| Epodonios-all | 6463 | yes | 4.14 | 0 |
| DeltaKronecker-all | 5415 | yes | 4.17 | 0 |
| Surfboard-tg-mixed | 5357 | yes | 2.02 | 0 |
| mahdibland-V2RayAggregator | 5204 | yes | 2.11 | 0 |
| barry-far-vless | 4788 | yes | 1.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4482 | yes | 1.82 | 0 |
| xiaoji235-airport-v2ray-all | 4304 | yes | 1.41 | 0 |
| Surfboard-tg-vless | 4158 | yes | 2.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 105 |
| speed | 102 |
| cn-block | 53 |
| 204 | 38 |
