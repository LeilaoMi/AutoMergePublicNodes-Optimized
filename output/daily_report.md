# AutoNodes 每日报告

生成时间：2026-10-14 13:05:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 4/90 |
| 原始节点数 | 97972 |
| 去重后节点数 | 27170 |
| TCP 可达数 | 3000 |
| 真测通过数 | 80 |
| verified 输出数 | 80 |
| global 输出数 | 84 |
| all 输出数 | 27170 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.6 |
| fetch | 8.1 |
| generate | 13.7 |
| geo | 1.6 |
| probe | 105.4 |
| real_test | 70.1 |
| tcp | 85.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 27 | 27 | 0 | 100.0% |
| hysteria2 | 12 | 9 | 3 | 75.0% |
| shadowsocks | 136 | 118 | 18 | 86.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 11 | 6 | 5 | 54.5% |
| vless | 173 | 119 | 54 | 68.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 52 |
| speed:ClientOSError | 11 |
| geo:ClientOSError | 4 |
| cn-block:TimeoutError | 3 |
| 204:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |
| 204:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7075 |
| ConnectionRefusedError | 1010 |
| gaierror | 235 |
| OSError | 232 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | prefer | 19 | 1.0 | 144 |
| Au1rxx-base64 | 0.853 | prefer | 209 | 0.785 | 1782 |
| mheidari-all | 0.797 | prefer | 90 | 0.722 | 23983 |
| Surfboard-tg-mixed | 0.794 | prefer | 33 | 0.727 | 7056 |
| ermaozi-get_subscribe | 0.546 | observe | 9 | 0.889 | 515 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7542 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9836 |

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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 449 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 340 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 335 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 187 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 165 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 160 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 84 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.722 | 65 | 25 | 90 |
| Surfboard-tg-mixed | 0.727 | 24 | 9 | 33 |
| Au1rxx-base64 | 0.785 | 164 | 45 | 209 |
| ermaozi-get_subscribe | 0.889 | 8 | 1 | 9 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23983 | yes | 6.28 | 0 |
| SoliSpirit-all | 9836 | yes | 4.75 | 0 |
| Epodonios-all | 7542 | yes | 7.48 | 0 |
| Surfboard-tg-mixed | 7056 | yes | 4.94 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.28 | 0 |
| barry-far-vless | 5831 | yes | 0.72 | 0 |
| Surfboard-tg-vless | 5579 | yes | 4.65 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 3.42 | 0 |
| DeltaKronecker-all | 4803 | yes | 5.04 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 3.72 | 0 |

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
| test_one_timeout | 52 |
| speed | 13 |
| geo | 6 |
| 204 | 5 |
| cn-block | 5 |
