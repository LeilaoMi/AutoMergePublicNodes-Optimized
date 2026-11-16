# AutoNodes 每日报告

生成时间：2026-11-16 06:52:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 82990 |
| 去重后节点数 | 27371 |
| TCP 可达数 | 3000 |
| 真测通过数 | 433 |
| verified 输出数 | 51 |
| global 输出数 | 300 |
| all 输出数 | 27371 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.8 |
| fetch | 6.4 |
| generate | 13.0 |
| geo | 1.5 |
| probe | 94.3 |
| real_test | 71.7 |
| tcp | 82.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 19 | 19 | 0 | 100.0% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 220 | 204 | 16 | 92.7% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 58 | 44 | 14 | 75.9% |
| vless | 201 | 151 | 50 | 75.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| 204:ProxyError | 18 |
| 204:TimeoutError | 4 |
| speed:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| cn-block:TimeoutError | 2 |
| geo:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6282 |
| ConnectionRefusedError | 944 |
| OSError | 234 |
| gaierror | 189 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.982 | prefer | 130 | 0.908 | 8824 |
| ermaozi | 0.94 | prefer | 19 | 1.0 | 471 |
| Au1rxx-base64 | 0.899 | prefer | 173 | 0.832 | 1751 |
| mheidari-all | 0.871 | prefer | 185 | 0.795 | 14209 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| tg-LonUp_M | 0.365 | observe | 3 | 1.0 | 164 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4545 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4916 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 3 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 453 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 448 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 331 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 309 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 308 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 300 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 278 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 273 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.795 | 147 | 38 | 185 |
| Au1rxx-base64 | 0.832 | 144 | 29 | 173 |
| Surfboard-tg-mixed | 0.908 | 118 | 12 | 130 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 2 | 0 | 2 |
| tg-LonUp_M | 1.0 | 3 | 0 | 3 |
| ermaozi | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14209 | yes | 3.65 | 0 |
| SoliSpirit-all | 11553 | yes | 4.83 | 0 |
| Surfboard-tg-mixed | 8824 | yes | 5.0 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.01 | 0 |
| barry-far-vless | 6294 | yes | 2.61 | 0 |
| Surfboard-tg-vless | 6113 | yes | 4.07 | 0 |
| 10ium-ScrapeCategorize-Vless | 4916 | yes | 3.29 | 0 |
| mahdibland-V2RayAggregator | 4545 | yes | 0.66 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.45 | 0 |
| DeltaKronecker-all | 2960 | yes | 5.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 44 |
| 204 | 25 |
| cn-block | 7 |
| speed | 3 |
| geo | 2 |
