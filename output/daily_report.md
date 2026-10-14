# AutoNodes 每日报告

生成时间：2026-10-14 12:17:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 5/89 |
| 原始节点数 | 98058 |
| 去重后节点数 | 27234 |
| TCP 可达数 | 3000 |
| 真测通过数 | 88 |
| verified 输出数 | 88 |
| global 输出数 | 98 |
| all 输出数 | 27234 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.1 |
| fetch | 8.0 |
| generate | 57.6 |
| geo | 1.6 |
| probe | 111.1 |
| real_test | 57.2 |
| tcp | 84.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 88 | 85 | 3 | 96.6% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 127 | 115 | 12 | 90.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 28 | 21 | 7 | 75.0% |
| vless | 187 | 116 | 71 | 62.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| speed:ClientOSError | 12 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 7 |
| cn-block:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 3 |
| 204:ProxyError | 2 |
| speed:TimeoutError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6898 |
| ConnectionRefusedError | 1016 |
| OSError | 233 |
| gaierror | 193 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.968 | prefer | 70 | 0.957 | 598 |
| zhangkai | 0.927 | prefer | 19 | 1.0 | 144 |
| mheidari-all | 0.866 | prefer | 54 | 0.796 | 23983 |
| Au1rxx-base64 | 0.841 | prefer | 211 | 0.773 | 1782 |
| Surfboard-tg-mixed | 0.716 | prefer | 86 | 0.64 | 7056 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7542 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 448 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 339 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 334 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 164 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 159 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 83 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.64 | 55 | 31 | 86 |
| Au1rxx-base64 | 0.773 | 163 | 48 | 211 |
| mheidari-all | 0.796 | 43 | 11 | 54 |
| ermaozi-get_subscribe | 0.957 | 67 | 3 | 70 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23983 | yes | 8.06 | 0 |
| SoliSpirit-all | 9836 | yes | 4.51 | 0 |
| Epodonios-all | 7542 | yes | 4.95 | 0 |
| Surfboard-tg-mixed | 7056 | yes | 4.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.48 | 0 |
| barry-far-vless | 5831 | yes | 2.08 | 0 |
| Surfboard-tg-vless | 5579 | yes | 5.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 3.92 | 0 |
| DeltaKronecker-all | 4803 | yes | 6.23 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 3.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 44 |
| speed | 14 |
| cn-block | 13 |
| 204 | 13 |
| geo | 10 |
