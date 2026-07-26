# AutoNodes 每日报告

生成时间：2026-07-26 03:36:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80527 |
| 去重后节点数 | 22461 |
| TCP 可达数 | 3000 |
| 真测通过数 | 913 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22461 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| generate | 20.1 |
| geo | 1.5 |
| probe | 69.1 |
| real_test | 192.8 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 76 | 76 | 0 | 100.0% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 159 | 136 | 23 | 85.5% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 590 | 552 | 38 | 93.6% |
| vless | 408 | 136 | 272 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 101 |
| speed:ClientOSError | 100 |
| speed:TimeoutError | 39 |
| cn-block:TimeoutError | 38 |
| geo:ClientOSError | 27 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 7 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4127 |
| ConnectionRefusedError | 694 |
| gaierror | 324 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 76 | 1.0 | 119 |
| Au1rxx-base64 | 0.94 | prefer | 489 | 0.888 | 1341 |
| Surfboard-tg-mixed | 0.899 | prefer | 70 | 0.829 | 5462 |
| DeltaKronecker-all | 0.714 | prefer | 230 | 0.635 | 5838 |
| mheidari-all | 0.604 | observe | 376 | 0.524 | 17224 |
| xiaoji235-airport-v2ray-all | 0.272 | observe | 2 | 0.5 | 1624 |
| tg-ConfigV2rayNG | 0.263 | observe | 1 | 1.0 | 200 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4879 |
| Epodonios-all | 0.255 | observe | 0 | None | 6569 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.524 | 197 | 179 | 376 |
| DeltaKronecker-all | 0.635 | 146 | 84 | 230 |
| Surfboard-tg-mixed | 0.829 | 58 | 12 | 70 |
| Au1rxx-base64 | 0.888 | 434 | 55 | 489 |
| tg-ConfigV2rayNG | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 76 | 0 | 76 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17224 | yes | 3.01 | 0 |
| Epodonios-all | 6569 | yes | 0.74 | 0 |
| SoliSpirit-all | 6505 | yes | 2.01 | 0 |
| DeltaKronecker-all | 5838 | yes | 2.51 | 0 |
| Surfboard-tg-mixed | 5462 | yes | 2.07 | 0 |
| mahdibland-V2RayAggregator | 4980 | yes | 1.84 | 0 |
| 10ium-ScrapeCategorize-Vless | 4879 | yes | 1.44 | 0 |
| barry-far-vless | 4852 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4196 | yes | 1.95 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.22 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 139 |
| geo | 128 |
| cn-block | 47 |
| 204 | 22 |
