# AutoNodes 每日报告

生成时间：2026-07-20 19:54:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 85798 |
| 去重后节点数 | 24302 |
| TCP 可达数 | 3000 |
| 真测通过数 | 415 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24302 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 38.9 |
| geo | 0.9 |
| probe | 61.6 |
| real_test | 132.5 |
| tcp | 33.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 123 | 103 | 20 | 83.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 297 | 214 | 83 | 72.1% |
| vless | 224 | 56 | 168 | 25.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 83 |
| speed:ClientOSError | 65 |
| cn-block:TimeoutError | 62 |
| 204:TimeoutError | 23 |
| geo:ClientOSError | 9 |
| cn-block:ClientOSError | 9 |
| 204:ProxyError | 7 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 3 |
| speed:TimeoutError | 3 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4542 |
| ConnectionRefusedError | 737 |
| gaierror | 517 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.885 | prefer | 228 | 0.86 | 719 |
| mheidari-all | 0.553 | observe | 108 | 0.472 | 19990 |
| Surfboard-tg-mixed | 0.547 | observe | 193 | 0.466 | 5499 |
| DeltaKronecker-all | 0.427 | observe | 119 | 0.345 | 5962 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5035 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4714 |
| Epodonios-all | 0.255 | observe | 0 | None | 6648 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7049 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.345 | 41 | 78 | 119 |
| Surfboard-tg-mixed | 0.466 | 90 | 103 | 193 |
| mheidari-all | 0.472 | 51 | 57 | 108 |
| Au1rxx-base64 | 0.86 | 196 | 32 | 228 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19990 | yes | 4.32 | 0 |
| SoliSpirit-all | 7049 | yes | 2.71 | 0 |
| Epodonios-all | 6648 | yes | 2.02 | 0 |
| DeltaKronecker-all | 5962 | yes | 4.06 | 0 |
| Surfboard-tg-mixed | 5499 | yes | 2.7 | 0 |
| mahdibland-V2RayAggregator | 5173 | yes | 1.09 | 0 |
| xiaoji235-airport-v2ray-all | 5035 | yes | 1.51 | 0 |
| barry-far-vless | 4959 | yes | 1.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 4714 | yes | 1.26 | 0 |
| Surfboard-tg-vless | 4237 | yes | 2.48 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 93 |
| cn-block | 74 |
| speed | 70 |
| 204 | 36 |
