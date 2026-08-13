# AutoNodes 每日报告

生成时间：2026-08-13 07:47:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 79301 |
| 去重后节点数 | 22373 |
| TCP 可达数 | 3000 |
| 真测通过数 | 687 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22373 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 28.4 |
| geo | 1.1 |
| probe | 62.4 |
| real_test | 146.9 |
| tcp | 33.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 17 | 15 | 2 | 88.2% |
| shadowsocks | 164 | 146 | 18 | 89.0% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 250 | 235 | 15 | 94.0% |
| vless | 236 | 157 | 79 | 66.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 31 |
| cn-block:TimeoutError | 20 |
| geo:ClientOSError | 16 |
| 204:TimeoutError | 14 |
| speed:TimeoutError | 8 |
| 204:ProxyError | 7 |
| speed:ClientOSError | 4 |
| geo:ProxyError | 4 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4413 |
| ConnectionRefusedError | 766 |
| gaierror | 314 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 464 | 0.948 | 1501 |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.744 | prefer | 135 | 0.667 | 5801 |
| mheidari-all | 0.616 | observe | 26 | 0.538 | 16910 |
| DeltaKronecker-all | 0.4 | observe | 48 | 0.312 | 4975 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5203 |
| Epodonios-all | 0.255 | observe | 0 | None | 6457 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7624 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4621 |

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
| DeltaKronecker-all | 0.312 | 15 | 33 | 48 |
| mheidari-all | 0.538 | 14 | 12 | 26 |
| Surfboard-tg-mixed | 0.667 | 90 | 45 | 135 |
| Au1rxx-base64 | 0.948 | 440 | 24 | 464 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16910 | yes | 4.11 | 0 |
| SoliSpirit-all | 7624 | yes | 2.64 | 0 |
| Epodonios-all | 6457 | yes | 4.32 | 0 |
| Surfboard-tg-mixed | 5801 | yes | 2.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 5203 | yes | 1.58 | 0 |
| mahdibland-V2RayAggregator | 5197 | yes | 2.44 | 0 |
| barry-far-vless | 4989 | yes | 1.33 | 0 |
| DeltaKronecker-all | 4975 | yes | 4.24 | 0 |
| Surfboard-tg-vless | 4621 | yes | 3.1 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.67 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 52 |
| cn-block | 27 |
| 204 | 24 |
| speed | 12 |
