# AutoNodes 每日报告

生成时间：2026-11-21 07:30:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82370 |
| 去重后节点数 | 27798 |
| TCP 可达数 | 3000 |
| 真测通过数 | 448 |
| verified 输出数 | 52 |
| global 输出数 | 300 |
| all 输出数 | 27798 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.0 |
| fetch | 6.9 |
| generate | 14.9 |
| geo | 1.5 |
| probe | 97.8 |
| real_test | 78.3 |
| tcp | 85.0 |
| write_verified | 0.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 247 | 221 | 26 | 89.5% |
| socks | 8 | 6 | 2 | 75.0% |
| trojan | 58 | 53 | 5 | 91.4% |
| vless | 192 | 139 | 53 | 72.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 57 |
| 204:ProxyError | 10 |
| cn-block:ClientOSError | 8 |
| 204:TimeoutError | 4 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6781 |
| ConnectionRefusedError | 994 |
| OSError | 237 |
| gaierror | 214 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | prefer | 24 | 1.0 | 443 |
| Surfboard-tg-mixed | 0.928 | prefer | 143 | 0.853 | 8565 |
| mheidari-all | 0.914 | prefer | 191 | 0.838 | 14439 |
| Au1rxx-base64 | 0.875 | prefer | 177 | 0.808 | 1751 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2910 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 117 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5045 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 463 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 458 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 341 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 319 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 318 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 310 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 288 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 283 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.808 | 143 | 34 | 177 |
| mheidari-all | 0.838 | 160 | 31 | 191 |
| Surfboard-tg-mixed | 0.853 | 122 | 21 | 143 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14439 | yes | 5.48 | 0 |
| SoliSpirit-all | 11789 | yes | 4.74 | 0 |
| Surfboard-tg-mixed | 8565 | yes | 4.18 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.63 | 0 |
| barry-far-vless | 5914 | yes | 2.44 | 0 |
| Surfboard-tg-vless | 5496 | yes | 3.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 5045 | yes | 2.71 | 0 |
| mahdibland-V2RayAggregator | 4518 | yes | 3.12 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.77 | 0 |
| DeltaKronecker-all | 2910 | yes | 5.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 57 |
| 204 | 15 |
| cn-block | 14 |
| geo | 1 |
