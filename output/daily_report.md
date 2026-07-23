# AutoNodes 每日报告

生成时间：2026-07-23 19:31:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83072 |
| 去重后节点数 | 22758 |
| TCP 可达数 | 3000 |
| 真测通过数 | 598 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22758 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 30.0 |
| geo | 1.3 |
| probe | 60.8 |
| real_test | 160.0 |
| tcp | 32.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 124 | 103 | 21 | 83.1% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 408 | 347 | 61 | 85.0% |
| vless | 359 | 105 | 254 | 29.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 119 |
| speed:ClientOSError | 92 |
| cn-block:TimeoutError | 61 |
| 204:TimeoutError | 18 |
| geo:ClientOSError | 12 |
| speed:TimeoutError | 11 |
| cn-block:ProxyError | 7 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4391 |
| ConnectionRefusedError | 691 |
| gaierror | 286 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.718 | prefer | 523 | 0.639 | 19362 |
| Au1rxx-base64 | 0.713 | prefer | 182 | 0.698 | 432 |
| DeltaKronecker-all | 0.638 | observe | 41 | 0.561 | 5572 |
| Surfboard-tg-mixed | 0.587 | observe | 150 | 0.507 | 5429 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 4399 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4757 |
| Epodonios-all | 0.255 | observe | 0 | None | 6563 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3966 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 6 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.507 | 76 | 74 | 150 |
| DeltaKronecker-all | 0.561 | 23 | 18 | 41 |
| mheidari-all | 0.639 | 334 | 189 | 523 |
| Au1rxx-base64 | 0.698 | 127 | 55 | 182 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19362 | yes | 3.59 | 0 |
| SoliSpirit-all | 6800 | yes | 2.08 | 0 |
| Epodonios-all | 6563 | yes | 2.06 | 0 |
| DeltaKronecker-all | 5572 | yes | 3.6 | 0 |
| Surfboard-tg-mixed | 5429 | yes | 2.82 | 0 |
| mahdibland-V2RayAggregator | 4971 | yes | 1.6 | 0 |
| barry-far-vless | 4890 | yes | 1.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 4757 | yes | 1.57 | 0 |
| xiaoji235-airport-v2ray-all | 4399 | yes | 0.93 | 0 |
| Surfboard-tg-vless | 4227 | yes | 2.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 132 |
| speed | 104 |
| cn-block | 73 |
| 204 | 29 |
