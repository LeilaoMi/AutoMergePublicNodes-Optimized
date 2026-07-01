# AutoNodes 每日报告

生成时间：2026-07-01 04:27:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75750 |
| 去重后节点数 | 23199 |
| TCP 可达数 | 3000 |
| 真测通过数 | 531 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23199 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 31.2 |
| geo | 1.4 |
| probe | 54.6 |
| real_test | 115.8 |
| tcp | 30.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 6 | 3 | 3 | 50.0% |
| shadowsocks | 143 | 132 | 11 | 92.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 153 | 123 | 30 | 80.4% |
| vless | 571 | 233 | 338 | 40.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 175 |
| geo:TimeoutError | 103 |
| geo:ClientOSError | 36 |
| speed:TimeoutError | 25 |
| 204:ProxyError | 14 |
| cn-block:TimeoutError | 10 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 7 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4285 |
| ConnectionRefusedError | 637 |
| gaierror | 151 |
| OSError | 144 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.831 | prefer | 50 | 0.84 | 90 |
| Surfboard-tg-mixed | 0.795 | prefer | 335 | 0.716 | 5595 |
| mheidari-all | 0.572 | observe | 297 | 0.492 | 16003 |
| DeltaKronecker-all | 0.412 | observe | 185 | 0.33 | 7352 |
| nscl5-all | 0.356 | observe | 2 | 1.0 | 1113 |
| abc-configs-readme-latest30 | 0.312 | observe | 2 | 1.0 | 18 |
| ermaozi | 0.256 | observe | 1 | 1.0 | 28 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4139 |
| Epodonios-all | 0.255 | observe | 0 | None | 6537 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |
| xiaoji235-airport-v2ray-all | 0.141 | observe | 3 | 0.0 | 0 | 1298 |
| chromego_merge | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| peasoft-NoMoreWalls | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.33 | 61 | 124 | 185 |
| mheidari-all | 0.492 | 146 | 151 | 297 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.716 | 240 | 95 | 335 |
| Au1rxx-base64 | 0.84 | 42 | 8 | 50 |
| ermaozi | 1.0 | 1 | 0 | 1 |
| abc-configs-readme-latest30 | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16003 | yes | 3.16 | 0 |
| DeltaKronecker-all | 7352 | yes | 3.31 | 0 |
| SoliSpirit-all | 6630 | yes | 3.07 | 0 |
| Epodonios-all | 6537 | yes | 2.71 | 0 |
| Surfboard-tg-mixed | 5595 | yes | 1.87 | 0 |
| mahdibland-V2RayAggregator | 5373 | yes | 1.67 | 0 |
| barry-far-vless | 4720 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 4151 | yes | 2.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 4139 | yes | 1.4 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.99 | 0 |

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
| speed | 200 |
| geo | 140 |
| 204 | 25 |
| cn-block | 19 |
