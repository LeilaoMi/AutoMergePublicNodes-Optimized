# AutoNodes 每日报告

生成时间：2026-11-07 22:04:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81598 |
| 去重后节点数 | 26916 |
| TCP 可达数 | 3000 |
| 真测通过数 | 338 |
| verified 输出数 | 41 |
| global 输出数 | 300 |
| all 输出数 | 26916 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.8 |
| fetch | 5.4 |
| generate | 11.4 |
| geo | 1.4 |
| probe | 85.4 |
| real_test | 57.3 |
| tcp | 78.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 19 | 19 | 0 | 100.0% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 110 | 103 | 7 | 93.6% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 110 | 91 | 19 | 82.7% |
| vless | 177 | 113 | 64 | 63.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 54 |
| 204:ProxyError | 13 |
| 204:TimeoutError | 11 |
| speed:TimeoutError | 4 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| speed:ClientOSError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6256 |
| ConnectionRefusedError | 1007 |
| OSError | 236 |
| gaierror | 203 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.942 | prefer | 19 | 1.0 | 515 |
| mheidari-all | 0.845 | prefer | 130 | 0.769 | 14235 |
| Au1rxx-base64 | 0.844 | prefer | 250 | 0.776 | 1751 |
| Surfboard-tg-mixed | 0.799 | prefer | 30 | 0.733 | 8421 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2734 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4866 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11058 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 428 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 423 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 306 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 284 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 283 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 275 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 253 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 248 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 159 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.733 | 22 | 8 | 30 |
| mheidari-all | 0.769 | 100 | 30 | 130 |
| Au1rxx-base64 | 0.776 | 194 | 56 | 250 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| ninja-vless | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14235 | yes | 4.45 | 0 |
| SoliSpirit-all | 11058 | yes | 2.54 | 0 |
| Surfboard-tg-mixed | 8421 | yes | 2.97 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.69 | 0 |
| barry-far-vless | 6134 | yes | 0.46 | 0 |
| Surfboard-tg-vless | 5923 | yes | 3.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 4866 | yes | 0.88 | 0 |
| mahdibland-V2RayAggregator | 4529 | yes | 2.37 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.76 | 0 |
| DeltaKronecker-all | 2734 | yes | 4.58 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 54 |
| 204 | 24 |
| cn-block | 7 |
| speed | 7 |
| geo | 2 |
