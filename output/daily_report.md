# AutoNodes 每日报告

生成时间：2026-07-02 09:26:53

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76108 |
| 去重后节点数 | 23111 |
| TCP 可达数 | 3000 |
| 真测通过数 | 418 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23111 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 37.4 |
| geo | 1.5 |
| probe | 48.4 |
| real_test | 106.9 |
| tcp | 30.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 2 | 3 | 40.0% |
| shadowsocks | 96 | 81 | 15 | 84.4% |
| socks | 43 | 35 | 8 | 81.4% |
| trojan | 236 | 151 | 85 | 64.0% |
| vless | 212 | 109 | 103 | 51.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 91 |
| 204:ProxyError | 36 |
| geo:TimeoutError | 30 |
| 204:TimeoutError | 14 |
| geo:ClientOSError | 11 |
| cn-block:ProxyError | 8 |
| 204:ClientOSError | 7 |
| cn-block:ClientOSError | 6 |
| cn-block:TimeoutError | 5 |
| speed:TimeoutError | 4 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4384 |
| ConnectionRefusedError | 686 |
| OSError | 150 |
| gaierror | 110 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.832 | prefer | 56 | 0.839 | 106 |
| Surfboard-tg-mixed | 0.764 | prefer | 261 | 0.686 | 5705 |
| mheidari-all | 0.705 | prefer | 70 | 0.629 | 15877 |
| DeltaKronecker-all | 0.619 | observe | 202 | 0.54 | 7467 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 179 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4254 |
| Epodonios-all | 0.255 | observe | 0 | None | 6497 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6729 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.141 | observe | 3 | 0.0 | 0 | 1293 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 3 | 3 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.54 | 109 | 93 | 202 |
| mheidari-all | 0.629 | 44 | 26 | 70 |
| Surfboard-tg-mixed | 0.686 | 179 | 82 | 261 |
| Au1rxx-base64 | 0.839 | 47 | 9 | 56 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15877 | yes | 4.16 | 0 |
| DeltaKronecker-all | 7467 | yes | 3.04 | 0 |
| SoliSpirit-all | 6729 | yes | 2.66 | 0 |
| Epodonios-all | 6497 | yes | 1.63 | 0 |
| Surfboard-tg-mixed | 5705 | yes | 2.22 | 0 |
| mahdibland-V2RayAggregator | 5365 | yes | 1.72 | 0 |
| barry-far-vless | 4756 | yes | 1.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4254 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 4232 | yes | 2.39 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.25 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 96 |
| 204 | 57 |
| geo | 42 |
| cn-block | 19 |
