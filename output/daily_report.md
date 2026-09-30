# AutoNodes 每日报告

生成时间：2026-09-30 05:13:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 96916 |
| 去重后节点数 | 27039 |
| TCP 可达数 | 3000 |
| 真测通过数 | 361 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27039 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 36.7 |
| geo | 1.5 |
| probe | 305.5 |
| real_test | 387.7 |
| tcp | 46.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 37 | 31 | 6 | 83.8% |
| hysteria2 | 24 | 23 | 1 | 95.8% |
| shadowsocks | 166 | 150 | 16 | 90.4% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 3 | 2 | 1 | 66.7% |
| vless | 485 | 150 | 335 | 30.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 158 |
| speed:TimeoutError | 53 |
| geo:ClientOSError | 51 |
| speed:ClientOSError | 43 |
| 204:ProxyError | 21 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 9 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 1 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6623 |
| ConnectionRefusedError | 1008 |
| gaierror | 288 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 100 | 0.96 | 1756 |
| ermaozi | 0.797 | prefer | 35 | 0.8 | 335 |
| Surfboard-tg-mixed | 0.702 | prefer | 146 | 0.623 | 7024 |
| DeltaKronecker-all | 0.48 | observe | 4 | 1.0 | 5528 |
| mheidari-all | 0.398 | observe | 429 | 0.317 | 22586 |
| tg-oneclickvpnkeys | 0.361 | observe | 3 | 1.0 | 74 |
| ermaozi-get_subscribe | 0.334 | observe | 4 | 0.75 | 353 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5314 |
| Epodonios-all | 0.255 | observe | 0 | None | 7591 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.317 | 136 | 293 | 429 |
| Surfboard-tg-mixed | 0.623 | 91 | 55 | 146 |
| ermaozi-get_subscribe | 0.75 | 3 | 1 | 4 |
| ermaozi | 0.8 | 28 | 7 | 35 |
| Au1rxx-base64 | 0.96 | 96 | 4 | 100 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| DeltaKronecker-all | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22586 | yes | 5.12 | 0 |
| SoliSpirit-all | 9347 | yes | 2.04 | 0 |
| Epodonios-all | 7591 | yes | 4.61 | 0 |
| Surfboard-tg-mixed | 7024 | yes | 4.04 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.5 | 0 |
| barry-far-vless | 5895 | yes | 0.68 | 0 |
| Surfboard-tg-vless | 5656 | yes | 3.3 | 0 |
| DeltaKronecker-all | 5528 | yes | 3.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 5314 | yes | 0.5 | 0 |
| mahdibland-V2RayAggregator | 4338 | yes | 2.48 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 210 |
| speed | 96 |
| 204 | 43 |
| cn-block | 12 |
