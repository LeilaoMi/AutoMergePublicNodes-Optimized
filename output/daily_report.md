# AutoNodes 每日报告

生成时间：2026-07-16 03:16:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 76031 |
| 去重后节点数 | 23073 |
| TCP 可达数 | 3000 |
| 真测通过数 | 438 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23073 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.6 |
| generate | 21.6 |
| geo | 1.4 |
| probe | 44.6 |
| real_test | 83.9 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 140 | 130 | 10 | 92.9% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 265 | 248 | 17 | 93.6% |
| vless | 100 | 13 | 87 | 13.0% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 44 |
| geo:TimeoutError | 32 |
| geo:ClientOSError | 16 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| 204:ProxyError | 3 |
| cn-block:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4523 |
| ConnectionRefusedError | 661 |
| gaierror | 259 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.961 | prefer | 88 | 0.966 | 148 |
| mheidari-all | 0.895 | prefer | 144 | 0.819 | 16541 |
| DeltaKronecker-all | 0.8 | prefer | 159 | 0.723 | 6421 |
| Surfboard-tg-mixed | 0.755 | prefer | 118 | 0.678 | 5384 |
| xiaoji235-airport-v2ray-all | 0.325 | observe | 1 | 1.0 | 1757 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3759 |
| Epodonios-all | 0.255 | observe | 0 | None | 6430 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| nscl5-all | 0.165 | observe | 2 | 0.0 | 0 | 1519 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 2 | 2 |
| Surfboard-tg-mixed | 0.678 | 80 | 38 | 118 |
| DeltaKronecker-all | 0.723 | 115 | 44 | 159 |
| mheidari-all | 0.819 | 118 | 26 | 144 |
| Au1rxx-base64 | 0.966 | 85 | 3 | 88 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16541 | yes | 2.73 | 0 |
| SoliSpirit-all | 6934 | yes | 1.39 | 0 |
| Epodonios-all | 6430 | yes | 1.46 | 0 |
| DeltaKronecker-all | 6421 | yes | 2.85 | 0 |
| Surfboard-tg-mixed | 5384 | yes | 1.7 | 0 |
| mahdibland-V2RayAggregator | 5183 | yes | 1.24 | 0 |
| barry-far-vless | 4781 | yes | 1.03 | 0 |
| Surfboard-tg-vless | 4135 | yes | 1.56 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 1.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 3759 | yes | 1.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 50 |
| geo | 48 |
| cn-block | 11 |
| 204 | 6 |
