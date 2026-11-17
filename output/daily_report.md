# AutoNodes 每日报告

生成时间：2026-11-17 08:11:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83224 |
| 去重后节点数 | 27691 |
| TCP 可达数 | 3000 |
| 真测通过数 | 445 |
| verified 输出数 | 50 |
| global 输出数 | 300 |
| all 输出数 | 27691 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 34.3 |
| fetch | 4.4 |
| generate | 8.5 |
| geo | 1.3 |
| probe | 67.7 |
| real_test | 78.7 |
| tcp | 69.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 70 | 61 | 9 | 87.1% |
| hysteria2 | 11 | 9 | 2 | 81.8% |
| shadowsocks | 218 | 196 | 22 | 89.9% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 87 | 63 | 24 | 72.4% |
| vless | 161 | 116 | 45 | 72.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 60 |
| 204:ProxyError | 16 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| speed:ClientOSError | 2 |
| speed:ClientPayloadError | 1 |
| geo:ClientOSError | 1 |
| cn-block:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5814 |
| ConnectionRefusedError | 976 |
| gaierror | 358 |
| OSError | 354 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.898 | prefer | 245 | 0.82 | 8623 |
| mheidari-all | 0.892 | prefer | 78 | 0.821 | 14792 |
| ermaozi | 0.889 | prefer | 79 | 0.873 | 621 |
| Au1rxx-base64 | 0.832 | prefer | 141 | 0.766 | 1751 |
| Surfboard-tg-vless | 0.4 | observe | 4 | 0.75 | 6028 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| tg-LonUp_M | 0.327 | observe | 4 | 0.75 | 169 |
| Pawdroid | 0.255 | observe | 1 | 1.0 | 12 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4964 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2915 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 455 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 450 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 333 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 311 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 310 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 302 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 280 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 275 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.75 | 3 | 1 | 4 |
| Surfboard-tg-vless | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.766 | 108 | 33 | 141 |
| Surfboard-tg-mixed | 0.82 | 201 | 44 | 245 |
| mheidari-all | 0.821 | 64 | 14 | 78 |
| ermaozi | 0.873 | 69 | 10 | 79 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Pawdroid | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14792 | yes | 3.47 | 0 |
| SoliSpirit-all | 11532 | yes | 3.38 | 0 |
| Surfboard-tg-mixed | 8623 | yes | 2.29 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.3 | 0 |
| barry-far-vless | 6053 | yes | 0.7 | 0 |
| Surfboard-tg-vless | 6028 | yes | 2.45 | 0 |
| 10ium-ScrapeCategorize-Vless | 4964 | yes | 1.76 | 0 |
| mahdibland-V2RayAggregator | 4545 | yes | 0.15 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.77 | 0 |
| DeltaKronecker-all | 2915 | yes | 3.72 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 60 |
| 204 | 30 |
| cn-block | 8 |
| speed | 4 |
| geo | 1 |
