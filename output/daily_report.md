# AutoNodes 每日报告

生成时间：2026-09-24 17:02:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 97092 |
| 去重后节点数 | 26416 |
| TCP 可达数 | 3000 |
| 真测通过数 | 405 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26416 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 80.8 |
| geo | 1.4 |
| probe | 220.4 |
| real_test | 202.3 |
| tcp | 43.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 36 | 24 | 12 | 66.7% |
| hysteria2 | 20 | 18 | 2 | 90.0% |
| shadowsocks | 163 | 150 | 13 | 92.0% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 15 | 12 | 3 | 80.0% |
| vless | 236 | 197 | 39 | 83.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 18 |
| 204:TimeoutError | 15 |
| cn-block:TimeoutError | 10 |
| speed:TimeoutError | 7 |
| cn-block:ProxyError | 6 |
| geo:TimeoutError | 6 |
| cn-block:ClientOSError | 4 |
| speed:ClientOSError | 3 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6366 |
| ConnectionRefusedError | 968 |
| gaierror | 293 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.988 | prefer | 262 | 0.924 | 1697 |
| mheidari-all | 0.95 | prefer | 67 | 0.881 | 22258 |
| Surfboard-tg-mixed | 0.793 | prefer | 106 | 0.717 | 7421 |
| ermaozi | 0.669 | observe | 33 | 0.667 | 298 |
| DeltaKronecker-all | 0.438 | observe | 3 | 1.0 | 5845 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 149 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 85 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5307 |
| Epodonios-all | 0.255 | observe | 0 | None | 7498 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| ermaozi-get_subscribe | 0.333 | 1 | 2 | 3 |
| ermaozi | 0.667 | 22 | 11 | 33 |
| Surfboard-tg-mixed | 0.717 | 76 | 30 | 106 |
| mheidari-all | 0.881 | 59 | 8 | 67 |
| Au1rxx-base64 | 0.924 | 242 | 20 | 262 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22258 | yes | 4.55 | 0 |
| SoliSpirit-all | 9120 | yes | 3.45 | 0 |
| Epodonios-all | 7498 | yes | 2.38 | 0 |
| Surfboard-tg-mixed | 7421 | yes | 2.94 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.6 | 0 |
| Surfboard-tg-vless | 5991 | yes | 3.14 | 0 |
| barry-far-vless | 5901 | yes | 1.06 | 0 |
| DeltaKronecker-all | 5845 | yes | 4.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 5307 | yes | 2.13 | 0 |
| mahdibland-V2RayAggregator | 4305 | yes | 0.66 | 0 |

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
| 204 | 34 |
| cn-block | 20 |
| speed | 10 |
| geo | 8 |
