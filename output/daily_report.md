# AutoNodes 每日报告

生成时间：2026-11-02 21:53:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 4/86 |
| 原始节点数 | 81771 |
| 去重后节点数 | 26678 |
| TCP 可达数 | 3000 |
| 真测通过数 | 413 |
| verified 输出数 | 55 |
| global 输出数 | 300 |
| all 输出数 | 26678 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 31.2 |
| fetch | 6.2 |
| generate | 12.8 |
| geo | 1.5 |
| probe | 93.8 |
| real_test | 76.6 |
| tcp | 81.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 32 | 32 | 0 | 100.0% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 160 | 148 | 12 | 92.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 116 | 113 | 3 | 97.4% |
| vless | 238 | 106 | 132 | 44.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 60 |
| geo:ClientOSError | 52 |
| 204:TimeoutError | 9 |
| 204:ProxyError | 7 |
| speed:ClientOSError | 5 |
| cn-block:TimeoutError | 5 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 2 |
| geo:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6180 |
| ConnectionRefusedError | 946 |
| OSError | 232 |
| gaierror | 102 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.911 | prefer | 75 | 0.84 | 8355 |
| Au1rxx-base64 | 0.91 | prefer | 291 | 0.842 | 1751 |
| zhangkai | 0.857 | prefer | 17 | 1.0 | 43 |
| ermaozi-get_subscribe | 0.771 | prefer | 14 | 1.0 | 403 |
| mheidari-all | 0.532 | observe | 164 | 0.451 | 14971 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 139 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4941 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2726 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 416 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 411 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 294 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 272 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 263 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 160 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 147 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.451 | 74 | 90 | 164 |
| Surfboard-tg-mixed | 0.84 | 63 | 12 | 75 |
| Au1rxx-base64 | 0.842 | 245 | 46 | 291 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 14 | 0 | 14 |
| zhangkai | 1.0 | 17 | 0 | 17 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14971 | yes | 5.55 | 0 |
| SoliSpirit-all | 10678 | yes | 3.08 | 0 |
| Surfboard-tg-mixed | 8355 | yes | 4.64 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.67 | 0 |
| barry-far-vless | 6131 | yes | 1.47 | 0 |
| Surfboard-tg-vless | 5917 | yes | 3.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4941 | yes | 1.78 | 0 |
| mahdibland-V2RayAggregator | 4726 | yes | 2.83 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.58 | 0 |
| DeltaKronecker-all | 2726 | yes | 5.6 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 60 |
| geo | 53 |
| 204 | 19 |
| cn-block | 10 |
| speed | 6 |
