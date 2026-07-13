# AutoNodes 每日报告

生成时间：2026-07-13 09:41:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 76766 |
| 去重后节点数 | 23821 |
| TCP 可达数 | 3000 |
| 真测通过数 | 288 |
| verified 输出数 | 288 |
| global 输出数 | 297 |
| all 输出数 | 23821 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 21.8 |
| geo | 1.4 |
| probe | 47.9 |
| real_test | 76.4 |
| tcp | 31.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 1 | 1 | 0 | 100.0% |
| shadowsocks | 85 | 66 | 19 | 77.6% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 209 | 164 | 45 | 78.5% |
| vless | 100 | 14 | 86 | 14.0% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 51 |
| speed:ClientOSError | 30 |
| 204:TimeoutError | 11 |
| geo:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 7 |
| cn-block:ProxyError | 6 |
| speed:ProxyError | 5 |
| geo:ProxyError | 5 |
| cn-block:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4383 |
| ConnectionRefusedError | 664 |
| gaierror | 272 |
| OSError | 191 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.815 | prefer | 66 | 0.742 | 16468 |
| DeltaKronecker-all | 0.688 | observe | 207 | 0.609 | 7926 |
| Surfboard-tg-mixed | 0.683 | observe | 114 | 0.605 | 5436 |
| Au1rxx-base64 | 0.413 | observe | 9 | 0.667 | 103 |
| xiaoji235-airport-v2ray-all | 0.321 | observe | 1 | 1.0 | 1647 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3897 |
| Epodonios-all | 0.255 | observe | 0 | None | 6476 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3979 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.152 | observe | 4 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| Surfboard-tg-mixed | 0.605 | 69 | 45 | 114 |
| DeltaKronecker-all | 0.609 | 126 | 81 | 207 |
| Au1rxx-base64 | 0.667 | 6 | 3 | 9 |
| mheidari-all | 0.742 | 49 | 17 | 66 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16468 | yes | 3.21 | 0 |
| DeltaKronecker-all | 7926 | yes | 3.48 | 0 |
| Epodonios-all | 6476 | yes | 1.58 | 0 |
| SoliSpirit-all | 6409 | yes | 2.01 | 0 |
| Surfboard-tg-mixed | 5436 | yes | 2.41 | 0 |
| mahdibland-V2RayAggregator | 5412 | yes | 1.66 | 0 |
| barry-far-vless | 4724 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4097 | yes | 2.54 | 0 |
| MatinGhanbari-all-sub | 3979 | yes | 1.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 3897 | yes | 1.41 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 65 |
| speed | 44 |
| 204 | 26 |
| cn-block | 16 |
