# AutoNodes 每日报告

生成时间：2026-10-16 14:56:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99200 |
| 去重后节点数 | 27685 |
| TCP 可达数 | 3000 |
| 真测通过数 | 421 |
| verified 输出数 | 77 |
| global 输出数 | 300 |
| all 输出数 | 27685 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 18.2 |
| fetch | 5.6 |
| generate | 10.5 |
| geo | 1.4 |
| probe | 80.4 |
| real_test | 75.7 |
| tcp | 86.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 55 | 4 | 93.2% |
| hysteria2 | 17 | 15 | 2 | 88.2% |
| shadowsocks | 146 | 137 | 9 | 93.8% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 37 | 31 | 6 | 83.8% |
| vless | 270 | 182 | 88 | 67.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 56 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 12 |
| 204:ProxyError | 7 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| cn-block:status | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6956 |
| ConnectionRefusedError | 1022 |
| OSError | 236 |
| gaierror | 178 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.941 | prefer | 58 | 0.931 | 618 |
| Au1rxx-base64 | 0.868 | prefer | 446 | 0.789 | 1991 |
| mheidari-all | 0.625 | observe | 20 | 0.55 | 23974 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 4946 |
| Surfboard-tg-mixed | 0.349 | observe | 3 | 0.667 | 7090 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 79 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1991 |
| Epodonios-all | 0.255 | observe | 0 | None | 7568 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 464 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 355 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 350 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 180 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 175 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 99 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.55 | 11 | 9 | 20 |
| Surfboard-tg-mixed | 0.667 | 2 | 1 | 3 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.789 | 352 | 94 | 446 |
| ermaozi | 0.931 | 54 | 4 | 58 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23974 | yes | 5.05 | 0 |
| SoliSpirit-all | 10094 | yes | 3.29 | 0 |
| Epodonios-all | 7568 | yes | 3.65 | 0 |
| Surfboard-tg-mixed | 7090 | yes | 3.25 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.24 | 0 |
| barry-far-vless | 5822 | yes | 2.2 | 0 |
| Surfboard-tg-vless | 5572 | yes | 3.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 2.34 | 0 |
| DeltaKronecker-all | 4946 | yes | 4.95 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 0.64 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 56 |
| 204 | 22 |
| speed | 14 |
| geo | 10 |
| cn-block | 9 |
