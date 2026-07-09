# AutoNodes 每日报告

生成时间：2026-07-09 15:25:21

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79415 |
| 去重后节点数 | 23963 |
| TCP 可达数 | 3000 |
| 真测通过数 | 242 |
| verified 输出数 | 242 |
| global 输出数 | 248 |
| all 输出数 | 23963 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 19.8 |
| geo | 1.3 |
| probe | 45.0 |
| real_test | 58.4 |
| tcp | 31.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 113 | 105 | 8 | 92.9% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 57 | 40 | 17 | 70.2% |
| vless | 172 | 48 | 124 | 27.9% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 83 |
| geo:TimeoutError | 28 |
| 204:ClientOSError | 9 |
| cn-block:ClientOSError | 7 |
| geo:ClientOSError | 7 |
| 204:TimeoutError | 5 |
| speed:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:TimeoutError | 2 |
| 204:ProxyError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4265 |
| ConnectionRefusedError | 859 |
| gaierror | 360 |
| OSError | 174 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.891 | prefer | 51 | 0.824 | 5805 |
| mheidari-all | 0.791 | prefer | 36 | 0.722 | 16991 |
| Au1rxx-base64 | 0.765 | prefer | 73 | 0.767 | 119 |
| DeltaKronecker-all | 0.492 | observe | 192 | 0.411 | 7533 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 2703 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4306 |
| Epodonios-all | 0.255 | observe | 0 | None | 6648 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3977 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6653 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 8 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.411 | 79 | 113 | 192 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.722 | 26 | 10 | 36 |
| Au1rxx-base64 | 0.767 | 56 | 17 | 73 |
| Surfboard-tg-mixed | 0.824 | 42 | 9 | 51 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16991 | yes | 3.15 | 0 |
| DeltaKronecker-all | 7533 | yes | 3.08 | 0 |
| SoliSpirit-all | 6653 | yes | 2.73 | 0 |
| Epodonios-all | 6648 | yes | 1.78 | 0 |
| Surfboard-tg-mixed | 5805 | yes | 2.67 | 0 |
| mahdibland-V2RayAggregator | 5440 | yes | 1.61 | 0 |
| barry-far-vless | 4797 | yes | 1.11 | 0 |
| Surfboard-tg-vless | 4318 | yes | 2.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 4306 | yes | 1.32 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 1.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 88 |
| geo | 36 |
| 204 | 15 |
| cn-block | 12 |
