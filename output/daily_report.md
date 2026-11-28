# AutoNodes 每日报告

生成时间：2026-11-28 08:08:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 77832 |
| 去重后节点数 | 26998 |
| TCP 可达数 | 3000 |
| 真测通过数 | 342 |
| verified 输出数 | 49 |
| global 输出数 | 300 |
| all 输出数 | 26998 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.7 |
| fetch | 4.9 |
| generate | 11.0 |
| geo | 1.5 |
| probe | 79.8 |
| real_test | 77.7 |
| tcp | 81.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 21 | 21 | 0 | 100.0% |
| hysteria2 | 8 | 8 | 0 | 100.0% |
| shadowsocks | 285 | 218 | 67 | 76.5% |
| socks | 9 | 9 | 0 | 100.0% |
| trojan | 11 | 7 | 4 | 63.6% |
| vless | 135 | 87 | 48 | 64.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 82 |
| 204:ClientOSError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 6 |
| 204:TimeoutError | 6 |
| speed:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| speed:TimeoutError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6736 |
| ConnectionRefusedError | 942 |
| gaierror | 252 |
| OSError | 250 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.973 | prefer | 21 | 1.0 | 405 |
| Surfboard-tg-mixed | 0.847 | prefer | 217 | 0.77 | 8437 |
| Au1rxx-base64 | 0.813 | prefer | 134 | 0.746 | 1751 |
| mheidari-all | 0.705 | prefer | 94 | 0.628 | 14211 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.269 | observe | 1 | 1.0 | 357 |
| tg-LonUp_M | 0.261 | observe | 1 | 1.0 | 157 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4895 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11621 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ShadowsocksM | 0.175 | observe | 0 | None | 0 | 4 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 477 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 472 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 355 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 333 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 332 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 324 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 302 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 297 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.628 | 59 | 35 | 94 |
| Au1rxx-base64 | 0.746 | 100 | 34 | 134 |
| Surfboard-tg-mixed | 0.77 | 167 | 50 | 217 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 21 | 0 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14211 | yes | 4.07 | 0 |
| SoliSpirit-all | 11621 | yes | 1.79 | 0 |
| Surfboard-tg-mixed | 8437 | yes | 2.49 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.74 | 0 |
| barry-far-vless | 5482 | yes | 0.89 | 0 |
| Surfboard-tg-vless | 5299 | yes | 2.32 | 0 |
| 10ium-ScrapeCategorize-Vless | 4895 | yes | 1.29 | 0 |
| mahdibland-V2RayAggregator | 4526 | yes | 2.07 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.38 | 0 |
| ninja-vless | 1791 | yes | 2.14 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 82 |
| 204 | 19 |
| cn-block | 10 |
| speed | 8 |
