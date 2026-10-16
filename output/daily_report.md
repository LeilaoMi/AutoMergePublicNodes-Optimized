# AutoNodes 每日报告

生成时间：2026-10-16 07:02:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/1 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99718 |
| 去重后节点数 | 27907 |
| TCP 可达数 | 3000 |
| 真测通过数 | 475 |
| verified 输出数 | 43 |
| global 输出数 | 300 |
| all 输出数 | 27907 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.5 |
| fetch | 8.3 |
| generate | 14.4 |
| geo | 1.5 |
| probe | 106.6 |
| real_test | 96.9 |
| tcp | 89.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 91 | 80 | 11 | 87.9% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 149 | 138 | 11 | 92.6% |
| trojan | 57 | 36 | 21 | 63.2% |
| vless | 302 | 204 | 98 | 67.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 76 |
| geo:ClientOSError | 16 |
| speed:ClientOSError | 14 |
| 204:ProxyError | 6 |
| speed:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 5 |
| 204:ClientOSError | 4 |
| speed:TimeoutError | 3 |
| geo:ProxyError | 2 |
| 204:TimeoutError | 2 |
| cn-block:TimeoutError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7265 |
| ConnectionRefusedError | 1007 |
| OSError | 237 |
| gaierror | 154 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.907 | prefer | 89 | 0.888 | 693 |
| Au1rxx-base64 | 0.904 | prefer | 448 | 0.826 | 1992 |
| mheidari-all | 0.495 | observe | 19 | 0.421 | 23985 |
| Surfboard-tg-mixed | 0.427 | observe | 47 | 0.34 | 7054 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7651 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10060 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5573 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 461 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 352 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 347 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 96 | 连续死亡次数 >= 2 |
| downweight | DeltaKronecker-all | 0.208 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.143 | 1 | 6 | 7 |
| Surfboard-tg-mixed | 0.34 | 16 | 31 | 47 |
| mheidari-all | 0.421 | 8 | 11 | 19 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.826 | 370 | 78 | 448 |
| ermaozi | 0.888 | 79 | 10 | 89 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23985 | yes | 6.58 | 0 |
| SoliSpirit-all | 10060 | yes | 5.05 | 0 |
| Epodonios-all | 7651 | yes | 5.25 | 0 |
| Surfboard-tg-mixed | 7054 | yes | 5.0 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 5.69 | 0 |
| barry-far-vless | 5882 | yes | 2.6 | 0 |
| Surfboard-tg-vless | 5573 | yes | 5.5 | 0 |
| DeltaKronecker-all | 5147 | yes | 4.92 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 2.31 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 2.2 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 76 |
| speed | 23 |
| geo | 19 |
| 204 | 12 |
| cn-block | 11 |
