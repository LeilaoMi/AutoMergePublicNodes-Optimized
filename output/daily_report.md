# AutoNodes 每日报告

生成时间：2026-11-10 01:46:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81932 |
| 去重后节点数 | 26820 |
| TCP 可达数 | 3000 |
| 真测通过数 | 600 |
| verified 输出数 | 145 |
| global 输出数 | 300 |
| all 输出数 | 26820 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.6 |
| fetch | 6.8 |
| generate | 14.7 |
| geo | 1.5 |
| probe | 90.8 |
| real_test | 87.1 |
| tcp | 78.2 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 85 | 85 | 0 | 100.0% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 228 | 214 | 14 | 93.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 129 | 123 | 6 | 95.3% |
| vless | 280 | 165 | 115 | 58.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 90 |
| speed:ClientOSError | 14 |
| geo:ClientOSError | 9 |
| 204:ProxyError | 7 |
| cn-block:TimeoutError | 7 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| 204:TimeoutError | 1 |
| speed:ProxyError | 1 |
| cn-block:status | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6232 |
| ConnectionRefusedError | 1001 |
| OSError | 241 |
| gaierror | 206 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 87 | 1.0 | 602 |
| Surfboard-tg-mixed | 0.936 | prefer | 214 | 0.86 | 8250 |
| Au1rxx-base64 | 0.897 | prefer | 258 | 0.829 | 1751 |
| mheidari-all | 0.743 | prefer | 170 | 0.665 | 14061 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 2754 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11226 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6133 |
| barry-far-vless | 0.255 | observe | 0 | None | 6103 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 436 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 431 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 314 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 292 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 291 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 283 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 261 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 256 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 180 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 167 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.665 | 113 | 57 | 170 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.829 | 214 | 44 | 258 |
| Surfboard-tg-mixed | 0.86 | 184 | 30 | 214 |
| ermaozi | 1.0 | 87 | 0 | 87 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 3.88 | 0 |
| SoliSpirit-all | 11226 | yes | 3.19 | 0 |
| Surfboard-tg-mixed | 8250 | yes | 5.34 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 4.29 | 0 |
| Surfboard-tg-vless | 6133 | yes | 4.11 | 0 |
| barry-far-vless | 6103 | yes | 2.53 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 2.81 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 1.96 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.32 | 0 |
| DeltaKronecker-all | 2754 | yes | 6.13 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 90 |
| speed | 15 |
| cn-block | 11 |
| 204 | 10 |
| geo | 10 |
