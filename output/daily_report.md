# AutoNodes 每日报告

生成时间：2026-09-20 11:11:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83340 |
| 去重后节点数 | 23411 |
| TCP 可达数 | 3000 |
| 真测通过数 | 471 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23411 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| generate | 71.3 |
| geo | 1.5 |
| probe | 213.6 |
| real_test | 227.7 |
| tcp | 38.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 54 | 43 | 11 | 79.6% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 171 | 154 | 17 | 90.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 20 | 9 | 11 | 45.0% |
| vless | 374 | 247 | 127 | 66.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 41 |
| geo:TimeoutError | 36 |
| 204:TimeoutError | 23 |
| 204:ProxyError | 21 |
| cn-block:TimeoutError | 16 |
| cn-block:ClientOSError | 12 |
| speed:TimeoutError | 12 |
| speed:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5203 |
| ConnectionRefusedError | 793 |
| gaierror | 335 |
| OSError | 15 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 1.0 | prefer | 41 | 0.951 | 15979 |
| Au1rxx-base64 | 0.942 | prefer | 269 | 0.881 | 1589 |
| ermaozi | 0.778 | prefer | 53 | 0.774 | 365 |
| Surfboard-tg-mixed | 0.719 | prefer | 189 | 0.64 | 7118 |
| DeltaKronecker-all | 0.47 | observe | 80 | 0.388 | 6092 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4315 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 89 |
| Epodonios-all | 0.255 | observe | 0 | None | 7603 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8786 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.388 | 31 | 49 | 80 |
| Surfboard-tg-mixed | 0.64 | 121 | 68 | 189 |
| ermaozi | 0.774 | 41 | 12 | 53 |
| Au1rxx-base64 | 0.881 | 237 | 32 | 269 |
| mheidari-all | 0.951 | 39 | 2 | 41 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15979 | yes | 2.5 | 0 |
| SoliSpirit-all | 8786 | yes | 1.45 | 0 |
| Epodonios-all | 7603 | yes | 2.61 | 0 |
| Surfboard-tg-mixed | 7118 | yes | 1.82 | 0 |
| DeltaKronecker-all | 6092 | yes | 2.5 | 0 |
| barry-far-vless | 5912 | yes | 1.27 | 0 |
| Surfboard-tg-vless | 5686 | yes | 1.92 | 0 |
| 10ium-ScrapeCategorize-Vless | 5238 | yes | 0.88 | 0 |
| mahdibland-V2RayAggregator | 4315 | yes | 0.86 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 77 |
| 204 | 45 |
| cn-block | 30 |
| speed | 17 |
