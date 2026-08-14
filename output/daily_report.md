# AutoNodes 每日报告

生成时间：2026-08-14 07:44:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 81257 |
| 去重后节点数 | 23189 |
| TCP 可达数 | 3000 |
| 真测通过数 | 847 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23189 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 33.0 |
| geo | 1.3 |
| probe | 66.9 |
| real_test | 172.5 |
| tcp | 34.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 178 | 169 | 9 | 94.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 350 | 334 | 16 | 95.4% |
| vless | 313 | 196 | 117 | 62.6% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 57 |
| geo:ClientOSError | 21 |
| speed:ClientOSError | 20 |
| speed:TimeoutError | 16 |
| cn-block:TimeoutError | 11 |
| 204:TimeoutError | 9 |
| 204:ProxyError | 6 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4485 |
| ConnectionRefusedError | 773 |
| gaierror | 301 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 652 | 0.939 | 1671 |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.705 | prefer | 102 | 0.627 | 5896 |
| DeltaKronecker-all | 0.471 | observe | 90 | 0.389 | 5969 |
| mheidari-all | 0.432 | observe | 14 | 0.429 | 16991 |
| nscl5-all | 0.326 | observe | 1 | 1.0 | 1768 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5157 |
| Epodonios-all | 0.255 | observe | 0 | None | 6568 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.389 | 35 | 55 | 90 |
| mheidari-all | 0.429 | 6 | 8 | 14 |
| Surfboard-tg-mixed | 0.627 | 64 | 38 | 102 |
| Au1rxx-base64 | 0.939 | 612 | 40 | 652 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16991 | yes | 4.17 | 0 |
| SoliSpirit-all | 7698 | yes | 2.7 | 0 |
| Epodonios-all | 6568 | yes | 4.39 | 0 |
| DeltaKronecker-all | 5969 | yes | 4.77 | 0 |
| Surfboard-tg-mixed | 5896 | yes | 3.63 | 0 |
| mahdibland-V2RayAggregator | 5332 | yes | 2.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 5157 | yes | 1.38 | 0 |
| barry-far-vless | 4969 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 4633 | yes | 3.01 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.66 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 79 |
| speed | 36 |
| 204 | 16 |
| cn-block | 13 |
