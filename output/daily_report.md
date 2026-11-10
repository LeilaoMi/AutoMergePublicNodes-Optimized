# AutoNodes 每日报告

生成时间：2026-11-10 02:27:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82150 |
| 去重后节点数 | 26759 |
| TCP 可达数 | 3000 |
| 真测通过数 | 587 |
| verified 输出数 | 127 |
| global 输出数 | 300 |
| all 输出数 | 26759 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.0 |
| fetch | 6.8 |
| generate | 14.4 |
| geo | 1.5 |
| probe | 94.1 |
| real_test | 85.2 |
| tcp | 77.0 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 86 | 85 | 1 | 98.8% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 229 | 222 | 7 | 96.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 129 | 123 | 6 | 95.3% |
| vless | 245 | 143 | 102 | 58.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 73 |
| speed:ClientOSError | 11 |
| cn-block:TimeoutError | 8 |
| geo:ClientOSError | 8 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 4 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:TimeoutError | 1 |
| cn-block:status | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6118 |
| ConnectionRefusedError | 1005 |
| OSError | 240 |
| gaierror | 229 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 89 | 0.989 | 602 |
| Surfboard-tg-mixed | 0.927 | prefer | 220 | 0.85 | 8250 |
| Au1rxx-base64 | 0.926 | prefer | 234 | 0.859 | 1751 |
| mheidari-all | 0.774 | prefer | 158 | 0.696 | 14061 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 2754 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11203 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6133 |
| barry-far-vless | 0.255 | observe | 0 | None | 6344 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 437 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 432 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 315 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 292 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 284 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 262 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 257 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 181 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 168 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.696 | 110 | 48 | 158 |
| Surfboard-tg-mixed | 0.85 | 187 | 33 | 220 |
| Au1rxx-base64 | 0.859 | 201 | 33 | 234 |
| ermaozi | 0.989 | 88 | 1 | 89 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 5.65 | 0 |
| SoliSpirit-all | 11203 | yes | 4.57 | 0 |
| Surfboard-tg-mixed | 8250 | yes | 3.85 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.64 | 0 |
| barry-far-vless | 6344 | yes | 2.84 | 0 |
| Surfboard-tg-vless | 6133 | yes | 3.55 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 2.52 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 3.15 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.62 | 0 |
| DeltaKronecker-all | 2754 | yes | 5.7 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 73 |
| cn-block | 12 |
| 204 | 11 |
| speed | 11 |
| geo | 10 |
