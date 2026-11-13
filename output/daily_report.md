# AutoNodes 每日报告

生成时间：2026-11-13 18:20:30

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83174 |
| 去重后节点数 | 26889 |
| TCP 可达数 | 3000 |
| 真测通过数 | 348 |
| verified 输出数 | 72 |
| global 输出数 | 300 |
| all 输出数 | 26889 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 34.5 |
| fetch | 8.0 |
| generate | 11.2 |
| geo | 1.6 |
| probe | 81.3 |
| real_test | 66.8 |
| tcp | 81.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 0 | 2 | 0.0% |
| http | 56 | 55 | 1 | 98.2% |
| hysteria2 | 11 | 9 | 2 | 81.8% |
| shadowsocks | 204 | 175 | 29 | 85.8% |
| trojan | 71 | 43 | 28 | 60.6% |
| vless | 112 | 66 | 46 | 58.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| 204:ProxyError | 21 |
| speed:ClientOSError | 11 |
| 204:TimeoutError | 8 |
| cn-block:TimeoutError | 7 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 3 |
| speed:TimeoutError | 2 |
| speed:ProxyError | 2 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6247 |
| ConnectionRefusedError | 953 |
| OSError | 238 |
| gaierror | 213 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.989 | prefer | 56 | 0.982 | 590 |
| Surfboard-tg-mixed | 0.88 | prefer | 128 | 0.805 | 8804 |
| Au1rxx-base64 | 0.814 | prefer | 170 | 0.747 | 1751 |
| mheidari-all | 0.71 | prefer | 98 | 0.633 | 14267 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4900 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2734 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11395 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6228 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 168 |
| ermaozi-get_subscribe | 0.145 | observe | 1 | 0.0 | 0 | 442 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 446 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 441 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 324 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 302 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 301 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.633 | 62 | 36 | 98 |
| Au1rxx-base64 | 0.747 | 127 | 43 | 170 |
| Surfboard-tg-mixed | 0.805 | 103 | 25 | 128 |
| ermaozi | 0.982 | 55 | 1 | 56 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14267 | yes | 3.53 | 0 |
| SoliSpirit-all | 11395 | yes | 2.98 | 0 |
| Surfboard-tg-mixed | 8804 | yes | 3.12 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.93 | 0 |
| barry-far-vless | 6409 | yes | 0.8 | 0 |
| Surfboard-tg-vless | 6228 | yes | 2.76 | 0 |
| 10ium-ScrapeCategorize-Vless | 4900 | yes | 0.44 | 0 |
| mahdibland-V2RayAggregator | 4624 | yes | 2.19 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.29 | 0 |
| DeltaKronecker-all | 2734 | yes | 3.96 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 44 |
| 204 | 32 |
| speed | 15 |
| cn-block | 11 |
| geo | 6 |
