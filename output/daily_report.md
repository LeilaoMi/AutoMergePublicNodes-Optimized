# AutoNodes 每日报告

生成时间：2026-10-17 04:45:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/1 |
| 清理建议：优先/观察 | 2/90 |
| 原始节点数 | 99687 |
| 去重后节点数 | 27779 |
| TCP 可达数 | 3000 |
| 真测通过数 | 536 |
| verified 输出数 | 145 |
| global 输出数 | 300 |
| all 输出数 | 27779 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.8 |
| fetch | 7.8 |
| generate | 14.1 |
| geo | 1.5 |
| probe | 92.8 |
| real_test | 99.9 |
| tcp | 85.4 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 99 | 95 | 4 | 96.0% |
| hysteria2 | 17 | 16 | 1 | 94.1% |
| shadowsocks | 161 | 151 | 10 | 93.8% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 43 | 39 | 4 | 90.7% |
| vless | 414 | 233 | 181 | 56.3% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 124 |
| geo:ClientOSError | 31 |
| speed:ClientOSError | 17 |
| 204:TimeoutError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| cn-block:TimeoutError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6556 |
| ConnectionRefusedError | 1036 |
| gaierror | 246 |
| OSError | 235 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | prefer | 100 | 0.98 | 702 |
| Au1rxx-base64 | 0.916 | prefer | 488 | 0.838 | 1993 |
| Surfboard-tg-mixed | 0.446 | observe | 8 | 0.625 | 7128 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 4946 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| peasoft-NoMoreWalls | 0.261 | observe | 1 | 1.0 | 139 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1993 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.108 | observe | 2 | 0.0 | 0 | 104 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 468 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 359 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 354 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 179 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 103 | 连续死亡次数 >= 2 |
| downweight | mheidari-all | 0.248 | 135 | 0.163 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.163 | 22 | 113 | 135 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.625 | 5 | 3 | 8 |
| Au1rxx-base64 | 0.838 | 409 | 79 | 488 |
| ermaozi | 0.98 | 98 | 2 | 100 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| peasoft-NoMoreWalls | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24092 | yes | 7.58 | 0 |
| SoliSpirit-all | 10040 | yes | 3.35 | 0 |
| Epodonios-all | 7630 | yes | 5.74 | 0 |
| Surfboard-tg-mixed | 7128 | yes | 4.29 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.37 | 0 |
| barry-far-vless | 5847 | yes | 1.93 | 0 |
| Surfboard-tg-vless | 5602 | yes | 6.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 1.71 | 0 |
| DeltaKronecker-all | 4946 | yes | 3.73 | 0 |
| mahdibland-V2RayAggregator | 4255 | yes | 2.88 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 124 |
| geo | 33 |
| speed | 18 |
| 204 | 14 |
| cn-block | 12 |
