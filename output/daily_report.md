# AutoNodes 每日报告

生成时间：2026-10-04 12:16:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 99561 |
| 去重后节点数 | 27370 |
| TCP 可达数 | 3000 |
| 真测通过数 | 406 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27370 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 152.3 |
| geo | 1.6 |
| probe | 231.7 |
| real_test | 191.5 |
| tcp | 47.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 3 | 0 | 100.0% |
| http | 24 | 23 | 1 | 95.8% |
| hysteria2 | 18 | 15 | 3 | 83.3% |
| shadowsocks | 147 | 133 | 14 | 90.5% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 79 | 72 | 7 | 91.1% |
| vless | 210 | 160 | 50 | 76.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 30 |
| 204:TimeoutError | 13 |
| geo:TimeoutError | 10 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| speed:TimeoutError | 5 |
| geo:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ClientOSError | 2 |
| 204:ProxyConnectionError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6590 |
| ConnectionRefusedError | 1103 |
| gaierror | 355 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.949 | prefer | 297 | 0.879 | 1816 |
| ermaozi | 0.949 | prefer | 24 | 0.958 | 646 |
| mheidari-all | 0.863 | prefer | 44 | 0.795 | 23332 |
| Surfboard-tg-mixed | 0.855 | prefer | 109 | 0.78 | 7269 |
| ermaozi-get_subscribe | 0.289 | observe | 3 | 0.667 | 505 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5173 |
| Epodonios-all | 0.255 | observe | 0 | None | 7796 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9804 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5821 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 4 | 4 |
| ermaozi-get_subscribe | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.78 | 85 | 24 | 109 |
| mheidari-all | 0.795 | 35 | 9 | 44 |
| Au1rxx-base64 | 0.879 | 261 | 36 | 297 |
| ermaozi | 0.958 | 23 | 1 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23332 | yes | 5.06 | 0 |
| SoliSpirit-all | 9804 | yes | 2.37 | 0 |
| Epodonios-all | 7796 | yes | 7.29 | 0 |
| Surfboard-tg-mixed | 7269 | yes | 5.69 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.36 | 0 |
| barry-far-vless | 6148 | yes | 0.55 | 0 |
| Surfboard-tg-vless | 5821 | yes | 3.41 | 0 |
| DeltaKronecker-all | 5267 | yes | 4.87 | 0 |
| 10ium-ScrapeCategorize-Vless | 5173 | yes | 0.78 | 0 |
| mahdibland-V2RayAggregator | 4338 | yes | 1.34 | 0 |

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
| cn-block | 37 |
| 204 | 20 |
| geo | 13 |
| speed | 7 |
