# AutoNodes 每日报告

生成时间：2026-10-24 11:20:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 92774 |
| 去重后节点数 | 24601 |
| TCP 可达数 | 3000 |
| 真测通过数 | 398 |
| verified 输出数 | 115 |
| global 输出数 | 300 |
| all 输出数 | 24601 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.3 |
| fetch | 9.3 |
| generate | 12.7 |
| geo | 1.5 |
| probe | 92.7 |
| real_test | 80.4 |
| tcp | 75.1 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 84 | 82 | 2 | 97.6% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 155 | 142 | 13 | 91.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 37 | 22 | 15 | 59.5% |
| vless | 209 | 142 | 67 | 67.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 50 |
| geo:ClientOSError | 14 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 8 |
| cn-block:TimeoutError | 6 |
| cn-block:ClientOSError | 3 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6140 |
| ConnectionRefusedError | 1057 |
| gaierror | 297 |
| OSError | 243 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.987 | prefer | 79 | 0.975 | 608 |
| Au1rxx-base64 | 0.89 | prefer | 252 | 0.829 | 1579 |
| mheidari-all | 0.88 | prefer | 43 | 0.814 | 23868 |
| Surfboard-tg-mixed | 0.74 | prefer | 104 | 0.663 | 7180 |
| tg-oneclickvpnkeys | 0.444 | observe | 5 | 1.0 | 113 |
| 10ium-HighSpeed | 0.345 | observe | 2 | 1.0 | 839 |
| roosterkid-openproxylist-v2ray | 0.275 | observe | 3 | 0.667 | 150 |
| Surfboard-tg-vless | 0.272 | observe | 7 | 0.286 | 5436 |
| chromego_merge | 0.264 | observe | 1 | 1.0 | 236 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 55 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ermaozi-get_subscribe | 0.148 | observe | 1 | 0.0 | 0 | 515 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 496 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 387 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 382 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 265 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 131 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 2 | 2 |
| Surfboard-tg-vless | 0.286 | 2 | 5 | 7 |
| Surfboard-tg-mixed | 0.663 | 69 | 35 | 104 |
| roosterkid-openproxylist-v2ray | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.814 | 35 | 8 | 43 |
| Au1rxx-base64 | 0.829 | 209 | 43 | 252 |
| ermaozi | 0.975 | 77 | 2 | 79 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23868 | yes | 6.44 | 0 |
| SoliSpirit-all | 10392 | yes | 5.06 | 0 |
| Epodonios-all | 7652 | yes | 3.85 | 0 |
| Surfboard-tg-mixed | 7180 | yes | 4.39 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.95 | 0 |
| barry-far-vless | 5737 | yes | 3.12 | 0 |
| Surfboard-tg-vless | 5436 | yes | 3.65 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 2.66 | 0 |
| mahdibland-V2RayAggregator | 4150 | yes | 1.63 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.2 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 50 |
| 204 | 18 |
| geo | 18 |
| cn-block | 11 |
| speed | 2 |
