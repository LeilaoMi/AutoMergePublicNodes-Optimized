# AutoNodes 每日报告

生成时间：2026-07-26 08:39:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 80985 |
| 去重后节点数 | 22458 |
| TCP 可达数 | 3000 |
| 真测通过数 | 919 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22458 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 40.7 |
| geo | 1.4 |
| probe | 69.9 |
| real_test | 201.0 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 76 | 75 | 1 | 98.7% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 138 | 121 | 17 | 87.7% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 613 | 560 | 53 | 91.4% |
| vless | 387 | 152 | 235 | 39.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 120 |
| cn-block:TimeoutError | 38 |
| speed:ClientOSError | 32 |
| geo:ClientOSError | 30 |
| 204:ProxyError | 22 |
| speed:TimeoutError | 21 |
| 204:TimeoutError | 18 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| geo:ProxyError | 6 |
| cn-block:ProxyError | 5 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4078 |
| ConnectionRefusedError | 687 |
| gaierror | 315 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.978 | prefer | 76 | 0.987 | 86 |
| Au1rxx-base64 | 0.955 | prefer | 454 | 0.899 | 1442 |
| mheidari-all | 0.924 | prefer | 197 | 0.848 | 17285 |
| Surfboard-tg-mixed | 0.69 | observe | 152 | 0.612 | 5458 |
| DeltaKronecker-all | 0.593 | observe | 341 | 0.513 | 5950 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6596 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4178 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.513 | 175 | 166 | 341 |
| Surfboard-tg-mixed | 0.612 | 93 | 59 | 152 |
| mheidari-all | 0.848 | 167 | 30 | 197 |
| Au1rxx-base64 | 0.899 | 408 | 46 | 454 |
| zhangkai | 0.987 | 75 | 1 | 76 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17285 | yes | 4.35 | 0 |
| SoliSpirit-all | 6596 | yes | 2.71 | 0 |
| Epodonios-all | 6589 | yes | 2.72 | 0 |
| DeltaKronecker-all | 5950 | yes | 4.89 | 0 |
| Surfboard-tg-mixed | 5458 | yes | 3.15 | 0 |
| mahdibland-V2RayAggregator | 4980 | yes | 2.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 1.67 | 0 |
| barry-far-vless | 4874 | yes | 1.86 | 0 |
| Surfboard-tg-vless | 4178 | yes | 3.34 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.94 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 156 |
| speed | 56 |
| cn-block | 50 |
| 204 | 46 |
