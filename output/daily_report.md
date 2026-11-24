# AutoNodes 每日报告

生成时间：2026-11-24 22:40:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 78228 |
| 去重后节点数 | 27398 |
| TCP 可达数 | 3000 |
| 真测通过数 | 363 |
| verified 输出数 | 86 |
| global 输出数 | 300 |
| all 输出数 | 27398 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.1 |
| fetch | 5.2 |
| generate | 11.7 |
| geo | 1.5 |
| probe | 82.8 |
| real_test | 53.8 |
| tcp | 81.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 4 | 3 | 1 | 75.0% |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 221 | 204 | 17 | 92.3% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 39 | 36 | 3 | 92.3% |
| vless | 111 | 90 | 21 | 81.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 26 |
| cn-block:ClientOSError | 8 |
| cn-block:ProxyError | 3 |
| 204:ProxyError | 2 |
| 204:TimeoutError | 2 |
| cn-block:TimeoutError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6682 |
| ConnectionRefusedError | 1062 |
| OSError | 245 |
| gaierror | 243 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 98 | 0.949 | 1751 |
| ermaozi | 0.975 | prefer | 23 | 1.0 | 366 |
| Surfboard-tg-mixed | 0.958 | prefer | 129 | 0.884 | 8239 |
| mheidari-all | 0.932 | prefer | 153 | 0.856 | 14970 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.333 | observe | 4 | 0.75 | 322 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4839 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11536 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5468 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 470 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 465 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 348 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 326 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 325 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 317 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 295 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 290 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.75 | 3 | 1 | 4 |
| mheidari-all | 0.856 | 131 | 22 | 153 |
| Surfboard-tg-mixed | 0.884 | 114 | 15 | 129 |
| Au1rxx-base64 | 0.949 | 93 | 5 | 98 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14970 | yes | 4.21 | 0 |
| SoliSpirit-all | 11536 | yes | 1.81 | 0 |
| Surfboard-tg-mixed | 8239 | yes | 3.02 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.49 | 0 |
| barry-far-vless | 5508 | yes | 0.57 | 0 |
| Surfboard-tg-vless | 5468 | yes | 2.47 | 0 |
| 10ium-ScrapeCategorize-Vless | 4839 | yes | 0.71 | 0 |
| mahdibland-V2RayAggregator | 4546 | yes | 2.29 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.21 | 0 |
| ninja-vless | 1791 | yes | 2.21 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 26 |
| cn-block | 12 |
| 204 | 4 |
| speed | 1 |
