# AutoNodes 每日报告

生成时间：2026-10-14 11:38:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 5/89 |
| 原始节点数 | 98043 |
| 去重后节点数 | 27216 |
| TCP 可达数 | 3000 |
| 真测通过数 | 84 |
| verified 输出数 | 84 |
| global 输出数 | 91 |
| all 输出数 | 27216 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 53.1 |
| geo | 1.5 |
| probe | 96.3 |
| real_test | 86.5 |
| tcp | 118.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 87 | 82 | 5 | 94.3% |
| hysteria2 | 14 | 11 | 3 | 78.6% |
| shadowsocks | 135 | 116 | 19 | 85.9% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 1 | 0 | 1 | 0.0% |
| vless | 176 | 106 | 70 | 60.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 52 |
| speed:ClientOSError | 11 |
| 204:ProxyError | 8 |
| cn-block:TimeoutError | 6 |
| geo:ClientOSError | 4 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| geo:TimeoutError | 3 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6399 |
| ConnectionRefusedError | 1044 |
| gaierror | 375 |
| OSError | 239 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | prefer | 19 | 1.0 | 144 |
| ermaozi-get_subscribe | 0.925 | prefer | 69 | 0.913 | 598 |
| Surfboard-tg-mixed | 0.83 | prefer | 26 | 0.769 | 7056 |
| Au1rxx-base64 | 0.822 | prefer | 203 | 0.754 | 1778 |
| mheidari-all | 0.704 | prefer | 99 | 0.626 | 23983 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7542 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9834 |

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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 447 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 338 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 333 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 163 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 158 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 82 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.626 | 62 | 37 | 99 |
| Au1rxx-base64 | 0.754 | 153 | 50 | 203 |
| Surfboard-tg-mixed | 0.769 | 20 | 6 | 26 |
| ermaozi-get_subscribe | 0.913 | 63 | 6 | 69 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23983 | yes | 5.76 | 0 |
| SoliSpirit-all | 9834 | yes | 3.31 | 0 |
| Epodonios-all | 7542 | yes | 4.37 | 0 |
| Surfboard-tg-mixed | 7056 | yes | 4.94 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.95 | 0 |
| barry-far-vless | 5831 | yes | 2.16 | 0 |
| Surfboard-tg-vless | 5579 | yes | 3.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 2.18 | 0 |
| DeltaKronecker-all | 4803 | yes | 4.52 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 1.64 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| trojan | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 52 |
| 204 | 15 |
| speed | 13 |
| cn-block | 12 |
| geo | 8 |
