# AutoNodes 每日报告

生成时间：2026-06-23 15:18:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77179 |
| 去重后节点数 | 22038 |
| TCP 可达数 | 3000 |
| 真测通过数 | 374 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22038 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 31.1 |
| geo | 1.4 |
| probe | 53.5 |
| real_test | 112.8 |
| tcp | 29.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 50 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 118 | 110 | 8 | 93.2% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 83 | 45 | 38 | 54.2% |
| vless | 398 | 163 | 235 | 41.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 108 |
| speed:ClientOSError | 94 |
| 204:ProxyError | 17 |
| 204:TimeoutError | 17 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 8 |
| 204:ClientOSError | 7 |
| geo:TimeoutError | 6 |
| speed:ProxyError | 5 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 4 |
| geo:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4164 |
| ConnectionRefusedError | 601 |
| gaierror | 164 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | prefer | 50 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.812 | prefer | 218 | 0.734 | 5438 |
| Au1rxx-base64 | 0.761 | prefer | 76 | 0.763 | 124 |
| mheidari-all | 0.537 | observe | 173 | 0.457 | 15591 |
| DeltaKronecker-all | 0.274 | observe | 137 | 0.19 | 6437 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4576 |
| Epodonios-all | 0.255 | observe | 0 | None | 8099 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7514 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4204 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 6 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.19 | 26 | 111 | 137 |
| mheidari-all | 0.457 | 79 | 94 | 173 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.734 | 160 | 58 | 218 |
| Au1rxx-base64 | 0.763 | 58 | 18 | 76 |
| snakem982 | 1.0 | 50 | 0 | 50 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15591 | yes | 3.76 | 0 |
| Epodonios-all | 8099 | yes | 2.14 | 0 |
| SoliSpirit-all | 7514 | yes | 1.86 | 0 |
| DeltaKronecker-all | 6437 | yes | 4.18 | 0 |
| Surfboard-tg-mixed | 5438 | yes | 2.48 | 0 |
| barry-far-vless | 5009 | yes | 1.42 | 0 |
| 10ium-ScrapeCategorize-Vless | 4576 | yes | 1.24 | 0 |
| mahdibland-V2RayAggregator | 4477 | yes | 1.53 | 0 |
| Surfboard-tg-vless | 4204 | yes | 2.29 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.54 | 0 |

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
| geo | 117 |
| speed | 103 |
| 204 | 41 |
| cn-block | 21 |
