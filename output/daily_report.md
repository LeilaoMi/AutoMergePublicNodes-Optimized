# AutoNodes 每日报告

生成时间：2026-11-07 06:16:57

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 81836 |
| 去重后节点数 | 26377 |
| TCP 可达数 | 3000 |
| 真测通过数 | 385 |
| verified 输出数 | 68 |
| global 输出数 | 300 |
| all 输出数 | 26377 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.7 |
| fetch | 4.9 |
| generate | 10.5 |
| geo | 1.5 |
| probe | 78.0 |
| real_test | 58.1 |
| tcp | 77.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 58 | 58 | 0 | 100.0% |
| hysteria2 | 14 | 11 | 3 | 78.6% |
| shadowsocks | 154 | 150 | 4 | 97.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 63 | 59 | 4 | 93.7% |
| vless | 174 | 106 | 68 | 60.9% |
| vmess | 1 | 0 | 1 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 49 |
| 204:ProxyError | 14 |
| 204:TimeoutError | 8 |
| geo:ClientOSError | 4 |
| speed:ClientOSError | 3 |
| cn-block:ClientOSError | 1 |
| 204:ClientOSError | 1 |
| cn-block:TimeoutError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6071 |
| ConnectionRefusedError | 1025 |
| OSError | 233 |
| gaierror | 201 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 59 | 1.0 | 562 |
| Au1rxx-base64 | 0.933 | prefer | 224 | 0.866 | 1751 |
| mheidari-all | 0.806 | prefer | 166 | 0.729 | 13634 |
| Surfboard-tg-mixed | 0.609 | observe | 12 | 0.75 | 8637 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 178 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4934 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2768 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11015 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6148 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 426 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 421 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 304 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 282 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 281 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 273 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 251 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 246 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 170 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 157 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.25 | 1 | 3 | 4 |
| mheidari-all | 0.729 | 121 | 45 | 166 |
| Surfboard-tg-mixed | 0.75 | 9 | 3 | 12 |
| Au1rxx-base64 | 0.866 | 194 | 30 | 224 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 59 | 0 | 59 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13634 | yes | 3.29 | 0 |
| SoliSpirit-all | 11015 | yes | 2.89 | 0 |
| Surfboard-tg-mixed | 8637 | yes | 2.88 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.9 | 0 |
| barry-far-vless | 6359 | yes | 0.55 | 0 |
| Surfboard-tg-vless | 6148 | yes | 2.48 | 0 |
| 10ium-ScrapeCategorize-Vless | 4934 | yes | 1.36 | 0 |
| mahdibland-V2RayAggregator | 4540 | yes | 2.26 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.85 | 0 |
| DeltaKronecker-all | 2768 | yes | 4.39 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vmess | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 49 |
| 204 | 23 |
| speed | 4 |
| geo | 4 |
| cn-block | 2 |
