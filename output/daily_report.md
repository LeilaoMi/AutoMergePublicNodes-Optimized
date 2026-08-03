# AutoNodes 每日报告

生成时间：2026-08-03 10:02:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 83372 |
| 去重后节点数 | 24502 |
| TCP 可达数 | 3000 |
| 真测通过数 | 676 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24502 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| generate | 42.4 |
| geo | 1.4 |
| probe | 67.2 |
| real_test | 194.3 |
| tcp | 37.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 143 | 143 | 0 | 100.0% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 150 | 123 | 27 | 82.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 30 | 26 | 4 | 86.7% |
| vless | 752 | 364 | 388 | 48.4% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 157 |
| 204:ProxyError | 83 |
| speed:TimeoutError | 48 |
| speed:ClientOSError | 32 |
| 204:TimeoutError | 28 |
| cn-block:TimeoutError | 27 |
| geo:ClientOSError | 25 |
| cn-block:ProxyError | 9 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 4 |
| speed:ProxyError | 3 |
| cn-block:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5053 |
| ConnectionRefusedError | 764 |
| gaierror | 242 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 144 | 1.0 | 344 |
| Au1rxx-base64 | 0.81 | prefer | 555 | 0.746 | 1629 |
| Surfboard-tg-mixed | 0.388 | observe | 24 | 0.292 | 5244 |
| DeltaKronecker-all | 0.379 | observe | 359 | 0.298 | 6205 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 3833 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 54 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5285 |
| Epodonios-all | 0.255 | observe | 0 | None | 5831 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6567 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | mheidari-all | 0.249 | 10 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.2 | 2 | 8 | 10 |
| Surfboard-tg-mixed | 0.292 | 7 | 17 | 24 |
| DeltaKronecker-all | 0.298 | 107 | 252 | 359 |
| Au1rxx-base64 | 0.746 | 414 | 141 | 555 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 144 | 0 | 144 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18806 | yes | 4.57 | 0 |
| SoliSpirit-all | 6567 | yes | 3.92 | 0 |
| DeltaKronecker-all | 6205 | yes | 3.43 | 0 |
| Epodonios-all | 5831 | yes | 3.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5285 | yes | 2.39 | 0 |
| Surfboard-tg-mixed | 5244 | yes | 2.74 | 0 |
| mahdibland-V2RayAggregator | 5196 | yes | 2.47 | 0 |
| barry-far-vless | 4492 | yes | 2.13 | 0 |
| Surfboard-tg-vless | 4132 | yes | 2.62 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.2 | 0 |

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
| geo | 186 |
| 204 | 116 |
| speed | 83 |
| cn-block | 38 |
