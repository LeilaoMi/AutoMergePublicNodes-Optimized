# AutoNodes 每日报告

生成时间：2026-10-23 11:55:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 14/1 |
| 清理建议：优先/观察 | 4/88 |
| 原始节点数 | 96151 |
| 去重后节点数 | 26910 |
| TCP 可达数 | 3000 |
| 真测通过数 | 414 |
| verified 输出数 | 140 |
| global 输出数 | 300 |
| all 输出数 | 26910 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.5 |
| fetch | 7.2 |
| generate | 13.9 |
| geo | 1.6 |
| probe | 93.8 |
| real_test | 75.0 |
| tcp | 80.5 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 106 | 101 | 5 | 95.3% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 152 | 143 | 9 | 94.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 48 | 32 | 16 | 66.7% |
| vless | 196 | 126 | 70 | 64.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 57 |
| 204:ProxyError | 10 |
| geo:ClientOSError | 8 |
| 204:TimeoutError | 7 |
| cn-block:TimeoutError | 7 |
| cn-block:ClientOSError | 5 |
| speed:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6349 |
| ConnectionRefusedError | 1055 |
| gaierror | 304 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.986 | prefer | 103 | 0.971 | 609 |
| Au1rxx-base64 | 0.859 | prefer | 250 | 0.8 | 1538 |
| Surfboard-tg-mixed | 0.812 | prefer | 95 | 0.737 | 6855 |
| mheidari-all | 0.802 | prefer | 52 | 0.731 | 23755 |
| DeltaKronecker-all | 0.401 | observe | 7 | 0.571 | 3871 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 164 |
| zhangkai | 0.256 | observe | 1 | 1.0 | 24 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4911 |
| Epodonios-all | 0.255 | observe | 0 | None | 7492 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.079 | downweight | 5 | 0.0 | 0 | 150 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 492 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 383 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 378 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 261 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 127 | 连续死亡次数 >= 2 |
| downweight | roosterkid-openproxylist-v2ray | 0.079 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 5 | 5 |
| tg-oneclickvpnkeys | 0.333 | 1 | 2 | 3 |
| DeltaKronecker-all | 0.571 | 4 | 3 | 7 |
| mheidari-all | 0.731 | 38 | 14 | 52 |
| Surfboard-tg-mixed | 0.737 | 70 | 25 | 95 |
| Au1rxx-base64 | 0.8 | 200 | 50 | 250 |
| ermaozi | 0.971 | 100 | 3 | 103 |
| zhangkai | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23755 | yes | 5.68 | 0 |
| SoliSpirit-all | 10293 | yes | 4.55 | 0 |
| Epodonios-all | 7492 | yes | 5.97 | 0 |
| Surfboard-tg-mixed | 6855 | yes | 4.09 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.85 | 0 |
| barry-far-vless | 5662 | yes | 1.04 | 0 |
| Surfboard-tg-vless | 5326 | yes | 4.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 1.27 | 0 |
| mahdibland-V2RayAggregator | 4230 | yes | 2.66 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.82 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 57 |
| 204 | 19 |
| cn-block | 13 |
| geo | 11 |
| speed | 3 |
