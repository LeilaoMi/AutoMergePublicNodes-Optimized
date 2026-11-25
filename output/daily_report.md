# AutoNodes 每日报告

生成时间：2026-11-25 08:55:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 78303 |
| 去重后节点数 | 27473 |
| TCP 可达数 | 3000 |
| 真测通过数 | 381 |
| verified 输出数 | 80 |
| global 输出数 | 300 |
| all 输出数 | 27473 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 27.4 |
| fetch | 6.6 |
| generate | 14.9 |
| geo | 1.6 |
| probe | 94.6 |
| real_test | 85.1 |
| tcp | 82.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 49 | 48 | 1 | 98.0% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 217 | 197 | 20 | 90.8% |
| socks | 14 | 11 | 3 | 78.6% |
| trojan | 46 | 19 | 27 | 41.3% |
| vless | 183 | 108 | 75 | 59.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 53 |
| 204:ProxyError | 29 |
| cn-block:TimeoutError | 12 |
| cn-block:ProxyError | 8 |
| geo:ProxyError | 6 |
| speed:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| 204:TimeoutError | 4 |
| geo:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| speed:TimeoutError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6881 |
| ConnectionRefusedError | 1052 |
| OSError | 242 |
| gaierror | 216 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.954 | prefer | 61 | 0.951 | 442 |
| mheidari-all | 0.847 | prefer | 58 | 0.776 | 14996 |
| Surfboard-tg-mixed | 0.796 | prefer | 241 | 0.718 | 8136 |
| Au1rxx-base64 | 0.793 | prefer | 153 | 0.725 | 1751 |
| roosterkid-openproxylist-v2ray | 0.363 | observe | 3 | 1.0 | 116 |
| ermaozi-get_subscribe | 0.326 | observe | 2 | 1.0 | 376 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4839 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11514 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 471 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 466 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 349 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 327 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 326 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 318 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 296 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 291 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.718 | 173 | 68 | 241 |
| Au1rxx-base64 | 0.725 | 111 | 42 | 153 |
| mheidari-all | 0.776 | 45 | 13 | 58 |
| ermaozi | 0.951 | 58 | 3 | 61 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| roosterkid-openproxylist-v2ray | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14996 | yes | 5.96 | 0 |
| SoliSpirit-all | 11514 | yes | 4.59 | 0 |
| Surfboard-tg-mixed | 8136 | yes | 4.33 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.85 | 0 |
| barry-far-vless | 5649 | yes | 2.53 | 0 |
| Surfboard-tg-vless | 5440 | yes | 4.07 | 0 |
| 10ium-ScrapeCategorize-Vless | 4839 | yes | 2.64 | 0 |
| mahdibland-V2RayAggregator | 4463 | yes | 3.14 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.97 | 0 |
| ninja-vless | 1791 | yes | 3.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 53 |
| 204 | 33 |
| cn-block | 25 |
| geo | 9 |
| speed | 7 |
