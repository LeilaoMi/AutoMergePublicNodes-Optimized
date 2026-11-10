# AutoNodes 每日报告

生成时间：2026-11-10 19:56:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 82772 |
| 去重后节点数 | 27016 |
| TCP 可达数 | 3000 |
| 真测通过数 | 406 |
| verified 输出数 | 93 |
| global 输出数 | 300 |
| all 输出数 | 27016 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.9 |
| fetch | 5.9 |
| generate | 12.5 |
| geo | 1.5 |
| probe | 90.5 |
| real_test | 76.9 |
| tcp | 76.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 70 | 67 | 3 | 95.7% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 200 | 178 | 22 | 89.0% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 87 | 41 | 46 | 47.1% |
| vless | 189 | 107 | 82 | 56.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 62 |
| 204:ProxyError | 32 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 11 |
| cn-block:ProxyError | 9 |
| 204:ClientOSError | 6 |
| geo:ProxyError | 6 |
| cn-block:TimeoutError | 5 |
| speed:ProxyError | 4 |
| geo:ClientOSError | 3 |
| speed:TimeoutError | 2 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6006 |
| ConnectionRefusedError | 1016 |
| gaierror | 310 |
| OSError | 240 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.956 | prefer | 71 | 0.944 | 619 |
| mheidari-all | 0.858 | prefer | 97 | 0.784 | 14274 |
| Au1rxx-base64 | 0.782 | prefer | 182 | 0.714 | 1751 |
| Surfboard-tg-mixed | 0.716 | prefer | 207 | 0.638 | 8562 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 2620 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4955 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11116 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| chromego_merge | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 440 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 435 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 318 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 296 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 295 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 287 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 265 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 260 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 171 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.638 | 132 | 75 | 207 |
| Au1rxx-base64 | 0.714 | 130 | 52 | 182 |
| mheidari-all | 0.784 | 76 | 21 | 97 |
| ermaozi | 0.944 | 67 | 4 | 71 |
| ninja-vless | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14274 | yes | 5.02 | 0 |
| SoliSpirit-all | 11116 | yes | 4.49 | 0 |
| Surfboard-tg-mixed | 8562 | yes | 3.88 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.0 | 0 |
| barry-far-vless | 6491 | yes | 0.73 | 0 |
| Surfboard-tg-vless | 6459 | yes | 3.6 | 0 |
| 10ium-ScrapeCategorize-Vless | 4955 | yes | 2.06 | 0 |
| mahdibland-V2RayAggregator | 4667 | yes | 1.08 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.13 | 0 |
| DeltaKronecker-all | 2620 | yes | 5.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 62 |
| 204 | 49 |
| speed | 20 |
| cn-block | 15 |
| geo | 9 |
