# AutoNodes 每日报告

生成时间：2026-08-22 12:54:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 92293 |
| 去重后节点数 | 23763 |
| TCP 可达数 | 3000 |
| 真测通过数 | 802 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23763 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 33.9 |
| geo | 1.1 |
| probe | 64.0 |
| real_test | 166.1 |
| tcp | 38.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 26 | 25 | 1 | 96.2% |
| shadowsocks | 190 | 174 | 16 | 91.6% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 175 | 174 | 1 | 99.4% |
| vless | 428 | 316 | 112 | 73.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 42 |
| geo:TimeoutError | 22 |
| cn-block:TimeoutError | 14 |
| 204:TimeoutError | 13 |
| speed:TimeoutError | 12 |
| speed:ClientOSError | 9 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 5 |
| speed:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5116 |
| ConnectionRefusedError | 958 |
| gaierror | 771 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 509 | 0.939 | 1674 |
| zhangkai | 0.988 | prefer | 112 | 0.991 | 144 |
| Surfboard-tg-mixed | 0.91 | prefer | 174 | 0.833 | 6287 |
| mheidari-all | 0.576 | observe | 133 | 0.496 | 21719 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 3321 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 161 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5096 |
| Epodonios-all | 0.255 | observe | 0 | None | 6868 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3984 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6876 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.496 | 66 | 67 | 133 |
| Surfboard-tg-mixed | 0.833 | 145 | 29 | 174 |
| Au1rxx-base64 | 0.939 | 478 | 31 | 509 |
| zhangkai | 0.991 | 111 | 1 | 112 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21719 | yes | 3.16 | 0 |
| SoliSpirit-all | 6876 | yes | 2.94 | 0 |
| Epodonios-all | 6868 | yes | 2.72 | 0 |
| Surfboard-tg-mixed | 6287 | yes | 2.56 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 2.64 | 0 |
| barry-far-vless | 5403 | yes | 1.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 5096 | yes | 1.31 | 0 |
| Surfboard-tg-vless | 5093 | yes | 3.29 | 0 |
| DeltaKronecker-all | 5015 | yes | 3.71 | 0 |
| mahdibland-V2RayAggregator | 4074 | yes | 1.83 | 0 |

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
| geo | 64 |
| speed | 24 |
| 204 | 23 |
| cn-block | 22 |
