# AutoNodes 每日报告

生成时间：2026-11-15 19:03:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 84509 |
| 去重后节点数 | 27682 |
| TCP 可达数 | 3000 |
| 真测通过数 | 339 |
| verified 输出数 | 44 |
| global 输出数 | 300 |
| all 输出数 | 27682 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 42.8 |
| fetch | 6.9 |
| generate | 14.7 |
| geo | 1.5 |
| probe | 95.5 |
| real_test | 65.8 |
| tcp | 76.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 222 | 188 | 34 | 84.7% |
| socks | 3 | 3 | 0 | 100.0% |
| trojan | 49 | 19 | 30 | 38.8% |
| vless | 130 | 96 | 34 | 73.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 47 |
| 204:ProxyError | 23 |
| 204:TimeoutError | 10 |
| cn-block:ProxyError | 6 |
| 204:ClientOSError | 4 |
| speed:ClientOSError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |
| cn-block:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5967 |
| ConnectionRefusedError | 980 |
| gaierror | 270 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.942 | prefer | 23 | 0.957 | 544 |
| mheidari-all | 0.887 | prefer | 55 | 0.818 | 14826 |
| Au1rxx-base64 | 0.832 | prefer | 128 | 0.766 | 1751 |
| Surfboard-tg-mixed | 0.827 | prefer | 235 | 0.749 | 9142 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4916 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3024 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11885 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6162 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 452 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 447 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 330 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 308 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 307 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 299 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 277 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 272 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.749 | 176 | 59 | 235 |
| Au1rxx-base64 | 0.766 | 98 | 30 | 128 |
| mheidari-all | 0.818 | 45 | 10 | 55 |
| ermaozi | 0.957 | 22 | 1 | 23 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14826 | yes | 5.6 | 0 |
| SoliSpirit-all | 11885 | yes | 3.29 | 0 |
| Surfboard-tg-mixed | 9142 | yes | 4.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.08 | 0 |
| barry-far-vless | 6310 | yes | 0.82 | 0 |
| Surfboard-tg-vless | 6162 | yes | 3.98 | 0 |
| 10ium-ScrapeCategorize-Vless | 4916 | yes | 0.58 | 0 |
| mahdibland-V2RayAggregator | 4584 | yes | 2.99 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.17 | 0 |
| DeltaKronecker-all | 3024 | yes | 4.9 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 47 |
| 204 | 37 |
| cn-block | 8 |
| speed | 6 |
| geo | 2 |
