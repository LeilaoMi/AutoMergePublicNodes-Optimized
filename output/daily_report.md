# AutoNodes 每日报告

生成时间：2026-11-23 07:58:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 83225 |
| 去重后节点数 | 28655 |
| TCP 可达数 | 3000 |
| 真测通过数 | 404 |
| verified 输出数 | 82 |
| global 输出数 | 300 |
| all 输出数 | 28655 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.8 |
| fetch | 7.0 |
| generate | 15.8 |
| geo | 1.6 |
| probe | 96.2 |
| real_test | 74.3 |
| tcp | 85.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 69 | 68 | 1 | 98.6% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 226 | 203 | 23 | 89.8% |
| socks | 12 | 11 | 1 | 91.7% |
| trojan | 27 | 17 | 10 | 63.0% |
| vless | 164 | 108 | 56 | 65.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 41 |
| 204:ProxyError | 22 |
| cn-block:ProxyError | 7 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 5 |
| 204:TimeoutError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 2 |
| 204:ClientOSError | 2 |
| speed:TimeoutError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6653 |
| ConnectionRefusedError | 1060 |
| gaierror | 300 |
| OSError | 247 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 74 | 1.0 | 486 |
| Au1rxx-base64 | 0.89 | prefer | 131 | 0.824 | 1751 |
| Surfboard-tg-mixed | 0.876 | prefer | 243 | 0.798 | 8701 |
| mheidari-all | 0.741 | prefer | 54 | 0.667 | 15418 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| roosterkid-openproxylist-v2ray | 0.316 | observe | 2 | 1.0 | 119 |
| ermaozi-get_subscribe | 0.272 | observe | 1 | 1.0 | 421 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5069 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2671 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 159 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 467 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 462 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 345 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 323 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 322 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 314 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 292 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 287 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.667 | 36 | 18 | 54 |
| Surfboard-tg-mixed | 0.798 | 194 | 49 | 243 |
| Au1rxx-base64 | 0.824 | 108 | 23 | 131 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 74 | 0 | 74 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15418 | yes | 6.03 | 0 |
| SoliSpirit-all | 11834 | yes | 2.46 | 0 |
| Surfboard-tg-mixed | 8701 | yes | 3.7 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.95 | 0 |
| barry-far-vless | 5831 | yes | 0.99 | 0 |
| Surfboard-tg-vless | 5650 | yes | 3.38 | 0 |
| 10ium-ScrapeCategorize-Vless | 5069 | yes | 1.23 | 0 |
| mahdibland-V2RayAggregator | 4514 | yes | 3.07 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.03 | 0 |
| DeltaKronecker-all | 2671 | yes | 5.82 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 41 |
| 204 | 27 |
| cn-block | 17 |
| speed | 4 |
| geo | 3 |
