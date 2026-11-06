# AutoNodes 每日报告

生成时间：2026-11-06 07:04:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 82780 |
| 去重后节点数 | 26710 |
| TCP 可达数 | 3000 |
| 真测通过数 | 440 |
| verified 输出数 | 123 |
| global 输出数 | 300 |
| all 输出数 | 26710 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.5 |
| fetch | 7.0 |
| generate | 14.7 |
| geo | 1.5 |
| probe | 91.0 |
| real_test | 68.9 |
| tcp | 79.3 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 102 | 99 | 3 | 97.1% |
| hysteria2 | 13 | 11 | 2 | 84.6% |
| shadowsocks | 149 | 141 | 8 | 94.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 76 | 68 | 8 | 89.5% |
| vless | 193 | 120 | 73 | 62.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 45 |
| 204:ProxyError | 16 |
| 204:TimeoutError | 10 |
| cn-block:TimeoutError | 7 |
| cn-block:ProxyError | 5 |
| geo:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| speed:TimeoutError | 2 |
| geo:TimeoutError | 1 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6286 |
| ConnectionRefusedError | 1002 |
| OSError | 234 |
| gaierror | 188 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.987 | prefer | 102 | 0.971 | 639 |
| mheidari-all | 0.869 | prefer | 197 | 0.792 | 14233 |
| Au1rxx-base64 | 0.858 | prefer | 229 | 0.79 | 1751 |
| Surfboard-tg-mixed | 0.4 | observe | 4 | 0.75 | 8762 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5039 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2653 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10891 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6268 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 424 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 419 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 302 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 280 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 279 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 249 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 168 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 155 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| Surfboard-tg-mixed | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.79 | 181 | 48 | 229 |
| mheidari-all | 0.792 | 156 | 41 | 197 |
| ermaozi | 0.971 | 99 | 3 | 102 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14233 | yes | 6.21 | 0 |
| SoliSpirit-all | 10891 | yes | 2.65 | 0 |
| Surfboard-tg-mixed | 8762 | yes | 4.92 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.62 | 0 |
| barry-far-vless | 6478 | yes | 2.14 | 0 |
| Surfboard-tg-vless | 6268 | yes | 3.85 | 0 |
| 10ium-ScrapeCategorize-Vless | 5039 | yes | 0.59 | 0 |
| mahdibland-V2RayAggregator | 4703 | yes | 3.11 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.28 | 0 |
| DeltaKronecker-all | 2653 | yes | 6.22 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 45 |
| 204 | 27 |
| cn-block | 15 |
| geo | 6 |
| speed | 2 |
