# AutoNodes 每日报告

生成时间：2026-10-20 05:06:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 94570 |
| 去重后节点数 | 26219 |
| TCP 可达数 | 3000 |
| 真测通过数 | 437 |
| verified 输出数 | 91 |
| global 输出数 | 300 |
| all 输出数 | 26219 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.2 |
| fetch | 8.3 |
| generate | 13.7 |
| geo | 1.5 |
| probe | 93.2 |
| real_test | 80.6 |
| tcp | 82.0 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 72 | 70 | 2 | 97.2% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 119 | 112 | 7 | 94.1% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 78 | 74 | 4 | 94.9% |
| vless | 279 | 166 | 113 | 59.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 82 |
| geo:ClientOSError | 18 |
| speed:ClientOSError | 11 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 5 |
| 204:ProxyError | 4 |
| 204:TimeoutError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6590 |
| ConnectionRefusedError | 1016 |
| OSError | 236 |
| gaierror | 201 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.948 | prefer | 53 | 0.943 | 510 |
| Au1rxx-base64 | 0.926 | prefer | 288 | 0.872 | 1418 |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 27 |
| DeltaKronecker-all | 0.913 | prefer | 64 | 0.844 | 3294 |
| Surfboard-tg-mixed | 0.624 | observe | 11 | 0.818 | 6911 |
| mheidari-all | 0.482 | observe | 125 | 0.4 | 23317 |
| SoliSpirit-all | 0.391 | observe | 2 | 1.0 | 10162 |
| 10ium-HighSpeed | 0.345 | observe | 2 | 1.0 | 839 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 172 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 479 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 370 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 365 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 248 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 114 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.4 | 50 | 75 | 125 |
| Surfboard-tg-mixed | 0.818 | 9 | 2 | 11 |
| DeltaKronecker-all | 0.844 | 54 | 10 | 64 |
| Au1rxx-base64 | 0.872 | 251 | 37 | 288 |
| ermaozi-get_subscribe | 0.943 | 50 | 3 | 53 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23317 | yes | 7.34 | 0 |
| SoliSpirit-all | 10162 | yes | 3.72 | 0 |
| Epodonios-all | 7379 | yes | 7.6 | 0 |
| Surfboard-tg-mixed | 6911 | yes | 5.57 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 5.15 | 0 |
| barry-far-vless | 5797 | yes | 3.1 | 0 |
| Surfboard-tg-vless | 5515 | yes | 5.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4940 | yes | 4.44 | 0 |
| mahdibland-V2RayAggregator | 4278 | yes | 3.24 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 82 |
| geo | 18 |
| speed | 11 |
| cn-block | 11 |
| 204 | 7 |
