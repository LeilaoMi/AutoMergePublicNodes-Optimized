# AutoNodes 每日报告

生成时间：2026-11-10 04:04:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82172 |
| 去重后节点数 | 26780 |
| TCP 可达数 | 3000 |
| 真测通过数 | 561 |
| verified 输出数 | 134 |
| global 输出数 | 300 |
| all 输出数 | 26780 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 17.5 |
| fetch | 5.9 |
| generate | 11.5 |
| geo | 1.6 |
| probe | 86.7 |
| real_test | 85.7 |
| tcp | 82.6 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 87 | 86 | 1 | 98.9% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 223 | 212 | 11 | 95.1% |
| trojan | 128 | 121 | 7 | 94.5% |
| vless | 230 | 130 | 100 | 56.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 66 |
| speed:ClientOSError | 15 |
| geo:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 4 |
| 204:TimeoutError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6490 |
| ConnectionRefusedError | 981 |
| OSError | 237 |
| gaierror | 142 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 88 | 0.989 | 602 |
| Surfboard-tg-mixed | 0.941 | prefer | 206 | 0.864 | 8228 |
| Au1rxx-base64 | 0.906 | prefer | 236 | 0.839 | 1751 |
| mheidari-all | 0.726 | prefer | 145 | 0.648 | 14061 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 2754 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 438 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 433 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 316 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 294 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 285 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 263 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 258 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 182 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 169 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.648 | 94 | 51 | 145 |
| Au1rxx-base64 | 0.839 | 198 | 38 | 236 |
| Surfboard-tg-mixed | 0.864 | 178 | 28 | 206 |
| ermaozi | 0.989 | 87 | 1 | 88 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 4.67 | 0 |
| SoliSpirit-all | 11245 | yes | 2.71 | 0 |
| Surfboard-tg-mixed | 8228 | yes | 4.03 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.35 | 0 |
| barry-far-vless | 6344 | yes | 0.69 | 0 |
| Surfboard-tg-vless | 6133 | yes | 2.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 1.78 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 2.59 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.28 | 0 |
| DeltaKronecker-all | 2754 | yes | 3.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 66 |
| speed | 22 |
| 204 | 13 |
| geo | 11 |
| cn-block | 7 |
