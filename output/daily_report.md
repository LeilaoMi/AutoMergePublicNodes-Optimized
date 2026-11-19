# AutoNodes 每日报告

生成时间：2026-11-19 07:43:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82154 |
| 去重后节点数 | 27481 |
| TCP 可达数 | 3000 |
| 真测通过数 | 417 |
| verified 输出数 | 65 |
| global 输出数 | 300 |
| all 输出数 | 27481 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.4 |
| fetch | 5.7 |
| generate | 12.2 |
| geo | 1.5 |
| probe | 89.2 |
| real_test | 77.0 |
| tcp | 80.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 10 | 9 | 1 | 90.0% |
| shadowsocks | 241 | 215 | 26 | 89.2% |
| socks | 3 | 3 | 0 | 100.0% |
| trojan | 56 | 35 | 21 | 62.5% |
| vless | 205 | 134 | 71 | 65.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 67 |
| 204:ProxyError | 20 |
| 204:TimeoutError | 15 |
| cn-block:ClientOSError | 9 |
| cn-block:TimeoutError | 6 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6104 |
| ConnectionRefusedError | 1009 |
| gaierror | 310 |
| OSError | 239 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.985 | prefer | 27 | 1.0 | 494 |
| Surfboard-tg-mixed | 0.937 | prefer | 131 | 0.863 | 8472 |
| mheidari-all | 0.849 | prefer | 193 | 0.772 | 14200 |
| Au1rxx-base64 | 0.765 | prefer | 188 | 0.697 | 1751 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4919 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2925 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11797 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5689 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| ermaozi-get_subscribe | 0.142 | observe | 1 | 0.0 | 0 | 358 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 459 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 454 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 337 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 315 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 314 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 306 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 284 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 279 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.697 | 131 | 57 | 188 |
| mheidari-all | 0.772 | 149 | 44 | 193 |
| Surfboard-tg-mixed | 0.863 | 113 | 18 | 131 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 27 | 0 | 27 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14200 | yes | 4.64 | 0 |
| SoliSpirit-all | 11797 | yes | 2.68 | 0 |
| Surfboard-tg-mixed | 8472 | yes | 3.51 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.79 | 0 |
| barry-far-vless | 5975 | yes | 0.9 | 0 |
| Surfboard-tg-vless | 5689 | yes | 2.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 4919 | yes | 0.68 | 0 |
| mahdibland-V2RayAggregator | 4458 | yes | 1.36 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.3 | 0 |
| DeltaKronecker-all | 2925 | yes | 5.01 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 67 |
| 204 | 35 |
| cn-block | 16 |
| geo | 1 |
| speed | 1 |
