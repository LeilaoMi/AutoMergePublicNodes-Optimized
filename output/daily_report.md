# AutoNodes 每日报告

生成时间：2026-06-22 21:00:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78026 |
| 去重后节点数 | 22898 |
| TCP 可达数 | 3000 |
| 真测通过数 | 723 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22898 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 30.6 |
| geo | 1.3 |
| probe | 58.1 |
| real_test | 147.7 |
| tcp | 31.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 58 | 58 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 72 | 67 | 5 | 93.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 59 | 41 | 18 | 69.5% |
| vless | 727 | 549 | 178 | 75.5% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 85 |
| 204:TimeoutError | 32 |
| cn-block:TimeoutError | 18 |
| geo:ClientOSError | 12 |
| geo:TimeoutError | 11 |
| speed:TimeoutError | 11 |
| 204:ProxyError | 9 |
| 204:ClientOSError | 7 |
| geo:ProxyError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| speed:ProxyError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4425 |
| ConnectionRefusedError | 596 |
| gaierror | 166 |
| OSError | 106 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.987 | prefer | 58 | 1.0 | 95 |
| mheidari-all | 0.919 | prefer | 345 | 0.841 | 15541 |
| Au1rxx-base64 | 0.862 | prefer | 102 | 0.863 | 150 |
| DeltaKronecker-all | 0.762 | prefer | 413 | 0.683 | 7452 |
| Surfboard-tg-mixed | 0.4 | observe | 4 | 0.75 | 5285 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4466 |
| Epodonios-all | 0.255 | observe | 0 | None | 8275 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3980 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7495 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.683 | 282 | 131 | 413 |
| Surfboard-tg-mixed | 0.75 | 3 | 1 | 4 |
| mheidari-all | 0.841 | 290 | 55 | 345 |
| Au1rxx-base64 | 0.863 | 88 | 14 | 102 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 58 | 0 | 58 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15541 | yes | 3.42 | 0 |
| Epodonios-all | 8275 | yes | 2.53 | 0 |
| SoliSpirit-all | 7495 | yes | 2.18 | 0 |
| DeltaKronecker-all | 7452 | yes | 3.82 | 0 |
| Surfboard-tg-mixed | 5285 | yes | 1.97 | 0 |
| barry-far-vless | 5141 | yes | 1.18 | 0 |
| mahdibland-V2RayAggregator | 4547 | yes | 1.62 | 0 |
| 10ium-ScrapeCategorize-Vless | 4466 | yes | 1.45 | 0 |
| Surfboard-tg-vless | 4112 | yes | 2.11 | 0 |
| MatinGhanbari-all-sub | 3980 | yes | 1.27 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 100 |
| 204 | 48 |
| geo | 27 |
| cn-block | 26 |
