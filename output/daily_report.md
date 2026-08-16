# AutoNodes 每日报告

生成时间：2026-08-16 06:54:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78586 |
| 去重后节点数 | 21819 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1129 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21819 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 27.0 |
| geo | 0.7 |
| probe | 76.5 |
| real_test | 215.3 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 153 | 143 | 10 | 93.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 613 | 600 | 13 | 97.9% |
| vless | 402 | 241 | 161 | 60.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 60 |
| speed:TimeoutError | 45 |
| geo:ClientOSError | 25 |
| speed:ClientOSError | 16 |
| 204:TimeoutError | 16 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4432 |
| ConnectionRefusedError | 773 |
| gaierror | 278 |
| OSError | 15 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 799 | 0.966 | 1997 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.754 | prefer | 191 | 0.675 | 5641 |
| mheidari-all | 0.691 | observe | 142 | 0.613 | 16464 |
| nscl5-all | 0.349 | observe | 3 | 0.667 | 2601 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4990 |
| DeltaKronecker-all | 0.315 | observe | 49 | 0.224 | 5092 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1997 |
| Epodonios-all | 0.255 | observe | 0 | None | 6328 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3986 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.224 | 11 | 38 | 49 |
| mheidari-all | 0.613 | 87 | 55 | 142 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.675 | 129 | 62 | 191 |
| Au1rxx-base64 | 0.966 | 772 | 27 | 799 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16464 | yes | 4.26 | 0 |
| SoliSpirit-all | 7355 | yes | 4.02 | 0 |
| Epodonios-all | 6328 | yes | 4.54 | 0 |
| Surfboard-tg-mixed | 5641 | yes | 5.1 | 0 |
| DeltaKronecker-all | 5092 | yes | 5.12 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 2.92 | 0 |
| barry-far-vless | 4736 | yes | 0.73 | 0 |
| Surfboard-tg-vless | 4360 | yes | 3.37 | 0 |
| MatinGhanbari-all-sub | 3986 | yes | 1.52 | 0 |
| mahdibland-V2RayAggregator | 3950 | yes | 2.9 | 0 |

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
| geo | 85 |
| speed | 61 |
| 204 | 24 |
| cn-block | 15 |
