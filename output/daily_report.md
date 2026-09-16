# AutoNodes 每日报告

生成时间：2026-09-16 16:45:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 89601 |
| 去重后节点数 | 24453 |
| TCP 可达数 | 3000 |
| 真测通过数 | 416 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24453 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 133.9 |
| geo | 1.5 |
| probe | 282.7 |
| real_test | 243.0 |
| tcp | 41.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 30 | 25 | 5 | 83.3% |
| hysteria2 | 22 | 18 | 4 | 81.8% |
| shadowsocks | 151 | 133 | 18 | 88.1% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 5 | 3 | 2 | 60.0% |
| vless | 355 | 234 | 121 | 65.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 31 |
| geo:ClientOSError | 29 |
| cn-block:TimeoutError | 19 |
| geo:TimeoutError | 17 |
| speed:ClientOSError | 16 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 12 |
| speed:TimeoutError | 8 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5954 |
| ConnectionRefusedError | 923 |
| gaierror | 368 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.87 | prefer | 260 | 0.804 | 1702 |
| ermaozi | 0.842 | prefer | 27 | 0.852 | 353 |
| mheidari-all | 0.833 | prefer | 79 | 0.759 | 17973 |
| DeltaKronecker-all | 0.761 | prefer | 114 | 0.684 | 6081 |
| Surfboard-tg-mixed | 0.609 | observe | 83 | 0.53 | 7470 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4206 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 207 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5115 |
| Epodonios-all | 0.255 | observe | 0 | None | 7938 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 2 | 2 |
| Surfboard-tg-mixed | 0.53 | 44 | 39 | 83 |
| DeltaKronecker-all | 0.684 | 78 | 36 | 114 |
| mheidari-all | 0.759 | 60 | 19 | 79 |
| Au1rxx-base64 | 0.804 | 209 | 51 | 260 |
| ermaozi | 0.852 | 23 | 4 | 27 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17973 | yes | 3.46 | 0 |
| SoliSpirit-all | 9093 | yes | 2.76 | 0 |
| Epodonios-all | 7938 | yes | 1.89 | 0 |
| Surfboard-tg-mixed | 7470 | yes | 2.65 | 0 |
| barry-far-vless | 6195 | yes | 1.86 | 0 |
| DeltaKronecker-all | 6081 | yes | 3.34 | 0 |
| Surfboard-tg-vless | 5979 | yes | 2.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 5115 | yes | 1.65 | 0 |
| mahdibland-V2RayAggregator | 4206 | yes | 1.68 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.0 | 0 |

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
| geo | 47 |
| 204 | 46 |
| cn-block | 35 |
| speed | 24 |
