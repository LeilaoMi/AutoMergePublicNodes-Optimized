# AutoNodes 每日报告

生成时间：2026-09-24 21:30:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 98134 |
| 去重后节点数 | 26548 |
| TCP 可达数 | 3000 |
| 真测通过数 | 370 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26548 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 77.3 |
| geo | 1.4 |
| probe | 214.8 |
| real_test | 159.8 |
| tcp | 43.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 16 | 10 | 6 | 62.5% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 132 | 121 | 11 | 91.7% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 16 | 13 | 3 | 81.2% |
| vless | 281 | 205 | 76 | 73.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 42 |
| 204:TimeoutError | 15 |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 9 |
| speed:TimeoutError | 5 |
| cn-block:ProxyError | 4 |
| speed:ClientOSError | 4 |
| geo:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5824 |
| ConnectionRefusedError | 988 |
| gaierror | 400 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.977 | prefer | 260 | 0.915 | 1626 |
| Surfboard-tg-mixed | 0.868 | prefer | 15 | 1.0 | 7419 |
| mheidari-all | 0.68 | observe | 173 | 0.601 | 22744 |
| ermaozi | 0.455 | observe | 15 | 0.533 | 298 |
| DeltaKronecker-all | 0.391 | observe | 2 | 1.0 | 5845 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4405 |
| ermaozi-get_subscribe | 0.267 | observe | 1 | 1.0 | 304 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 65 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5307 |
| Epodonios-all | 0.255 | observe | 0 | None | 7888 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.533 | 8 | 7 | 15 |
| mheidari-all | 0.601 | 104 | 69 | 173 |
| Au1rxx-base64 | 0.915 | 238 | 22 | 260 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 2 | 0 | 2 |
| Surfboard-tg-mixed | 1.0 | 15 | 0 | 15 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22744 | yes | 4.69 | 0 |
| SoliSpirit-all | 9086 | yes | 3.61 | 0 |
| Epodonios-all | 7888 | yes | 2.46 | 0 |
| Surfboard-tg-mixed | 7419 | yes | 3.65 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.42 | 0 |
| barry-far-vless | 6215 | yes | 0.72 | 0 |
| Surfboard-tg-vless | 5963 | yes | 2.99 | 0 |
| DeltaKronecker-all | 5845 | yes | 4.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 5307 | yes | 1.99 | 0 |
| mahdibland-V2RayAggregator | 4405 | yes | 2.11 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 60 |
| 204 | 26 |
| speed | 9 |
| geo | 5 |
