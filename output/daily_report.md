# AutoNodes 每日报告

生成时间：2026-08-04 08:52:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 85567 |
| 去重后节点数 | 24255 |
| TCP 可达数 | 3000 |
| 真测通过数 | 548 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24255 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 27.2 |
| geo | 1.4 |
| probe | 65.4 |
| real_test | 152.9 |
| tcp | 36.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 67 | 67 | 0 | 100.0% |
| hysteria2 | 19 | 17 | 2 | 89.5% |
| shadowsocks | 143 | 121 | 22 | 84.6% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 129 | 119 | 10 | 92.2% |
| vless | 439 | 221 | 218 | 50.3% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 129 |
| speed:TimeoutError | 44 |
| 204:TimeoutError | 23 |
| speed:ClientOSError | 12 |
| 204:ProxyError | 11 |
| 204:ClientOSError | 10 |
| cn-block:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4703 |
| ConnectionRefusedError | 798 |
| gaierror | 304 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 67 | 1.0 | 92 |
| Au1rxx-base64 | 0.81 | prefer | 589 | 0.744 | 1672 |
| DeltaKronecker-all | 0.423 | observe | 33 | 0.333 | 5788 |
| mheidari-all | 0.393 | observe | 30 | 0.3 | 20242 |
| Surfboard-tg-mixed | 0.353 | observe | 75 | 0.267 | 5211 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 6811 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 178 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 57 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5251 |
| Epodonios-all | 0.255 | observe | 0 | None | 5819 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.152 | observe | 4 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| Surfboard-tg-mixed | 0.267 | 20 | 55 | 75 |
| mheidari-all | 0.3 | 9 | 21 | 30 |
| DeltaKronecker-all | 0.333 | 11 | 22 | 33 |
| Au1rxx-base64 | 0.744 | 438 | 151 | 589 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20242 | yes | 6.0 | 0 |
| SoliSpirit-all | 6811 | yes | 2.27 | 0 |
| Epodonios-all | 5819 | yes | 4.64 | 0 |
| DeltaKronecker-all | 5788 | yes | 4.85 | 0 |
| 10ium-ScrapeCategorize-Vless | 5251 | yes | 0.71 | 0 |
| Surfboard-tg-mixed | 5211 | yes | 3.83 | 0 |
| xiaoji235-airport-v2ray-all | 5127 | yes | 1.68 | 0 |
| mahdibland-V2RayAggregator | 5110 | yes | 3.07 | 0 |
| barry-far-vless | 4536 | yes | 1.02 | 0 |
| Surfboard-tg-vless | 4191 | yes | 3.5 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 138 |
| speed | 56 |
| 204 | 44 |
| cn-block | 17 |
