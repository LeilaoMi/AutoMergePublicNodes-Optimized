# AutoNodes 每日报告

生成时间：2026-10-14 12:10:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 4/90 |
| 原始节点数 | 98048 |
| 去重后节点数 | 27228 |
| TCP 可达数 | 3000 |
| 真测通过数 | 88 |
| verified 输出数 | 88 |
| global 输出数 | 97 |
| all 输出数 | 27228 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| generate | 54.3 |
| geo | 1.5 |
| probe | 108.3 |
| real_test | 75.6 |
| tcp | 114.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 88 | 82 | 6 | 93.2% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 140 | 121 | 19 | 86.4% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 12 | 5 | 7 | 41.7% |
| vless | 199 | 130 | 69 | 65.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 60 |
| speed:ClientOSError | 9 |
| geo:ClientOSError | 8 |
| cn-block:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| 204:TimeoutError | 3 |
| 204:ClientOSError | 3 |
| 204:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6001 |
| ConnectionRefusedError | 1058 |
| gaierror | 398 |
| OSError | 242 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | prefer | 19 | 1.0 | 144 |
| ermaozi-get_subscribe | 0.925 | prefer | 69 | 0.913 | 598 |
| mheidari-all | 0.877 | prefer | 72 | 0.806 | 23983 |
| Au1rxx-base64 | 0.855 | prefer | 211 | 0.787 | 1778 |
| Surfboard-tg-mixed | 0.616 | observe | 82 | 0.537 | 7056 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7542 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9834 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 448 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 339 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 334 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 164 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 159 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 83 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.537 | 44 | 38 | 82 |
| Au1rxx-base64 | 0.787 | 166 | 45 | 211 |
| mheidari-all | 0.806 | 58 | 14 | 72 |
| ermaozi-get_subscribe | 0.913 | 63 | 6 | 69 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23983 | yes | 5.35 | 0 |
| SoliSpirit-all | 9834 | yes | 4.67 | 0 |
| Epodonios-all | 7542 | yes | 6.85 | 0 |
| Surfboard-tg-mixed | 7056 | yes | 6.35 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.76 | 0 |
| barry-far-vless | 5831 | yes | 1.87 | 0 |
| Surfboard-tg-vless | 5579 | yes | 4.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 1.46 | 0 |
| DeltaKronecker-all | 4803 | yes | 6.4 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 2.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 60 |
| cn-block | 16 |
| speed | 11 |
| geo | 9 |
| 204 | 8 |
