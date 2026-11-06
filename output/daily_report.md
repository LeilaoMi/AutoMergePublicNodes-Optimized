# AutoNodes 每日报告

生成时间：2026-11-06 19:36:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/1 |
| 清理建议：优先/观察 | 3/85 |
| 原始节点数 | 82563 |
| 去重后节点数 | 26734 |
| TCP 可达数 | 3000 |
| 真测通过数 | 279 |
| verified 输出数 | 123 |
| global 输出数 | 282 |
| all 输出数 | 26734 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 22.2 |
| fetch | 4.8 |
| generate | 11.1 |
| geo | 1.4 |
| probe | 79.6 |
| real_test | 57.5 |
| tcp | 77.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 32 | 32 | 0 | 100.0% |
| hysteria2 | 15 | 11 | 4 | 73.3% |
| shadowsocks | 112 | 107 | 5 | 95.5% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 66 | 37 | 29 | 56.1% |
| vless | 128 | 92 | 36 | 71.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 31 |
| 204:ProxyError | 29 |
| cn-block:ProxyError | 5 |
| 204:TimeoutError | 4 |
| geo:ProxyError | 3 |
| 204:ClientOSError | 2 |
| cn-block:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6188 |
| ConnectionRefusedError | 1026 |
| gaierror | 235 |
| OSError | 234 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.992 | prefer | 33 | 1.0 | 513 |
| mheidari-all | 0.861 | prefer | 103 | 0.786 | 14184 |
| Au1rxx-base64 | 0.853 | prefer | 205 | 0.785 | 1751 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 2768 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 179 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4934 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10962 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6135 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 425 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 420 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 303 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 281 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 280 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 272 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 250 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 245 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 169 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 156 | 连续死亡次数 >= 2 |
| downweight | Surfboard-tg-mixed | 0.239 | 12 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.167 | 2 | 10 | 12 |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.785 | 161 | 44 | 205 |
| mheidari-all | 0.786 | 81 | 22 | 103 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 33 | 0 | 33 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14184 | yes | 2.57 | 0 |
| SoliSpirit-all | 10962 | yes | 2.91 | 0 |
| Surfboard-tg-mixed | 8758 | yes | 2.84 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.87 | 0 |
| barry-far-vless | 6479 | yes | 1.06 | 0 |
| Surfboard-tg-vless | 6135 | yes | 3.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4934 | yes | 1.63 | 0 |
| mahdibland-V2RayAggregator | 4703 | yes | 2.18 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.91 | 0 |
| DeltaKronecker-all | 2768 | yes | 4.33 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 35 |
| test_one_timeout | 31 |
| cn-block | 6 |
| geo | 4 |
| speed | 1 |
