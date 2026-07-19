# AutoNodes 每日报告

生成时间：2026-07-19 08:32:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84921 |
| 去重后节点数 | 23703 |
| TCP 可达数 | 3000 |
| 真测通过数 | 793 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23703 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 25.3 |
| geo | 1.3 |
| probe | 70.4 |
| real_test | 195.7 |
| tcp | 32.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 139 | 121 | 18 | 87.1% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 617 | 571 | 46 | 92.5% |
| vless | 542 | 53 | 489 | 9.8% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 249 |
| geo:TimeoutError | 171 |
| geo:ClientOSError | 54 |
| cn-block:TimeoutError | 35 |
| speed:TimeoutError | 18 |
| 204:TimeoutError | 12 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4330 |
| ConnectionRefusedError | 663 |
| gaierror | 493 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.929 | prefer | 177 | 0.853 | 5438 |
| Au1rxx-base64 | 0.854 | prefer | 123 | 0.854 | 149 |
| DeltaKronecker-all | 0.62 | observe | 274 | 0.54 | 6235 |
| mheidari-all | 0.556 | observe | 731 | 0.476 | 20430 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 4642 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4478 |
| Epodonios-all | 0.255 | observe | 0 | None | 6647 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.476 | 348 | 383 | 731 |
| DeltaKronecker-all | 0.54 | 148 | 126 | 274 |
| Surfboard-tg-mixed | 0.853 | 151 | 26 | 177 |
| Au1rxx-base64 | 0.854 | 105 | 18 | 123 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20430 | yes | 3.37 | 0 |
| SoliSpirit-all | 6843 | yes | 2.5 | 0 |
| Epodonios-all | 6647 | yes | 3.56 | 0 |
| DeltaKronecker-all | 6235 | yes | 3.91 | 0 |
| Surfboard-tg-mixed | 5438 | yes | 1.69 | 0 |
| mahdibland-V2RayAggregator | 5355 | yes | 1.44 | 0 |
| barry-far-vless | 4872 | yes | 1.37 | 0 |
| xiaoji235-airport-v2ray-all | 4642 | yes | 1.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4478 | yes | 0.97 | 0 |
| Surfboard-tg-vless | 4126 | yes | 1.84 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.098 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 268 |
| geo | 226 |
| cn-block | 44 |
| 204 | 16 |
