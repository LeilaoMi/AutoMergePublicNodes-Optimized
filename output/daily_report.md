# AutoNodes 每日报告

生成时间：2026-10-27 12:31:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 4/88 |
| 原始节点数 | 96776 |
| 去重后节点数 | 26731 |
| TCP 可达数 | 3000 |
| 真测通过数 | 483 |
| verified 输出数 | 143 |
| global 输出数 | 300 |
| all 输出数 | 26731 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.4 |
| fetch | 5.3 |
| generate | 10.8 |
| geo | 1.6 |
| probe | 84.9 |
| real_test | 91.6 |
| tcp | 84.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 88 | 86 | 2 | 97.7% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 157 | 140 | 17 | 89.2% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 91 | 68 | 23 | 74.7% |
| vless | 291 | 174 | 117 | 59.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 70 |
| speed:ClientOSError | 31 |
| geo:ClientOSError | 28 |
| 204:ProxyError | 10 |
| cn-block:ClientOSError | 7 |
| cn-block:TimeoutError | 5 |
| 204:TimeoutError | 4 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6639 |
| ConnectionRefusedError | 1083 |
| OSError | 238 |
| gaierror | 221 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.991 | prefer | 89 | 0.978 | 603 |
| Au1rxx-base64 | 0.838 | prefer | 345 | 0.768 | 1774 |
| mheidari-all | 0.805 | prefer | 49 | 0.735 | 24516 |
| Surfboard-tg-mixed | 0.741 | prefer | 110 | 0.664 | 7059 |
| DeltaKronecker-all | 0.466 | observe | 42 | 0.381 | 3052 |
| roosterkid-openproxylist-v2ray | 0.455 | observe | 7 | 0.857 | 150 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 7509 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 507 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 398 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 393 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 276 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 254 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 253 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 245 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 223 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 142 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| SoliSpirit-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.381 | 16 | 26 | 42 |
| Surfboard-tg-mixed | 0.664 | 73 | 37 | 110 |
| mheidari-all | 0.735 | 36 | 13 | 49 |
| Au1rxx-base64 | 0.768 | 265 | 80 | 345 |
| roosterkid-openproxylist-v2ray | 0.857 | 6 | 1 | 7 |
| ermaozi | 0.978 | 87 | 2 | 89 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24516 | yes | 4.32 | 0 |
| SoliSpirit-all | 10615 | yes | 2.46 | 0 |
| Epodonios-all | 7509 | yes | 2.49 | 0 |
| Surfboard-tg-mixed | 7059 | yes | 2.73 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.66 | 0 |
| barry-far-vless | 5497 | yes | 1.07 | 0 |
| Surfboard-tg-vless | 5319 | yes | 2.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 0.93 | 0 |
| mahdibland-V2RayAggregator | 4573 | yes | 2.18 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.13 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 70 |
| speed | 33 |
| geo | 30 |
| 204 | 15 |
| cn-block | 12 |
