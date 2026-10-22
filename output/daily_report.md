# AutoNodes 每日报告

生成时间：2026-10-22 21:50:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 96237 |
| 去重后节点数 | 26704 |
| TCP 可达数 | 3000 |
| 真测通过数 | 367 |
| verified 输出数 | 113 |
| global 输出数 | 300 |
| all 输出数 | 26704 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.7 |
| fetch | 7.5 |
| generate | 14.2 |
| geo | 1.7 |
| probe | 95.4 |
| real_test | 69.5 |
| tcp | 79.6 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 74 | 72 | 2 | 97.3% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 124 | 118 | 6 | 95.2% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 35 | 35 | 0 | 100.0% |
| vless | 194 | 132 | 62 | 68.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 35 |
| speed:ClientOSError | 15 |
| 204:ProxyError | 7 |
| cn-block:ProxyError | 4 |
| geo:ClientOSError | 4 |
| 204:TimeoutError | 3 |
| cn-block:ClientOSError | 2 |
| 204:ClientOSError | 2 |
| geo:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6444 |
| ConnectionRefusedError | 1051 |
| gaierror | 241 |
| OSError | 238 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.982 | prefer | 72 | 0.972 | 573 |
| Au1rxx-base64 | 0.884 | prefer | 265 | 0.823 | 1601 |
| mheidari-all | 0.88 | prefer | 78 | 0.808 | 23896 |
| Surfboard-tg-mixed | 0.664 | observe | 9 | 1.0 | 7066 |
| DeltaKronecker-all | 0.407 | observe | 11 | 0.455 | 3641 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10026 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4176 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 175 |
| tg-oneclickvpnkeys | 0.257 | observe | 1 | 1.0 | 54 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 490 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 381 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 376 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 259 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 125 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.455 | 5 | 6 | 11 |
| mheidari-all | 0.808 | 63 | 15 | 78 |
| Au1rxx-base64 | 0.823 | 218 | 47 | 265 |
| ermaozi | 0.972 | 70 | 2 | 72 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23896 | yes | 6.23 | 0 |
| SoliSpirit-all | 10026 | yes | 5.51 | 0 |
| Epodonios-all | 7550 | yes | 5.56 | 0 |
| Surfboard-tg-mixed | 7066 | yes | 4.02 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.4 | 0 |
| barry-far-vless | 5640 | yes | 1.4 | 0 |
| Surfboard-tg-vless | 5426 | yes | 3.78 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 1.64 | 0 |
| mahdibland-V2RayAggregator | 4176 | yes | 2.92 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 35 |
| speed | 16 |
| 204 | 12 |
| cn-block | 6 |
| geo | 5 |
