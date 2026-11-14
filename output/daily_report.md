# AutoNodes 每日报告

生成时间：2026-11-14 06:48:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83825 |
| 去重后节点数 | 27035 |
| TCP 可达数 | 3000 |
| 真测通过数 | 468 |
| verified 输出数 | 89 |
| global 输出数 | 300 |
| all 输出数 | 27035 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 76.1 |
| fetch | 4.7 |
| generate | 8.5 |
| geo | 1.4 |
| probe | 70.8 |
| real_test | 79.7 |
| tcp | 67.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 1 | 2 | 33.3% |
| http | 71 | 68 | 3 | 95.8% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 209 | 191 | 18 | 91.4% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 106 | 95 | 11 | 89.6% |
| vless | 185 | 99 | 86 | 53.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 49 |
| speed:ClientOSError | 28 |
| 204:ProxyError | 18 |
| cn-block:TimeoutError | 7 |
| 204:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5757 |
| ConnectionRefusedError | 978 |
| gaierror | 347 |
| OSError | 344 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.958 | prefer | 74 | 0.946 | 597 |
| Au1rxx-base64 | 0.888 | prefer | 196 | 0.821 | 1751 |
| mheidari-all | 0.834 | prefer | 67 | 0.761 | 14251 |
| Surfboard-tg-mixed | 0.816 | prefer | 248 | 0.738 | 8942 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4551 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 162 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| ermaozi-get_subscribe | 0.274 | observe | 1 | 1.0 | 471 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4900 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 448 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 443 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 326 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 304 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 303 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 295 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 273 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 268 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 179 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.738 | 183 | 65 | 248 |
| mheidari-all | 0.761 | 51 | 16 | 67 |
| Au1rxx-base64 | 0.821 | 161 | 35 | 196 |
| ermaozi | 0.946 | 70 | 4 | 74 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14251 | yes | 3.87 | 0 |
| SoliSpirit-all | 11507 | yes | 1.73 | 0 |
| Surfboard-tg-mixed | 8942 | yes | 2.74 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.49 | 0 |
| barry-far-vless | 6640 | yes | 0.59 | 0 |
| Surfboard-tg-vless | 6457 | yes | 2.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4900 | yes | 0.42 | 0 |
| mahdibland-V2RayAggregator | 4551 | yes | 1.88 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.28 | 0 |
| DeltaKronecker-all | 2734 | yes | 3.76 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 49 |
| speed | 30 |
| 204 | 27 |
| cn-block | 14 |
| geo | 2 |
