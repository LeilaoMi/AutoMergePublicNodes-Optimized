# AutoNodes 每日报告

生成时间：2026-08-11 19:13:53

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 81101 |
| 去重后节点数 | 23129 |
| TCP 可达数 | 3000 |
| 真测通过数 | 563 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23129 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 13.3 |
| generate | 38.2 |
| geo | 1.3 |
| probe | 51.9 |
| real_test | 117.8 |
| tcp | 35.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 125 | 125 | 0 | 100.0% |
| hysteria2 | 22 | 19 | 3 | 86.4% |
| shadowsocks | 146 | 127 | 19 | 87.0% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 112 | 108 | 4 | 96.4% |
| vless | 243 | 181 | 62 | 74.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 20 |
| 204:TimeoutError | 15 |
| cn-block:TimeoutError | 12 |
| speed:TimeoutError | 11 |
| geo:ClientOSError | 9 |
| 204:ClientOSError | 7 |
| geo:TimeoutError | 6 |
| speed:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4621 |
| ConnectionRefusedError | 793 |
| gaierror | 315 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.998 | prefer | 125 | 1.0 | 159 |
| Au1rxx-base64 | 0.933 | prefer | 375 | 0.875 | 1503 |
| Surfboard-tg-mixed | 0.822 | prefer | 95 | 0.747 | 6169 |
| mheidari-all | 0.792 | prefer | 50 | 0.72 | 16649 |
| DeltaKronecker-all | 0.3 | observe | 5 | 0.4 | 5522 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5419 |
| Epodonios-all | 0.255 | observe | 0 | None | 6745 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7634 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.4 | 2 | 3 | 5 |
| mheidari-all | 0.72 | 36 | 14 | 50 |
| Surfboard-tg-mixed | 0.747 | 71 | 24 | 95 |
| Au1rxx-base64 | 0.875 | 328 | 47 | 375 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 125 | 0 | 125 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16649 | yes | 4.56 | 0 |
| SoliSpirit-all | 7634 | yes | 3.28 | 0 |
| Epodonios-all | 6745 | yes | 2.58 | 0 |
| Surfboard-tg-mixed | 6169 | yes | 3.13 | 0 |
| DeltaKronecker-all | 5522 | yes | 4.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 5419 | yes | 1.43 | 0 |
| barry-far-vless | 5313 | yes | 0.99 | 0 |
| mahdibland-V2RayAggregator | 5196 | yes | 2.66 | 0 |
| Surfboard-tg-vless | 5045 | yes | 3.5 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.82 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 42 |
| geo | 16 |
| speed | 16 |
| cn-block | 15 |
