# AutoNodes 每日报告

生成时间：2026-11-26 21:49:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/1 |
| 清理建议：优先/观察 | 4/83 |
| 原始节点数 | 78821 |
| 去重后节点数 | 27291 |
| TCP 可达数 | 3000 |
| 真测通过数 | 350 |
| verified 输出数 | 63 |
| global 输出数 | 300 |
| all 输出数 | 27291 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 44.1 |
| fetch | 6.7 |
| generate | 14.5 |
| geo | 1.5 |
| probe | 105.2 |
| real_test | 77.7 |
| tcp | 79.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 2 | 3 | 40.0% |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 7 | 6 | 1 | 85.7% |
| shadowsocks | 280 | 219 | 61 | 78.2% |
| socks | 9 | 8 | 1 | 88.9% |
| trojan | 14 | 12 | 2 | 85.7% |
| vless | 131 | 88 | 43 | 67.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 75 |
| speed:TimeoutError | 11 |
| cn-block:ClientOSError | 9 |
| cn-block:TimeoutError | 4 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| 204:ProxyError | 2 |
| 204:ClientOSError | 1 |
| speed:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6680 |
| ConnectionRefusedError | 967 |
| OSError | 246 |
| gaierror | 244 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.974 | prefer | 22 | 1.0 | 393 |
| Surfboard-tg-mixed | 0.924 | prefer | 145 | 0.848 | 8568 |
| Au1rxx-base64 | 0.822 | prefer | 127 | 0.756 | 1751 |
| mheidari-all | 0.749 | prefer | 164 | 0.671 | 14669 |
| tg-LonUp_M | 0.365 | observe | 3 | 1.0 | 168 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| tg-proxy_mtm | 0.258 | observe | 1 | 1.0 | 67 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4936 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11794 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 474 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 469 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 352 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 330 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 329 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 321 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 299 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 294 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| downweight | ermaozi-get_subscribe | 0.232 | 5 | 0.4 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.4 | 2 | 3 | 5 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.671 | 110 | 54 | 164 |
| Au1rxx-base64 | 0.756 | 96 | 31 | 127 |
| Surfboard-tg-mixed | 0.848 | 123 | 22 | 145 |
| tg-proxy_mtm | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 3 | 0 | 3 |
| ermaozi | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14669 | yes | 3.86 | 0 |
| SoliSpirit-all | 11794 | yes | 2.91 | 0 |
| Surfboard-tg-mixed | 8568 | yes | 4.1 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.39 | 0 |
| barry-far-vless | 5607 | yes | 1.5 | 0 |
| Surfboard-tg-vless | 5426 | yes | 3.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 4936 | yes | 1.72 | 0 |
| mahdibland-V2RayAggregator | 4485 | yes | 2.88 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.86 | 0 |
| ninja-vless | 1791 | yes | 3.08 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 75 |
| cn-block | 16 |
| speed | 12 |
| 204 | 7 |
| geo | 1 |
