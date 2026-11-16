# AutoNodes 每日报告

生成时间：2026-11-16 22:23:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83258 |
| 去重后节点数 | 27658 |
| TCP 可达数 | 3000 |
| 真测通过数 | 527 |
| verified 输出数 | 27 |
| global 输出数 | 300 |
| all 输出数 | 27658 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 38.1 |
| fetch | 4.9 |
| generate | 11.5 |
| geo | 1.4 |
| probe | 78.6 |
| real_test | 84.8 |
| tcp | 80.7 |
| write_verified | 0.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 234 | 216 | 18 | 92.3% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 94 | 91 | 3 | 96.8% |
| vless | 230 | 185 | 45 | 80.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 38 |
| 204:ProxyError | 11 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| cn-block:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| speed:ClientOSError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6331 |
| ConnectionRefusedError | 970 |
| OSError | 239 |
| gaierror | 207 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.985 | prefer | 25 | 1.0 | 548 |
| Surfboard-tg-mixed | 0.968 | prefer | 275 | 0.891 | 8691 |
| mheidari-all | 0.967 | prefer | 113 | 0.894 | 14735 |
| Au1rxx-base64 | 0.928 | prefer | 174 | 0.862 | 1751 |
| Surfboard-tg-vless | 0.391 | observe | 2 | 1.0 | 6010 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 170 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4964 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2915 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 454 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 449 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 332 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 310 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 309 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 301 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 279 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 274 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.862 | 150 | 24 | 174 |
| Surfboard-tg-mixed | 0.891 | 245 | 30 | 275 |
| mheidari-all | 0.894 | 101 | 12 | 113 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |
| Surfboard-tg-vless | 1.0 | 2 | 0 | 2 |
| ninja-vless | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 25 | 0 | 25 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14735 | yes | 3.13 | 0 |
| SoliSpirit-all | 11743 | yes | 2.36 | 0 |
| Surfboard-tg-mixed | 8691 | yes | 3.38 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.92 | 0 |
| barry-far-vless | 6209 | yes | 0.38 | 0 |
| Surfboard-tg-vless | 6010 | yes | 2.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4964 | yes | 0.79 | 0 |
| mahdibland-V2RayAggregator | 4545 | yes | 2.06 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.61 | 0 |
| DeltaKronecker-all | 2915 | yes | 3.78 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 38 |
| 204 | 19 |
| cn-block | 6 |
| speed | 2 |
| geo | 1 |
