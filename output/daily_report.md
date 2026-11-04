# AutoNodes 每日报告

生成时间：2026-11-04 19:59:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82735 |
| 去重后节点数 | 26928 |
| TCP 可达数 | 3000 |
| 真测通过数 | 365 |
| verified 输出数 | 40 |
| global 输出数 | 300 |
| all 输出数 | 26928 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.2 |
| fetch | 35.3 |
| generate | 12.3 |
| geo | 1.5 |
| probe | 86.3 |
| real_test | 74.4 |
| tcp | 82.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 18 | 16 | 2 | 88.9% |
| hysteria2 | 17 | 12 | 5 | 70.6% |
| shadowsocks | 222 | 190 | 32 | 85.6% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 52 | 25 | 27 | 48.1% |
| vless | 180 | 121 | 59 | 67.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 66 |
| 204:ProxyError | 21 |
| 204:TimeoutError | 10 |
| 204:ClientOSError | 9 |
| cn-block:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| speed:ClientOSError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6330 |
| ConnectionRefusedError | 974 |
| OSError | 232 |
| gaierror | 141 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.88 | prefer | 163 | 0.804 | 15192 |
| Surfboard-tg-mixed | 0.805 | prefer | 67 | 0.731 | 8707 |
| zhangkai | 0.796 | prefer | 18 | 0.889 | 43 |
| Au1rxx-base64 | 0.759 | prefer | 239 | 0.69 | 1751 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| ermaozi | 0.315 | observe | 2 | 1.0 | 83 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 174 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2526 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 421 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 416 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 299 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 277 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 276 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 268 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 246 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 165 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 152 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.69 | 165 | 74 | 239 |
| Surfboard-tg-mixed | 0.731 | 49 | 18 | 67 |
| mheidari-all | 0.804 | 131 | 32 | 163 |
| zhangkai | 0.889 | 16 | 2 | 18 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15192 | yes | 4.91 | 0 |
| SoliSpirit-all | 10836 | yes | 4.8 | 0 |
| Surfboard-tg-mixed | 8707 | yes | 4.49 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 0.77 | 0 |
| barry-far-vless | 6348 | yes | 3.09 | 0 |
| Surfboard-tg-vless | 6137 | yes | 4.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 3.16 | 0 |
| mahdibland-V2RayAggregator | 4608 | yes | 0.61 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.91 | 0 |
| DeltaKronecker-all | 2526 | yes | 5.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 66 |
| 204 | 40 |
| cn-block | 13 |
| speed | 5 |
| geo | 4 |
