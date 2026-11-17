# AutoNodes 每日报告

生成时间：2026-11-17 21:10:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82265 |
| 去重后节点数 | 27554 |
| TCP 可达数 | 3000 |
| 真测通过数 | 392 |
| verified 输出数 | 48 |
| global 输出数 | 300 |
| all 输出数 | 27554 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.2 |
| fetch | 7.2 |
| generate | 16.2 |
| geo | 1.6 |
| probe | 96.7 |
| real_test | 75.0 |
| tcp | 81.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 10 | 9 | 1 | 90.0% |
| shadowsocks | 224 | 206 | 18 | 92.0% |
| trojan | 88 | 55 | 33 | 62.5% |
| vless | 161 | 100 | 61 | 62.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 50 |
| 204:ProxyError | 30 |
| cn-block:ProxyError | 8 |
| 204:TimeoutError | 8 |
| geo:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6259 |
| ConnectionRefusedError | 969 |
| OSError | 241 |
| gaierror | 229 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.977 | prefer | 21 | 1.0 | 517 |
| mheidari-all | 0.927 | prefer | 83 | 0.855 | 14572 |
| Surfboard-tg-mixed | 0.85 | prefer | 224 | 0.772 | 8416 |
| Au1rxx-base64 | 0.774 | prefer | 167 | 0.707 | 1751 |
| tg-LonUp_M | 0.456 | observe | 7 | 0.857 | 171 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2790 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| tg-ShadowsocksM | 0.258 | observe | 1 | 1.0 | 64 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4928 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 456 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 451 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 334 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 312 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 311 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 303 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 281 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 276 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 187 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.707 | 118 | 49 | 167 |
| Surfboard-tg-mixed | 0.772 | 173 | 51 | 224 |
| mheidari-all | 0.855 | 71 | 12 | 83 |
| tg-LonUp_M | 0.857 | 6 | 1 | 7 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-ShadowsocksM | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 21 | 0 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14572 | yes | 6.39 | 0 |
| SoliSpirit-all | 11534 | yes | 2.73 | 0 |
| Surfboard-tg-mixed | 8416 | yes | 5.29 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.66 | 0 |
| barry-far-vless | 6032 | yes | 0.81 | 0 |
| Surfboard-tg-vless | 5789 | yes | 3.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 4928 | yes | 1.9 | 0 |
| mahdibland-V2RayAggregator | 4601 | yes | 3.2 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.99 | 0 |
| DeltaKronecker-all | 2790 | yes | 6.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 50 |
| 204 | 40 |
| cn-block | 14 |
| geo | 6 |
| speed | 3 |
