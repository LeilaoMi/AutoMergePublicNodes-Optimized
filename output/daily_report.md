# AutoNodes 每日报告

生成时间：2026-11-14 18:22:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83318 |
| 去重后节点数 | 27127 |
| TCP 可达数 | 3000 |
| 真测通过数 | 314 |
| verified 输出数 | 89 |
| global 输出数 | 300 |
| all 输出数 | 27127 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.9 |
| fetch | 5.1 |
| generate | 10.6 |
| geo | 1.5 |
| probe | 78.7 |
| real_test | 59.5 |
| tcp | 75.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 26 | 24 | 2 | 92.3% |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 200 | 185 | 15 | 92.5% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 67 | 22 | 45 | 32.8% |
| vless | 93 | 68 | 25 | 73.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 32 |
| test_one_timeout:15.0s | 25 |
| cn-block:ProxyError | 11 |
| 204:TimeoutError | 7 |
| cn-block:TimeoutError | 5 |
| geo:ProxyError | 5 |
| speed:ProxyError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5979 |
| ConnectionRefusedError | 973 |
| gaierror | 303 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.947 | prefer | 25 | 0.96 | 527 |
| Surfboard-tg-mixed | 0.899 | prefer | 136 | 0.824 | 8883 |
| mheidari-all | 0.855 | prefer | 87 | 0.782 | 14109 |
| Au1rxx-base64 | 0.761 | prefer | 150 | 0.693 | 1751 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2652 |
| ermaozi-get_subscribe | 0.271 | observe | 1 | 1.0 | 405 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 179 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4966 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 449 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 444 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 327 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 305 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 304 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 296 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 274 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 269 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 180 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.693 | 104 | 46 | 150 |
| mheidari-all | 0.782 | 68 | 19 | 87 |
| Surfboard-tg-mixed | 0.824 | 112 | 24 | 136 |
| ermaozi | 0.96 | 24 | 1 | 25 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14109 | yes | 4.3 | 0 |
| SoliSpirit-all | 11700 | yes | 2.74 | 0 |
| Surfboard-tg-mixed | 8883 | yes | 2.86 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.2 | 0 |
| barry-far-vless | 6457 | yes | 2.49 | 0 |
| Surfboard-tg-vless | 6276 | yes | 2.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4966 | yes | 1.32 | 0 |
| mahdibland-V2RayAggregator | 4551 | yes | 2.19 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 2.29 | 0 |
| DeltaKronecker-all | 2652 | yes | 3.52 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 41 |
| test_one_timeout | 25 |
| cn-block | 17 |
| geo | 5 |
| speed | 3 |
