# AutoNodes 每日报告

生成时间：2026-07-04 19:26:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78729 |
| 去重后节点数 | 23672 |
| TCP 可达数 | 3000 |
| 真测通过数 | 202 |
| verified 输出数 | 202 |
| global 输出数 | 208 |
| all 输出数 | 23672 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 38.8 |
| geo | 1.4 |
| probe | 47.4 |
| real_test | 70.3 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 119 | 90 | 29 | 75.6% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 109 | 60 | 49 | 55.0% |
| vless | 29 | 4 | 25 | 13.8% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 30 |
| 204:ProxyError | 24 |
| 204:ClientOSError | 12 |
| geo:TimeoutError | 10 |
| cn-block:TimeoutError | 10 |
| speed:ClientOSError | 7 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 3 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4455 |
| ConnectionRefusedError | 690 |
| OSError | 152 |
| gaierror | 102 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.852 | prefer | 31 | 0.871 | 100 |
| Surfboard-tg-mixed | 0.697 | observe | 92 | 0.62 | 6107 |
| mheidari-all | 0.667 | observe | 61 | 0.59 | 16429 |
| DeltaKronecker-all | 0.604 | observe | 82 | 0.524 | 7309 |
| nscl5-all | 0.303 | observe | 1 | 1.0 | 1189 |
| tg-ConfigV2rayNG | 0.263 | observe | 1 | 1.0 | 200 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 6997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.524 | 43 | 39 | 82 |
| mheidari-all | 0.59 | 36 | 25 | 61 |
| Surfboard-tg-mixed | 0.62 | 57 | 35 | 92 |
| Au1rxx-base64 | 0.871 | 27 | 4 | 31 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-ConfigV2rayNG | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16429 | yes | 3.11 | 0 |
| DeltaKronecker-all | 7309 | yes | 3.21 | 0 |
| Epodonios-all | 7003 | yes | 1.63 | 0 |
| SoliSpirit-all | 6970 | yes | 2.14 | 0 |
| Surfboard-tg-mixed | 6107 | yes | 2.4 | 0 |
| mahdibland-V2RayAggregator | 5366 | yes | 1.71 | 0 |
| barry-far-vless | 5100 | yes | 2.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 0.68 | 0 |
| Surfboard-tg-vless | 4528 | yes | 2.15 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.0 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 66 |
| cn-block | 17 |
| geo | 14 |
| speed | 7 |
