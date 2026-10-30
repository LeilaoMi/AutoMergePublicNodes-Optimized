# AutoNodes 每日报告

生成时间：2026-10-30 13:17:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 2/86 |
| 原始节点数 | 100257 |
| 去重后节点数 | 27804 |
| TCP 可达数 | 3000 |
| 真测通过数 | 440 |
| verified 输出数 | 80 |
| global 输出数 | 300 |
| all 输出数 | 27804 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 20.8 |
| fetch | 8.1 |
| generate | 15.3 |
| geo | 1.6 |
| probe | 96.9 |
| real_test | 92.5 |
| tcp | 87.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 27 | 1 | 96.4% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 163 | 144 | 19 | 88.3% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 165 | 120 | 45 | 72.7% |
| vless | 235 | 137 | 98 | 58.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 91 |
| geo:ClientOSError | 22 |
| 204:TimeoutError | 15 |
| 204:ProxyError | 13 |
| cn-block:TimeoutError | 7 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 5 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7064 |
| ConnectionRefusedError | 1105 |
| OSError | 243 |
| gaierror | 209 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.955 | prefer | 28 | 0.964 | 550 |
| Au1rxx-base64 | 0.93 | prefer | 340 | 0.862 | 1751 |
| Surfboard-tg-mixed | 0.622 | observe | 140 | 0.543 | 7902 |
| mheidari-all | 0.534 | observe | 95 | 0.453 | 34171 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2724 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10521 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5822 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 516 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 407 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 402 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 285 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 263 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 262 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 254 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 151 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.453 | 43 | 52 | 95 |
| Surfboard-tg-mixed | 0.543 | 76 | 64 | 140 |
| Au1rxx-base64 | 0.862 | 293 | 47 | 340 |
| ermaozi | 0.964 | 27 | 1 | 28 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34171 | yes | 6.96 | 0 |
| SoliSpirit-all | 10521 | yes | 5.02 | 0 |
| Surfboard-tg-mixed | 7902 | yes | 4.6 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.21 | 0 |
| barry-far-vless | 5942 | yes | 0.78 | 0 |
| Surfboard-tg-vless | 5822 | yes | 4.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 2.98 | 0 |
| mahdibland-V2RayAggregator | 4445 | yes | 3.36 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.1 | 0 |
| DeltaKronecker-all | 2724 | yes | 7.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 91 |
| 204 | 31 |
| geo | 27 |
| cn-block | 12 |
| speed | 3 |
