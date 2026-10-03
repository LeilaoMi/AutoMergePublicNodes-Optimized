# AutoNodes 每日报告

生成时间：2026-10-03 05:00:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98934 |
| 去重后节点数 | 27176 |
| TCP 可达数 | 3000 |
| 真测通过数 | 453 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27176 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 75.8 |
| geo | 1.2 |
| probe | 337.6 |
| real_test | 394.7 |
| tcp | 47.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 5 | 1 | 83.3% |
| http | 24 | 23 | 1 | 95.8% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 166 | 153 | 13 | 92.2% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 26 | 18 | 8 | 69.2% |
| vless | 547 | 237 | 310 | 43.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 143 |
| speed:TimeoutError | 76 |
| geo:ClientOSError | 33 |
| cn-block:TimeoutError | 22 |
| 204:ProxyError | 19 |
| speed:ClientOSError | 18 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6572 |
| ConnectionRefusedError | 1169 |
| gaierror | 402 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.956 | prefer | 269 | 0.888 | 1751 |
| ermaozi | 0.949 | prefer | 24 | 0.958 | 645 |
| Surfboard-tg-mixed | 0.741 | prefer | 54 | 0.667 | 7256 |
| mheidari-all | 0.432 | observe | 424 | 0.351 | 23323 |
| ermaozi-get_subscribe | 0.341 | observe | 4 | 0.75 | 516 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| DeltaKronecker-all | 0.255 | observe | 9 | 0.222 | 4981 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5276 |
| Epodonios-all | 0.255 | observe | 0 | None | 7743 |
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
| DeltaKronecker-all | 0.222 | 2 | 7 | 9 |
| mheidari-all | 0.351 | 149 | 275 | 424 |
| Surfboard-tg-mixed | 0.667 | 36 | 18 | 54 |
| ermaozi-get_subscribe | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.888 | 239 | 30 | 269 |
| ermaozi | 0.958 | 23 | 1 | 24 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23323 | yes | 4.46 | 0 |
| SoliSpirit-all | 9351 | yes | 3.13 | 0 |
| Epodonios-all | 7743 | yes | 2.48 | 0 |
| Surfboard-tg-mixed | 7256 | yes | 4.0 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.08 | 0 |
| barry-far-vless | 6214 | yes | 2.85 | 0 |
| Surfboard-tg-vless | 5980 | yes | 4.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 5276 | yes | 2.15 | 0 |
| DeltaKronecker-all | 4981 | yes | 4.67 | 0 |
| mahdibland-V2RayAggregator | 4357 | yes | 2.53 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 177 |
| speed | 95 |
| 204 | 31 |
| cn-block | 30 |
