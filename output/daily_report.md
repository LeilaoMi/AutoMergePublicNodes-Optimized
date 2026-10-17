# AutoNodes 每日报告

生成时间：2026-10-17 20:49:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99294 |
| 去重后节点数 | 27807 |
| TCP 可达数 | 3000 |
| 真测通过数 | 364 |
| verified 输出数 | 66 |
| global 输出数 | 300 |
| all 输出数 | 27807 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.5 |
| fetch | 4.0 |
| generate | 7.7 |
| geo | 1.4 |
| probe | 74.4 |
| real_test | 78.5 |
| tcp | 91.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 31 | 26 | 5 | 83.9% |
| hysteria2 | 13 | 11 | 2 | 84.6% |
| shadowsocks | 141 | 126 | 15 | 89.4% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 27 | 25 | 2 | 92.6% |
| vless | 246 | 175 | 71 | 71.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| speed:ClientOSError | 12 |
| 204:TimeoutError | 11 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 6 |
| cn-block:TimeoutError | 5 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 2 |
| speed:ClientPayloadError | 1 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7635 |
| ConnectionRefusedError | 1001 |
| OSError | 232 |
| gaierror | 67 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.925 | prefer | 28 | 0.929 | 623 |
| Au1rxx-base64 | 0.887 | prefer | 393 | 0.809 | 1992 |
| mheidari-all | 0.674 | observe | 30 | 0.6 | 23876 |
| Surfboard-tg-mixed | 0.438 | observe | 3 | 1.0 | 7109 |
| Surfboard-tg-vless | 0.335 | observe | 1 | 1.0 | 5614 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 176 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4986 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7590 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.108 | observe | 2 | 0.0 | 0 | 99 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| DeltaKronecker-all | 0.17 | observe | 3 | 0.0 | 0 | 4999 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 471 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 362 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 357 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 187 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 182 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 106 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.6 | 18 | 12 | 30 |
| Au1rxx-base64 | 0.809 | 318 | 75 | 393 |
| ermaozi | 0.929 | 26 | 2 | 28 |
| Surfboard-tg-vless | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23876 | yes | 3.21 | 0 |
| SoliSpirit-all | 10112 | yes | 2.52 | 0 |
| Epodonios-all | 7590 | yes | 2.87 | 0 |
| Surfboard-tg-mixed | 7109 | yes | 2.71 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.52 | 0 |
| barry-far-vless | 5860 | yes | 1.18 | 0 |
| Surfboard-tg-vless | 5614 | yes | 2.6 | 0 |
| DeltaKronecker-all | 4999 | yes | 3.38 | 0 |
| 10ium-ScrapeCategorize-Vless | 4986 | yes | 1.04 | 0 |
| mahdibland-V2RayAggregator | 4295 | yes | 1.76 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 44 |
| 204 | 20 |
| cn-block | 16 |
| speed | 14 |
| geo | 3 |
