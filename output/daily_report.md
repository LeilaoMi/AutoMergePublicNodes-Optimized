# AutoNodes 每日报告

生成时间：2026-10-30 22:34:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 80795 |
| 去重后节点数 | 26300 |
| TCP 可达数 | 3000 |
| 真测通过数 | 546 |
| verified 输出数 | 107 |
| global 输出数 | 300 |
| all 输出数 | 26300 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.5 |
| fetch | 6.0 |
| generate | 11.8 |
| geo | 1.5 |
| probe | 82.7 |
| real_test | 89.6 |
| tcp | 77.0 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 3 | 0 | 100.0% |
| http | 29 | 28 | 1 | 96.6% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 177 | 158 | 19 | 89.3% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 181 | 175 | 6 | 96.7% |
| vless | 248 | 169 | 79 | 68.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 55 |
| geo:ClientOSError | 16 |
| cn-block:ClientOSError | 13 |
| 204:TimeoutError | 6 |
| geo:ProxyError | 4 |
| 204:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| speed:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ClientConnectionResetError | 1 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5935 |
| ConnectionRefusedError | 932 |
| OSError | 235 |
| gaierror | 173 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.957 | prefer | 29 | 0.966 | 550 |
| Au1rxx-base64 | 0.951 | prefer | 341 | 0.883 | 1751 |
| Surfboard-tg-mixed | 0.863 | prefer | 164 | 0.787 | 7917 |
| mheidari-all | 0.813 | prefer | 114 | 0.737 | 14611 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.328 | observe | 2 | 1.0 | 430 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2724 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 517 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 408 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 403 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 286 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 264 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 263 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 255 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 152 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.737 | 84 | 30 | 114 |
| Surfboard-tg-mixed | 0.787 | 129 | 35 | 164 |
| Au1rxx-base64 | 0.883 | 301 | 40 | 341 |
| ermaozi | 0.966 | 28 | 1 | 29 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14611 | yes | 3.63 | 0 |
| SoliSpirit-all | 10557 | yes | 2.53 | 0 |
| Surfboard-tg-mixed | 7917 | yes | 3.19 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.11 | 0 |
| barry-far-vless | 6013 | yes | 1.13 | 0 |
| Surfboard-tg-vless | 5777 | yes | 1.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 1.45 | 0 |
| mahdibland-V2RayAggregator | 4459 | yes | 2.82 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.25 | 0 |
| DeltaKronecker-all | 2724 | yes | 5.44 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 55 |
| geo | 20 |
| cn-block | 17 |
| 204 | 10 |
| speed | 4 |
