# AutoNodes 每日报告

生成时间：2026-10-13 22:40:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98441 |
| 去重后节点数 | 27354 |
| TCP 可达数 | 3000 |
| 真测通过数 | 412 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27354 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| generate | 96.9 |
| geo | 1.5 |
| probe | 316.6 |
| real_test | 266.6 |
| tcp | 47.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 5 | 0 | 100.0% |
| http | 23 | 15 | 8 | 65.2% |
| hysteria2 | 10 | 9 | 1 | 90.0% |
| shadowsocks | 121 | 106 | 15 | 87.6% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 76 | 75 | 1 | 98.7% |
| vless | 234 | 202 | 32 | 86.3% |
| vmess | 1 | 0 | 1 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 18 |
| 204:ProxyConnectionError | 15 |
| speed:ClientOSError | 8 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:ClientOSError | 2 |
| speed:TimeoutError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6766 |
| ConnectionRefusedError | 1041 |
| gaierror | 329 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | prefer | 350 | 0.906 | 1806 |
| mheidari-all | 0.928 | prefer | 64 | 0.859 | 23973 |
| Surfboard-tg-mixed | 0.858 | prefer | 25 | 0.8 | 7123 |
| zhangkai | 0.658 | observe | 21 | 0.667 | 144 |
| ermaozi-get_subscribe | 0.43 | observe | 6 | 0.833 | 534 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5086 |
| Epodonios-all | 0.255 | observe | 0 | None | 7631 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9832 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5683 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 3 | 3 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| zhangkai | 0.667 | 14 | 7 | 21 |
| Surfboard-tg-mixed | 0.8 | 20 | 5 | 25 |
| ermaozi-get_subscribe | 0.833 | 5 | 1 | 6 |
| mheidari-all | 0.859 | 55 | 9 | 64 |
| Au1rxx-base64 | 0.906 | 317 | 33 | 350 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23973 | yes | 5.83 | 0 |
| SoliSpirit-all | 9832 | yes | 4.93 | 0 |
| Epodonios-all | 7631 | yes | 7.35 | 0 |
| Surfboard-tg-mixed | 7123 | yes | 5.16 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.59 | 0 |
| barry-far-vless | 5929 | yes | 2.93 | 0 |
| Surfboard-tg-vless | 5683 | yes | 6.63 | 0 |
| 10ium-ScrapeCategorize-Vless | 5086 | yes | 2.69 | 0 |
| DeltaKronecker-all | 5076 | yes | 5.52 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 0.25 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| vmess | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 25 |
| 204 | 23 |
| speed | 9 |
| geo | 4 |
