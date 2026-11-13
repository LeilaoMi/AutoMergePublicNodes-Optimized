# AutoNodes 每日报告

生成时间：2026-11-13 07:01:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 20/0 |
| 清理建议：优先/观察 | 4/83 |
| 原始节点数 | 82620 |
| 去重后节点数 | 26689 |
| TCP 可达数 | 3000 |
| 真测通过数 | 487 |
| verified 输出数 | 92 |
| global 输出数 | 300 |
| all 输出数 | 26689 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 22.7 |
| fetch | 4.9 |
| generate | 10.4 |
| geo | 1.4 |
| probe | 77.9 |
| real_test | 83.5 |
| tcp | 74.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 72 | 71 | 1 | 98.6% |
| hysteria2 | 12 | 10 | 2 | 83.3% |
| shadowsocks | 218 | 196 | 22 | 89.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 107 | 93 | 14 | 86.9% |
| vless | 210 | 117 | 93 | 55.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 61 |
| speed:ClientOSError | 34 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 8 |
| cn-block:TimeoutError | 6 |
| geo:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| speed:TimeoutError | 1 |
| 204:ClientOSError | 1 |
| geo:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5974 |
| ConnectionRefusedError | 957 |
| gaierror | 325 |
| OSError | 241 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.997 | prefer | 72 | 0.986 | 594 |
| Au1rxx-base64 | 0.868 | prefer | 211 | 0.801 | 1751 |
| mheidari-all | 0.822 | prefer | 64 | 0.75 | 13793 |
| Surfboard-tg-mixed | 0.809 | prefer | 271 | 0.731 | 8675 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4998 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2737 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11327 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6119 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| ermaozi-get_subscribe | 0.146 | observe | 1 | 0.0 | 0 | 456 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 445 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 440 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 323 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 301 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 300 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 292 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 270 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 265 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 189 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 176 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.731 | 198 | 73 | 271 |
| mheidari-all | 0.75 | 48 | 16 | 64 |
| Au1rxx-base64 | 0.801 | 169 | 42 | 211 |
| ermaozi | 0.986 | 71 | 1 | 72 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13793 | yes | 4.0 | 0 |
| SoliSpirit-all | 11327 | yes | 2.23 | 0 |
| Surfboard-tg-mixed | 8675 | yes | 3.04 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.46 | 0 |
| barry-far-vless | 6543 | yes | 0.56 | 0 |
| Surfboard-tg-vless | 6119 | yes | 2.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 4998 | yes | 0.74 | 0 |
| mahdibland-V2RayAggregator | 4582 | yes | 2.18 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.59 | 0 |
| DeltaKronecker-all | 2737 | yes | 4.24 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 61 |
| speed | 36 |
| 204 | 19 |
| cn-block | 11 |
| geo | 7 |
