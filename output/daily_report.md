# AutoNodes 每日报告

生成时间：2026-06-27 08:48:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77212 |
| 去重后节点数 | 22994 |
| TCP 可达数 | 3000 |
| 真测通过数 | 440 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22994 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 38.0 |
| geo | 1.5 |
| probe | 55.0 |
| real_test | 114.1 |
| tcp | 30.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 18 | 18 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 130 | 109 | 21 | 83.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 178 | 126 | 52 | 70.8% |
| vless | 296 | 180 | 116 | 60.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 72 |
| 204:TimeoutError | 29 |
| geo:TimeoutError | 21 |
| 204:ClientOSError | 19 |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 11 |
| speed:TimeoutError | 7 |
| geo:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4341 |
| ConnectionRefusedError | 647 |
| gaierror | 145 |
| OSError | 139 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.89 | prefer | 18 | 1.0 | 39 |
| Surfboard-tg-mixed | 0.797 | prefer | 277 | 0.718 | 5179 |
| Au1rxx-base64 | 0.76 | prefer | 35 | 0.771 | 91 |
| DeltaKronecker-all | 0.75 | prefer | 89 | 0.674 | 6822 |
| mheidari-all | 0.723 | prefer | 208 | 0.644 | 16368 |
| nscl5-all | 0.359 | observe | 2 | 1.0 | 1186 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 7844 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3979 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7359 |

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
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.644 | 134 | 74 | 208 |
| DeltaKronecker-all | 0.674 | 60 | 29 | 89 |
| Surfboard-tg-mixed | 0.718 | 199 | 78 | 277 |
| Au1rxx-base64 | 0.771 | 27 | 8 | 35 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 18 | 0 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16368 | yes | 3.77 | 0 |
| Epodonios-all | 7844 | yes | 2.71 | 0 |
| SoliSpirit-all | 7359 | yes | 2.27 | 0 |
| DeltaKronecker-all | 6822 | yes | 3.34 | 0 |
| mahdibland-V2RayAggregator | 5283 | yes | 1.73 | 0 |
| Surfboard-tg-mixed | 5179 | yes | 2.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 1.13 | 0 |
| barry-far-vless | 4577 | yes | 1.96 | 0 |
| MatinGhanbari-all-sub | 3979 | yes | 1.79 | 0 |
| Surfboard-tg-vless | 3796 | yes | 1.63 | 0 |

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
| speed | 82 |
| 204 | 59 |
| geo | 29 |
| cn-block | 20 |
