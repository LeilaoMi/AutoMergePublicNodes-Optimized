# AutoNodes 每日报告

生成时间：2026-06-27 13:58:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77289 |
| 去重后节点数 | 23018 |
| TCP 可达数 | 3000 |
| 真测通过数 | 296 |
| verified 输出数 | 296 |
| global 输出数 | 300 |
| all 输出数 | 23018 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 36.5 |
| geo | 1.4 |
| probe | 48.8 |
| real_test | 94.7 |
| tcp | 30.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 18 | 18 | 0 | 100.0% |
| hysteria2 | 4 | 3 | 1 | 75.0% |
| shadowsocks | 116 | 88 | 28 | 75.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 201 | 79 | 122 | 39.3% |
| vless | 152 | 106 | 46 | 69.7% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 103 |
| 204:ProxyError | 20 |
| 204:TimeoutError | 19 |
| 204:ClientOSError | 15 |
| geo:ClientOSError | 9 |
| cn-block:TimeoutError | 9 |
| speed:TimeoutError | 6 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 4 |
| geo:TimeoutError | 4 |
| speed:ProxyError | 4 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4331 |
| ConnectionRefusedError | 643 |
| gaierror | 171 |
| OSError | 139 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.913 | prefer | 20 | 0.95 | 93 |
| snakem982 | 0.89 | prefer | 18 | 1.0 | 39 |
| mheidari-all | 0.864 | prefer | 49 | 0.796 | 16363 |
| Surfboard-tg-mixed | 0.768 | prefer | 229 | 0.69 | 5186 |
| DeltaKronecker-all | 0.428 | observe | 176 | 0.347 | 6822 |
| nscl5-all | 0.255 | observe | 2 | 0.5 | 1186 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 7866 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3978 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7361 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.347 | 61 | 115 | 176 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.69 | 158 | 71 | 229 |
| mheidari-all | 0.796 | 39 | 10 | 49 |
| Au1rxx-base64 | 0.95 | 19 | 1 | 20 |
| snakem982 | 1.0 | 18 | 0 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16363 | yes | 3.27 | 0 |
| Epodonios-all | 7866 | yes | 1.83 | 0 |
| SoliSpirit-all | 7361 | yes | 2.18 | 0 |
| DeltaKronecker-all | 6822 | yes | 3.58 | 0 |
| mahdibland-V2RayAggregator | 5283 | yes | 2.45 | 0 |
| Surfboard-tg-mixed | 5186 | yes | 2.87 | 0 |
| barry-far-vless | 4584 | yes | 1.67 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 1.86 | 0 |
| MatinGhanbari-all-sub | 3978 | yes | 1.51 | 0 |
| Surfboard-tg-vless | 3808 | yes | 1.95 | 0 |

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
| speed | 113 |
| 204 | 54 |
| cn-block | 17 |
| geo | 15 |
