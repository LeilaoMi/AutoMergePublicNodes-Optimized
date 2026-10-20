# AutoNodes 每日报告

生成时间：2026-10-20 11:55:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 94098 |
| 去重后节点数 | 26454 |
| TCP 可达数 | 3000 |
| 真测通过数 | 472 |
| verified 输出数 | 136 |
| global 输出数 | 300 |
| all 输出数 | 26454 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.4 |
| fetch | 4.1 |
| generate | 8.4 |
| geo | 1.4 |
| probe | 75.6 |
| real_test | 97.2 |
| tcp | 80.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 77 | 74 | 3 | 96.1% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 162 | 144 | 18 | 88.9% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 82 | 40 | 42 | 48.8% |
| vless | 330 | 208 | 122 | 63.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 89 |
| geo:ClientOSError | 29 |
| 204:TimeoutError | 20 |
| speed:ClientOSError | 11 |
| 204:ProxyError | 9 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| geo:TimeoutError | 3 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6604 |
| ConnectionRefusedError | 1023 |
| OSError | 236 |
| gaierror | 193 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 27 |
| ermaozi-get_subscribe | 0.951 | prefer | 56 | 0.946 | 510 |
| mheidari-all | 0.945 | prefer | 50 | 0.88 | 23400 |
| Au1rxx-base64 | 0.848 | prefer | 309 | 0.803 | 1192 |
| Surfboard-tg-mixed | 0.667 | observe | 90 | 0.589 | 6911 |
| tg-LonUp_M | 0.495 | observe | 8 | 0.875 | 167 |
| DeltaKronecker-all | 0.468 | observe | 127 | 0.386 | 3519 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 65 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4967 |
| Epodonios-all | 0.255 | observe | 0 | None | 7377 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 480 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 371 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 366 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 249 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 115 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.386 | 49 | 78 | 127 |
| Surfboard-tg-mixed | 0.589 | 53 | 37 | 90 |
| Au1rxx-base64 | 0.803 | 248 | 61 | 309 |
| tg-LonUp_M | 0.875 | 7 | 1 | 8 |
| mheidari-all | 0.88 | 44 | 6 | 50 |
| ermaozi-get_subscribe | 0.946 | 53 | 3 | 56 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23400 | yes | 3.38 | 0 |
| SoliSpirit-all | 9884 | yes | 2.07 | 0 |
| Epodonios-all | 7377 | yes | 2.98 | 0 |
| Surfboard-tg-mixed | 6911 | yes | 2.39 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.12 | 0 |
| barry-far-vless | 5733 | yes | 0.25 | 0 |
| Surfboard-tg-vless | 5515 | yes | 2.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4967 | yes | 0.37 | 0 |
| mahdibland-V2RayAggregator | 4278 | yes | 0.13 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 89 |
| geo | 36 |
| 204 | 34 |
| cn-block | 18 |
| speed | 12 |
