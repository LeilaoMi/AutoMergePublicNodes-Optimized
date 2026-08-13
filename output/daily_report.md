# AutoNodes 每日报告

生成时间：2026-08-13 02:29:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 79753 |
| 去重后节点数 | 22383 |
| TCP 可达数 | 3000 |
| 真测通过数 | 669 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22383 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 23.5 |
| geo | 1.4 |
| probe | 60.4 |
| real_test | 167.7 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 23 | 20 | 3 | 87.0% |
| shadowsocks | 171 | 161 | 10 | 94.2% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 145 | 130 | 15 | 89.7% |
| vless | 680 | 226 | 454 | 33.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 237 |
| geo:ClientOSError | 93 |
| speed:TimeoutError | 71 |
| speed:ClientOSError | 42 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4232 |
| ConnectionRefusedError | 792 |
| gaierror | 376 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Au1rxx-base64 | 0.934 | prefer | 403 | 0.876 | 1489 |
| Surfboard-tg-mixed | 0.71 | prefer | 163 | 0.632 | 5894 |
| mheidari-all | 0.432 | observe | 14 | 0.429 | 16809 |
| DeltaKronecker-all | 0.262 | observe | 438 | 0.18 | 4975 |
| Epodonios-all | 0.255 | observe | 0 | None | 6571 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7660 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4734 |
| barry-far-vless | 0.255 | observe | 0 | None | 5066 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| 10ium-ScrapeCategorize-Vless | 0.17 | observe | 3 | 0.0 | 0 | 5328 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.18 | 79 | 359 | 438 |
| mheidari-all | 0.429 | 6 | 8 | 14 |
| Surfboard-tg-mixed | 0.632 | 103 | 60 | 163 |
| Au1rxx-base64 | 0.876 | 353 | 50 | 403 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16809 | yes | 4.92 | 0 |
| SoliSpirit-all | 7660 | yes | 3.18 | 0 |
| Epodonios-all | 6571 | yes | 2.9 | 0 |
| Surfboard-tg-mixed | 5894 | yes | 3.86 | 0 |
| 10ium-ScrapeCategorize-Vless | 5328 | yes | 2.47 | 0 |
| mahdibland-V2RayAggregator | 5209 | yes | 2.64 | 0 |
| barry-far-vless | 5066 | yes | 2.15 | 0 |
| DeltaKronecker-all | 4975 | yes | 3.85 | 0 |
| Surfboard-tg-vless | 4734 | yes | 3.66 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 330 |
| speed | 115 |
| cn-block | 23 |
| 204 | 16 |
