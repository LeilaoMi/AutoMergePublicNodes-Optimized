# AutoNodes 每日报告

生成时间：2026-11-18 20:46:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82675 |
| 去重后节点数 | 27633 |
| TCP 可达数 | 3000 |
| 真测通过数 | 361 |
| verified 输出数 | 35 |
| global 输出数 | 300 |
| all 输出数 | 27633 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 37.4 |
| fetch | 5.2 |
| generate | 9.1 |
| geo | 1.4 |
| probe | 69.1 |
| real_test | 71.9 |
| tcp | 69.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 222 | 201 | 21 | 90.5% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 57 | 28 | 29 | 49.1% |
| vless | 161 | 104 | 57 | 64.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 57 |
| 204:ProxyError | 27 |
| 204:TimeoutError | 7 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| cn-block:TimeoutError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |
| 204:ClientOSError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5770 |
| ConnectionRefusedError | 1024 |
| gaierror | 421 |
| OSError | 357 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.975 | prefer | 20 | 1.0 | 508 |
| mheidari-all | 0.889 | prefer | 87 | 0.816 | 14408 |
| Surfboard-tg-mixed | 0.823 | prefer | 247 | 0.745 | 8521 |
| Au1rxx-base64 | 0.82 | prefer | 114 | 0.754 | 1751 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 11959 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4919 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2925 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5794 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 168 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 458 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 453 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 336 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 314 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 313 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 305 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 283 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 278 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 189 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.745 | 184 | 63 | 247 |
| Au1rxx-base64 | 0.754 | 86 | 28 | 114 |
| mheidari-all | 0.816 | 71 | 16 | 87 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14408 | yes | 3.46 | 0 |
| SoliSpirit-all | 11959 | yes | 3.34 | 0 |
| Surfboard-tg-mixed | 8521 | yes | 2.6 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.4 | 0 |
| barry-far-vless | 5945 | yes | 0.5 | 0 |
| Surfboard-tg-vless | 5794 | yes | 2.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 4919 | yes | 0.37 | 0 |
| mahdibland-V2RayAggregator | 4458 | yes | 1.78 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.71 | 0 |
| DeltaKronecker-all | 2925 | yes | 3.26 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 57 |
| 204 | 35 |
| cn-block | 11 |
| geo | 3 |
| speed | 2 |
