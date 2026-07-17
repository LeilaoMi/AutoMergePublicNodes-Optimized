# AutoNodes 每日报告

生成时间：2026-07-17 13:55:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 79167 |
| 去重后节点数 | 24892 |
| TCP 可达数 | 3000 |
| 真测通过数 | 515 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24892 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 43.8 |
| geo | 1.2 |
| probe | 55.6 |
| real_test | 141.3 |
| tcp | 33.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 134 | 102 | 32 | 76.1% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 449 | 366 | 83 | 81.5% |
| vless | 134 | 3 | 131 | 2.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 82 |
| speed:ClientOSError | 60 |
| 204:TimeoutError | 45 |
| cn-block:TimeoutError | 22 |
| 204:ClientOSError | 13 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 6 |
| 204:ProxyError | 5 |
| geo:ClientOSError | 4 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4564 |
| ConnectionRefusedError | 660 |
| gaierror | 232 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.961 | prefer | 191 | 0.885 | 16536 |
| Au1rxx-base64 | 0.933 | prefer | 94 | 0.936 | 150 |
| Surfboard-tg-mixed | 0.694 | observe | 125 | 0.616 | 5276 |
| DeltaKronecker-all | 0.535 | observe | 312 | 0.455 | 8967 |
| nscl5-all | 0.328 | observe | 1 | 1.0 | 1821 |
| xiaoji235-airport-v2ray-all | 0.322 | observe | 1 | 1.0 | 1680 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4428 |
| Epodonios-all | 0.255 | observe | 0 | None | 6455 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.455 | 142 | 170 | 312 |
| Surfboard-tg-mixed | 0.616 | 77 | 48 | 125 |
| mheidari-all | 0.885 | 169 | 22 | 191 |
| Au1rxx-base64 | 0.936 | 88 | 6 | 94 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16361 | yes | 3.9 | 0 |
| DeltaKronecker-all | 8967 | yes | 3.39 | 0 |
| SoliSpirit-all | 6764 | yes | 1.21 | 0 |
| Epodonios-all | 6455 | yes | 1.5 | 0 |
| Surfboard-tg-mixed | 5276 | yes | 2.82 | 0 |
| mahdibland-V2RayAggregator | 5208 | yes | 1.64 | 0 |
| barry-far-vless | 4743 | yes | 0.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 4428 | yes | 0.9 | 0 |
| Surfboard-tg-vless | 4097 | yes | 2.68 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 0.97 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.022 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 87 |
| speed | 66 |
| 204 | 63 |
| cn-block | 32 |
