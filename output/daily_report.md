# AutoNodes 每日报告

生成时间：2026-10-25 16:39:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 3/89 |
| 原始节点数 | 98405 |
| 去重后节点数 | 27202 |
| TCP 可达数 | 3000 |
| 真测通过数 | 380 |
| verified 输出数 | 105 |
| global 输出数 | 300 |
| all 输出数 | 27202 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.4 |
| fetch | 7.7 |
| generate | 14.5 |
| geo | 1.5 |
| probe | 99.1 |
| real_test | 80.8 |
| tcp | 84.2 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 63 | 62 | 1 | 98.4% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 145 | 124 | 21 | 85.5% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 27 | 20 | 7 | 74.1% |
| vless | 241 | 158 | 83 | 65.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 74 |
| 204:TimeoutError | 8 |
| geo:ClientOSError | 8 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| speed:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6699 |
| ConnectionRefusedError | 1049 |
| gaierror | 233 |
| OSError | 232 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.992 | prefer | 63 | 0.984 | 575 |
| Au1rxx-base64 | 0.879 | prefer | 297 | 0.815 | 1657 |
| mheidari-all | 0.805 | prefer | 38 | 0.737 | 24301 |
| Surfboard-tg-mixed | 0.592 | observe | 80 | 0.512 | 7560 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| DeltaKronecker-all | 0.298 | observe | 11 | 0.273 | 3849 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 7729 |

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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 501 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 392 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 387 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 270 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 248 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 247 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 136 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.273 | 3 | 8 | 11 |
| Surfboard-tg-mixed | 0.512 | 41 | 39 | 80 |
| mheidari-all | 0.737 | 28 | 10 | 38 |
| Au1rxx-base64 | 0.815 | 242 | 55 | 297 |
| ermaozi | 0.984 | 62 | 1 | 63 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |
| ninja-vless | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24301 | yes | 6.57 | 0 |
| SoliSpirit-all | 10761 | yes | 2.73 | 0 |
| Epodonios-all | 7729 | yes | 3.55 | 0 |
| Surfboard-tg-mixed | 7560 | yes | 4.14 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.34 | 0 |
| barry-far-vless | 5928 | yes | 1.49 | 0 |
| Surfboard-tg-vless | 5715 | yes | 3.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 1.27 | 0 |
| mahdibland-V2RayAggregator | 4177 | yes | 3.18 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.59 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 74 |
| 204 | 17 |
| geo | 10 |
| cn-block | 9 |
| speed | 3 |
