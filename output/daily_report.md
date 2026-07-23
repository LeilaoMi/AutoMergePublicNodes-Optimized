# AutoNodes 每日报告

生成时间：2026-07-23 14:21:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83515 |
| 去重后节点数 | 22818 |
| TCP 可达数 | 3000 |
| 真测通过数 | 840 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22818 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 29.6 |
| geo | 1.1 |
| probe | 69.2 |
| real_test | 216.3 |
| tcp | 32.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 137 | 115 | 22 | 83.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 664 | 542 | 122 | 81.6% |
| vless | 398 | 140 | 258 | 35.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 104 |
| geo:TimeoutError | 80 |
| cn-block:TimeoutError | 69 |
| geo:ClientOSError | 43 |
| 204:ProxyError | 40 |
| 204:TimeoutError | 28 |
| speed:TimeoutError | 12 |
| cn-block:ProxyError | 10 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| geo:ProxyError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4252 |
| ConnectionRefusedError | 682 |
| gaierror | 341 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.928 | prefer | 353 | 0.85 | 19424 |
| Surfboard-tg-mixed | 0.793 | prefer | 85 | 0.718 | 5390 |
| Au1rxx-base64 | 0.79 | prefer | 196 | 0.776 | 432 |
| DeltaKronecker-all | 0.586 | observe | 569 | 0.506 | 5572 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4399 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4757 |
| Epodonios-all | 0.255 | observe | 0 | None | 6487 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.506 | 288 | 281 | 569 |
| Surfboard-tg-mixed | 0.718 | 61 | 24 | 85 |
| Au1rxx-base64 | 0.776 | 152 | 44 | 196 |
| mheidari-all | 0.85 | 300 | 53 | 353 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19424 | yes | 3.64 | 0 |
| SoliSpirit-all | 7332 | yes | 2.18 | 0 |
| Epodonios-all | 6487 | yes | 1.95 | 0 |
| DeltaKronecker-all | 5572 | yes | 3.73 | 0 |
| Surfboard-tg-mixed | 5390 | yes | 2.37 | 0 |
| mahdibland-V2RayAggregator | 4954 | yes | 3.09 | 0 |
| barry-far-vless | 4823 | yes | 1.26 | 0 |
| 10ium-ScrapeCategorize-Vless | 4757 | yes | 0.94 | 0 |
| xiaoji235-airport-v2ray-all | 4399 | yes | 1.28 | 0 |
| Surfboard-tg-vless | 4196 | yes | 2.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 127 |
| speed | 116 |
| cn-block | 86 |
| 204 | 74 |
