# AutoNodes 每日报告

生成时间：2026-06-23 20:17:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77271 |
| 去重后节点数 | 22334 |
| TCP 可达数 | 3000 |
| 真测通过数 | 369 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22334 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 35.4 |
| geo | 1.4 |
| probe | 62.3 |
| real_test | 124.2 |
| tcp | 29.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 50 | 0 | 100.0% |
| hysteria2 | 2 | 1 | 1 | 50.0% |
| shadowsocks | 114 | 99 | 15 | 86.8% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 137 | 74 | 63 | 54.0% |
| vless | 297 | 140 | 157 | 47.1% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 60 |
| speed:ClientOSError | 56 |
| cn-block:TimeoutError | 26 |
| 204:TimeoutError | 24 |
| 204:ProxyError | 21 |
| geo:TimeoutError | 13 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| cn-block:ProxyError | 6 |
| 204:ClientOSError | 5 |
| speed:ProxyError | 5 |
| geo:ProxyError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4268 |
| ConnectionRefusedError | 612 |
| gaierror | 142 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | prefer | 50 | 1.0 | 73 |
| Au1rxx-base64 | 0.797 | prefer | 70 | 0.8 | 124 |
| Surfboard-tg-mixed | 0.722 | prefer | 216 | 0.644 | 5373 |
| DeltaKronecker-all | 0.55 | observe | 81 | 0.469 | 6437 |
| mheidari-all | 0.532 | observe | 184 | 0.451 | 15741 |
| Surfboard-tg-vless | 0.335 | observe | 1 | 1.0 | 4175 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4576 |
| Epodonios-all | 0.255 | observe | 0 | None | 8167 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 9 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.451 | 83 | 101 | 184 |
| DeltaKronecker-all | 0.469 | 38 | 43 | 81 |
| Surfboard-tg-mixed | 0.644 | 139 | 77 | 216 |
| Au1rxx-base64 | 0.8 | 56 | 14 | 70 |
| Surfboard-tg-vless | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 50 | 0 | 50 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15741 | yes | 3.0 | 0 |
| Epodonios-all | 8167 | yes | 2.08 | 0 |
| SoliSpirit-all | 7442 | yes | 2.54 | 0 |
| DeltaKronecker-all | 6437 | yes | 3.73 | 0 |
| Surfboard-tg-mixed | 5373 | yes | 2.41 | 0 |
| barry-far-vless | 4987 | yes | 1.05 | 0 |
| mahdibland-V2RayAggregator | 4664 | yes | 1.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4576 | yes | 1.12 | 0 |
| Surfboard-tg-vless | 4175 | yes | 2.54 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.11 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 77 |
| speed | 68 |
| 204 | 50 |
| cn-block | 41 |
