# AutoNodes 每日报告

生成时间：2026-10-03 20:58:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 99458 |
| 去重后节点数 | 27317 |
| TCP 可达数 | 3000 |
| 真测通过数 | 324 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27317 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| generate | 74.1 |
| geo | 0.8 |
| probe | 129.3 |
| real_test | 135.6 |
| tcp | 47.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 23 | 21 | 2 | 91.3% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 90 | 80 | 10 | 88.9% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 45 | 42 | 3 | 93.3% |
| vless | 191 | 166 | 25 | 86.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 6 |
| geo:TimeoutError | 5 |
| 204:ProxyConnectionError | 4 |
| 204:TimeoutError | 3 |
| geo:ClientOSError | 3 |
| 204:ProxyError | 2 |
| speed:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| 204:ClientOSError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6664 |
| ConnectionRefusedError | 1150 |
| gaierror | 357 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.984 | prefer | 293 | 0.915 | 1802 |
| ermaozi | 0.872 | prefer | 24 | 0.875 | 656 |
| mheidari-all | 0.83 | prefer | 42 | 0.762 | 23599 |
| Surfboard-tg-mixed | 0.438 | observe | 3 | 1.0 | 7340 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5192 |
| Epodonios-all | 0.255 | observe | 0 | None | 7819 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3995 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9376 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5938 |
| barry-far-vless | 0.255 | observe | 0 | None | 6176 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.762 | 32 | 10 | 42 |
| ermaozi | 0.875 | 21 | 3 | 24 |
| Au1rxx-base64 | 0.915 | 268 | 25 | 293 |
| Surfboard-tg-mixed | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23599 | yes | 6.79 | 0 |
| SoliSpirit-all | 9376 | yes | 3.51 | 0 |
| Epodonios-all | 7819 | yes | 3.76 | 0 |
| Surfboard-tg-mixed | 7340 | yes | 4.35 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.29 | 0 |
| barry-far-vless | 6176 | yes | 0.84 | 0 |
| Surfboard-tg-vless | 5938 | yes | 4.59 | 0 |
| DeltaKronecker-all | 5207 | yes | 5.68 | 0 |
| 10ium-ScrapeCategorize-Vless | 5192 | yes | 4.63 | 0 |
| mahdibland-V2RayAggregator | 4285 | yes | 3.48 | 0 |

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
| cn-block | 16 |
| 204 | 10 |
| speed | 9 |
| geo | 8 |
