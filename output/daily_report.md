# AutoNodes 每日报告

生成时间：2026-07-29 03:18:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76585 |
| 去重后节点数 | 21579 |
| TCP 可达数 | 3000 |
| 真测通过数 | 604 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21579 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| generate | 28.1 |
| geo | 1.3 |
| probe | 53.7 |
| real_test | 134.4 |
| tcp | 31.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 64 | 64 | 0 | 100.0% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 206 | 189 | 17 | 91.7% |
| socks | 9 | 5 | 4 | 55.6% |
| trojan | 87 | 80 | 7 | 92.0% |
| vless | 487 | 251 | 236 | 51.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 87 |
| speed:TimeoutError | 45 |
| speed:ClientOSError | 42 |
| cn-block:TimeoutError | 34 |
| geo:ClientOSError | 27 |
| 204:TimeoutError | 10 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4145 |
| ConnectionRefusedError | 741 |
| gaierror | 308 |
| OSError | 221 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.982 | prefer | 294 | 0.939 | 1151 |
| zhangkai | 0.977 | prefer | 65 | 0.985 | 167 |
| DeltaKronecker-all | 0.889 | prefer | 134 | 0.813 | 4038 |
| Surfboard-tg-mixed | 0.602 | observe | 21 | 0.524 | 5708 |
| mheidari-all | 0.487 | observe | 347 | 0.406 | 17232 |
| 10ium-ScrapeCategorize-Vless | 0.349 | observe | 3 | 0.667 | 4972 |
| tg-Farah_VPN | 0.263 | observe | 1 | 1.0 | 200 |
| Epodonios-all | 0.255 | observe | 0 | None | 6752 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3968 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6491 |

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
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.406 | 141 | 206 | 347 |
| Surfboard-tg-mixed | 0.524 | 11 | 10 | 21 |
| 10ium-ScrapeCategorize-Vless | 0.667 | 2 | 1 | 3 |
| DeltaKronecker-all | 0.813 | 109 | 25 | 134 |
| Au1rxx-base64 | 0.939 | 276 | 18 | 294 |
| zhangkai | 0.985 | 64 | 1 | 65 |
| tg-Farah_VPN | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17232 | yes | 3.81 | 0 |
| Epodonios-all | 6752 | yes | 2.7 | 0 |
| SoliSpirit-all | 6491 | yes | 2.94 | 0 |
| Surfboard-tg-mixed | 5708 | yes | 3.07 | 0 |
| mahdibland-V2RayAggregator | 5059 | yes | 2.19 | 0 |
| barry-far-vless | 5026 | yes | 1.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 4972 | yes | 2.1 | 0 |
| Surfboard-tg-vless | 4480 | yes | 2.35 | 0 |
| DeltaKronecker-all | 4038 | yes | 3.53 | 0 |
| MatinGhanbari-all-sub | 3968 | yes | 2.69 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 114 |
| speed | 87 |
| cn-block | 43 |
| 204 | 20 |
