# AutoNodes 每日报告

生成时间：2026-11-24 10:09:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 79067 |
| 去重后节点数 | 27838 |
| TCP 可达数 | 3000 |
| 真测通过数 | 355 |
| verified 输出数 | 80 |
| global 输出数 | 300 |
| all 输出数 | 27838 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.4 |
| fetch | 3.9 |
| generate | 9.6 |
| geo | 1.4 |
| probe | 74.5 |
| real_test | 66.8 |
| tcp | 83.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 46 | 45 | 1 | 97.8% |
| hysteria2 | 8 | 8 | 0 | 100.0% |
| shadowsocks | 220 | 191 | 29 | 86.8% |
| socks | 13 | 11 | 2 | 84.6% |
| trojan | 42 | 32 | 10 | 76.2% |
| vless | 122 | 77 | 45 | 63.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 48 |
| 204:ProxyError | 15 |
| 204:TimeoutError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7135 |
| ConnectionRefusedError | 1073 |
| OSError | 242 |
| gaierror | 225 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.983 | prefer | 54 | 0.981 | 460 |
| mheidari-all | 0.926 | prefer | 63 | 0.857 | 15386 |
| Surfboard-tg-mixed | 0.85 | prefer | 202 | 0.772 | 8220 |
| Au1rxx-base64 | 0.833 | prefer | 129 | 0.767 | 1751 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.284 | observe | 3 | 0.667 | 388 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 167 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5064 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11363 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 469 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 464 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 347 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 325 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 324 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 316 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 294 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 289 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.767 | 99 | 30 | 129 |
| Surfboard-tg-mixed | 0.772 | 156 | 46 | 202 |
| mheidari-all | 0.857 | 54 | 9 | 63 |
| ermaozi | 0.981 | 53 | 1 | 54 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15386 | yes | 2.93 | 0 |
| SoliSpirit-all | 11363 | yes | 1.71 | 0 |
| Surfboard-tg-mixed | 8220 | yes | 2.03 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.0 | 0 |
| barry-far-vless | 5849 | yes | 0.24 | 0 |
| Surfboard-tg-vless | 5327 | yes | 1.84 | 0 |
| 10ium-ScrapeCategorize-Vless | 5064 | yes | 1.12 | 0 |
| mahdibland-V2RayAggregator | 4587 | yes | 1.56 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.57 | 0 |
| ninja-vless | 1791 | yes | 1.6 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 48 |
| 204 | 26 |
| cn-block | 11 |
| geo | 3 |
