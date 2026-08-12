# AutoNodes 每日报告

生成时间：2026-08-12 02:27:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 80730 |
| 去重后节点数 | 22951 |
| TCP 可达数 | 3000 |
| 真测通过数 | 699 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22951 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 36.4 |
| geo | 1.5 |
| probe | 56.0 |
| real_test | 156.0 |
| tcp | 34.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 20 | 17 | 3 | 85.0% |
| shadowsocks | 166 | 155 | 11 | 93.4% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 140 | 119 | 21 | 85.0% |
| vless | 557 | 278 | 279 | 49.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 107 |
| geo:ClientOSError | 56 |
| speed:TimeoutError | 50 |
| cn-block:TimeoutError | 40 |
| speed:ClientOSError | 27 |
| 204:TimeoutError | 20 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |
| speed:ClientPayloadError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4690 |
| ConnectionRefusedError | 775 |
| gaierror | 258 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Au1rxx-base64 | 0.919 | prefer | 446 | 0.854 | 1650 |
| Surfboard-tg-mixed | 0.749 | prefer | 161 | 0.671 | 5950 |
| mheidari-all | 0.494 | observe | 172 | 0.413 | 16697 |
| nscl5-all | 0.267 | observe | 2 | 0.5 | 1481 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5419 |
| Epodonios-all | 0.255 | observe | 0 | None | 6635 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7586 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4851 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.175 | 103 | 0.087 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.087 | 9 | 94 | 103 |
| ninja-vless | 0.333 | 1 | 2 | 3 |
| mheidari-all | 0.413 | 71 | 101 | 172 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.671 | 108 | 53 | 161 |
| Au1rxx-base64 | 0.854 | 381 | 65 | 446 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16697 | yes | 3.22 | 0 |
| SoliSpirit-all | 7586 | yes | 2.29 | 0 |
| Epodonios-all | 6635 | yes | 2.17 | 0 |
| Surfboard-tg-mixed | 5950 | yes | 3.41 | 0 |
| DeltaKronecker-all | 5522 | yes | 3.43 | 0 |
| 10ium-ScrapeCategorize-Vless | 5419 | yes | 1.96 | 0 |
| barry-far-vless | 5220 | yes | 1.79 | 0 |
| mahdibland-V2RayAggregator | 5196 | yes | 1.91 | 0 |
| Surfboard-tg-vless | 4851 | yes | 2.29 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.03 | 0 |

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
| geo | 164 |
| speed | 78 |
| cn-block | 47 |
| 204 | 28 |
