# AutoNodes 每日报告

生成时间：2026-11-14 22:39:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 82855 |
| 去重后节点数 | 27069 |
| TCP 可达数 | 3000 |
| 真测通过数 | 450 |
| verified 输出数 | 89 |
| global 输出数 | 300 |
| all 输出数 | 27069 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 31.1 |
| fetch | 5.8 |
| generate | 11.9 |
| geo | 1.6 |
| probe | 88.5 |
| real_test | 74.8 |
| tcp | 83.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 229 | 210 | 19 | 91.7% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 67 | 62 | 5 | 92.5% |
| vless | 195 | 138 | 57 | 70.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 48 |
| 204:ProxyError | 11 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 2 |
| cn-block:TimeoutError | 2 |
| cn-block:ProxyError | 2 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6332 |
| ConnectionRefusedError | 968 |
| OSError | 237 |
| gaierror | 176 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.984 | prefer | 25 | 1.0 | 527 |
| mheidari-all | 0.942 | prefer | 85 | 0.871 | 13757 |
| Surfboard-tg-mixed | 0.928 | prefer | 208 | 0.851 | 9013 |
| Au1rxx-base64 | 0.878 | prefer | 211 | 0.81 | 1751 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2652 |
| ermaozi-get_subscribe | 0.271 | observe | 1 | 1.0 | 405 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 168 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4966 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| chromego_merge | 0.025 | observe | 0 | None | 1 | 0 |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 450 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 445 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 328 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 306 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 305 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 297 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 275 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 270 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 181 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.81 | 171 | 40 | 211 |
| Surfboard-tg-mixed | 0.851 | 177 | 31 | 208 |
| mheidari-all | 0.871 | 74 | 11 | 85 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 25 | 0 | 25 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13757 | yes | 5.0 | 0 |
| SoliSpirit-all | 11640 | yes | 2.3 | 0 |
| Surfboard-tg-mixed | 9013 | yes | 4.18 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.12 | 0 |
| barry-far-vless | 6499 | yes | 1.62 | 0 |
| Surfboard-tg-vless | 6319 | yes | 2.74 | 0 |
| 10ium-ScrapeCategorize-Vless | 4966 | yes | 1.31 | 0 |
| mahdibland-V2RayAggregator | 4551 | yes | 2.34 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.68 | 0 |
| DeltaKronecker-all | 2652 | yes | 3.11 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 48 |
| 204 | 24 |
| cn-block | 6 |
| speed | 3 |
| geo | 1 |
