# AutoNodes 每日报告

生成时间：2026-06-28 09:24:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 75942 |
| 去重后节点数 | 22914 |
| TCP 可达数 | 3000 |
| 真测通过数 | 585 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22914 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 45.4 |
| geo | 1.4 |
| probe | 53.5 |
| real_test | 139.3 |
| tcp | 30.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 96 | 79 | 17 | 82.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 179 | 135 | 44 | 75.4% |
| vless | 432 | 328 | 104 | 75.9% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 83 |
| geo:TimeoutError | 13 |
| 204:TimeoutError | 13 |
| 204:ProxyError | 12 |
| speed:TimeoutError | 12 |
| 204:ClientOSError | 10 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 5 |
| geo:ClientOSError | 4 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4302 |
| ConnectionRefusedError | 636 |
| gaierror | 167 |
| OSError | 121 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.882 | prefer | 331 | 0.804 | 16289 |
| Surfboard-tg-mixed | 0.839 | prefer | 235 | 0.762 | 5004 |
| Au1rxx-base64 | 0.83 | prefer | 61 | 0.836 | 117 |
| DeltaKronecker-all | 0.682 | observe | 86 | 0.605 | 6788 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7560 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6983 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 179 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 7 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.605 | 52 | 34 | 86 |
| Surfboard-tg-mixed | 0.762 | 179 | 56 | 235 |
| mheidari-all | 0.804 | 266 | 65 | 331 |
| Au1rxx-base64 | 0.836 | 51 | 10 | 61 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16289 | yes | 3.59 | 0 |
| Epodonios-all | 7560 | yes | 2.25 | 0 |
| SoliSpirit-all | 6983 | yes | 2.26 | 0 |
| DeltaKronecker-all | 6788 | yes | 3.74 | 0 |
| mahdibland-V2RayAggregator | 5325 | yes | 1.97 | 0 |
| Surfboard-tg-mixed | 5004 | yes | 2.87 | 0 |
| barry-far-vless | 4456 | yes | 1.55 | 0 |
| 10ium-ScrapeCategorize-Vless | 4327 | yes | 1.74 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.83 | 0 |
| Surfboard-tg-vless | 3679 | yes | 1.8 | 0 |

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
| speed | 95 |
| 204 | 35 |
| geo | 20 |
| cn-block | 16 |
