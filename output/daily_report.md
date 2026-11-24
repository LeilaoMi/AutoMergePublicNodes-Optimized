# AutoNodes 每日报告

生成时间：2026-11-24 00:07:53

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 80217 |
| 去重后节点数 | 27776 |
| TCP 可达数 | 3000 |
| 真测通过数 | 457 |
| verified 输出数 | 82 |
| global 输出数 | 300 |
| all 输出数 | 27776 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.7 |
| fetch | 6.9 |
| generate | 14.6 |
| geo | 1.5 |
| probe | 96.6 |
| real_test | 72.3 |
| tcp | 83.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 26 | 26 | 0 | 100.0% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 237 | 228 | 9 | 96.2% |
| socks | 8 | 7 | 1 | 87.5% |
| trojan | 76 | 70 | 6 | 92.1% |
| vless | 273 | 121 | 152 | 44.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 94 |
| speed:ClientOSError | 24 |
| geo:ClientOSError | 14 |
| 204:ProxyError | 11 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| speed:TimeoutError | 1 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6685 |
| ConnectionRefusedError | 1074 |
| gaierror | 303 |
| OSError | 244 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.982 | prefer | 27 | 1.0 | 420 |
| Au1rxx-base64 | 0.896 | prefer | 165 | 0.83 | 1751 |
| Surfboard-tg-mixed | 0.86 | prefer | 275 | 0.782 | 8626 |
| mheidari-all | 0.606 | observe | 152 | 0.526 | 15543 |
| ermaozi-get_subscribe | 0.324 | observe | 2 | 1.0 | 330 |
| SoliSpirit-all | 0.287 | observe | 2 | 0.5 | 11809 |
| xiaoji235-airport-v2ray-all | 0.255 | observe | 9 | 0.222 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5064 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5667 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 468 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 463 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 346 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 324 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 323 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 315 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 288 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.222 | 2 | 7 | 9 |
| SoliSpirit-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.526 | 80 | 72 | 152 |
| Surfboard-tg-mixed | 0.782 | 215 | 60 | 275 |
| Au1rxx-base64 | 0.83 | 137 | 28 | 165 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 27 | 0 | 27 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15543 | yes | 5.99 | 0 |
| SoliSpirit-all | 11809 | yes | 4.92 | 0 |
| Surfboard-tg-mixed | 8626 | yes | 4.26 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.91 | 0 |
| barry-far-vless | 5847 | yes | 3.35 | 0 |
| Surfboard-tg-vless | 5667 | yes | 3.48 | 0 |
| 10ium-ScrapeCategorize-Vless | 5064 | yes | 3.24 | 0 |
| mahdibland-V2RayAggregator | 4514 | yes | 0.71 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.65 | 0 |
| ninja-vless | 1791 | yes | 3.17 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 94 |
| speed | 26 |
| 204 | 21 |
| geo | 19 |
| cn-block | 9 |
