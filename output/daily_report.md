# AutoNodes 每日报告

生成时间：2026-10-22 17:24:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 96736 |
| 去重后节点数 | 26708 |
| TCP 可达数 | 3000 |
| 真测通过数 | 351 |
| verified 输出数 | 111 |
| global 输出数 | 300 |
| all 输出数 | 26708 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.0 |
| fetch | 7.4 |
| generate | 14.0 |
| geo | 1.5 |
| probe | 94.7 |
| real_test | 72.9 |
| tcp | 81.9 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 71 | 70 | 1 | 98.6% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 146 | 121 | 25 | 82.9% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 42 | 33 | 9 | 78.6% |
| vless | 183 | 116 | 67 | 63.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 67 |
| speed:ClientOSError | 13 |
| cn-block:TimeoutError | 6 |
| geo:ClientOSError | 6 |
| 204:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| geo:TimeoutError | 2 |
| 204:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6544 |
| ConnectionRefusedError | 1036 |
| OSError | 237 |
| gaierror | 222 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.995 | prefer | 70 | 0.986 | 573 |
| mheidari-all | 0.83 | prefer | 70 | 0.757 | 24062 |
| Au1rxx-base64 | 0.82 | prefer | 251 | 0.761 | 1529 |
| Surfboard-tg-mixed | 0.735 | prefer | 53 | 0.66 | 7066 |
| DeltaKronecker-all | 0.314 | observe | 9 | 0.333 | 3641 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 70 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |
| Epodonios-all | 0.255 | observe | 0 | None | 7538 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 489 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 380 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 375 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 258 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 124 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.333 | 1 | 2 | 3 |
| DeltaKronecker-all | 0.333 | 3 | 6 | 9 |
| Surfboard-tg-mixed | 0.66 | 35 | 18 | 53 |
| mheidari-all | 0.757 | 53 | 17 | 70 |
| Au1rxx-base64 | 0.761 | 191 | 60 | 251 |
| ermaozi | 0.986 | 69 | 1 | 70 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24062 | yes | 7.38 | 0 |
| SoliSpirit-all | 10555 | yes | 3.73 | 0 |
| Epodonios-all | 7538 | yes | 6.38 | 0 |
| Surfboard-tg-mixed | 7066 | yes | 3.93 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.82 | 0 |
| barry-far-vless | 5601 | yes | 1.47 | 0 |
| Surfboard-tg-vless | 5426 | yes | 4.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 4.99 | 0 |
| mahdibland-V2RayAggregator | 4164 | yes | 2.79 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.97 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 67 |
| speed | 13 |
| cn-block | 10 |
| geo | 9 |
| 204 | 7 |
