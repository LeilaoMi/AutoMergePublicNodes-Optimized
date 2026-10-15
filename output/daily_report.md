# AutoNodes 每日报告

生成时间：2026-10-15 21:14:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 99675 |
| 去重后节点数 | 27750 |
| TCP 可达数 | 3000 |
| 真测通过数 | 85 |
| verified 输出数 | 85 |
| global 输出数 | 93 |
| all 输出数 | 27750 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 27.4 |
| fetch | 5.4 |
| generate | 10.9 |
| geo | 1.5 |
| probe | 102.7 |
| real_test | 68.9 |
| tcp | 83.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 67 | 65 | 2 | 97.0% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 127 | 114 | 13 | 89.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 22 | 10 | 12 | 45.5% |
| vless | 222 | 129 | 93 | 58.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 69 |
| speed:ClientOSError | 19 |
| 204:TimeoutError | 9 |
| 204:ProxyError | 9 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 3 |
| geo:ClientOSError | 2 |
| geo:TimeoutError | 1 |
| speed:ProxyError | 1 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6877 |
| ConnectionRefusedError | 1044 |
| gaierror | 257 |
| OSError | 238 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.982 | prefer | 66 | 0.97 | 659 |
| Au1rxx-base64 | 0.773 | prefer | 355 | 0.701 | 1827 |
| mheidari-all | 0.628 | observe | 29 | 0.552 | 24072 |
| Surfboard-tg-mixed | 0.391 | observe | 2 | 1.0 | 7166 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 89 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5089 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5147 |
| Epodonios-all | 0.255 | observe | 0 | None | 7793 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9888 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 456 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 347 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 342 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 167 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 91 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.552 | 16 | 13 | 29 |
| Au1rxx-base64 | 0.701 | 249 | 106 | 355 |
| ermaozi | 0.97 | 64 | 2 | 66 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24072 | yes | 4.4 | 0 |
| SoliSpirit-all | 9888 | yes | 3.96 | 0 |
| Epodonios-all | 7793 | yes | 4.56 | 0 |
| Surfboard-tg-mixed | 7166 | yes | 3.02 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.95 | 0 |
| barry-far-vless | 5957 | yes | 2.23 | 0 |
| Surfboard-tg-vless | 5625 | yes | 3.4 | 0 |
| DeltaKronecker-all | 5147 | yes | 5.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 5089 | yes | 1.93 | 0 |
| mahdibland-V2RayAggregator | 4235 | yes | 2.54 | 0 |

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
| test_one_timeout | 69 |
| speed | 20 |
| 204 | 18 |
| cn-block | 9 |
| geo | 6 |
