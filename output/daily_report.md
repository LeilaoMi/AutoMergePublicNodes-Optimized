# AutoNodes 每日报告

生成时间：2026-06-17 19:19:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/39 |
| 原始节点数 | 43688 |
| 去重后节点数 | 18013 |
| TCP 可达数 | 3000 |
| 真测通过数 | 987 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 18013 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| generate | 35.7 |
| geo | 1.2 |
| probe | 72.5 |
| real_test | 220.7 |
| tcp | 19.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 4 | 2 | 2 | 50.0% |
| shadowsocks | 115 | 96 | 19 | 83.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 11 | 1 | 10 | 9.1% |
| vless | 1108 | 860 | 248 | 77.6% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 147 |
| 204:TimeoutError | 30 |
| 204:ProxyError | 24 |
| cn-block:TimeoutError | 21 |
| geo:ClientOSError | 13 |
| cn-block:ClientOSError | 10 |
| 204:ClientOSError | 8 |
| geo:TimeoutError | 7 |
| speed:TimeoutError | 7 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 4 |
| speed:ProxyError | 4 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2710 |
| ConnectionRefusedError | 449 |
| gaierror | 72 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.933 | prefer | 236 | 0.856 | 4729 |
| Au1rxx-base64 | 0.883 | prefer | 64 | 0.891 | 108 |
| snakem982 | 0.88 | prefer | 55 | 0.891 | 73 |
| mheidari-all | 0.872 | prefer | 22 | 0.818 | 2000 |
| DeltaKronecker-all | 0.823 | prefer | 886 | 0.744 | 7763 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 2000 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.127 | observe | 2 | 0.0 | 0 | 588 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tonykong-base64 | 0.175 | observe | 0 | None | 0 | 5 |
| tonykong-clash | 0.175 | observe | 0 | None | 0 | 5 |
| Barabama-we | 0.176 | observe | 0 | None | 0 | 23 |
| Mr8AHAL | 0.176 | observe | 0 | None | 0 | 26 |
| abc-configs-readme-latest30 | 0.176 | observe | 0 | None | 0 | 18 |
| barabama-nodefree | 0.176 | observe | 0 | None | 0 | 23 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.744 | 659 | 227 | 886 |
| mheidari-all | 0.818 | 18 | 4 | 22 |
| Surfboard-tg-mixed | 0.856 | 202 | 34 | 236 |
| snakem982 | 0.891 | 49 | 6 | 55 |
| Au1rxx-base64 | 0.891 | 57 | 7 | 64 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 3.16 | 0 |
| Surfboard-tg-mixed | 4729 | yes | 1.69 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.39 | 0 |
| Surfboard-tg-vless | 3741 | yes | 1.8 | 0 |
| Epodonios-all | 3000 | yes | 2.17 | 0 |
| SoliSpirit-all | 3000 | yes | 2.3 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 2.05 | 0 |
| mheidari-all | 2000 | yes | 2.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.65 | 0 |
| barry-far-vless | 2000 | yes | 1.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| trojan | 0.091 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 159 |
| 204 | 62 |
| cn-block | 35 |
| geo | 24 |
