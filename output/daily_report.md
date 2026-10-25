# AutoNodes 每日报告

生成时间：2026-10-25 21:02:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 3/89 |
| 原始节点数 | 98673 |
| 去重后节点数 | 27238 |
| TCP 可达数 | 3000 |
| 真测通过数 | 363 |
| verified 输出数 | 105 |
| global 输出数 | 300 |
| all 输出数 | 27238 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 18.8 |
| fetch | 5.3 |
| generate | 10.6 |
| geo | 1.9 |
| probe | 80.1 |
| real_test | 71.8 |
| tcp | 84.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 63 | 62 | 1 | 98.4% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 112 | 105 | 7 | 93.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 40 | 30 | 10 | 75.0% |
| vless | 225 | 155 | 70 | 68.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 47 |
| 204:TimeoutError | 11 |
| cn-block:TimeoutError | 9 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 4 |
| 204:ProxyError | 3 |
| 204:ClientOSError | 3 |
| speed:ClientOSError | 3 |
| geo:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6905 |
| ConnectionRefusedError | 1046 |
| OSError | 236 |
| gaierror | 177 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.992 | prefer | 63 | 0.984 | 575 |
| Au1rxx-base64 | 0.873 | prefer | 326 | 0.807 | 1702 |
| mheidari-all | 0.772 | prefer | 37 | 0.703 | 24713 |
| Surfboard-tg-mixed | 0.563 | observe | 16 | 0.562 | 7442 |
| DeltaKronecker-all | 0.314 | observe | 9 | 0.333 | 3849 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 53 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 7913 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10415 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 175 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 502 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 393 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 388 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 249 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 248 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 137 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.333 | 3 | 6 | 9 |
| Surfboard-tg-mixed | 0.562 | 9 | 7 | 16 |
| mheidari-all | 0.703 | 26 | 11 | 37 |
| Au1rxx-base64 | 0.807 | 263 | 63 | 326 |
| ermaozi | 0.984 | 62 | 1 | 63 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24713 | yes | 4.75 | 0 |
| SoliSpirit-all | 10415 | yes | 1.4 | 0 |
| Epodonios-all | 7913 | yes | 2.74 | 0 |
| Surfboard-tg-mixed | 7442 | yes | 3.12 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.87 | 0 |
| barry-far-vless | 5934 | yes | 1.01 | 0 |
| Surfboard-tg-vless | 5721 | yes | 2.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 0.34 | 0 |
| mahdibland-V2RayAggregator | 4177 | yes | 2.31 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.07 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 47 |
| 204 | 17 |
| cn-block | 13 |
| geo | 8 |
| speed | 4 |
