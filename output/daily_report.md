# AutoNodes 每日报告

生成时间：2026-06-26 14:40:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76363 |
| 去重后节点数 | 22728 |
| TCP 可达数 | 3000 |
| 真测通过数 | 402 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22728 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 40.2 |
| geo | 1.4 |
| probe | 54.5 |
| real_test | 89.1 |
| tcp | 30.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 120 | 104 | 16 | 86.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 63 | 33 | 30 | 52.4% |
| vless | 367 | 221 | 146 | 60.2% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 101 |
| 204:TimeoutError | 15 |
| 204:ClientOSError | 13 |
| geo:TimeoutError | 12 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 11 |
| geo:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4321 |
| ConnectionRefusedError | 626 |
| gaierror | 165 |
| OSError | 118 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Au1rxx-base64 | 0.891 | prefer | 51 | 0.902 | 108 |
| Surfboard-tg-mixed | 0.823 | prefer | 165 | 0.745 | 5176 |
| mheidari-all | 0.785 | prefer | 218 | 0.706 | 16250 |
| DeltaKronecker-all | 0.413 | observe | 121 | 0.331 | 6283 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1175 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4567 |
| Epodonios-all | 0.255 | observe | 0 | None | 7885 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3981 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.331 | 40 | 81 | 121 |
| mheidari-all | 0.706 | 154 | 64 | 218 |
| Surfboard-tg-mixed | 0.745 | 123 | 42 | 165 |
| Au1rxx-base64 | 0.902 | 46 | 5 | 51 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16250 | yes | 2.69 | 0 |
| Epodonios-all | 7885 | yes | 2.08 | 0 |
| SoliSpirit-all | 7254 | yes | 2.01 | 0 |
| DeltaKronecker-all | 6283 | yes | 2.79 | 0 |
| mahdibland-V2RayAggregator | 5185 | yes | 1.35 | 0 |
| Surfboard-tg-mixed | 5176 | yes | 1.9 | 0 |
| barry-far-vless | 4612 | yes | 0.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4567 | yes | 0.6 | 0 |
| MatinGhanbari-all-sub | 3981 | yes | 0.9 | 0 |
| Surfboard-tg-vless | 3834 | yes | 1.59 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 109 |
| 204 | 39 |
| geo | 25 |
| cn-block | 19 |
