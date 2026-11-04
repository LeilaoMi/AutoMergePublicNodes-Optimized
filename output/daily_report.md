# AutoNodes 每日报告

生成时间：2026-11-04 14:28:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 4/86 |
| 原始节点数 | 82244 |
| 去重后节点数 | 26846 |
| TCP 可达数 | 3000 |
| 真测通过数 | 395 |
| verified 输出数 | 33 |
| global 输出数 | 300 |
| all 输出数 | 26846 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.9 |
| fetch | 5.4 |
| generate | 11.9 |
| geo | 1.5 |
| probe | 82.0 |
| real_test | 75.3 |
| tcp | 80.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 20 | 1 | 95.2% |
| hysteria2 | 12 | 9 | 3 | 75.0% |
| shadowsocks | 227 | 206 | 21 | 90.7% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 84 | 54 | 30 | 64.3% |
| vless | 161 | 106 | 55 | 65.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 63 |
| 204:ProxyError | 14 |
| cn-block:ProxyError | 10 |
| 204:TimeoutError | 8 |
| geo:ProxyError | 3 |
| 204:ClientOSError | 3 |
| cn-block:TimeoutError | 3 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 2 |
| 204:ServerDisconnectedError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6191 |
| ConnectionRefusedError | 974 |
| OSError | 234 |
| gaierror | 196 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.944 | prefer | 108 | 0.87 | 15179 |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 43 |
| Surfboard-tg-mixed | 0.864 | prefer | 114 | 0.789 | 8518 |
| Au1rxx-base64 | 0.793 | prefer | 258 | 0.725 | 1751 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 177 |
| ermaozi | 0.315 | observe | 2 | 1.0 | 83 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2526 |

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
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 420 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 415 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 298 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 276 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 275 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 267 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 245 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 164 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 151 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.725 | 187 | 71 | 258 |
| Surfboard-tg-mixed | 0.789 | 90 | 24 | 114 |
| mheidari-all | 0.87 | 94 | 14 | 108 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 2 | 0 | 2 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15179 | yes | 3.71 | 0 |
| SoliSpirit-all | 10830 | yes | 2.75 | 0 |
| Surfboard-tg-mixed | 8518 | yes | 2.86 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.35 | 0 |
| barry-far-vless | 6238 | yes | 1.23 | 0 |
| Surfboard-tg-vless | 5997 | yes | 3.3 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 0.76 | 0 |
| mahdibland-V2RayAggregator | 4608 | yes | 2.36 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.08 | 0 |
| DeltaKronecker-all | 2526 | yes | 4.75 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 63 |
| 204 | 26 |
| cn-block | 16 |
| geo | 4 |
| speed | 2 |
