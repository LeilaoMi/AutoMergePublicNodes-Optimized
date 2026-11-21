# AutoNodes 每日报告

生成时间：2026-11-21 19:33:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 83259 |
| 去重后节点数 | 27850 |
| TCP 可达数 | 3000 |
| 真测通过数 | 274 |
| verified 输出数 | 36 |
| global 输出数 | 279 |
| all 输出数 | 27850 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 23.5 |
| fetch | 6.7 |
| generate | 15.0 |
| geo | 1.5 |
| probe | 95.2 |
| real_test | 85.5 |
| tcp | 78.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 19 | 17 | 2 | 89.5% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 246 | 159 | 87 | 64.6% |
| socks | 11 | 10 | 1 | 90.9% |
| trojan | 51 | 12 | 39 | 23.5% |
| vless | 124 | 73 | 51 | 58.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 107 |
| 204:ProxyError | 27 |
| cn-block:ClientOSError | 10 |
| cn-block:TimeoutError | 8 |
| cn-block:ProxyError | 6 |
| 204:TimeoutError | 6 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 5 |
| speed:ProxyError | 3 |
| speed:TimeoutError | 2 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6179 |
| ConnectionRefusedError | 1015 |
| gaierror | 329 |
| OSError | 240 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.88 | prefer | 20 | 0.9 | 403 |
| mheidari-all | 0.877 | prefer | 77 | 0.805 | 14536 |
| Surfboard-tg-mixed | 0.707 | prefer | 226 | 0.628 | 8779 |
| Au1rxx-base64 | 0.505 | observe | 136 | 0.434 | 1751 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| ermaozi-get_subscribe | 0.267 | observe | 1 | 1.0 | 303 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 141 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5030 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2989 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 176 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 464 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 459 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 342 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 320 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 319 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 311 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 289 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 284 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.434 | 59 | 77 | 136 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.628 | 142 | 84 | 226 |
| mheidari-all | 0.805 | 62 | 15 | 77 |
| ermaozi | 0.9 | 18 | 2 | 20 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14536 | yes | 5.18 | 0 |
| SoliSpirit-all | 12097 | yes | 2.62 | 0 |
| Surfboard-tg-mixed | 8779 | yes | 4.25 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.9 | 0 |
| barry-far-vless | 5966 | yes | 1.48 | 0 |
| Surfboard-tg-vless | 5784 | yes | 3.36 | 0 |
| 10ium-ScrapeCategorize-Vless | 5030 | yes | 1.71 | 0 |
| mahdibland-V2RayAggregator | 4482 | yes | 2.95 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.85 | 0 |
| DeltaKronecker-all | 2989 | yes | 5.82 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 107 |
| 204 | 38 |
| cn-block | 24 |
| speed | 6 |
| geo | 5 |
