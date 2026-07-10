# AutoNodes 每日报告

生成时间：2026-07-10 09:49:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75289 |
| 去重后节点数 | 23428 |
| TCP 可达数 | 3000 |
| 真测通过数 | 250 |
| verified 输出数 | 250 |
| global 输出数 | 279 |
| all 输出数 | 23428 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 45.6 |
| geo | 1.4 |
| probe | 53.6 |
| real_test | 94.4 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 93 | 83 | 10 | 89.2% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 199 | 109 | 90 | 54.8% |
| vless | 53 | 14 | 39 | 26.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 32 |
| cn-block:ProxyError | 16 |
| speed:ClientOSError | 14 |
| geo:TimeoutError | 14 |
| cn-block:TimeoutError | 12 |
| cn-block:ClientOSError | 10 |
| geo:ProxyError | 10 |
| 204:ClientOSError | 7 |
| 204:TimeoutError | 7 |
| speed:ProxyError | 7 |
| geo:ClientOSError | 6 |
| speed:TimeoutError | 5 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4272 |
| ConnectionRefusedError | 662 |
| gaierror | 271 |
| OSError | 177 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.87 | prefer | 28 | 0.893 | 75 |
| Surfboard-tg-mixed | 0.747 | prefer | 91 | 0.67 | 5466 |
| mheidari-all | 0.624 | observe | 66 | 0.545 | 15738 |
| DeltaKronecker-all | 0.622 | observe | 166 | 0.542 | 7600 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1148 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4165 |
| Epodonios-all | 0.255 | observe | 0 | None | 6278 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.542 | 90 | 76 | 166 |
| mheidari-all | 0.545 | 36 | 30 | 66 |
| Surfboard-tg-mixed | 0.67 | 61 | 30 | 91 |
| Au1rxx-base64 | 0.893 | 25 | 3 | 28 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15738 | yes | 3.49 | 0 |
| DeltaKronecker-all | 7600 | yes | 3.65 | 0 |
| SoliSpirit-all | 6680 | yes | 2.33 | 0 |
| Epodonios-all | 6278 | yes | 0.91 | 0 |
| Surfboard-tg-mixed | 5466 | yes | 0.34 | 0 |
| mahdibland-V2RayAggregator | 5391 | yes | 2.79 | 0 |
| barry-far-vless | 4587 | yes | 1.63 | 0 |
| 10ium-ScrapeCategorize-Vless | 4165 | yes | 1.47 | 0 |
| Surfboard-tg-vless | 4082 | yes | 2.61 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.96 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 46 |
| cn-block | 38 |
| geo | 30 |
| speed | 26 |
