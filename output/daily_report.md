# AutoNodes 每日报告

生成时间：2026-11-22 19:55:30

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82521 |
| 去重后节点数 | 28181 |
| TCP 可达数 | 3000 |
| 真测通过数 | 322 |
| verified 输出数 | 41 |
| global 输出数 | 300 |
| all 输出数 | 28181 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.4 |
| fetch | 6.9 |
| generate | 14.9 |
| geo | 1.6 |
| probe | 96.5 |
| real_test | 61.8 |
| tcp | 82.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 3 | 0 | 100.0% |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 8 | 6 | 2 | 75.0% |
| shadowsocks | 236 | 196 | 40 | 83.1% |
| socks | 6 | 6 | 0 | 100.0% |
| trojan | 44 | 12 | 32 | 27.3% |
| vless | 124 | 82 | 42 | 66.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 55 |
| 204:ProxyError | 27 |
| cn-block:ClientOSError | 10 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 5 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| geo:ClientOSError | 1 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6541 |
| ConnectionRefusedError | 1065 |
| gaierror | 325 |
| OSError | 245 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.977 | prefer | 23 | 1.0 | 415 |
| Surfboard-tg-mixed | 0.847 | prefer | 161 | 0.77 | 8739 |
| mheidari-all | 0.787 | prefer | 121 | 0.711 | 14491 |
| Au1rxx-base64 | 0.734 | prefer | 129 | 0.667 | 1751 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.371 | observe | 3 | 1.0 | 318 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2671 |
| tg-LonUp_M | 0.275 | observe | 3 | 0.667 | 167 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 109 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5069 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 1 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 466 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 461 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 344 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 322 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 321 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 313 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 291 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 286 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.667 | 86 | 43 | 129 |
| mheidari-all | 0.711 | 86 | 35 | 121 |
| Surfboard-tg-mixed | 0.77 | 124 | 37 | 161 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| ermaozi-get_subscribe | 1.0 | 3 | 0 | 3 |
| ermaozi | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14491 | yes | 5.45 | 0 |
| SoliSpirit-all | 12183 | yes | 3.07 | 0 |
| Surfboard-tg-mixed | 8739 | yes | 3.42 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.61 | 0 |
| barry-far-vless | 5881 | yes | 1.81 | 0 |
| Surfboard-tg-vless | 5664 | yes | 3.63 | 0 |
| 10ium-ScrapeCategorize-Vless | 5069 | yes | 2.04 | 0 |
| mahdibland-V2RayAggregator | 4512 | yes | 2.98 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.12 | 0 |
| DeltaKronecker-all | 2671 | yes | 5.88 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 55 |
| 204 | 36 |
| cn-block | 16 |
| speed | 5 |
| geo | 4 |
