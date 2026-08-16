# AutoNodes 每日报告

生成时间：2026-08-16 01:48:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 79337 |
| 去重后节点数 | 22383 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1147 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22383 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 34.9 |
| geo | 0.5 |
| probe | 74.7 |
| real_test | 238.1 |
| tcp | 33.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 149 | 143 | 6 | 96.0% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 584 | 575 | 9 | 98.5% |
| vless | 517 | 284 | 233 | 54.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 94 |
| speed:TimeoutError | 64 |
| cn-block:TimeoutError | 30 |
| geo:ClientOSError | 28 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 9 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4078 |
| ConnectionRefusedError | 809 |
| gaierror | 388 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 787 | 0.978 | 1995 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.802 | prefer | 156 | 0.724 | 5707 |
| mheidari-all | 0.568 | observe | 252 | 0.488 | 16315 |
| nscl5-all | 0.391 | observe | 2 | 1.0 | 2601 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 145 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1995 |
| Epodonios-all | 0.255 | observe | 0 | None | 6340 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3984 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7329 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.249 | 69 | 0.159 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.159 | 11 | 58 | 69 |
| mheidari-all | 0.488 | 123 | 129 | 252 |
| Surfboard-tg-mixed | 0.724 | 113 | 43 | 156 |
| Au1rxx-base64 | 0.978 | 770 | 17 | 787 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16315 | yes | 5.0 | 0 |
| SoliSpirit-all | 7329 | yes | 3.63 | 0 |
| Epodonios-all | 6340 | yes | 0.88 | 0 |
| DeltaKronecker-all | 5773 | yes | 5.11 | 0 |
| Surfboard-tg-mixed | 5707 | yes | 3.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 5113 | yes | 3.87 | 0 |
| barry-far-vless | 4782 | yes | 3.07 | 0 |
| Surfboard-tg-vless | 4387 | yes | 4.05 | 0 |
| MatinGhanbari-all-sub | 3984 | yes | 3.15 | 0 |
| mahdibland-V2RayAggregator | 3935 | yes | 0.37 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 122 |
| speed | 78 |
| cn-block | 34 |
| 204 | 15 |
