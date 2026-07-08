# AutoNodes 每日报告

生成时间：2026-07-08 08:41:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 83146 |
| 去重后节点数 | 24737 |
| TCP 可达数 | 3000 |
| 真测通过数 | 356 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24737 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 26.0 |
| geo | 1.3 |
| probe | 43.5 |
| real_test | 88.1 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 4 | 1 | 80.0% |
| shadowsocks | 125 | 109 | 16 | 87.2% |
| socks | 7 | 6 | 1 | 85.7% |
| trojan | 205 | 176 | 29 | 85.9% |
| vless | 70 | 19 | 51 | 27.1% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 29 |
| speed:ClientOSError | 20 |
| 204:ProxyError | 10 |
| cn-block:TimeoutError | 7 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 7 |
| geo:ClientOSError | 5 |
| speed:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4638 |
| ConnectionRefusedError | 809 |
| OSError | 170 |
| gaierror | 69 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.859 | prefer | 84 | 0.786 | 17974 |
| Au1rxx-base64 | 0.846 | prefer | 67 | 0.851 | 134 |
| DeltaKronecker-all | 0.842 | prefer | 141 | 0.766 | 8321 |
| Surfboard-tg-mixed | 0.787 | prefer | 121 | 0.711 | 5842 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 3640 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4408 |
| Epodonios-all | 0.255 | observe | 0 | None | 6817 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 11 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.711 | 86 | 35 | 121 |
| DeltaKronecker-all | 0.766 | 108 | 33 | 141 |
| mheidari-all | 0.786 | 66 | 18 | 84 |
| Au1rxx-base64 | 0.851 | 57 | 10 | 67 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17974 | yes | 3.71 | 0 |
| DeltaKronecker-all | 8321 | yes | 3.71 | 0 |
| Epodonios-all | 6817 | yes | 3.11 | 0 |
| SoliSpirit-all | 6807 | yes | 2.98 | 0 |
| Surfboard-tg-mixed | 5842 | yes | 2.41 | 0 |
| mahdibland-V2RayAggregator | 5352 | yes | 0.48 | 0 |
| barry-far-vless | 4981 | yes | 1.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4408 | yes | 1.03 | 0 |
| Surfboard-tg-vless | 4337 | yes | 1.95 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 1.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 36 |
| speed | 25 |
| 204 | 24 |
| cn-block | 13 |
