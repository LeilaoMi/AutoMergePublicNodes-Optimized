# AutoNodes 每日报告

生成时间：2026-08-23 01:49:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 83081 |
| 去重后节点数 | 23824 |
| TCP 可达数 | 3000 |
| 真测通过数 | 848 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23824 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 11.7 |
| generate | 31.4 |
| geo | 1.4 |
| probe | 59.3 |
| real_test | 179.2 |
| tcp | 41.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 114 | 114 | 0 | 100.0% |
| hysteria2 | 23 | 22 | 1 | 95.7% |
| shadowsocks | 187 | 183 | 4 | 97.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 188 | 169 | 19 | 89.9% |
| vless | 540 | 356 | 184 | 65.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 91 |
| speed:TimeoutError | 44 |
| geo:ClientOSError | 26 |
| cn-block:TimeoutError | 18 |
| speed:ClientOSError | 15 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| 204:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5558 |
| ConnectionRefusedError | 963 |
| gaierror | 507 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 513 | 0.938 | 1658 |
| zhangkai | 0.997 | prefer | 113 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.931 | prefer | 173 | 0.855 | 6297 |
| mheidari-all | 0.619 | observe | 163 | 0.54 | 14498 |
| nscl5-all | 0.355 | observe | 2 | 1.0 | 1082 |
| tg-oneclickvpnkeys | 0.317 | observe | 2 | 1.0 | 146 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 5974 |
| Epodonios-all | 0.255 | observe | 0 | None | 6920 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3986 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7010 |

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
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.243 | 84 | 0.155 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.155 | 13 | 71 | 84 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.54 | 88 | 75 | 163 |
| Surfboard-tg-mixed | 0.855 | 148 | 25 | 173 |
| Au1rxx-base64 | 0.938 | 481 | 32 | 513 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14498 | yes | 4.32 | 0 |
| SoliSpirit-all | 7010 | yes | 1.69 | 0 |
| Epodonios-all | 6920 | yes | 4.59 | 0 |
| Surfboard-tg-mixed | 6297 | yes | 3.71 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.35 | 0 |
| barry-far-vless | 5496 | yes | 0.4 | 0 |
| Surfboard-tg-vless | 5114 | yes | 2.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 5096 | yes | 0.74 | 0 |
| DeltaKronecker-all | 5015 | yes | 3.34 | 0 |
| mahdibland-V2RayAggregator | 4074 | yes | 2.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 119 |
| speed | 60 |
| cn-block | 22 |
| 204 | 8 |
