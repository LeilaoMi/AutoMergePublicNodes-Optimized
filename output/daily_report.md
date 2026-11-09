# AutoNodes 每日报告

生成时间：2026-11-09 22:42:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81601 |
| 去重后节点数 | 26712 |
| TCP 可达数 | 3000 |
| 真测通过数 | 476 |
| verified 输出数 | 55 |
| global 输出数 | 300 |
| all 输出数 | 26712 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 22.8 |
| fetch | 5.2 |
| generate | 10.9 |
| geo | 1.4 |
| probe | 81.0 |
| real_test | 79.2 |
| tcp | 81.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 19 | 19 | 0 | 100.0% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 221 | 208 | 13 | 94.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 122 | 117 | 5 | 95.9% |
| vless | 182 | 121 | 61 | 66.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 36 |
| cn-block:TimeoutError | 9 |
| cn-block:ProxyError | 7 |
| 204:ProxyError | 6 |
| 204:TimeoutError | 6 |
| speed:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| speed:TimeoutError | 2 |
| geo:TimeoutError | 1 |
| cn-block:ClientOSError | 1 |
| geo:ProxyError | 1 |
| cn-block:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6505 |
| ConnectionRefusedError | 973 |
| OSError | 239 |
| gaierror | 104 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.942 | prefer | 19 | 1.0 | 518 |
| Surfboard-tg-mixed | 0.941 | prefer | 192 | 0.865 | 8250 |
| mheidari-all | 0.941 | prefer | 106 | 0.868 | 14061 |
| Au1rxx-base64 | 0.898 | prefer | 237 | 0.831 | 1751 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2754 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11213 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 433 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 428 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 311 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 289 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 288 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 280 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 258 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 253 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 164 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.831 | 197 | 40 | 237 |
| Surfboard-tg-mixed | 0.865 | 166 | 26 | 192 |
| mheidari-all | 0.868 | 92 | 14 | 106 |
| ninja-vless | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 4.06 | 0 |
| SoliSpirit-all | 11213 | yes | 3.87 | 0 |
| Surfboard-tg-mixed | 8250 | yes | 2.74 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.57 | 0 |
| Surfboard-tg-vless | 6133 | yes | 2.94 | 0 |
| barry-far-vless | 6103 | yes | 1.02 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 0.42 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 2.19 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.47 | 0 |
| DeltaKronecker-all | 2754 | yes | 4.1 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 36 |
| cn-block | 18 |
| 204 | 17 |
| speed | 8 |
| geo | 2 |
