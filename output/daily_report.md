# AutoNodes 每日报告

生成时间：2026-07-20 03:43:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 85667 |
| 去重后节点数 | 24257 |
| TCP 可达数 | 3000 |
| 真测通过数 | 590 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24257 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 42.4 |
| geo | 0.6 |
| probe | 56.8 |
| real_test | 115.3 |
| tcp | 33.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 157 | 147 | 10 | 93.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 376 | 309 | 67 | 82.2% |
| vless | 306 | 88 | 218 | 28.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 133 |
| cn-block:TimeoutError | 52 |
| geo:TimeoutError | 39 |
| geo:ClientOSError | 30 |
| speed:TimeoutError | 15 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4343 |
| ConnectionRefusedError | 699 |
| gaierror | 673 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.942 | prefer | 246 | 0.902 | 1060 |
| mheidari-all | 0.707 | prefer | 148 | 0.628 | 19582 |
| nscl5-all | 0.698 | observe | 32 | 0.625 | 2118 |
| DeltaKronecker-all | 0.661 | observe | 170 | 0.582 | 6235 |
| Surfboard-tg-mixed | 0.574 | observe | 239 | 0.494 | 5225 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4478 |
| Epodonios-all | 0.255 | observe | 0 | None | 6589 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

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
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.189 | 11 | 0.091 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.091 | 1 | 10 | 11 |
| Surfboard-tg-mixed | 0.494 | 118 | 121 | 239 |
| DeltaKronecker-all | 0.582 | 99 | 71 | 170 |
| nscl5-all | 0.625 | 20 | 12 | 32 |
| mheidari-all | 0.628 | 93 | 55 | 148 |
| Au1rxx-base64 | 0.902 | 222 | 24 | 246 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19582 | yes | 4.44 | 0 |
| SoliSpirit-all | 7105 | yes | 3.27 | 0 |
| Epodonios-all | 6589 | yes | 0.76 | 0 |
| DeltaKronecker-all | 6235 | yes | 4.09 | 0 |
| mahdibland-V2RayAggregator | 5229 | yes | 2.59 | 0 |
| Surfboard-tg-mixed | 5225 | yes | 2.51 | 0 |
| xiaoji235-airport-v2ray-all | 5035 | yes | 1.42 | 0 |
| barry-far-vless | 4960 | yes | 1.77 | 0 |
| 10ium-ScrapeCategorize-Vless | 4478 | yes | 1.34 | 0 |
| Surfboard-tg-vless | 4116 | yes | 3.05 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 148 |
| geo | 69 |
| cn-block | 58 |
| 204 | 21 |
