# AutoNodes 每日报告

生成时间：2026-11-25 21:55:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 78555 |
| 去重后节点数 | 27517 |
| TCP 可达数 | 3000 |
| 真测通过数 | 360 |
| verified 输出数 | 81 |
| global 输出数 | 300 |
| all 输出数 | 27517 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.0 |
| fetch | 7.0 |
| generate | 17.5 |
| geo | 1.7 |
| probe | 108.3 |
| real_test | 59.7 |
| tcp | 80.9 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 3 | 2 | 60.0% |
| http | 25 | 23 | 2 | 92.0% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 221 | 193 | 28 | 87.3% |
| socks | 7 | 7 | 0 | 100.0% |
| trojan | 8 | 7 | 1 | 87.5% |
| vless | 161 | 126 | 35 | 78.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 38 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| cn-block:TimeoutError | 3 |
| geo:ProxyError | 2 |
| speed:TimeoutError | 1 |
| geo:ClientOSError | 1 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6711 |
| ConnectionRefusedError | 1071 |
| gaierror | 286 |
| OSError | 244 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.995 | prefer | 91 | 0.934 | 1751 |
| ermaozi | 0.979 | prefer | 25 | 1.0 | 403 |
| Surfboard-tg-mixed | 0.897 | prefer | 129 | 0.822 | 8209 |
| mheidari-all | 0.878 | prefer | 176 | 0.801 | 15044 |
| tg-LonUp_M | 0.446 | observe | 5 | 1.0 | 173 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.307 | observe | 5 | 0.6 | 356 |
| SoliSpirit-all | 0.287 | observe | 2 | 0.5 | 11598 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4958 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 472 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 467 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 350 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 328 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 327 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 319 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 297 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 292 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 2 | 2 |
| SoliSpirit-all | 0.5 | 1 | 1 | 2 |
| ermaozi-get_subscribe | 0.6 | 3 | 2 | 5 |
| mheidari-all | 0.801 | 141 | 35 | 176 |
| Surfboard-tg-mixed | 0.822 | 106 | 23 | 129 |
| Au1rxx-base64 | 0.934 | 85 | 6 | 91 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 5 | 0 | 5 |
| ermaozi | 1.0 | 25 | 0 | 25 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15044 | yes | 4.84 | 0 |
| SoliSpirit-all | 11598 | yes | 3.45 | 0 |
| Surfboard-tg-mixed | 8209 | yes | 5.21 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.96 | 0 |
| barry-far-vless | 5559 | yes | 1.4 | 0 |
| Surfboard-tg-vless | 5378 | yes | 3.62 | 0 |
| 10ium-ScrapeCategorize-Vless | 4958 | yes | 0.97 | 0 |
| mahdibland-V2RayAggregator | 4463 | yes | 3.13 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.06 | 0 |
| ninja-vless | 1791 | yes | 3.38 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 38 |
| 204 | 14 |
| cn-block | 12 |
| geo | 3 |
| speed | 2 |
