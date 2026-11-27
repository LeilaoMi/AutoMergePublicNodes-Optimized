# AutoNodes 每日报告

生成时间：2026-11-27 21:32:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 78578 |
| 去重后节点数 | 27356 |
| TCP 可达数 | 3000 |
| 真测通过数 | 382 |
| verified 输出数 | 79 |
| global 输出数 | 300 |
| all 输出数 | 27356 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 20.8 |
| fetch | 4.8 |
| generate | 10.8 |
| geo | 1.4 |
| probe | 81.7 |
| real_test | 79.0 |
| tcp | 80.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 44 | 44 | 0 | 100.0% |
| hysteria2 | 10 | 10 | 0 | 100.0% |
| shadowsocks | 283 | 218 | 65 | 77.0% |
| socks | 13 | 12 | 1 | 92.3% |
| trojan | 5 | 4 | 1 | 80.0% |
| vless | 151 | 106 | 45 | 70.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 75 |
| speed:TimeoutError | 6 |
| 204:TimeoutError | 6 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| speed:ClientOSError | 4 |
| geo:ClientOSError | 3 |
| speed:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |
| cn-block:ProxyError | 1 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6652 |
| ConnectionRefusedError | 990 |
| gaierror | 251 |
| OSError | 247 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | prefer | 48 | 0.979 | 466 |
| Au1rxx-base64 | 0.864 | prefer | 134 | 0.799 | 1751 |
| Surfboard-tg-mixed | 0.843 | prefer | 222 | 0.766 | 8496 |
| mheidari-all | 0.733 | prefer | 93 | 0.656 | 14418 |
| tg-LonUp_M | 0.52 | observe | 7 | 1.0 | 174 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4459 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.272 | observe | 1 | 1.0 | 417 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4895 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 476 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 471 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 354 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 332 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 331 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 323 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 301 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 296 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.656 | 61 | 32 | 93 |
| Surfboard-tg-mixed | 0.766 | 170 | 52 | 222 |
| Au1rxx-base64 | 0.799 | 107 | 27 | 134 |
| ermaozi | 0.979 | 47 | 1 | 48 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 7 | 0 | 7 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14418 | yes | 4.19 | 0 |
| SoliSpirit-all | 11762 | yes | 1.87 | 0 |
| Surfboard-tg-mixed | 8496 | yes | 2.58 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.58 | 0 |
| barry-far-vless | 5607 | yes | 1.03 | 0 |
| Surfboard-tg-vless | 5391 | yes | 2.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 4895 | yes | 0.89 | 0 |
| mahdibland-V2RayAggregator | 4459 | yes | 1.96 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.92 | 0 |
| ninja-vless | 1791 | yes | 2.2 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 75 |
| 204 | 12 |
| speed | 12 |
| cn-block | 7 |
| geo | 6 |
