# AutoNodes 每日报告

生成时间：2026-09-16 21:16:53

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 89335 |
| 去重后节点数 | 24603 |
| TCP 可达数 | 3000 |
| 真测通过数 | 377 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24603 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 84.8 |
| geo | 1.5 |
| probe | 215.5 |
| real_test | 206.3 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 34 | 25 | 9 | 73.5% |
| hysteria2 | 17 | 16 | 1 | 94.1% |
| shadowsocks | 107 | 98 | 9 | 91.6% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 8 | 8 | 0 | 100.0% |
| vless | 299 | 227 | 72 | 75.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 15 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 13 |
| 204:ProxyError | 12 |
| geo:TimeoutError | 10 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| 204:ProxyConnectionError | 5 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5371 |
| ConnectionRefusedError | 943 |
| gaierror | 491 |
| OSError | 237 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.904 | prefer | 72 | 0.833 | 17985 |
| Au1rxx-base64 | 0.89 | prefer | 254 | 0.827 | 1651 |
| DeltaKronecker-all | 0.82 | prefer | 102 | 0.745 | 6081 |
| ermaozi | 0.781 | prefer | 28 | 0.786 | 353 |
| Surfboard-tg-mixed | 0.519 | observe | 5 | 1.0 | 7483 |
| tg-oneclickvpnkeys | 0.364 | observe | 3 | 1.0 | 140 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5115 |
| Epodonios-all | 0.255 | observe | 0 | None | 7934 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.25 | 1 | 3 | 4 |
| DeltaKronecker-all | 0.745 | 76 | 26 | 102 |
| ermaozi | 0.786 | 22 | 6 | 28 |
| Au1rxx-base64 | 0.827 | 210 | 44 | 254 |
| mheidari-all | 0.833 | 60 | 12 | 72 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| Surfboard-tg-mixed | 1.0 | 5 | 0 | 5 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17985 | yes | 5.44 | 0 |
| SoliSpirit-all | 8999 | yes | 2.88 | 0 |
| Epodonios-all | 7934 | yes | 3.41 | 0 |
| Surfboard-tg-mixed | 7483 | yes | 4.53 | 0 |
| barry-far-vless | 6197 | yes | 1.71 | 0 |
| DeltaKronecker-all | 6081 | yes | 5.94 | 0 |
| Surfboard-tg-vless | 5919 | yes | 3.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5115 | yes | 1.93 | 0 |
| mahdibland-V2RayAggregator | 4234 | yes | 3.1 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.49 | 0 |

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
| 204 | 32 |
| geo | 26 |
| cn-block | 18 |
| speed | 18 |
