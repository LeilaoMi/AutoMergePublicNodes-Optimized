# AutoNodes 每日报告

生成时间：2026-07-08 19:44:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83228 |
| 去重后节点数 | 24965 |
| TCP 可达数 | 3000 |
| 真测通过数 | 288 |
| verified 输出数 | 288 |
| global 输出数 | 291 |
| all 输出数 | 24965 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 19.7 |
| geo | 1.4 |
| probe | 43.7 |
| real_test | 75.8 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 4 | 1 | 80.0% |
| shadowsocks | 117 | 107 | 10 | 91.5% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 155 | 122 | 33 | 78.7% |
| vless | 41 | 10 | 31 | 24.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 30 |
| 204:TimeoutError | 10 |
| geo:TimeoutError | 8 |
| 204:ClientOSError | 7 |
| geo:ClientOSError | 7 |
| geo:ProxyError | 5 |
| 204:ProxyError | 4 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4565 |
| ConnectionRefusedError | 830 |
| gaierror | 217 |
| OSError | 170 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.921 | prefer | 86 | 0.849 | 8321 |
| mheidari-all | 0.906 | prefer | 67 | 0.836 | 18123 |
| Au1rxx-base64 | 0.845 | prefer | 67 | 0.851 | 120 |
| Surfboard-tg-mixed | 0.69 | observe | 103 | 0.612 | 5933 |
| xiaoji235-airport-v2ray-all | 0.4 | observe | 4 | 0.75 | 3640 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4408 |
| Epodonios-all | 0.255 | observe | 0 | None | 6761 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6878 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 3 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.612 | 63 | 40 | 103 |
| xiaoji235-airport-v2ray-all | 0.75 | 3 | 1 | 4 |
| mheidari-all | 0.836 | 56 | 11 | 67 |
| DeltaKronecker-all | 0.849 | 73 | 13 | 86 |
| Au1rxx-base64 | 0.851 | 57 | 10 | 67 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18123 | yes | 3.78 | 0 |
| DeltaKronecker-all | 8321 | yes | 4.08 | 0 |
| SoliSpirit-all | 6878 | yes | 2.71 | 0 |
| Epodonios-all | 6761 | yes | 1.86 | 0 |
| Surfboard-tg-mixed | 5933 | yes | 2.09 | 0 |
| mahdibland-V2RayAggregator | 5361 | yes | 0.24 | 0 |
| barry-far-vless | 4940 | yes | 2.12 | 0 |
| Surfboard-tg-vless | 4429 | yes | 2.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 4408 | yes | 1.92 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 2.84 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 31 |
| 204 | 21 |
| geo | 20 |
| cn-block | 4 |
