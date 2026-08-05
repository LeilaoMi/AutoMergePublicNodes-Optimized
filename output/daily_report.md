# AutoNodes 每日报告

生成时间：2026-08-05 03:00:30

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 86570 |
| 去重后节点数 | 24353 |
| TCP 可达数 | 3000 |
| 真测通过数 | 652 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24353 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 25.7 |
| geo | 1.3 |
| probe | 63.3 |
| real_test | 204.1 |
| tcp | 36.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 53 | 53 | 0 | 100.0% |
| hysteria2 | 20 | 20 | 0 | 100.0% |
| shadowsocks | 167 | 153 | 14 | 91.6% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 178 | 150 | 28 | 84.3% |
| vless | 823 | 271 | 552 | 32.9% |
| vmess | 4 | 2 | 2 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 291 |
| speed:ClientOSError | 133 |
| geo:ClientOSError | 55 |
| cn-block:TimeoutError | 55 |
| speed:TimeoutError | 29 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 9 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |
| cn-block:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4944 |
| ConnectionRefusedError | 854 |
| gaierror | 299 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 401 | 0.945 | 1440 |
| zhangkai | 0.984 | prefer | 51 | 1.0 | 72 |
| Surfboard-tg-mixed | 0.651 | observe | 26 | 0.577 | 5655 |
| DeltaKronecker-all | 0.354 | observe | 716 | 0.274 | 5788 |
| tg-oneclickvpnkeys | 0.318 | observe | 2 | 1.0 | 161 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5251 |
| Epodonios-all | 0.255 | observe | 0 | None | 6252 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7076 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | mheidari-all | 0.25 | 51 | 0.157 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.157 | 8 | 43 | 51 |
| DeltaKronecker-all | 0.274 | 196 | 520 | 716 |
| Surfboard-tg-mixed | 0.577 | 15 | 11 | 26 |
| Au1rxx-base64 | 0.945 | 379 | 22 | 401 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 51 | 0 | 51 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20244 | yes | 4.93 | 0 |
| SoliSpirit-all | 7076 | yes | 1.71 | 0 |
| Epodonios-all | 6252 | yes | 3.2 | 0 |
| DeltaKronecker-all | 5788 | yes | 3.66 | 0 |
| Surfboard-tg-mixed | 5655 | yes | 2.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 5251 | yes | 1.08 | 0 |
| mahdibland-V2RayAggregator | 5141 | yes | 2.08 | 0 |
| barry-far-vless | 4815 | yes | 1.22 | 0 |
| xiaoji235-airport-v2ray-all | 4655 | yes | 2.55 | 0 |
| Surfboard-tg-vless | 4478 | yes | 2.53 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 347 |
| speed | 163 |
| cn-block | 58 |
| 204 | 29 |
