# AutoNodes 每日报告

生成时间：2026-09-25 17:05:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 97420 |
| 去重后节点数 | 26475 |
| TCP 可达数 | 3000 |
| 真测通过数 | 330 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26475 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| generate | 81.9 |
| geo | 1.5 |
| probe | 213.4 |
| real_test | 159.2 |
| tcp | 43.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 23 | 8 | 15 | 34.8% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 128 | 113 | 15 | 88.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 5 | 5 | 0 | 100.0% |
| vless | 295 | 189 | 106 | 64.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 44 |
| 204:TimeoutError | 25 |
| 204:ProxyError | 21 |
| cn-block:TimeoutError | 21 |
| 204:ProxyConnectionError | 10 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 4 |
| 204:ClientOSError | 2 |
| speed:ClientOSError | 2 |
| geo:ClientOSError | 1 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5582 |
| ConnectionRefusedError | 965 |
| gaierror | 431 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.945 | prefer | 258 | 0.88 | 1699 |
| Surfboard-tg-mixed | 0.729 | prefer | 35 | 0.657 | 7258 |
| mheidari-all | 0.557 | observe | 147 | 0.476 | 22782 |
| ermaozi | 0.386 | observe | 18 | 0.389 | 304 |
| DeltaKronecker-all | 0.32 | observe | 4 | 0.5 | 5452 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 67 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5293 |
| Epodonios-all | 0.255 | observe | 0 | None | 7757 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9237 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 4 | 4 |
| ermaozi | 0.389 | 7 | 11 | 18 |
| mheidari-all | 0.476 | 70 | 77 | 147 |
| DeltaKronecker-all | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.657 | 23 | 12 | 35 |
| Au1rxx-base64 | 0.88 | 227 | 31 | 258 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22782 | yes | 6.08 | 0 |
| SoliSpirit-all | 9237 | yes | 4.87 | 0 |
| Epodonios-all | 7757 | yes | 3.45 | 0 |
| Surfboard-tg-mixed | 7258 | yes | 4.13 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.01 | 0 |
| barry-far-vless | 6083 | yes | 2.31 | 0 |
| Surfboard-tg-vless | 5857 | yes | 3.85 | 0 |
| DeltaKronecker-all | 5452 | yes | 5.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 5293 | yes | 1.27 | 0 |
| mahdibland-V2RayAggregator | 4324 | yes | 1.89 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 65 |
| 204 | 58 |
| speed | 10 |
| geo | 6 |
