# AutoNodes 每日报告

生成时间：2026-07-01 14:52:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 76903 |
| 去重后节点数 | 23340 |
| TCP 可达数 | 3000 |
| 真测通过数 | 400 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23340 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 49.7 |
| geo | 1.4 |
| probe | 49.0 |
| real_test | 100.7 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 6 | 1 | 5 | 16.7% |
| shadowsocks | 122 | 100 | 22 | 82.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 150 | 100 | 50 | 66.7% |
| vless | 370 | 157 | 213 | 42.4% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 169 |
| geo:TimeoutError | 22 |
| 204:TimeoutError | 18 |
| cn-block:TimeoutError | 16 |
| cn-block:ClientOSError | 15 |
| 204:ClientOSError | 15 |
| geo:ClientOSError | 14 |
| 204:ProxyError | 11 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4369 |
| ConnectionRefusedError | 635 |
| gaierror | 204 |
| OSError | 143 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.846 | prefer | 55 | 0.855 | 96 |
| Surfboard-tg-mixed | 0.686 | observe | 275 | 0.607 | 5849 |
| mheidari-all | 0.575 | observe | 212 | 0.495 | 15660 |
| DeltaKronecker-all | 0.493 | observe | 107 | 0.411 | 7631 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4308 |
| Epodonios-all | 0.255 | observe | 0 | None | 6803 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6937 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.125 | downweight | 5 | 0.0 | 0 | 1298 |
| chromego_merge | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| peasoft-NoMoreWalls | 0.175 | observe | 0 | None | 0 | 3 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.125 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 5 | 5 |
| DeltaKronecker-all | 0.411 | 44 | 63 | 107 |
| mheidari-all | 0.495 | 105 | 107 | 212 |
| Surfboard-tg-mixed | 0.607 | 167 | 108 | 275 |
| Au1rxx-base64 | 0.855 | 47 | 8 | 55 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15660 | yes | 3.47 | 0 |
| DeltaKronecker-all | 7631 | yes | 3.45 | 0 |
| SoliSpirit-all | 6937 | yes | 2.06 | 0 |
| Epodonios-all | 6803 | yes | 1.54 | 0 |
| Surfboard-tg-mixed | 5849 | yes | 1.86 | 0 |
| mahdibland-V2RayAggregator | 5331 | yes | 1.95 | 0 |
| barry-far-vless | 4908 | yes | 1.7 | 0 |
| Surfboard-tg-vless | 4351 | yes | 2.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 4308 | yes | 1.44 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.78 | 0 |

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
| speed | 175 |
| 204 | 44 |
| geo | 36 |
| cn-block | 36 |
