# AutoNodes 每日报告

生成时间：2026-07-21 03:24:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84510 |
| 去重后节点数 | 24299 |
| TCP 可达数 | 3000 |
| 真测通过数 | 599 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24299 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 21.4 |
| geo | 1.4 |
| probe | 63.5 |
| real_test | 164.0 |
| tcp | 33.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 2 | 1 | 66.7% |
| shadowsocks | 145 | 136 | 9 | 93.8% |
| socks | 17 | 16 | 1 | 94.1% |
| trojan | 426 | 375 | 51 | 88.0% |
| vless | 529 | 33 | 496 | 6.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 222 |
| geo:TimeoutError | 193 |
| speed:TimeoutError | 50 |
| cn-block:TimeoutError | 40 |
| geo:ClientOSError | 38 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 4 |
| 204:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4371 |
| ConnectionRefusedError | 682 |
| gaierror | 526 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.904 | prefer | 123 | 0.829 | 5509 |
| Au1rxx-base64 | 0.882 | prefer | 206 | 0.869 | 405 |
| DeltaKronecker-all | 0.631 | observe | 174 | 0.552 | 5962 |
| mheidari-all | 0.381 | observe | 615 | 0.301 | 20195 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4714 |
| Epodonios-all | 0.255 | observe | 0 | None | 6601 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6928 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.301 | 185 | 430 | 615 |
| DeltaKronecker-all | 0.552 | 96 | 78 | 174 |
| Surfboard-tg-mixed | 0.829 | 102 | 21 | 123 |
| Au1rxx-base64 | 0.869 | 179 | 27 | 206 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20195 | yes | 3.7 | 0 |
| SoliSpirit-all | 6928 | yes | 3.01 | 0 |
| Epodonios-all | 6601 | yes | 3.18 | 0 |
| DeltaKronecker-all | 5962 | yes | 3.88 | 0 |
| Surfboard-tg-mixed | 5509 | yes | 1.73 | 0 |
| mahdibland-V2RayAggregator | 5173 | yes | 1.82 | 0 |
| barry-far-vless | 4952 | yes | 1.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 4714 | yes | 1.48 | 0 |
| xiaoji235-airport-v2ray-all | 4304 | yes | 1.25 | 0 |
| Surfboard-tg-vless | 4238 | yes | 2.69 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.062 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 272 |
| geo | 231 |
| cn-block | 47 |
| 204 | 8 |
