# AutoNodes 每日报告

生成时间：2026-10-28 22:47:57

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 3/85 |
| 原始节点数 | 99282 |
| 去重后节点数 | 27866 |
| TCP 可达数 | 3000 |
| 真测通过数 | 412 |
| verified 输出数 | 76 |
| global 输出数 | 300 |
| all 输出数 | 27866 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.6 |
| fetch | 7.7 |
| generate | 15.4 |
| geo | 1.7 |
| probe | 101.4 |
| real_test | 74.7 |
| tcp | 85.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 28 | 1 | 96.6% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 130 | 122 | 8 | 93.8% |
| trojan | 52 | 49 | 3 | 94.2% |
| vless | 296 | 201 | 95 | 67.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 68 |
| geo:ClientOSError | 11 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 6 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:TimeoutError | 1 |
| speed:ClientOSError | 1 |
| speed:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6743 |
| ConnectionRefusedError | 1099 |
| gaierror | 328 |
| OSError | 241 |
| SSRFBlocked | 5 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.956 | prefer | 29 | 0.966 | 513 |
| Au1rxx-base64 | 0.951 | prefer | 310 | 0.884 | 1746 |
| Surfboard-tg-mixed | 0.853 | prefer | 16 | 0.938 | 7686 |
| mheidari-all | 0.65 | observe | 163 | 0.571 | 33849 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2801 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5004 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10359 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5749 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ShadowsocksM | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 511 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 402 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 397 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 280 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 258 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 257 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 249 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 146 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.571 | 93 | 70 | 163 |
| Au1rxx-base64 | 0.884 | 274 | 36 | 310 |
| Surfboard-tg-mixed | 0.938 | 15 | 1 | 16 |
| ermaozi | 0.966 | 28 | 1 | 29 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 33849 | yes | 6.62 | 0 |
| SoliSpirit-all | 10359 | yes | 4.14 | 0 |
| Surfboard-tg-mixed | 7686 | yes | 3.94 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.48 | 0 |
| barry-far-vless | 5963 | yes | 1.47 | 0 |
| Surfboard-tg-vless | 5749 | yes | 3.62 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 1.72 | 0 |
| mahdibland-V2RayAggregator | 4323 | yes | 2.46 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.24 | 0 |
| DeltaKronecker-all | 2801 | yes | 6.34 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 68 |
| 204 | 16 |
| geo | 11 |
| cn-block | 10 |
| speed | 3 |
