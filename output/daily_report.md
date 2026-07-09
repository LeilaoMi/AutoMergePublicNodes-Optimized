# AutoNodes 每日报告

生成时间：2026-07-09 10:08:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 79146 |
| 去重后节点数 | 23828 |
| TCP 可达数 | 3000 |
| 真测通过数 | 320 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23828 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 35.4 |
| geo | 1.3 |
| probe | 51.0 |
| real_test | 99.1 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 109 | 90 | 19 | 82.6% |
| socks | 9 | 7 | 2 | 77.8% |
| trojan | 180 | 91 | 89 | 50.6% |
| vless | 214 | 86 | 128 | 40.2% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 83 |
| 204:ProxyError | 40 |
| geo:TimeoutError | 33 |
| 204:TimeoutError | 23 |
| geo:ClientOSError | 11 |
| cn-block:TimeoutError | 11 |
| 204:ClientOSError | 9 |
| geo:ProxyError | 9 |
| cn-block:ProxyError | 7 |
| cn-block:ClientOSError | 5 |
| speed:TimeoutError | 4 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4475 |
| ConnectionRefusedError | 828 |
| gaierror | 262 |
| OSError | 173 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.743 | prefer | 63 | 0.746 | 118 |
| DeltaKronecker-all | 0.645 | observe | 113 | 0.566 | 7533 |
| mheidari-all | 0.586 | observe | 75 | 0.507 | 17088 |
| Surfboard-tg-mixed | 0.574 | observe | 265 | 0.494 | 5778 |
| xiaoji235-airport-v2ray-all | 0.48 | observe | 4 | 1.0 | 2703 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4306 |
| Epodonios-all | 0.255 | observe | 0 | None | 6686 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6293 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 2 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.494 | 131 | 134 | 265 |
| mheidari-all | 0.507 | 38 | 37 | 75 |
| DeltaKronecker-all | 0.566 | 64 | 49 | 113 |
| Au1rxx-base64 | 0.746 | 47 | 16 | 63 |
| xiaoji235-airport-v2ray-all | 1.0 | 4 | 0 | 4 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17088 | yes | 3.8 | 0 |
| DeltaKronecker-all | 7533 | yes | 4.14 | 0 |
| Epodonios-all | 6686 | yes | 1.77 | 0 |
| SoliSpirit-all | 6293 | yes | 2.5 | 0 |
| Surfboard-tg-mixed | 5778 | yes | 2.48 | 0 |
| mahdibland-V2RayAggregator | 5440 | yes | 1.87 | 0 |
| barry-far-vless | 4851 | yes | 2.02 | 0 |
| 10ium-ScrapeCategorize-Vless | 4306 | yes | 1.39 | 0 |
| Surfboard-tg-vless | 4286 | yes | 2.84 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 0.96 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 90 |
| 204 | 72 |
| geo | 53 |
| cn-block | 23 |
