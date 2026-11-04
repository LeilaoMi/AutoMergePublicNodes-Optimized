# AutoNodes 每日报告

生成时间：2026-11-04 06:45:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 3/87 |
| 原始节点数 | 82812 |
| 去重后节点数 | 26757 |
| TCP 可达数 | 3000 |
| 真测通过数 | 424 |
| verified 输出数 | 61 |
| global 输出数 | 300 |
| all 输出数 | 26757 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.4 |
| fetch | 5.1 |
| generate | 10.7 |
| geo | 1.5 |
| probe | 79.1 |
| real_test | 84.2 |
| tcp | 80.8 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 14 | 10 | 4 | 71.4% |
| shadowsocks | 183 | 175 | 8 | 95.6% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 95 | 86 | 9 | 90.5% |
| vless | 293 | 132 | 161 | 45.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 70 |
| geo:ClientOSError | 45 |
| 204:ProxyError | 31 |
| cn-block:TimeoutError | 8 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 6 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| speed:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 1 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6143 |
| ConnectionRefusedError | 955 |
| OSError | 232 |
| gaierror | 181 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.945 | prefer | 19 | 1.0 | 578 |
| Au1rxx-base64 | 0.853 | prefer | 288 | 0.785 | 1751 |
| Surfboard-tg-mixed | 0.714 | prefer | 12 | 0.917 | 8544 |
| mheidari-all | 0.662 | observe | 285 | 0.582 | 15179 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 130 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5017 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2526 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 176 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 419 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 414 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 297 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 275 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 274 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 163 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 150 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.582 | 166 | 119 | 285 |
| Au1rxx-base64 | 0.785 | 226 | 62 | 288 |
| Surfboard-tg-mixed | 0.917 | 11 | 1 | 12 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15179 | yes | 4.5 | 0 |
| SoliSpirit-all | 10853 | yes | 3.18 | 0 |
| Surfboard-tg-mixed | 8544 | yes | 0.56 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.93 | 0 |
| barry-far-vless | 6238 | yes | 1.04 | 0 |
| Surfboard-tg-vless | 6022 | yes | 3.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 5017 | yes | 0.73 | 0 |
| mahdibland-V2RayAggregator | 4608 | yes | 2.57 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.1 | 0 |
| DeltaKronecker-all | 2526 | yes | 4.68 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 70 |
| geo | 49 |
| 204 | 41 |
| cn-block | 19 |
| speed | 6 |
