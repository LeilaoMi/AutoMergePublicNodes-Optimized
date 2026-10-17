# AutoNodes 每日报告

生成时间：2026-10-17 11:00:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99307 |
| 去重后节点数 | 27832 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 121 |
| global 输出数 | 300 |
| all 输出数 | 27832 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.6 |
| fetch | 6.0 |
| generate | 10.8 |
| geo | 1.5 |
| probe | 82.2 |
| real_test | 91.7 |
| tcp | 87.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 99 | 93 | 6 | 93.9% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 155 | 144 | 11 | 92.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 60 | 32 | 28 | 53.3% |
| vless | 283 | 189 | 94 | 66.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 71 |
| geo:ClientOSError | 22 |
| speed:ClientOSError | 12 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 9 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| speed:TimeoutError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7188 |
| ConnectionRefusedError | 1023 |
| OSError | 233 |
| gaierror | 185 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | prefer | 99 | 0.96 | 702 |
| Au1rxx-base64 | 0.898 | prefer | 426 | 0.819 | 1994 |
| Surfboard-tg-mixed | 0.48 | observe | 43 | 0.395 | 7171 |
| mheidari-all | 0.385 | observe | 8 | 0.5 | 23828 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 7611 |
| DeltaKronecker-all | 0.292 | observe | 31 | 0.194 | 4999 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4986 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1994 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9902 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.108 | observe | 2 | 0.0 | 0 | 105 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 12 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 469 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 360 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 355 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 180 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 104 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.194 | 6 | 25 | 31 |
| Surfboard-tg-mixed | 0.395 | 17 | 26 | 43 |
| mheidari-all | 0.5 | 4 | 4 | 8 |
| Au1rxx-base64 | 0.819 | 349 | 77 | 426 |
| ermaozi | 0.96 | 95 | 4 | 99 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23828 | yes | 4.49 | 0 |
| SoliSpirit-all | 9902 | yes | 5.05 | 0 |
| Epodonios-all | 7611 | yes | 4.63 | 0 |
| Surfboard-tg-mixed | 7171 | yes | 3.95 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.72 | 0 |
| barry-far-vless | 5842 | yes | 2.25 | 0 |
| Surfboard-tg-vless | 5617 | yes | 3.79 | 0 |
| DeltaKronecker-all | 4999 | yes | 5.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 4986 | yes | 4.08 | 0 |
| mahdibland-V2RayAggregator | 4255 | yes | 2.78 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 71 |
| 204 | 23 |
| geo | 22 |
| speed | 16 |
| cn-block | 9 |
