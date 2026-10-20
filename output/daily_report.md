# AutoNodes 每日报告

生成时间：2026-10-20 17:24:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 94143 |
| 去重后节点数 | 26403 |
| TCP 可达数 | 3000 |
| 真测通过数 | 323 |
| verified 输出数 | 71 |
| global 输出数 | 300 |
| all 输出数 | 26403 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 18.3 |
| fetch | 6.0 |
| generate | 11.4 |
| geo | 1.5 |
| probe | 84.8 |
| real_test | 73.8 |
| tcp | 80.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 29 | 0 | 100.0% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 114 | 102 | 12 | 89.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 37 | 28 | 9 | 75.7% |
| vless | 198 | 153 | 45 | 77.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 41 |
| speed:ClientOSError | 10 |
| geo:ClientOSError | 5 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| 204:ProxyError | 2 |
| 204:TimeoutError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6496 |
| ConnectionRefusedError | 1054 |
| OSError | 235 |
| gaierror | 216 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | prefer | 27 | 1.0 | 31 |
| Au1rxx-base64 | 0.88 | prefer | 257 | 0.829 | 1348 |
| mheidari-all | 0.858 | prefer | 70 | 0.786 | 23236 |
| Surfboard-tg-mixed | 0.523 | observe | 15 | 0.533 | 6911 |
| DeltaKronecker-all | 0.489 | observe | 6 | 0.833 | 3519 |
| chromego_merge | 0.448 | observe | 5 | 1.0 | 227 |
| ermaozi | 0.36 | observe | 3 | 1.0 | 55 |
| Epodonios-all | 0.349 | observe | 3 | 0.667 | 7384 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10084 |
| tg-oneclickvpnkeys | 0.314 | observe | 2 | 1.0 | 79 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 5 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 481 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 372 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 367 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 250 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 116 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.533 | 8 | 7 | 15 |
| Epodonios-all | 0.667 | 2 | 1 | 3 |
| tg-proxy_kafee | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.786 | 55 | 15 | 70 |
| Au1rxx-base64 | 0.829 | 213 | 44 | 257 |
| DeltaKronecker-all | 0.833 | 5 | 1 | 6 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23236 | yes | 4.76 | 0 |
| SoliSpirit-all | 10084 | yes | 5.29 | 0 |
| Epodonios-all | 7384 | yes | 4.99 | 0 |
| Surfboard-tg-mixed | 6911 | yes | 3.4 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.77 | 0 |
| barry-far-vless | 5732 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 5515 | yes | 3.07 | 0 |
| 10ium-ScrapeCategorize-Vless | 4967 | yes | 2.57 | 0 |
| mahdibland-V2RayAggregator | 4127 | yes | 2.46 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.52 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 41 |
| speed | 11 |
| cn-block | 8 |
| geo | 5 |
| 204 | 4 |
