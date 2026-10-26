# AutoNodes 每日报告

生成时间：2026-10-26 13:23:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 4/88 |
| 原始节点数 | 96713 |
| 去重后节点数 | 26589 |
| TCP 可达数 | 3000 |
| 真测通过数 | 469 |
| verified 输出数 | 128 |
| global 输出数 | 300 |
| all 输出数 | 26589 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 35.7 |
| fetch | 6.8 |
| generate | 12.6 |
| geo | 1.7 |
| probe | 90.3 |
| real_test | 88.7 |
| tcp | 82.4 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 105 | 103 | 2 | 98.1% |
| hysteria2 | 17 | 16 | 1 | 94.1% |
| shadowsocks | 156 | 139 | 17 | 89.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 52 | 41 | 11 | 78.8% |
| vless | 260 | 169 | 91 | 65.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 60 |
| speed:ClientOSError | 14 |
| geo:ClientOSError | 14 |
| 204:TimeoutError | 10 |
| cn-block:TimeoutError | 10 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6551 |
| ConnectionRefusedError | 1042 |
| gaierror | 297 |
| OSError | 237 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.988 | prefer | 105 | 0.971 | 643 |
| Au1rxx-base64 | 0.846 | prefer | 354 | 0.78 | 1689 |
| Surfboard-tg-mixed | 0.812 | prefer | 54 | 0.741 | 7197 |
| mheidari-all | 0.74 | prefer | 51 | 0.667 | 24314 |
| DeltaKronecker-all | 0.482 | observe | 14 | 0.5 | 3004 |
| roosterkid-openproxylist-v2ray | 0.445 | observe | 5 | 1.0 | 150 |
| zhangkai | 0.36 | observe | 3 | 1.0 | 43 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10312 |
| chromego_merge | 0.265 | observe | 1 | 1.0 | 252 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 177 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| peasoft-NoMoreWalls | 0.108 | observe | 2 | 0.0 | 0 | 117 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 10 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 504 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 395 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 390 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 273 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 251 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 250 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 139 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| barry-far-vless | 0.0 | 0 | 1 | 1 |
| peasoft-NoMoreWalls | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.5 | 7 | 7 | 14 |
| mheidari-all | 0.667 | 34 | 17 | 51 |
| Surfboard-tg-mixed | 0.741 | 40 | 14 | 54 |
| Au1rxx-base64 | 0.78 | 276 | 78 | 354 |
| ermaozi | 0.971 | 102 | 3 | 105 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| chromego_merge | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24314 | yes | 5.08 | 0 |
| SoliSpirit-all | 10312 | yes | 2.75 | 0 |
| Epodonios-all | 7666 | yes | 6.15 | 0 |
| Surfboard-tg-mixed | 7197 | yes | 5.72 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.25 | 0 |
| barry-far-vless | 5877 | yes | 0.63 | 0 |
| Surfboard-tg-vless | 5522 | yes | 4.38 | 0 |
| 10ium-ScrapeCategorize-Vless | 4919 | yes | 1.45 | 0 |
| mahdibland-V2RayAggregator | 4228 | yes | 2.87 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.7 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 60 |
| 204 | 19 |
| geo | 15 |
| cn-block | 15 |
| speed | 14 |
