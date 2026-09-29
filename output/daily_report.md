# AutoNodes 每日报告

生成时间：2026-09-29 05:28:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/2 |
| 清理建议：优先/观察 | 2/103 |
| 原始节点数 | 96799 |
| 去重后节点数 | 27001 |
| TCP 可达数 | 3000 |
| 真测通过数 | 504 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27001 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| generate | 74.3 |
| geo | 1.5 |
| probe | 312.4 |
| real_test | 478.3 |
| tcp | 44.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 38 | 25 | 13 | 65.8% |
| hysteria2 | 27 | 24 | 3 | 88.9% |
| shadowsocks | 139 | 125 | 14 | 89.9% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 26 | 14 | 12 | 53.8% |
| vless | 746 | 314 | 432 | 42.1% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 175 |
| speed:TimeoutError | 89 |
| speed:ClientOSError | 70 |
| geo:ClientOSError | 57 |
| 204:TimeoutError | 22 |
| 204:ProxyError | 18 |
| cn-block:TimeoutError | 18 |
| 204:ProxyConnectionError | 14 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 4 |
| speed:ClientPayloadError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6044 |
| ConnectionRefusedError | 999 |
| gaierror | 479 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.849 | prefer | 355 | 0.786 | 1609 |
| Surfboard-tg-mixed | 0.747 | prefer | 37 | 0.676 | 7005 |
| ermaozi | 0.691 | observe | 32 | 0.688 | 354 |
| mheidari-all | 0.403 | observe | 540 | 0.322 | 22589 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 121 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5326 |
| Epodonios-all | 0.255 | observe | 0 | None | 7625 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9567 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5633 |

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
| downweight | DeltaKronecker-all | 0.197 | 9 | 0.111 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ermaozi-get_subscribe | 0.219 | 6 | 0.333 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.111 | 1 | 8 | 9 |
| mheidari-all | 0.322 | 174 | 366 | 540 |
| ermaozi-get_subscribe | 0.333 | 2 | 4 | 6 |
| Surfboard-tg-mixed | 0.676 | 25 | 12 | 37 |
| ermaozi | 0.688 | 22 | 10 | 32 |
| Au1rxx-base64 | 0.786 | 279 | 76 | 355 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22589 | yes | 6.3 | 0 |
| SoliSpirit-all | 9567 | yes | 2.74 | 0 |
| Epodonios-all | 7625 | yes | 3.57 | 0 |
| Surfboard-tg-mixed | 7005 | yes | 4.08 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.44 | 0 |
| barry-far-vless | 6028 | yes | 1.51 | 0 |
| Surfboard-tg-vless | 5633 | yes | 3.81 | 0 |
| DeltaKronecker-all | 5428 | yes | 4.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 5326 | yes | 3.26 | 0 |
| mahdibland-V2RayAggregator | 4237 | yes | 3.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 233 |
| speed | 161 |
| 204 | 58 |
| cn-block | 27 |
