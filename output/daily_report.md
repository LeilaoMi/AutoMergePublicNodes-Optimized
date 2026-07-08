# AutoNodes 每日报告

生成时间：2026-07-08 14:31:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83404 |
| 去重后节点数 | 24825 |
| TCP 可达数 | 3000 |
| 真测通过数 | 280 |
| verified 输出数 | 280 |
| global 输出数 | 292 |
| all 输出数 | 24825 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 35.2 |
| geo | 1.3 |
| probe | 43.3 |
| real_test | 78.2 |
| tcp | 32.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 4 | 1 | 80.0% |
| shadowsocks | 131 | 110 | 21 | 84.0% |
| socks | 7 | 5 | 2 | 71.4% |
| trojan | 166 | 114 | 52 | 68.7% |
| vless | 36 | 5 | 31 | 13.9% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 22 |
| 204:ProxyError | 19 |
| geo:TimeoutError | 14 |
| 204:TimeoutError | 11 |
| speed:ProxyError | 10 |
| geo:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| cn-block:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4675 |
| ConnectionRefusedError | 825 |
| OSError | 170 |
| gaierror | 80 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.849 | prefer | 56 | 0.857 | 116 |
| Surfboard-tg-mixed | 0.814 | prefer | 122 | 0.738 | 5938 |
| mheidari-all | 0.759 | prefer | 76 | 0.684 | 18015 |
| DeltaKronecker-all | 0.639 | observe | 91 | 0.56 | 8321 |
| xiaoji235-airport-v2ray-all | 0.4 | observe | 4 | 0.75 | 3640 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4408 |
| Epodonios-all | 0.255 | observe | 0 | None | 6852 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3969 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6934 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 11 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 3 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.56 | 51 | 40 | 91 |
| mheidari-all | 0.684 | 52 | 24 | 76 |
| Surfboard-tg-mixed | 0.738 | 90 | 32 | 122 |
| xiaoji235-airport-v2ray-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.857 | 48 | 8 | 56 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18015 | yes | 3.88 | 0 |
| DeltaKronecker-all | 8321 | yes | 4.01 | 0 |
| SoliSpirit-all | 6934 | yes | 1.89 | 0 |
| Epodonios-all | 6852 | yes | 1.71 | 0 |
| Surfboard-tg-mixed | 5938 | yes | 2.09 | 0 |
| mahdibland-V2RayAggregator | 5352 | yes | 1.8 | 0 |
| barry-far-vless | 4939 | yes | 1.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 4408 | yes | 1.56 | 0 |
| Surfboard-tg-vless | 4397 | yes | 2.4 | 0 |
| MatinGhanbari-all-sub | 3969 | yes | 1.36 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 36 |
| speed | 34 |
| geo | 22 |
| cn-block | 15 |
