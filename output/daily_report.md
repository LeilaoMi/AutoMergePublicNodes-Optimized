# AutoNodes 每日报告

生成时间：2026-11-20 20:37:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 82572 |
| 去重后节点数 | 27861 |
| TCP 可达数 | 3000 |
| 真测通过数 | 368 |
| verified 输出数 | 41 |
| global 输出数 | 300 |
| all 输出数 | 27861 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.8 |
| fetch | 6.1 |
| generate | 13.0 |
| geo | 1.6 |
| probe | 92.4 |
| real_test | 77.0 |
| tcp | 85.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 22 | 3 | 88.0% |
| hysteria2 | 13 | 11 | 2 | 84.6% |
| shadowsocks | 229 | 198 | 31 | 86.5% |
| socks | 14 | 13 | 1 | 92.9% |
| trojan | 42 | 11 | 31 | 26.2% |
| vless | 196 | 126 | 70 | 64.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 65 |
| 204:ProxyError | 39 |
| cn-block:ProxyError | 8 |
| 204:TimeoutError | 7 |
| cn-block:ClientOSError | 7 |
| speed:TimeoutError | 4 |
| cn-block:TimeoutError | 3 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6732 |
| ConnectionRefusedError | 998 |
| OSError | 238 |
| gaierror | 212 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.882 | prefer | 27 | 0.889 | 492 |
| mheidari-all | 0.875 | prefer | 115 | 0.8 | 14341 |
| Surfboard-tg-mixed | 0.847 | prefer | 213 | 0.77 | 8704 |
| Au1rxx-base64 | 0.676 | observe | 158 | 0.608 | 1751 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2910 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 130 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5045 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 462 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 457 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 340 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 318 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 317 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 309 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 287 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 282 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.608 | 96 | 62 | 158 |
| Surfboard-tg-mixed | 0.77 | 164 | 49 | 213 |
| mheidari-all | 0.8 | 92 | 23 | 115 |
| ermaozi | 0.889 | 24 | 3 | 27 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14341 | yes | 5.21 | 0 |
| SoliSpirit-all | 11804 | yes | 3.95 | 0 |
| Surfboard-tg-mixed | 8704 | yes | 4.18 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.11 | 0 |
| barry-far-vless | 5776 | yes | 1.82 | 0 |
| Surfboard-tg-vless | 5734 | yes | 3.87 | 0 |
| 10ium-ScrapeCategorize-Vless | 5045 | yes | 2.19 | 0 |
| mahdibland-V2RayAggregator | 4518 | yes | 2.64 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.38 | 0 |
| DeltaKronecker-all | 2910 | yes | 4.6 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 65 |
| 204 | 49 |
| cn-block | 18 |
| speed | 5 |
| geo | 1 |
