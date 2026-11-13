# AutoNodes 每日报告

生成时间：2026-11-13 19:56:57

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83309 |
| 去重后节点数 | 26903 |
| TCP 可达数 | 3000 |
| 真测通过数 | 393 |
| verified 输出数 | 89 |
| global 输出数 | 300 |
| all 输出数 | 26903 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.2 |
| fetch | 4.1 |
| generate | 9.4 |
| geo | 1.4 |
| probe | 71.2 |
| real_test | 71.6 |
| tcp | 82.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 56 | 55 | 1 | 98.2% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 206 | 174 | 32 | 84.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 49 | 30 | 19 | 61.2% |
| vless | 197 | 120 | 77 | 60.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 49 |
| 204:ProxyError | 28 |
| speed:ClientOSError | 27 |
| 204:TimeoutError | 8 |
| cn-block:TimeoutError | 5 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |
| geo:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6433 |
| ConnectionRefusedError | 943 |
| OSError | 235 |
| gaierror | 181 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.989 | prefer | 56 | 0.982 | 590 |
| Au1rxx-base64 | 0.818 | prefer | 153 | 0.752 | 1751 |
| Surfboard-tg-mixed | 0.799 | prefer | 226 | 0.721 | 8804 |
| mheidari-all | 0.767 | prefer | 81 | 0.691 | 14267 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| ermaozi-get_subscribe | 0.273 | observe | 1 | 1.0 | 442 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4900 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2734 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 175 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 447 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 442 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 325 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 303 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 302 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 294 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 272 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 267 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 178 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.691 | 56 | 25 | 81 |
| Surfboard-tg-mixed | 0.721 | 163 | 63 | 226 |
| Au1rxx-base64 | 0.752 | 115 | 38 | 153 |
| ermaozi | 0.982 | 55 | 1 | 56 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14267 | yes | 2.61 | 0 |
| SoliSpirit-all | 11528 | yes | 2.42 | 0 |
| Surfboard-tg-mixed | 8804 | yes | 1.79 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.68 | 0 |
| barry-far-vless | 6409 | yes | 1.5 | 0 |
| Surfboard-tg-vless | 6228 | yes | 2.26 | 0 |
| 10ium-ScrapeCategorize-Vless | 4900 | yes | 1.33 | 0 |
| mahdibland-V2RayAggregator | 4624 | yes | 0.12 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.66 | 0 |
| DeltaKronecker-all | 2734 | yes | 3.32 | 0 |

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
| test_one_timeout | 49 |
| 204 | 39 |
| speed | 30 |
| cn-block | 9 |
| geo | 3 |
