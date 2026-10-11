# AutoNodes 每日报告

生成时间：2026-10-11 21:54:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 99284 |
| 去重后节点数 | 27441 |
| TCP 可达数 | 3000 |
| 真测通过数 | 505 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27441 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 73.7 |
| geo | 1.3 |
| probe | 280.6 |
| real_test | 317.5 |
| tcp | 45.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 7 | 2 | 5 | 28.6% |
| http | 40 | 25 | 15 | 62.5% |
| hysteria2 | 19 | 16 | 3 | 84.2% |
| shadowsocks | 134 | 118 | 16 | 88.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 177 | 174 | 3 | 98.3% |
| vless | 192 | 167 | 25 | 87.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 16 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 10 |
| speed:ClientOSError | 7 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| geo:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5906 |
| ConnectionRefusedError | 1068 |
| gaierror | 518 |
| OSError | 242 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 388 | 0.93 | 1858 |
| DeltaKronecker-all | 0.943 | prefer | 49 | 0.878 | 5372 |
| mheidari-all | 0.915 | prefer | 77 | 0.844 | 23882 |
| ermaozi | 0.635 | observe | 39 | 0.615 | 635 |
| Surfboard-tg-mixed | 0.586 | observe | 10 | 0.8 | 7031 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 104 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 53 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5099 |
| Epodonios-all | 0.255 | observe | 0 | None | 7711 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.213 | 7 | 0.286 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.286 | 2 | 5 | 7 |
| ermaozi | 0.615 | 24 | 15 | 39 |
| Surfboard-tg-mixed | 0.8 | 8 | 2 | 10 |
| mheidari-all | 0.844 | 65 | 12 | 77 |
| DeltaKronecker-all | 0.878 | 43 | 6 | 49 |
| Au1rxx-base64 | 0.93 | 361 | 27 | 388 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23882 | yes | 4.68 | 0 |
| SoliSpirit-all | 9704 | yes | 2.3 | 0 |
| Epodonios-all | 7711 | yes | 5.15 | 0 |
| Surfboard-tg-mixed | 7031 | yes | 3.03 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.06 | 0 |
| barry-far-vless | 5966 | yes | 1.33 | 0 |
| Surfboard-tg-vless | 5590 | yes | 3.38 | 0 |
| DeltaKronecker-all | 5372 | yes | 4.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5099 | yes | 1.0 | 0 |
| mahdibland-V2RayAggregator | 4284 | yes | 2.61 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| cn-block | 20 |
| speed | 13 |
| geo | 5 |
