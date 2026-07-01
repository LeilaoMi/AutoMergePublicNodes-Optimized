# AutoNodes 每日报告

生成时间：2026-07-01 20:07:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 77093 |
| 去重后节点数 | 23359 |
| TCP 可达数 | 3000 |
| 真测通过数 | 269 |
| verified 输出数 | 269 |
| global 输出数 | 290 |
| all 输出数 | 23359 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 46.9 |
| geo | 1.3 |
| probe | 55.1 |
| real_test | 97.9 |
| tcp | 31.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 8 | 3 | 5 | 37.5% |
| shadowsocks | 119 | 95 | 24 | 79.8% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 150 | 34 | 116 | 22.7% |
| vless | 171 | 95 | 76 | 55.6% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 101 |
| 204:TimeoutError | 25 |
| 204:ProxyError | 22 |
| cn-block:TimeoutError | 17 |
| 204:ClientOSError | 15 |
| cn-block:ClientOSError | 11 |
| geo:TimeoutError | 11 |
| cn-block:ProxyError | 7 |
| geo:ClientOSError | 7 |
| geo:ProxyError | 4 |
| speed:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4431 |
| ConnectionRefusedError | 637 |
| gaierror | 190 |
| OSError | 144 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.792 | prefer | 50 | 0.8 | 82 |
| Surfboard-tg-mixed | 0.657 | observe | 220 | 0.577 | 5816 |
| mheidari-all | 0.602 | observe | 65 | 0.523 | 16033 |
| DeltaKronecker-all | 0.35 | observe | 113 | 0.265 | 7631 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1113 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4308 |
| Epodonios-all | 0.255 | observe | 0 | None | 6737 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6642 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.125 | downweight | 5 | 0.0 | 0 | 1298 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.125 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 5 | 5 |
| DeltaKronecker-all | 0.265 | 30 | 83 | 113 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.523 | 34 | 31 | 65 |
| Surfboard-tg-mixed | 0.577 | 127 | 93 | 220 |
| Au1rxx-base64 | 0.8 | 40 | 10 | 50 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16033 | yes | 3.52 | 0 |
| DeltaKronecker-all | 7631 | yes | 4.0 | 0 |
| Epodonios-all | 6737 | yes | 1.81 | 0 |
| SoliSpirit-all | 6642 | yes | 1.87 | 0 |
| Surfboard-tg-mixed | 5816 | yes | 2.12 | 0 |
| mahdibland-V2RayAggregator | 5331 | yes | 1.56 | 0 |
| barry-far-vless | 4858 | yes | 1.43 | 0 |
| Surfboard-tg-vless | 4378 | yes | 2.3 | 0 |
| 10ium-ScrapeCategorize-Vless | 4308 | yes | 1.27 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.61 | 0 |

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
| speed | 104 |
| 204 | 62 |
| cn-block | 35 |
| geo | 22 |
