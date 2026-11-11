# AutoNodes 每日报告

生成时间：2026-11-11 06:49:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 82378 |
| 去重后节点数 | 26936 |
| TCP 可达数 | 3000 |
| 真测通过数 | 464 |
| verified 输出数 | 92 |
| global 输出数 | 300 |
| all 输出数 | 26936 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.2 |
| fetch | 5.9 |
| generate | 11.9 |
| geo | 1.5 |
| probe | 85.9 |
| real_test | 76.5 |
| tcp | 83.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 81 | 81 | 0 | 100.0% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 210 | 193 | 17 | 91.9% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 80 | 73 | 7 | 91.2% |
| vless | 191 | 106 | 85 | 55.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 69 |
| speed:ClientOSError | 12 |
| 204:ProxyError | 9 |
| cn-block:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| 204:TimeoutError | 3 |
| geo:ClientOSError | 2 |
| speed:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6605 |
| ConnectionRefusedError | 964 |
| OSError | 236 |
| gaierror | 126 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.99 | prefer | 85 | 0.976 | 601 |
| Surfboard-tg-mixed | 0.93 | prefer | 125 | 0.856 | 8415 |
| Au1rxx-base64 | 0.847 | prefer | 222 | 0.779 | 1751 |
| mheidari-all | 0.78 | prefer | 138 | 0.703 | 13964 |
| ninja-vless | 0.43 | observe | 3 | 1.0 | 1791 |
| barry-far-vless | 0.335 | observe | 1 | 1.0 | 6562 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4955 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2620 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 2 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 441 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 436 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 319 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 297 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 296 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 288 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 261 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.703 | 97 | 41 | 138 |
| Au1rxx-base64 | 0.779 | 173 | 49 | 222 |
| Surfboard-tg-mixed | 0.856 | 107 | 18 | 125 |
| ermaozi | 0.976 | 83 | 2 | 85 |
| barry-far-vless | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13964 | yes | 5.26 | 0 |
| SoliSpirit-all | 11127 | yes | 1.65 | 0 |
| Surfboard-tg-mixed | 8415 | yes | 3.68 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.3 | 0 |
| barry-far-vless | 6562 | yes | 0.74 | 0 |
| Surfboard-tg-vless | 6298 | yes | 2.98 | 0 |
| 10ium-ScrapeCategorize-Vless | 4955 | yes | 0.93 | 0 |
| mahdibland-V2RayAggregator | 4589 | yes | 2.58 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.25 | 0 |
| DeltaKronecker-all | 2620 | yes | 5.06 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 69 |
| 204 | 15 |
| speed | 14 |
| cn-block | 12 |
| geo | 2 |
