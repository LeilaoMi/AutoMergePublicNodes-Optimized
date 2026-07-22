# AutoNodes 每日报告

生成时间：2026-07-22 08:42:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 82215 |
| 去重后节点数 | 22710 |
| TCP 可达数 | 3000 |
| 真测通过数 | 659 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22710 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 43.6 |
| geo | 1.2 |
| probe | 60.2 |
| real_test | 168.3 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 139 | 117 | 22 | 84.2% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 450 | 413 | 37 | 91.8% |
| vless | 429 | 87 | 342 | 20.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 224 |
| speed:ClientOSError | 77 |
| cn-block:TimeoutError | 36 |
| speed:TimeoutError | 18 |
| geo:ClientOSError | 16 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 10 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4160 |
| ConnectionRefusedError | 678 |
| gaierror | 353 |
| OSError | 221 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.846 | prefer | 202 | 0.832 | 432 |
| Surfboard-tg-mixed | 0.674 | observe | 195 | 0.595 | 5352 |
| mheidari-all | 0.641 | observe | 570 | 0.561 | 19493 |
| DeltaKronecker-all | 0.402 | observe | 57 | 0.316 | 5212 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 4246 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4613 |
| Epodonios-all | 0.255 | observe | 0 | None | 6417 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3972 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6813 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.316 | 18 | 39 | 57 |
| mheidari-all | 0.561 | 320 | 250 | 570 |
| Surfboard-tg-mixed | 0.595 | 116 | 79 | 195 |
| Au1rxx-base64 | 0.832 | 168 | 34 | 202 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19493 | yes | 3.51 | 0 |
| SoliSpirit-all | 6813 | yes | 2.74 | 0 |
| Epodonios-all | 6417 | yes | 3.7 | 0 |
| Surfboard-tg-mixed | 5352 | yes | 2.3 | 0 |
| DeltaKronecker-all | 5212 | yes | 3.4 | 0 |
| mahdibland-V2RayAggregator | 5204 | yes | 1.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 4613 | yes | 1.34 | 0 |
| barry-far-vless | 4606 | yes | 1.13 | 0 |
| xiaoji235-airport-v2ray-all | 4246 | yes | 0.95 | 0 |
| Surfboard-tg-vless | 4161 | yes | 2.09 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 240 |
| speed | 95 |
| cn-block | 45 |
| 204 | 23 |
