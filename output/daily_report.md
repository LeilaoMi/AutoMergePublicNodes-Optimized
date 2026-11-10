# AutoNodes 每日报告

生成时间：2026-11-10 07:35:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81817 |
| 去重后节点数 | 26754 |
| TCP 可达数 | 3000 |
| 真测通过数 | 488 |
| verified 输出数 | 108 |
| global 输出数 | 300 |
| all 输出数 | 26754 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 39.9 |
| fetch | 7.0 |
| generate | 14.0 |
| geo | 1.5 |
| probe | 98.0 |
| real_test | 86.7 |
| tcp | 79.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 85 | 84 | 1 | 98.8% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 215 | 198 | 17 | 92.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 120 | 103 | 17 | 85.8% |
| vless | 144 | 90 | 54 | 62.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 47 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 7 |
| speed:ClientOSError | 7 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| geo:ProxyError | 2 |
| geo:ClientOSError | 2 |
| speed:ProxyError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6294 |
| ConnectionRefusedError | 1008 |
| OSError | 238 |
| gaierror | 158 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.99 | prefer | 86 | 0.977 | 602 |
| Au1rxx-base64 | 0.897 | prefer | 223 | 0.83 | 1751 |
| Surfboard-tg-mixed | 0.895 | prefer | 176 | 0.818 | 8228 |
| mheidari-all | 0.869 | prefer | 88 | 0.795 | 13900 |
| DeltaKronecker-all | 0.391 | observe | 2 | 1.0 | 2754 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11021 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 439 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 434 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 317 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 295 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 294 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 286 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 264 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 259 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 170 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| peasoft-NoMoreWalls | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.795 | 70 | 18 | 88 |
| Surfboard-tg-mixed | 0.818 | 144 | 32 | 176 |
| Au1rxx-base64 | 0.83 | 185 | 38 | 223 |
| ermaozi | 0.977 | 84 | 2 | 86 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| DeltaKronecker-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13900 | yes | 4.99 | 0 |
| SoliSpirit-all | 11021 | yes | 3.14 | 0 |
| Surfboard-tg-mixed | 8228 | yes | 4.13 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.68 | 0 |
| barry-far-vless | 6344 | yes | 0.78 | 0 |
| Surfboard-tg-vless | 6133 | yes | 3.55 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 1.32 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 3.13 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.43 | 0 |
| DeltaKronecker-all | 2754 | yes | 5.76 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 47 |
| 204 | 21 |
| speed | 12 |
| cn-block | 7 |
| geo | 4 |
