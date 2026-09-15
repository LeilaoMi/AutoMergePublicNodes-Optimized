# AutoNodes 每日报告

生成时间：2026-09-15 11:38:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 90261 |
| 去重后节点数 | 25575 |
| TCP 可达数 | 3000 |
| 真测通过数 | 426 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25575 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.6 |
| generate | 72.5 |
| geo | 1.3 |
| probe | 287.7 |
| real_test | 224.3 |
| tcp | 41.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 53 | 36 | 17 | 67.9% |
| hysteria2 | 18 | 16 | 2 | 88.9% |
| shadowsocks | 155 | 146 | 9 | 94.2% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 12 | 6 | 6 | 50.0% |
| vless | 307 | 220 | 87 | 71.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 22 |
| 204:ProxyError | 20 |
| geo:ClientOSError | 20 |
| cn-block:TimeoutError | 20 |
| cn-block:ClientOSError | 14 |
| geo:TimeoutError | 10 |
| speed:TimeoutError | 8 |
| speed:ClientOSError | 7 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5673 |
| ConnectionRefusedError | 958 |
| gaierror | 404 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.902 | prefer | 313 | 0.847 | 1440 |
| mheidari-all | 0.901 | prefer | 65 | 0.831 | 21594 |
| Surfboard-tg-mixed | 0.684 | observe | 109 | 0.606 | 7608 |
| ermaozi | 0.684 | observe | 52 | 0.673 | 425 |
| DeltaKronecker-all | 0.401 | observe | 7 | 0.571 | 5932 |
| ermaozi-get_subscribe | 0.273 | observe | 1 | 1.0 | 447 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 148 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |
| Epodonios-all | 0.255 | observe | 0 | None | 8009 |
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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.571 | 4 | 3 | 7 |
| Surfboard-tg-mixed | 0.606 | 66 | 43 | 109 |
| ermaozi | 0.673 | 35 | 17 | 52 |
| mheidari-all | 0.831 | 54 | 11 | 65 |
| Au1rxx-base64 | 0.847 | 265 | 48 | 313 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21594 | yes | 2.53 | 0 |
| SoliSpirit-all | 8760 | yes | 1.49 | 0 |
| Epodonios-all | 8009 | yes | 2.63 | 0 |
| Surfboard-tg-mixed | 7608 | yes | 3.17 | 0 |
| barry-far-vless | 6343 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 6177 | yes | 2.04 | 0 |
| DeltaKronecker-all | 5932 | yes | 2.7 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 1.0 | 0 |
| mahdibland-V2RayAggregator | 4258 | yes | 0.77 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.04 | 0 |

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
| 204 | 44 |
| cn-block | 35 |
| geo | 30 |
| speed | 15 |
