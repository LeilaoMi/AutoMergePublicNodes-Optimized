# AutoNodes 每日报告

生成时间：2026-11-09 06:56:30

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81041 |
| 去重后节点数 | 26687 |
| TCP 可达数 | 3000 |
| 真测通过数 | 440 |
| verified 输出数 | 44 |
| global 输出数 | 300 |
| all 输出数 | 26687 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.8 |
| fetch | 6.9 |
| generate | 14.6 |
| geo | 1.5 |
| probe | 98.5 |
| real_test | 70.2 |
| tcp | 78.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 21 | 20 | 1 | 95.2% |
| hysteria2 | 10 | 10 | 0 | 100.0% |
| shadowsocks | 221 | 207 | 14 | 93.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 122 | 99 | 23 | 81.1% |
| vless | 168 | 102 | 66 | 60.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 60 |
| 204:ProxyError | 13 |
| cn-block:ProxyError | 9 |
| geo:ClientOSError | 8 |
| speed:ClientOSError | 5 |
| cn-block:TimeoutError | 3 |
| geo:ProxyError | 2 |
| 204:TimeoutError | 2 |
| speed:ProxyError | 1 |
| 204:ClientOSError | 1 |
| cn-block:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6137 |
| ConnectionRefusedError | 982 |
| OSError | 237 |
| gaierror | 228 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.934 | prefer | 21 | 0.952 | 519 |
| Surfboard-tg-mixed | 0.897 | prefer | 124 | 0.823 | 8133 |
| Au1rxx-base64 | 0.888 | prefer | 240 | 0.821 | 1751 |
| mheidari-all | 0.827 | prefer | 156 | 0.75 | 13820 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 173 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5035 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3024 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 432 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 427 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 310 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 288 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 287 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 279 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 257 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 252 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 176 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 163 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.75 | 117 | 39 | 156 |
| Au1rxx-base64 | 0.821 | 197 | 43 | 240 |
| Surfboard-tg-mixed | 0.823 | 102 | 22 | 124 |
| ermaozi | 0.952 | 20 | 1 | 21 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13820 | yes | 4.68 | 0 |
| SoliSpirit-all | 10927 | yes | 3.1 | 0 |
| Surfboard-tg-mixed | 8133 | yes | 4.06 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.63 | 0 |
| barry-far-vless | 6048 | yes | 0.51 | 0 |
| Surfboard-tg-vless | 5838 | yes | 3.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5035 | yes | 1.89 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 3.12 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.12 | 0 |
| DeltaKronecker-all | 3024 | yes | 5.7 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 60 |
| 204 | 16 |
| cn-block | 13 |
| geo | 11 |
| speed | 6 |
