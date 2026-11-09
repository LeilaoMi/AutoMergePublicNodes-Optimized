# AutoNodes 每日报告

生成时间：2026-11-09 22:56:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81601 |
| 去重后节点数 | 26712 |
| TCP 可达数 | 3000 |
| 真测通过数 | 457 |
| verified 输出数 | 48 |
| global 输出数 | 300 |
| all 输出数 | 26712 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 18.1 |
| fetch | 5.0 |
| generate | 10.9 |
| geo | 1.6 |
| probe | 79.5 |
| real_test | 64.2 |
| tcp | 81.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 18 | 18 | 0 | 100.0% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 222 | 204 | 18 | 91.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 125 | 120 | 5 | 96.0% |
| vless | 152 | 103 | 49 | 67.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 6 |
| speed:ClientOSError | 4 |
| speed:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:TimeoutError | 2 |
| cn-block:status | 1 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6369 |
| ConnectionRefusedError | 999 |
| OSError | 240 |
| gaierror | 157 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.961 | prefer | 141 | 0.887 | 8250 |
| Au1rxx-base64 | 0.946 | prefer | 231 | 0.879 | 1751 |
| ermaozi | 0.909 | prefer | 18 | 1.0 | 518 |
| mheidari-all | 0.867 | prefer | 134 | 0.791 | 14061 |
| ninja-vless | 0.43 | observe | 3 | 1.0 | 1791 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2754 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11213 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 434 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 429 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 312 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 290 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 289 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 281 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 259 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 254 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 178 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 165 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.791 | 106 | 28 | 134 |
| Au1rxx-base64 | 0.879 | 203 | 28 | 231 |
| Surfboard-tg-mixed | 0.887 | 125 | 16 | 141 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 3 | 0 | 3 |
| ermaozi | 1.0 | 18 | 0 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 3.98 | 0 |
| SoliSpirit-all | 11213 | yes | 2.5 | 0 |
| Surfboard-tg-mixed | 8250 | yes | 2.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.47 | 0 |
| Surfboard-tg-vless | 6133 | yes | 2.97 | 0 |
| barry-far-vless | 6103 | yes | 0.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 0.62 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 1.88 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.21 | 0 |
| DeltaKronecker-all | 2754 | yes | 2.67 | 0 |

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
| test_one_timeout | 44 |
| 204 | 15 |
| speed | 7 |
| cn-block | 6 |
| geo | 1 |
