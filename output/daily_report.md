# AutoNodes 每日报告

生成时间：2026-06-26 20:02:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 75726 |
| 去重后节点数 | 22770 |
| TCP 可达数 | 3000 |
| 真测通过数 | 293 |
| verified 输出数 | 293 |
| global 输出数 | 300 |
| all 输出数 | 22770 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 29.8 |
| geo | 1.4 |
| probe | 53.9 |
| real_test | 83.5 |
| tcp | 30.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 18 | 18 | 0 | 100.0% |
| hysteria2 | 4 | 3 | 1 | 75.0% |
| shadowsocks | 117 | 85 | 32 | 72.6% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 62 | 28 | 34 | 45.2% |
| vless | 237 | 157 | 80 | 66.2% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 34 |
| 204:TimeoutError | 26 |
| 204:ClientOSError | 21 |
| 204:ProxyError | 20 |
| cn-block:TimeoutError | 17 |
| geo:TimeoutError | 13 |
| cn-block:ClientOSError | 5 |
| speed:TimeoutError | 5 |
| geo:ClientOSError | 4 |
| geo:ProxyError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4341 |
| ConnectionRefusedError | 644 |
| gaierror | 128 |
| OSError | 118 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.89 | prefer | 18 | 1.0 | 39 |
| Au1rxx-base64 | 0.824 | prefer | 37 | 0.838 | 86 |
| mheidari-all | 0.741 | prefer | 125 | 0.664 | 16147 |
| Surfboard-tg-mixed | 0.732 | prefer | 196 | 0.653 | 5075 |
| DeltaKronecker-all | 0.58 | observe | 62 | 0.5 | 6283 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| nscl5-all | 0.255 | observe | 2 | 0.5 | 1175 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4567 |
| Epodonios-all | 0.255 | observe | 0 | None | 7688 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3981 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.5 | 31 | 31 | 62 |
| Surfboard-tg-mixed | 0.653 | 128 | 68 | 196 |
| mheidari-all | 0.664 | 83 | 42 | 125 |
| Au1rxx-base64 | 0.838 | 31 | 6 | 37 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 18 | 0 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16147 | yes | 3.38 | 0 |
| Epodonios-all | 7688 | yes | 2.63 | 0 |
| SoliSpirit-all | 7108 | yes | 2.81 | 0 |
| DeltaKronecker-all | 6283 | yes | 3.4 | 0 |
| mahdibland-V2RayAggregator | 5248 | yes | 1.66 | 0 |
| Surfboard-tg-mixed | 5075 | yes | 2.11 | 0 |
| 10ium-ScrapeCategorize-Vless | 4567 | yes | 1.47 | 0 |
| barry-far-vless | 4543 | yes | 1.95 | 0 |
| MatinGhanbari-all-sub | 3981 | yes | 2.04 | 0 |
| Surfboard-tg-vless | 3761 | yes | 1.79 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 67 |
| speed | 40 |
| cn-block | 22 |
| geo | 20 |
