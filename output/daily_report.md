# AutoNodes 每日报告

生成时间：2026-11-05 20:10:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82601 |
| 去重后节点数 | 26726 |
| TCP 可达数 | 3000 |
| 真测通过数 | 402 |
| verified 输出数 | 34 |
| global 输出数 | 300 |
| all 输出数 | 26726 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.8 |
| fetch | 4.7 |
| generate | 8.8 |
| geo | 1.5 |
| probe | 73.0 |
| real_test | 73.1 |
| tcp | 80.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 64 | 62 | 2 | 96.9% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 205 | 185 | 20 | 90.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 82 | 42 | 40 | 51.2% |
| vless | 163 | 100 | 63 | 61.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 53 |
| test_one_timeout:15.0s | 50 |
| cn-block:ClientOSError | 6 |
| cn-block:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6307 |
| ConnectionRefusedError | 978 |
| OSError | 234 |
| gaierror | 129 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.993 | prefer | 63 | 0.984 | 593 |
| mheidari-all | 0.942 | prefer | 107 | 0.869 | 14461 |
| Surfboard-tg-mixed | 0.771 | prefer | 134 | 0.694 | 8690 |
| Au1rxx-base64 | 0.756 | prefer | 218 | 0.688 | 1751 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2653 |
| peasoft-NoMoreWalls | 0.259 | observe | 1 | 1.0 | 96 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5039 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10977 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.133 | observe | 1 | 0.0 | 0 | 140 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 423 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 418 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 301 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 279 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 278 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 270 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 248 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 167 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 154 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.333 | 1 | 2 | 3 |
| Au1rxx-base64 | 0.688 | 150 | 68 | 218 |
| Surfboard-tg-mixed | 0.694 | 93 | 41 | 134 |
| mheidari-all | 0.869 | 93 | 14 | 107 |
| ermaozi | 0.984 | 62 | 1 | 63 |
| peasoft-NoMoreWalls | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14461 | yes | 3.85 | 0 |
| SoliSpirit-all | 10977 | yes | 1.87 | 0 |
| Surfboard-tg-mixed | 8690 | yes | 3.2 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 0.9 | 0 |
| barry-far-vless | 6358 | yes | 0.36 | 0 |
| Surfboard-tg-vless | 6065 | yes | 4.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 5039 | yes | 1.37 | 0 |
| mahdibland-V2RayAggregator | 4612 | yes | 1.71 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.95 | 0 |
| DeltaKronecker-all | 2653 | yes | 3.9 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 59 |
| test_one_timeout | 50 |
| cn-block | 17 |
| speed | 1 |
| geo | 1 |
