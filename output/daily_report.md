# AutoNodes 每日报告

生成时间：2026-08-16 12:55:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 79021 |
| 去重后节点数 | 21933 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1100 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21933 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 33.5 |
| geo | 1.2 |
| probe | 62.6 |
| real_test | 227.3 |
| tcp | 34.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 147 | 135 | 12 | 91.8% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 602 | 600 | 2 | 99.7% |
| vless | 315 | 224 | 91 | 71.1% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 24 |
| geo:TimeoutError | 23 |
| geo:ClientOSError | 17 |
| speed:TimeoutError | 16 |
| 204:ClientOSError | 6 |
| cn-block:TimeoutError | 6 |
| speed:ClientOSError | 5 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 4 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4493 |
| ConnectionRefusedError | 798 |
| gaierror | 264 |
| OSError | 15 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 807 | 0.963 | 1994 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| mheidari-all | 0.971 | prefer | 99 | 0.899 | 16375 |
| Surfboard-tg-mixed | 0.794 | prefer | 145 | 0.717 | 5800 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4990 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 2601 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1994 |
| Epodonios-all | 0.255 | observe | 0 | None | 6483 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3989 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7383 |

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
| DeltaKronecker-all | 0.151 | downweight | 26 | 0.038 | 0 | 5092 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.151 | 26 | 0.038 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.038 | 1 | 25 | 26 |
| Surfboard-tg-mixed | 0.717 | 104 | 41 | 145 |
| mheidari-all | 0.899 | 89 | 10 | 99 |
| Au1rxx-base64 | 0.963 | 777 | 30 | 807 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16375 | yes | 4.01 | 0 |
| SoliSpirit-all | 7383 | yes | 2.02 | 0 |
| Epodonios-all | 6483 | yes | 4.23 | 0 |
| Surfboard-tg-mixed | 5800 | yes | 3.18 | 0 |
| DeltaKronecker-all | 5092 | yes | 4.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 1.18 | 0 |
| barry-far-vless | 4839 | yes | 0.56 | 0 |
| Surfboard-tg-vless | 4502 | yes | 3.32 | 0 |
| MatinGhanbari-all-sub | 3989 | yes | 0.94 | 0 |
| mahdibland-V2RayAggregator | 3950 | yes | 2.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 41 |
| 204 | 34 |
| speed | 21 |
| cn-block | 11 |
