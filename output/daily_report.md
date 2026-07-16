# AutoNodes 每日报告

生成时间：2026-07-16 19:24:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79788 |
| 去重后节点数 | 24632 |
| TCP 可达数 | 3000 |
| 真测通过数 | 411 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24632 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 42.4 |
| geo | 0.9 |
| probe | 48.8 |
| real_test | 93.3 |
| tcp | 33.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 113 | 92 | 21 | 81.4% |
| socks | 9 | 7 | 2 | 77.8% |
| trojan | 335 | 265 | 70 | 79.1% |
| vless | 60 | 6 | 54 | 10.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 37 |
| geo:TimeoutError | 35 |
| speed:ClientOSError | 20 |
| cn-block:TimeoutError | 19 |
| 204:ProxyError | 10 |
| 204:ClientOSError | 7 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| speed:TimeoutError | 4 |
| speed:ProxyError | 4 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4612 |
| ConnectionRefusedError | 674 |
| gaierror | 235 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.925 | prefer | 97 | 0.928 | 149 |
| mheidari-all | 0.863 | prefer | 127 | 0.787 | 16694 |
| Surfboard-tg-mixed | 0.771 | prefer | 92 | 0.696 | 5554 |
| DeltaKronecker-all | 0.668 | observe | 202 | 0.589 | 8462 |
| xiaoji235-airport-v2ray-all | 0.325 | observe | 1 | 1.0 | 1757 |
| nscl5-all | 0.316 | observe | 1 | 1.0 | 1519 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4470 |
| Epodonios-all | 0.255 | observe | 0 | None | 6586 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.589 | 119 | 83 | 202 |
| Surfboard-tg-mixed | 0.696 | 64 | 28 | 92 |
| mheidari-all | 0.787 | 100 | 27 | 127 |
| Au1rxx-base64 | 0.928 | 90 | 7 | 97 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16694 | yes | 3.63 | 0 |
| DeltaKronecker-all | 8462 | yes | 3.46 | 0 |
| SoliSpirit-all | 7013 | yes | 2.43 | 0 |
| Epodonios-all | 6586 | yes | 1.85 | 0 |
| Surfboard-tg-mixed | 5554 | yes | 2.12 | 0 |
| mahdibland-V2RayAggregator | 5260 | yes | 1.93 | 0 |
| barry-far-vless | 4954 | yes | 1.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4470 | yes | 1.54 | 0 |
| Surfboard-tg-vless | 4319 | yes | 3.17 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.97 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 54 |
| geo | 37 |
| speed | 28 |
| cn-block | 28 |
