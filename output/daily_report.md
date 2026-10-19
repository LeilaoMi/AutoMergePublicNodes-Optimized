# AutoNodes 每日报告

生成时间：2026-10-19 13:42:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 95109 |
| 去重后节点数 | 26270 |
| TCP 可达数 | 3000 |
| 真测通过数 | 394 |
| verified 输出数 | 71 |
| global 输出数 | 300 |
| all 输出数 | 26270 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 20.5 |
| fetch | 7.3 |
| generate | 14.0 |
| geo | 1.5 |
| probe | 99.6 |
| real_test | 86.4 |
| tcp | 80.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 39 | 36 | 3 | 92.3% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 149 | 127 | 22 | 85.2% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 28 | 21 | 7 | 75.0% |
| vless | 357 | 197 | 160 | 55.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 85 |
| speed:ClientOSError | 42 |
| geo:ClientOSError | 31 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 8 |
| cn-block:TimeoutError | 8 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 3 |
| speed:TimeoutError | 2 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6488 |
| ConnectionRefusedError | 1034 |
| OSError | 240 |
| gaierror | 215 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | prefer | 19 | 1.0 | 144 |
| Au1rxx-base64 | 0.868 | prefer | 362 | 0.801 | 1717 |
| ermaozi-get_subscribe | 0.815 | prefer | 18 | 0.889 | 508 |
| Surfboard-tg-mixed | 0.641 | observe | 55 | 0.564 | 6948 |
| ermaozi | 0.441 | observe | 5 | 1.0 | 42 |
| mheidari-all | 0.373 | observe | 5 | 0.6 | 23446 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4940 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 167 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| DeltaKronecker-all | 0.31 | observe | 120 | 0.225 | 3294 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 12 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-PrivateVPNs | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 477 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 368 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 363 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 246 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 224 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 223 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 188 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 112 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.225 | 27 | 93 | 120 |
| Surfboard-tg-mixed | 0.564 | 31 | 24 | 55 |
| mheidari-all | 0.6 | 3 | 2 | 5 |
| Au1rxx-base64 | 0.801 | 290 | 72 | 362 |
| ermaozi-get_subscribe | 0.889 | 16 | 2 | 18 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23446 | yes | 5.38 | 0 |
| SoliSpirit-all | 10136 | yes | 3.99 | 0 |
| Epodonios-all | 7331 | yes | 5.9 | 0 |
| Surfboard-tg-mixed | 6948 | yes | 3.79 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.57 | 0 |
| barry-far-vless | 5622 | yes | 0.9 | 0 |
| Surfboard-tg-vless | 5438 | yes | 4.02 | 0 |
| 10ium-ScrapeCategorize-Vless | 4940 | yes | 4.99 | 0 |
| mahdibland-V2RayAggregator | 4314 | yes | 0.78 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.99 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 85 |
| speed | 44 |
| geo | 32 |
| 204 | 20 |
| cn-block | 14 |
