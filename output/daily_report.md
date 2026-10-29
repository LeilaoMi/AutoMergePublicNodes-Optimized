# AutoNodes 每日报告

生成时间：2026-10-29 06:05:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 3/85 |
| 原始节点数 | 99478 |
| 去重后节点数 | 27953 |
| TCP 可达数 | 3000 |
| 真测通过数 | 542 |
| verified 输出数 | 84 |
| global 输出数 | 300 |
| all 输出数 | 27953 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.0 |
| fetch | 7.7 |
| generate | 15.0 |
| geo | 1.7 |
| probe | 96.6 |
| real_test | 89.4 |
| tcp | 86.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 71 | 70 | 1 | 98.6% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 171 | 162 | 9 | 94.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 143 | 121 | 22 | 84.6% |
| vless | 309 | 176 | 133 | 57.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 93 |
| geo:ClientOSError | 26 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 10 |
| cn-block:ClientOSError | 8 |
| geo:ProxyError | 5 |
| speed:ClientOSError | 5 |
| cn-block:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| speed:TimeoutError | 2 |
| speed:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6803 |
| ConnectionRefusedError | 1107 |
| gaierror | 301 |
| OSError | 243 |
| SSRFBlocked | 5 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.995 | prefer | 71 | 0.986 | 560 |
| Au1rxx-base64 | 0.926 | prefer | 331 | 0.861 | 1681 |
| Surfboard-tg-mixed | 0.742 | prefer | 143 | 0.664 | 7653 |
| mheidari-all | 0.633 | observe | 157 | 0.554 | 34088 |
| xiaoji235-airport-v2ray-all | 0.446 | observe | 5 | 0.8 | 6752 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5004 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2801 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10416 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 512 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 403 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 398 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 281 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 259 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 258 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 250 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 223 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 147 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.554 | 87 | 70 | 157 |
| Surfboard-tg-mixed | 0.664 | 95 | 48 | 143 |
| xiaoji235-airport-v2ray-all | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.861 | 285 | 46 | 331 |
| ermaozi | 0.986 | 70 | 1 | 71 |
| ninja-vless | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34088 | yes | 6.75 | 0 |
| SoliSpirit-all | 10416 | yes | 1.96 | 0 |
| Surfboard-tg-mixed | 7653 | yes | 4.32 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.78 | 0 |
| barry-far-vless | 5902 | yes | 1.27 | 0 |
| Surfboard-tg-vless | 5723 | yes | 3.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 0.81 | 0 |
| mahdibland-V2RayAggregator | 4323 | yes | 0.27 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.61 | 0 |
| DeltaKronecker-all | 2801 | yes | 6.75 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 93 |
| geo | 31 |
| 204 | 21 |
| cn-block | 13 |
| speed | 8 |
