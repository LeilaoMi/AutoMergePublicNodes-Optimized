# AutoNodes 每日报告

生成时间：2026-11-09 22:36:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81601 |
| 去重后节点数 | 26711 |
| TCP 可达数 | 3000 |
| 真测通过数 | 472 |
| verified 输出数 | 30 |
| global 输出数 | 300 |
| all 输出数 | 26711 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.2 |
| fetch | 6.8 |
| generate | 14.0 |
| geo | 1.5 |
| probe | 97.7 |
| real_test | 71.4 |
| tcp | 76.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 19 | 19 | 0 | 100.0% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 222 | 204 | 18 | 91.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 122 | 116 | 6 | 95.1% |
| vless | 169 | 122 | 47 | 72.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 48 |
| 204:ProxyError | 7 |
| speed:ClientOSError | 5 |
| 204:TimeoutError | 3 |
| cn-block:TimeoutError | 3 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6143 |
| ConnectionRefusedError | 1003 |
| OSError | 240 |
| gaierror | 234 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.982 | prefer | 100 | 0.91 | 14061 |
| Au1rxx-base64 | 0.951 | prefer | 225 | 0.884 | 1751 |
| ermaozi | 0.942 | prefer | 19 | 1.0 | 518 |
| Surfboard-tg-mixed | 0.892 | prefer | 200 | 0.815 | 8250 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11213 |
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
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.815 | 163 | 37 | 200 |
| Au1rxx-base64 | 0.884 | 199 | 26 | 225 |
| mheidari-all | 0.91 | 91 | 9 | 100 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 4.11 | 0 |
| SoliSpirit-all | 11213 | yes | 3.04 | 0 |
| Surfboard-tg-mixed | 8250 | yes | 4.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.85 | 0 |
| Surfboard-tg-vless | 6133 | yes | 3.42 | 0 |
| barry-far-vless | 6103 | yes | 2.42 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 2.65 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 2.32 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.3 | 0 |
| DeltaKronecker-all | 2754 | yes | 6.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 48 |
| 204 | 12 |
| cn-block | 7 |
| speed | 5 |
| geo | 1 |
