# AutoNodes 每日报告

生成时间：2026-08-06 14:29:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 89832 |
| 去重后节点数 | 24596 |
| TCP 可达数 | 3000 |
| 真测通过数 | 482 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24596 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 26.0 |
| geo | 1.5 |
| probe | 47.5 |
| real_test | 95.6 |
| tcp | 37.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 21 | 18 | 3 | 85.7% |
| shadowsocks | 157 | 142 | 15 | 90.4% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 159 | 156 | 3 | 98.1% |
| vless | 209 | 141 | 68 | 67.5% |
| vmess | 4 | 3 | 1 | 75.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 24 |
| geo:TimeoutError | 18 |
| 204:TimeoutError | 15 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 7 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4983 |
| ConnectionRefusedError | 818 |
| gaierror | 295 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 405 | 0.941 | 1577 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.617 | observe | 119 | 0.538 | 5904 |
| mheidari-all | 0.602 | observe | 17 | 0.588 | 20767 |
| DeltaKronecker-all | 0.461 | observe | 11 | 0.545 | 5897 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 5184 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5219 |
| Epodonios-all | 0.255 | observe | 0 | None | 6534 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7693 |

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
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.538 | 64 | 55 | 119 |
| DeltaKronecker-all | 0.545 | 6 | 5 | 11 |
| mheidari-all | 0.588 | 10 | 7 | 17 |
| Au1rxx-base64 | 0.941 | 381 | 24 | 405 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20767 | yes | 4.97 | 0 |
| SoliSpirit-all | 7693 | yes | 3.86 | 0 |
| Epodonios-all | 6534 | yes | 5.31 | 0 |
| Surfboard-tg-mixed | 5904 | yes | 3.04 | 0 |
| DeltaKronecker-all | 5897 | yes | 4.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 5219 | yes | 2.48 | 0 |
| mahdibland-V2RayAggregator | 5212 | yes | 2.39 | 0 |
| xiaoji235-airport-v2ray-all | 5184 | yes | 2.16 | 0 |
| barry-far-vless | 5092 | yes | 2.29 | 0 |
| Surfboard-tg-vless | 4729 | yes | 3.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 43 |
| 204 | 22 |
| cn-block | 21 |
| speed | 7 |
