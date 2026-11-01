# AutoNodes 每日报告

生成时间：2026-11-01 06:29:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/1 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 80495 |
| 去重后节点数 | 26309 |
| TCP 可达数 | 3000 |
| 真测通过数 | 617 |
| verified 输出数 | 98 |
| global 输出数 | 300 |
| all 输出数 | 26309 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.3 |
| fetch | 5.1 |
| generate | 11.2 |
| geo | 1.4 |
| probe | 79.4 |
| real_test | 105.9 |
| tcp | 76.8 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 84 | 83 | 1 | 98.8% |
| hysteria2 | 20 | 15 | 5 | 75.0% |
| shadowsocks | 138 | 128 | 10 | 92.8% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 225 | 204 | 21 | 90.7% |
| vless | 385 | 187 | 198 | 48.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 128 |
| geo:ClientOSError | 63 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 10 |
| 204:ProxyError | 8 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 2 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5842 |
| ConnectionRefusedError | 959 |
| OSError | 235 |
| gaierror | 172 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.993 | prefer | 66 | 0.985 | 558 |
| Au1rxx-base64 | 0.939 | prefer | 319 | 0.871 | 1751 |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 43 |
| Surfboard-tg-mixed | 0.757 | prefer | 16 | 0.812 | 7809 |
| mheidari-all | 0.648 | observe | 424 | 0.568 | 14747 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 178 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4970 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2848 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10495 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| chromego_merge | 0.138 | observe | 1 | 0.0 | 0 | 251 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 521 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 412 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 407 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 290 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 268 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 267 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 259 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 156 | 连续死亡次数 >= 2 |
| downweight | xiaoji235-airport-v2ray-all | 0.202 | 8 | 0.125 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| chromego_merge | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.125 | 1 | 7 | 8 |
| mheidari-all | 0.568 | 241 | 183 | 424 |
| Surfboard-tg-mixed | 0.812 | 13 | 3 | 16 |
| Au1rxx-base64 | 0.871 | 278 | 41 | 319 |
| ermaozi-get_subscribe | 0.985 | 65 | 1 | 66 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14747 | yes | 3.37 | 0 |
| SoliSpirit-all | 10495 | yes | 2.23 | 0 |
| Surfboard-tg-mixed | 7809 | yes | 2.97 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.89 | 0 |
| barry-far-vless | 5805 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 5637 | yes | 2.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 4970 | yes | 1.31 | 0 |
| mahdibland-V2RayAggregator | 4680 | yes | 2.49 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.62 | 0 |
| DeltaKronecker-all | 2848 | yes | 4.36 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 128 |
| geo | 64 |
| 204 | 23 |
| speed | 14 |
| cn-block | 7 |
