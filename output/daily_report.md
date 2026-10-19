# AutoNodes 每日报告

生成时间：2026-10-19 04:59:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 97393 |
| 去重后节点数 | 27778 |
| TCP 可达数 | 3000 |
| 真测通过数 | 511 |
| verified 输出数 | 118 |
| global 输出数 | 300 |
| all 输出数 | 27778 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.9 |
| fetch | 7.9 |
| generate | 14.6 |
| geo | 1.5 |
| probe | 94.1 |
| real_test | 100.9 |
| tcp | 86.3 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 99 | 98 | 1 | 99.0% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 147 | 133 | 14 | 90.5% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 49 | 42 | 7 | 85.7% |
| vless | 369 | 219 | 150 | 59.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 117 |
| geo:ClientOSError | 19 |
| speed:ClientOSError | 15 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 4 |
| 204:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 1 |
| 204:TimeoutError | 1 |
| geo:ProxyError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7085 |
| ConnectionRefusedError | 1033 |
| gaierror | 351 |
| OSError | 238 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | prefer | 101 | 0.98 | 696 |
| Au1rxx-base64 | 0.918 | prefer | 436 | 0.851 | 1726 |
| DeltaKronecker-all | 0.557 | observe | 6 | 1.0 | 4750 |
| Surfboard-tg-mixed | 0.489 | observe | 6 | 0.833 | 7003 |
| mheidari-all | 0.323 | observe | 134 | 0.239 | 23518 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7467 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9822 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Pawdroid | 0.105 | observe | 2 | 0.0 | 0 | 20 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 476 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 367 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 362 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 245 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 223 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 187 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 111 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 2 | 2 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.239 | 32 | 102 | 134 |
| Surfboard-tg-mixed | 0.833 | 5 | 1 | 6 |
| Au1rxx-base64 | 0.851 | 371 | 65 | 436 |
| ermaozi | 0.98 | 99 | 2 | 101 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 6 | 0 | 6 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23518 | yes | 5.14 | 0 |
| SoliSpirit-all | 9822 | yes | 3.58 | 0 |
| Epodonios-all | 7467 | yes | 6.3 | 0 |
| Surfboard-tg-mixed | 7003 | yes | 3.91 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.31 | 0 |
| barry-far-vless | 5700 | yes | 1.03 | 0 |
| Surfboard-tg-vless | 5523 | yes | 4.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4983 | yes | 2.61 | 0 |
| DeltaKronecker-all | 4750 | yes | 4.58 | 0 |
| mahdibland-V2RayAggregator | 4246 | yes | 3.54 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 117 |
| geo | 23 |
| speed | 16 |
| 204 | 10 |
| cn-block | 8 |
