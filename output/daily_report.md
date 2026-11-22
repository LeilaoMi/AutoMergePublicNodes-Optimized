# AutoNodes 每日报告

生成时间：2026-11-22 07:09:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 83494 |
| 去重后节点数 | 28090 |
| TCP 可达数 | 3000 |
| 真测通过数 | 282 |
| verified 输出数 | 52 |
| global 输出数 | 284 |
| all 输出数 | 28090 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.4 |
| fetch | 5.5 |
| generate | 11.5 |
| geo | 1.6 |
| probe | 85.9 |
| real_test | 65.8 |
| tcp | 77.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 29 | 28 | 1 | 96.6% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 95 | 89 | 6 | 93.7% |
| socks | 8 | 7 | 1 | 87.5% |
| trojan | 36 | 28 | 8 | 77.8% |
| vless | 214 | 126 | 88 | 58.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 45 |
| 204:ProxyError | 16 |
| cn-block:ClientOSError | 14 |
| cn-block:ProxyError | 7 |
| speed:ProxyError | 6 |
| 204:TimeoutError | 5 |
| geo:ProxyError | 4 |
| geo:ClientOSError | 2 |
| speed:TimeoutError | 2 |
| cn-block:TimeoutError | 2 |
| speed:ClientOSError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6149 |
| ConnectionRefusedError | 1035 |
| gaierror | 322 |
| OSError | 245 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.881 | prefer | 125 | 0.816 | 1751 |
| ermaozi | 0.823 | prefer | 17 | 0.941 | 399 |
| mheidari-all | 0.735 | prefer | 224 | 0.656 | 14453 |
| zhangkai | 0.688 | observe | 12 | 1.0 | 27 |
| Surfboard-tg-mixed | 0.606 | observe | 9 | 0.889 | 8778 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.282 | observe | 3 | 0.667 | 327 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 146 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5030 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 1 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 465 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 460 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 343 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 321 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 320 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 312 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 290 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 285 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.656 | 147 | 77 | 224 |
| ermaozi-get_subscribe | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.816 | 102 | 23 | 125 |
| Surfboard-tg-mixed | 0.889 | 8 | 1 | 9 |
| ermaozi | 0.941 | 16 | 1 | 17 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 12 | 0 | 12 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14453 | yes | 3.79 | 0 |
| SoliSpirit-all | 12093 | yes | 3.48 | 0 |
| Surfboard-tg-mixed | 8778 | yes | 3.07 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.48 | 0 |
| barry-far-vless | 6124 | yes | 2.62 | 0 |
| Surfboard-tg-vless | 5942 | yes | 2.83 | 0 |
| 10ium-ScrapeCategorize-Vless | 5030 | yes | 2.03 | 0 |
| mahdibland-V2RayAggregator | 4512 | yes | 0.68 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.69 | 0 |
| DeltaKronecker-all | 2989 | yes | 4.92 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 45 |
| cn-block | 23 |
| 204 | 22 |
| speed | 9 |
| geo | 6 |
