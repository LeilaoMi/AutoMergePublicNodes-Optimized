# AutoNodes 每日报告

生成时间：2026-11-08 06:23:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81513 |
| 去重后节点数 | 27137 |
| TCP 可达数 | 3000 |
| 真测通过数 | 519 |
| verified 输出数 | 59 |
| global 输出数 | 300 |
| all 输出数 | 27137 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.8 |
| fetch | 3.8 |
| generate | 9.2 |
| geo | 1.4 |
| probe | 67.8 |
| real_test | 88.7 |
| tcp | 81.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 94 | 93 | 1 | 98.9% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 212 | 198 | 14 | 93.4% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 134 | 119 | 15 | 88.8% |
| vless | 171 | 94 | 77 | 55.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 70 |
| 204:ProxyError | 15 |
| 204:TimeoutError | 10 |
| geo:ClientOSError | 6 |
| cn-block:TimeoutError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:TimeoutError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6356 |
| ConnectionRefusedError | 1005 |
| OSError | 239 |
| gaierror | 150 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 95 | 0.989 | 613 |
| Surfboard-tg-mixed | 0.936 | prefer | 109 | 0.862 | 8112 |
| Au1rxx-base64 | 0.903 | prefer | 237 | 0.835 | 1751 |
| mheidari-all | 0.784 | prefer | 187 | 0.706 | 14505 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2734 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4866 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10963 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5849 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 429 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 424 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 307 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 285 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 284 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 276 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 254 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 249 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 173 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 160 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.706 | 132 | 55 | 187 |
| Au1rxx-base64 | 0.835 | 198 | 39 | 237 |
| Surfboard-tg-mixed | 0.862 | 94 | 15 | 109 |
| ermaozi | 0.989 | 94 | 1 | 95 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14505 | yes | 3.64 | 0 |
| SoliSpirit-all | 10963 | yes | 2.41 | 0 |
| Surfboard-tg-mixed | 8112 | yes | 2.43 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.24 | 0 |
| barry-far-vless | 6061 | yes | 1.2 | 0 |
| Surfboard-tg-vless | 5849 | yes | 2.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 4866 | yes | 1.32 | 0 |
| mahdibland-V2RayAggregator | 4529 | yes | 0.92 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.41 | 0 |
| DeltaKronecker-all | 2734 | yes | 3.55 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 70 |
| 204 | 27 |
| geo | 8 |
| cn-block | 5 |
