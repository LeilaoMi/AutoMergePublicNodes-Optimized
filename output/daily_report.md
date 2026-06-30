# AutoNodes 每日报告

生成时间：2026-06-30 20:09:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75832 |
| 去重后节点数 | 23070 |
| TCP 可达数 | 3000 |
| 真测通过数 | 191 |
| verified 输出数 | 191 |
| global 输出数 | 197 |
| all 输出数 | 23070 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 34.3 |
| geo | 1.4 |
| probe | 51.3 |
| real_test | 79.7 |
| tcp | 30.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 109 | 93 | 16 | 85.3% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 255 | 32 | 223 | 12.5% |
| vless | 73 | 23 | 50 | 31.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 193 |
| 204:ProxyError | 31 |
| 204:ClientOSError | 13 |
| 204:TimeoutError | 12 |
| geo:TimeoutError | 9 |
| geo:ClientOSError | 8 |
| geo:ProxyError | 5 |
| speed:TimeoutError | 5 |
| cn-block:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4403 |
| ConnectionRefusedError | 619 |
| OSError | 132 |
| gaierror | 115 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.88 | prefer | 33 | 0.818 | 15848 |
| Au1rxx-base64 | 0.831 | prefer | 27 | 0.852 | 83 |
| Surfboard-tg-mixed | 0.628 | observe | 82 | 0.549 | 5645 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.303 | observe | 1 | 1.0 | 1204 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1136 |
| DeltaKronecker-all | 0.267 | observe | 298 | 0.185 | 7352 |
| abc-configs-readme-latest30 | 0.256 | observe | 1 | 1.0 | 19 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4139 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| chromego_merge | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| peasoft-NoMoreWalls | 0.175 | observe | 0 | None | 0 | 3 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.185 | 55 | 243 | 298 |
| Surfboard-tg-mixed | 0.549 | 45 | 37 | 82 |
| mheidari-all | 0.818 | 27 | 6 | 33 |
| Au1rxx-base64 | 0.852 | 23 | 4 | 27 |
| abc-configs-readme-latest30 | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15848 | yes | 3.3 | 0 |
| DeltaKronecker-all | 7352 | yes | 3.68 | 0 |
| SoliSpirit-all | 6636 | yes | 2.98 | 0 |
| Epodonios-all | 6581 | yes | 1.12 | 0 |
| Surfboard-tg-mixed | 5645 | yes | 2.27 | 0 |
| mahdibland-V2RayAggregator | 5373 | yes | 1.72 | 0 |
| barry-far-vless | 4802 | yes | 1.81 | 0 |
| Surfboard-tg-vless | 4233 | yes | 1.87 | 0 |
| 10ium-ScrapeCategorize-Vless | 4139 | yes | 1.65 | 0 |
| MatinGhanbari-all-sub | 3979 | yes | 1.91 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| real_ok_drop_50pct | real-test ok dropped from 485 to 191 |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 200 |
| 204 | 56 |
| geo | 22 |
| cn-block | 12 |
