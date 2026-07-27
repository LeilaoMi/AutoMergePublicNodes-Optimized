# AutoNodes 每日报告

生成时间：2026-07-27 19:47:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 85905 |
| 去重后节点数 | 22931 |
| TCP 可达数 | 3000 |
| 真测通过数 | 712 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22931 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 37.9 |
| geo | 1.4 |
| probe | 65.2 |
| real_test | 169.4 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 59 | 0 | 100.0% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 131 | 99 | 32 | 75.6% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 417 | 389 | 28 | 93.3% |
| vless | 330 | 152 | 178 | 46.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 94 |
| speed:ClientOSError | 59 |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 16 |
| geo:ClientOSError | 15 |
| cn-block:ClientOSError | 11 |
| speed:TimeoutError | 10 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4338 |
| ConnectionRefusedError | 751 |
| gaierror | 296 |
| OSError | 222 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.987 | prefer | 59 | 1.0 | 74 |
| Au1rxx-base64 | 0.975 | prefer | 446 | 0.917 | 1499 |
| DeltaKronecker-all | 0.672 | observe | 69 | 0.594 | 5643 |
| mheidari-all | 0.627 | observe | 358 | 0.547 | 19371 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 3959 |
| Surfboard-tg-mixed | 0.326 | observe | 15 | 0.267 | 5739 |
| tg-Farah_VPN | 0.263 | observe | 1 | 1.0 | 200 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4831 |
| Epodonios-all | 0.255 | observe | 0 | None | 6710 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3964 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.267 | 4 | 11 | 15 |
| mheidari-all | 0.547 | 196 | 162 | 358 |
| DeltaKronecker-all | 0.594 | 41 | 28 | 69 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.917 | 409 | 37 | 446 |
| tg-Farah_VPN | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 59 | 0 | 59 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19371 | yes | 4.53 | 0 |
| Epodonios-all | 6710 | yes | 0.7 | 0 |
| SoliSpirit-all | 6251 | yes | 3.06 | 0 |
| Surfboard-tg-mixed | 5739 | yes | 4.11 | 0 |
| DeltaKronecker-all | 5643 | yes | 4.32 | 0 |
| barry-far-vless | 5170 | yes | 0.71 | 0 |
| mahdibland-V2RayAggregator | 4997 | yes | 0.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4831 | yes | 0.88 | 0 |
| Surfboard-tg-vless | 4648 | yes | 1.29 | 0 |
| MatinGhanbari-all-sub | 3964 | yes | 1.97 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 111 |
| speed | 70 |
| cn-block | 30 |
| 204 | 30 |
