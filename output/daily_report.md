# AutoNodes 每日报告

生成时间：2026-06-22 12:19:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75883 |
| 去重后节点数 | 22484 |
| TCP 可达数 | 3000 |
| 真测通过数 | 509 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22484 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 22.2 |
| geo | 1.3 |
| probe | 50.6 |
| real_test | 98.5 |
| tcp | 30.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 76 | 68 | 8 | 89.5% |
| trojan | 178 | 107 | 71 | 60.1% |
| vless | 311 | 258 | 53 | 83.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 51 |
| 204:ProxyError | 23 |
| 204:TimeoutError | 16 |
| geo:TimeoutError | 11 |
| cn-block:ProxyError | 7 |
| cn-block:TimeoutError | 7 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 3 |
| speed:ProxyError | 3 |
| cn-block:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4274 |
| ConnectionRefusedError | 599 |
| gaierror | 135 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | prefer | 69 | 1.0 | 131 |
| mheidari-all | 0.921 | prefer | 293 | 0.843 | 14984 |
| Au1rxx-base64 | 0.91 | prefer | 82 | 0.915 | 136 |
| DeltaKronecker-all | 0.673 | observe | 187 | 0.594 | 7452 |
| Surfboard-tg-mixed | 0.401 | observe | 7 | 0.571 | 5168 |
| Epodonios-all | 0.391 | observe | 2 | 1.0 | 7787 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4466 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3982 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7031 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.571 | 4 | 3 | 7 |
| DeltaKronecker-all | 0.594 | 111 | 76 | 187 |
| mheidari-all | 0.843 | 247 | 46 | 293 |
| Au1rxx-base64 | 0.915 | 75 | 7 | 82 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Epodonios-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 69 | 0 | 69 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14984 | yes | 3.69 | 0 |
| Epodonios-all | 7787 | yes | 2.74 | 0 |
| DeltaKronecker-all | 7452 | yes | 3.36 | 0 |
| SoliSpirit-all | 7031 | yes | 2.74 | 0 |
| Surfboard-tg-mixed | 5168 | yes | 1.86 | 0 |
| barry-far-vless | 4897 | yes | 1.36 | 0 |
| mahdibland-V2RayAggregator | 4559 | yes | 1.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4466 | yes | 1.75 | 0 |
| Surfboard-tg-vless | 3984 | yes | 2.17 | 0 |
| MatinGhanbari-all-sub | 3982 | yes | 1.44 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 59 |
| 204 | 42 |
| cn-block | 16 |
| geo | 15 |
