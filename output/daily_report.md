# AutoNodes 每日报告

生成时间：2026-07-04 08:48:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78924 |
| 去重后节点数 | 23515 |
| TCP 可达数 | 3000 |
| 真测通过数 | 350 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23515 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 29.7 |
| geo | 1.4 |
| probe | 44.8 |
| real_test | 88.5 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 120 | 103 | 17 | 85.8% |
| socks | 22 | 19 | 3 | 86.4% |
| trojan | 224 | 171 | 53 | 76.3% |
| vless | 58 | 13 | 45 | 22.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 36 |
| geo:TimeoutError | 17 |
| 204:ClientOSError | 14 |
| speed:ClientOSError | 11 |
| speed:ProxyError | 8 |
| cn-block:ClientOSError | 7 |
| cn-block:ProxyError | 6 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 4 |
| geo:ClientOSError | 4 |
| geo:ProxyError | 3 |
| speed:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4474 |
| ConnectionRefusedError | 659 |
| OSError | 152 |
| gaierror | 70 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.836 | prefer | 22 | 0.864 | 77 |
| Surfboard-tg-mixed | 0.83 | prefer | 114 | 0.754 | 6152 |
| DeltaKronecker-all | 0.804 | prefer | 201 | 0.726 | 7309 |
| mheidari-all | 0.747 | prefer | 88 | 0.67 | 16136 |
| nscl5-all | 0.359 | observe | 2 | 1.0 | 1189 |
| Surfboard-tg-vless | 0.335 | observe | 1 | 1.0 | 4573 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 7154 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.67 | 59 | 29 | 88 |
| DeltaKronecker-all | 0.726 | 146 | 55 | 201 |
| Surfboard-tg-mixed | 0.754 | 86 | 28 | 114 |
| Au1rxx-base64 | 0.864 | 19 | 3 | 22 |
| Surfboard-tg-vless | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16136 | yes | 3.18 | 0 |
| DeltaKronecker-all | 7309 | yes | 4.07 | 0 |
| Epodonios-all | 7154 | yes | 3.7 | 0 |
| SoliSpirit-all | 7126 | yes | 2.28 | 0 |
| Surfboard-tg-mixed | 6152 | yes | 2.52 | 0 |
| mahdibland-V2RayAggregator | 5333 | yes | 1.58 | 0 |
| barry-far-vless | 5278 | yes | 0.97 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 0.79 | 0 |
| Surfboard-tg-vless | 4573 | yes | 2.68 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 1.07 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 56 |
| geo | 24 |
| speed | 21 |
| cn-block | 17 |
