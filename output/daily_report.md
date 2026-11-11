# AutoNodes 每日报告

生成时间：2026-11-11 19:48:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 82898 |
| 去重后节点数 | 26904 |
| TCP 可达数 | 3000 |
| 真测通过数 | 422 |
| verified 输出数 | 80 |
| global 输出数 | 300 |
| all 输出数 | 26904 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.4 |
| fetch | 5.2 |
| generate | 11.4 |
| geo | 1.5 |
| probe | 83.2 |
| real_test | 85.9 |
| tcp | 82.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 82 | 81 | 1 | 98.8% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 186 | 170 | 16 | 91.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 86 | 52 | 34 | 60.5% |
| vless | 201 | 107 | 94 | 53.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 60 |
| 204:ProxyError | 42 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 8 |
| speed:ProxyError | 5 |
| cn-block:TimeoutError | 5 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| geo:ClientOSError | 2 |
| speed:TimeoutError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6243 |
| ConnectionRefusedError | 979 |
| OSError | 236 |
| gaierror | 211 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 82 | 0.988 | 608 |
| Au1rxx-base64 | 0.777 | prefer | 189 | 0.709 | 1751 |
| mheidari-all | 0.768 | prefer | 91 | 0.692 | 14491 |
| Surfboard-tg-mixed | 0.767 | prefer | 199 | 0.688 | 8393 |
| SoliSpirit-all | 0.48 | observe | 4 | 1.0 | 11151 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2629 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4981 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6306 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 442 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 437 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 320 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 298 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 297 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 289 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 267 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 262 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 173 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.688 | 137 | 62 | 199 |
| mheidari-all | 0.692 | 63 | 28 | 91 |
| Au1rxx-base64 | 0.709 | 134 | 55 | 189 |
| ermaozi | 0.988 | 81 | 1 | 82 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| SoliSpirit-all | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14491 | yes | 2.7 | 0 |
| SoliSpirit-all | 11151 | yes | 4.4 | 0 |
| Surfboard-tg-mixed | 8393 | yes | 3.48 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.96 | 0 |
| barry-far-vless | 6516 | yes | 1.41 | 0 |
| Surfboard-tg-vless | 6306 | yes | 3.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4981 | yes | 0.75 | 0 |
| mahdibland-V2RayAggregator | 4589 | yes | 2.31 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.81 | 0 |
| DeltaKronecker-all | 2629 | yes | 4.19 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 60 |
| 204 | 53 |
| speed | 20 |
| cn-block | 9 |
| geo | 6 |
