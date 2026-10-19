# AutoNodes 每日报告

生成时间：2026-10-19 22:34:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 5/88 |
| 原始节点数 | 94461 |
| 去重后节点数 | 26025 |
| TCP 可达数 | 3000 |
| 真测通过数 | 471 |
| verified 输出数 | 38 |
| global 输出数 | 300 |
| all 输出数 | 26025 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.8 |
| fetch | 7.1 |
| generate | 13.5 |
| geo | 1.6 |
| probe | 97.5 |
| real_test | 76.1 |
| tcp | 78.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 24 | 22 | 2 | 91.7% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 156 | 141 | 15 | 90.4% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 105 | 98 | 7 | 93.3% |
| vless | 265 | 195 | 70 | 73.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 34 |
| speed:ClientOSError | 14 |
| geo:ClientOSError | 13 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 5 |
| 204:TimeoutError | 4 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6398 |
| ConnectionRefusedError | 1031 |
| gaierror | 257 |
| OSError | 235 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 27 |
| mheidari-all | 0.926 | prefer | 63 | 0.857 | 23238 |
| DeltaKronecker-all | 0.913 | prefer | 70 | 0.843 | 3294 |
| Au1rxx-base64 | 0.902 | prefer | 283 | 0.848 | 1411 |
| Surfboard-tg-mixed | 0.842 | prefer | 120 | 0.767 | 7064 |
| roosterkid-openproxylist-v2ray | 0.364 | observe | 3 | 1.0 | 150 |
| 10ium-HighSpeed | 0.345 | observe | 2 | 1.0 | 839 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 9850 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 170 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 478 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 369 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 364 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 247 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 224 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 189 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 113 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.25 | 1 | 3 | 4 |
| ermaozi-get_subscribe | 0.333 | 1 | 2 | 3 |
| Surfboard-tg-mixed | 0.767 | 92 | 28 | 120 |
| DeltaKronecker-all | 0.843 | 59 | 11 | 70 |
| Au1rxx-base64 | 0.848 | 240 | 43 | 283 |
| mheidari-all | 0.857 | 54 | 9 | 63 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23238 | yes | 5.86 | 0 |
| SoliSpirit-all | 9850 | yes | 4.04 | 0 |
| Epodonios-all | 7515 | yes | 6.15 | 0 |
| Surfboard-tg-mixed | 7064 | yes | 5.21 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.5 | 0 |
| barry-far-vless | 5797 | yes | 1.24 | 0 |
| Surfboard-tg-vless | 5579 | yes | 4.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4940 | yes | 1.48 | 0 |
| mahdibland-V2RayAggregator | 4278 | yes | 2.55 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.02 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 34 |
| 204 | 21 |
| speed | 15 |
| cn-block | 13 |
| geo | 13 |
