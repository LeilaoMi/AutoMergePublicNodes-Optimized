# AutoNodes 每日报告

生成时间：2026-07-09 03:53:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80290 |
| 去重后节点数 | 24881 |
| TCP 可达数 | 3000 |
| 真测通过数 | 391 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24881 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 36.0 |
| geo | 1.4 |
| probe | 47.1 |
| real_test | 81.9 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 3 | 1 | 75.0% |
| shadowsocks | 134 | 126 | 8 | 94.0% |
| socks | 13 | 11 | 2 | 84.6% |
| trojan | 159 | 140 | 19 | 88.1% |
| vless | 226 | 70 | 156 | 31.0% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 86 |
| speed:ClientOSError | 55 |
| geo:ClientOSError | 19 |
| 204:ClientOSError | 8 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:TimeoutError | 3 |
| 204:ProxyError | 1 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4652 |
| ConnectionRefusedError | 829 |
| OSError | 174 |
| gaierror | 171 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.936 | prefer | 56 | 0.946 | 128 |
| Surfboard-tg-mixed | 0.923 | prefer | 81 | 0.852 | 5750 |
| mheidari-all | 0.822 | prefer | 91 | 0.747 | 17104 |
| DeltaKronecker-all | 0.608 | observe | 305 | 0.528 | 8321 |
| xiaoji235-airport-v2ray-all | 0.4 | observe | 4 | 0.75 | 2703 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4408 |
| Epodonios-all | 0.255 | observe | 0 | None | 6606 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6800 |

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
| ermaozi | 0.175 | observe | 0 | None | 0 | 2 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 2 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.528 | 161 | 144 | 305 |
| mheidari-all | 0.747 | 68 | 23 | 91 |
| xiaoji235-airport-v2ray-all | 0.75 | 3 | 1 | 4 |
| Surfboard-tg-mixed | 0.852 | 69 | 12 | 81 |
| Au1rxx-base64 | 0.946 | 53 | 3 | 56 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17104 | yes | 3.08 | 0 |
| DeltaKronecker-all | 8321 | yes | 3.64 | 0 |
| SoliSpirit-all | 6800 | yes | 2.05 | 0 |
| Epodonios-all | 6606 | yes | 1.61 | 0 |
| Surfboard-tg-mixed | 5750 | yes | 2.63 | 0 |
| mahdibland-V2RayAggregator | 5361 | yes | 1.41 | 0 |
| barry-far-vless | 4787 | yes | 0.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 4408 | yes | 0.6 | 0 |
| Surfboard-tg-vless | 4251 | yes | 2.39 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 1.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 105 |
| speed | 61 |
| 204 | 12 |
| cn-block | 8 |
