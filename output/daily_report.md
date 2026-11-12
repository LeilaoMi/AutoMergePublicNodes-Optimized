# AutoNodes 每日报告

生成时间：2026-11-12 20:12:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 20/0 |
| 清理建议：优先/观察 | 4/83 |
| 原始节点数 | 83498 |
| 去重后节点数 | 26911 |
| TCP 可达数 | 3000 |
| 真测通过数 | 383 |
| verified 输出数 | 61 |
| global 输出数 | 300 |
| all 输出数 | 26911 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.4 |
| fetch | 7.1 |
| generate | 14.7 |
| geo | 1.5 |
| probe | 98.3 |
| real_test | 71.4 |
| tcp | 81.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 55 | 53 | 2 | 96.4% |
| hysteria2 | 10 | 10 | 0 | 100.0% |
| shadowsocks | 196 | 178 | 18 | 90.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 68 | 38 | 30 | 55.9% |
| vless | 165 | 103 | 62 | 62.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 33 |
| test_one_timeout:15.0s | 33 |
| speed:ClientOSError | 19 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6489 |
| ConnectionRefusedError | 954 |
| OSError | 238 |
| gaierror | 158 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.954 | prefer | 56 | 0.946 | 579 |
| Au1rxx-base64 | 0.876 | prefer | 168 | 0.81 | 1751 |
| Surfboard-tg-mixed | 0.799 | prefer | 215 | 0.721 | 8770 |
| mheidari-all | 0.747 | prefer | 55 | 0.673 | 14228 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4998 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2737 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11515 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6332 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 5 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 444 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 439 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 322 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 300 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 299 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 291 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 269 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 264 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 188 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 175 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.673 | 37 | 18 | 55 |
| Surfboard-tg-mixed | 0.721 | 155 | 60 | 215 |
| Au1rxx-base64 | 0.81 | 136 | 32 | 168 |
| ermaozi | 0.946 | 53 | 3 | 56 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14228 | yes | 4.77 | 0 |
| SoliSpirit-all | 11515 | yes | 3.17 | 0 |
| Surfboard-tg-mixed | 8770 | yes | 3.56 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.68 | 0 |
| barry-far-vless | 6555 | yes | 1.98 | 0 |
| Surfboard-tg-vless | 6332 | yes | 4.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 4998 | yes | 0.99 | 0 |
| mahdibland-V2RayAggregator | 4618 | yes | 3.18 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.72 | 0 |
| DeltaKronecker-all | 2737 | yes | 6.2 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 42 |
| test_one_timeout | 33 |
| speed | 23 |
| cn-block | 12 |
| geo | 3 |
