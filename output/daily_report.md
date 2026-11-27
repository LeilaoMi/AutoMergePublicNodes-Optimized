# AutoNodes 每日报告

生成时间：2026-11-27 08:51:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 2/86 |
| 原始节点数 | 78402 |
| 去重后节点数 | 27160 |
| TCP 可达数 | 3000 |
| 真测通过数 | 393 |
| verified 输出数 | 51 |
| global 输出数 | 300 |
| all 输出数 | 27160 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.1 |
| fetch | 4.1 |
| generate | 9.0 |
| geo | 1.4 |
| probe | 68.4 |
| real_test | 74.8 |
| tcp | 82.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 42 | 42 | 0 | 100.0% |
| hysteria2 | 10 | 7 | 3 | 70.0% |
| shadowsocks | 280 | 224 | 56 | 80.0% |
| socks | 19 | 18 | 1 | 94.7% |
| trojan | 114 | 39 | 75 | 34.2% |
| vless | 123 | 79 | 44 | 64.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 65 |
| 204:ClientOSError | 63 |
| 204:ProxyError | 11 |
| geo:ClientOSError | 9 |
| speed:ClientOSError | 8 |
| cn-block:TimeoutError | 6 |
| cn-block:ClientOSError | 6 |
| 204:TimeoutError | 6 |
| speed:TimeoutError | 5 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6745 |
| ConnectionRefusedError | 983 |
| OSError | 243 |
| gaierror | 187 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | prefer | 53 | 1.0 | 422 |
| Surfboard-tg-mixed | 0.801 | prefer | 238 | 0.723 | 8568 |
| Au1rxx-base64 | 0.689 | observe | 187 | 0.62 | 1751 |
| mheidari-all | 0.658 | observe | 100 | 0.58 | 14315 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| tg-LonUp_M | 0.365 | observe | 3 | 1.0 | 173 |
| tg-oneclickvpnkeys | 0.363 | observe | 3 | 1.0 | 116 |
| ermaozi-get_subscribe | 0.284 | observe | 3 | 0.667 | 391 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 147 |
| tg-proxy_mtm | 0.258 | observe | 1 | 1.0 | 67 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-PrivateVPNs | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 475 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 470 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 353 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 331 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 330 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 322 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 300 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 295 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.58 | 58 | 42 | 100 |
| Au1rxx-base64 | 0.62 | 116 | 71 | 187 |
| ermaozi-get_subscribe | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.723 | 172 | 66 | 238 |
| tg-proxy_mtm | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| tg-LonUp_M | 1.0 | 3 | 0 | 3 |
| ermaozi | 1.0 | 53 | 0 | 53 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14315 | yes | 3.54 | 0 |
| SoliSpirit-all | 11572 | yes | 1.62 | 0 |
| Surfboard-tg-mixed | 8568 | yes | 2.02 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.37 | 0 |
| barry-far-vless | 5609 | yes | 0.51 | 0 |
| Surfboard-tg-vless | 5426 | yes | 2.45 | 0 |
| 10ium-ScrapeCategorize-Vless | 4936 | yes | 0.68 | 0 |
| mahdibland-V2RayAggregator | 4459 | yes | 1.7 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.87 | 0 |
| ninja-vless | 1791 | yes | 1.81 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 80 |
| test_one_timeout | 65 |
| speed | 13 |
| cn-block | 12 |
| geo | 10 |
