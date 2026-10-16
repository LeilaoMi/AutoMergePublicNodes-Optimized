# AutoNodes 每日报告

生成时间：2026-10-16 15:03:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/1 |
| 清理建议：优先/观察 | 2/90 |
| 原始节点数 | 99199 |
| 去重后节点数 | 27691 |
| TCP 可达数 | 3000 |
| 真测通过数 | 393 |
| verified 输出数 | 79 |
| global 输出数 | 300 |
| all 输出数 | 27691 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 18.1 |
| fetch | 8.0 |
| generate | 14.2 |
| geo | 1.5 |
| probe | 96.0 |
| real_test | 86.8 |
| tcp | 87.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 61 | 60 | 1 | 98.4% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 138 | 126 | 12 | 91.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 36 | 30 | 6 | 83.3% |
| vless | 268 | 163 | 105 | 60.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 61 |
| speed:ClientOSError | 13 |
| 204:TimeoutError | 11 |
| 204:ClientOSError | 11 |
| cn-block:TimeoutError | 6 |
| geo:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 4 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 4 |
| speed:ProxyError | 1 |
| cn-block:status | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6904 |
| ConnectionRefusedError | 1037 |
| OSError | 237 |
| gaierror | 235 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 59 | 1.0 | 618 |
| Au1rxx-base64 | 0.833 | prefer | 424 | 0.755 | 1991 |
| mheidari-all | 0.625 | observe | 20 | 0.55 | 23974 |
| Surfboard-tg-mixed | 0.32 | observe | 4 | 0.5 | 7090 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1991 |
| Epodonios-all | 0.255 | observe | 0 | None | 7568 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10094 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

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
| downweight | DeltaKronecker-all | 0.197 | 9 | 0.111 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.111 | 1 | 8 | 9 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.5 | 2 | 2 | 4 |
| mheidari-all | 0.55 | 11 | 9 | 20 |
| Au1rxx-base64 | 0.755 | 320 | 104 | 424 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 59 | 0 | 59 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23974 | yes | 6.57 | 0 |
| SoliSpirit-all | 10094 | yes | 3.63 | 0 |
| Epodonios-all | 7568 | yes | 5.01 | 0 |
| Surfboard-tg-mixed | 7090 | yes | 4.65 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.23 | 0 |
| barry-far-vless | 5822 | yes | 1.56 | 0 |
| Surfboard-tg-vless | 5572 | yes | 4.42 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 0.56 | 0 |
| DeltaKronecker-all | 4946 | yes | 6.71 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 3.72 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 61 |
| 204 | 26 |
| cn-block | 15 |
| speed | 14 |
| geo | 10 |
