# AutoNodes 每日报告

生成时间：2026-07-28 14:28:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 86876 |
| 去重后节点数 | 23503 |
| TCP 可达数 | 3000 |
| 真测通过数 | 530 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23503 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 23.6 |
| generate | 41.3 |
| geo | 1.4 |
| probe | 59.1 |
| real_test | 133.8 |
| tcp | 33.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 12 | 8 | 4 | 66.7% |
| shadowsocks | 165 | 149 | 16 | 90.3% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 178 | 153 | 25 | 86.0% |
| vless | 266 | 148 | 118 | 55.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 62 |
| geo:ClientOSError | 23 |
| 204:TimeoutError | 22 |
| speed:ClientOSError | 18 |
| cn-block:TimeoutError | 15 |
| speed:TimeoutError | 10 |
| 204:ProxyError | 9 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4505 |
| ConnectionRefusedError | 750 |
| gaierror | 282 |
| OSError | 222 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 69 | 1.0 | 81 |
| Au1rxx-base64 | 0.965 | prefer | 197 | 0.914 | 1391 |
| mheidari-all | 0.926 | prefer | 50 | 0.86 | 18775 |
| Surfboard-tg-mixed | 0.816 | prefer | 51 | 0.745 | 5928 |
| DeltaKronecker-all | 0.689 | observe | 323 | 0.61 | 5965 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.259 | observe | 3 | 0.333 | 3959 |
| Pawdroid | 0.256 | observe | 1 | 1.0 | 17 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4972 |
| Epodonios-all | 0.255 | observe | 0 | None | 6785 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.333 | 1 | 2 | 3 |
| DeltaKronecker-all | 0.61 | 197 | 126 | 323 |
| Surfboard-tg-mixed | 0.745 | 38 | 13 | 51 |
| mheidari-all | 0.86 | 43 | 7 | 50 |
| Au1rxx-base64 | 0.914 | 180 | 17 | 197 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Pawdroid | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 69 | 0 | 69 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18775 | yes | 4.08 | 0 |
| SoliSpirit-all | 6846 | yes | 2.21 | 0 |
| Epodonios-all | 6785 | yes | 4.54 | 0 |
| DeltaKronecker-all | 5965 | yes | 4.62 | 0 |
| Surfboard-tg-mixed | 5928 | yes | 3.22 | 0 |
| barry-far-vless | 5220 | yes | 1.3 | 0 |
| mahdibland-V2RayAggregator | 4991 | yes | 2.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4972 | yes | 0.85 | 0 |
| Surfboard-tg-vless | 4700 | yes | 2.77 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.38 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 86 |
| 204 | 34 |
| speed | 30 |
| cn-block | 16 |
