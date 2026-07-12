# AutoNodes 每日报告

生成时间：2026-07-12 08:29:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76269 |
| 去重后节点数 | 24037 |
| TCP 可达数 | 3000 |
| 真测通过数 | 408 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24037 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 34.7 |
| geo | 1.3 |
| probe | 46.3 |
| real_test | 94.1 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 1 | 1 | 0 | 100.0% |
| shadowsocks | 99 | 87 | 12 | 87.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 239 | 193 | 46 | 80.8% |
| vless | 237 | 84 | 153 | 35.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 83 |
| geo:TimeoutError | 45 |
| 204:ProxyError | 18 |
| geo:ClientOSError | 14 |
| cn-block:ClientOSError | 14 |
| 204:TimeoutError | 9 |
| speed:TimeoutError | 7 |
| cn-block:ProxyError | 6 |
| 204:ClientOSError | 6 |
| cn-block:TimeoutError | 5 |
| geo:ProxyError | 3 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4439 |
| ConnectionRefusedError | 643 |
| gaierror | 237 |
| OSError | 201 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.824 | prefer | 84 | 0.75 | 16299 |
| Au1rxx-base64 | 0.784 | prefer | 57 | 0.789 | 118 |
| DeltaKronecker-all | 0.716 | prefer | 185 | 0.638 | 8141 |
| Surfboard-tg-mixed | 0.65 | observe | 256 | 0.57 | 5318 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4003 |
| Epodonios-all | 0.255 | observe | 0 | None | 6278 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6422 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4019 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.57 | 146 | 110 | 256 |
| DeltaKronecker-all | 0.638 | 118 | 67 | 185 |
| mheidari-all | 0.75 | 63 | 21 | 84 |
| Au1rxx-base64 | 0.789 | 45 | 12 | 57 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16299 | yes | 3.55 | 0 |
| DeltaKronecker-all | 8141 | yes | 3.94 | 0 |
| SoliSpirit-all | 6422 | yes | 1.44 | 0 |
| Epodonios-all | 6278 | yes | 1.66 | 0 |
| mahdibland-V2RayAggregator | 5416 | yes | 0.81 | 0 |
| Surfboard-tg-mixed | 5318 | yes | 2.18 | 0 |
| barry-far-vless | 4645 | yes | 1.09 | 0 |
| Surfboard-tg-vless | 4019 | yes | 2.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 4003 | yes | 1.63 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 1.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 92 |
| geo | 62 |
| 204 | 33 |
| cn-block | 25 |
