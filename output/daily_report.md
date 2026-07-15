# AutoNodes 每日报告

生成时间：2026-07-15 08:27:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75676 |
| 去重后节点数 | 22853 |
| TCP 可达数 | 3000 |
| 真测通过数 | 292 |
| verified 输出数 | 292 |
| global 输出数 | 300 |
| all 输出数 | 22853 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| generate | 39.0 |
| geo | 1.6 |
| probe | 43.4 |
| real_test | 87.7 |
| tcp | 31.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 39 | 29 | 10 | 74.4% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 217 | 189 | 28 | 87.1% |
| vless | 144 | 30 | 114 | 20.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 65 |
| speed:ClientOSError | 46 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 11 |
| geo:ClientOSError | 6 |
| speed:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4220 |
| ConnectionRefusedError | 635 |
| gaierror | 346 |
| OSError | 208 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.818 | prefer | 101 | 0.743 | 16158 |
| DeltaKronecker-all | 0.721 | prefer | 140 | 0.643 | 6421 |
| Surfboard-tg-mixed | 0.627 | observe | 159 | 0.547 | 5640 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 3759 |
| Au1rxx-base64 | 0.317 | observe | 2 | 1.0 | 149 |
| Epodonios-all | 0.255 | observe | 0 | None | 6608 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6437 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4320 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.333 | 1 | 2 | 3 |
| Surfboard-tg-mixed | 0.547 | 87 | 72 | 159 |
| DeltaKronecker-all | 0.643 | 90 | 50 | 140 |
| mheidari-all | 0.743 | 75 | 26 | 101 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| Au1rxx-base64 | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16158 | yes | 2.82 | 0 |
| Epodonios-all | 6608 | yes | 3.2 | 0 |
| SoliSpirit-all | 6437 | yes | 1.63 | 0 |
| DeltaKronecker-all | 6421 | yes | 2.97 | 0 |
| Surfboard-tg-mixed | 5640 | yes | 2.01 | 0 |
| mahdibland-V2RayAggregator | 5187 | yes | 1.52 | 0 |
| barry-far-vless | 4712 | yes | 0.82 | 0 |
| Surfboard-tg-vless | 4320 | yes | 1.77 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 3759 | yes | 0.96 | 0 |

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
| geo | 72 |
| speed | 51 |
| cn-block | 16 |
| 204 | 14 |
