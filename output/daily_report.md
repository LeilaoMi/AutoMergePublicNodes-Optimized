# AutoNodes 每日报告

生成时间：2026-11-18 07:47:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 5/84 |
| 原始节点数 | 81549 |
| 去重后节点数 | 27516 |
| TCP 可达数 | 3000 |
| 真测通过数 | 424 |
| verified 输出数 | 45 |
| global 输出数 | 300 |
| all 输出数 | 27516 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.7 |
| fetch | 5.8 |
| generate | 12.2 |
| geo | 1.5 |
| probe | 87.3 |
| real_test | 70.9 |
| tcp | 81.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 31 | 29 | 2 | 93.5% |
| hysteria2 | 12 | 10 | 2 | 83.3% |
| shadowsocks | 227 | 207 | 20 | 91.2% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 66 | 52 | 14 | 78.8% |
| vless | 180 | 126 | 54 | 70.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 56 |
| 204:ProxyError | 9 |
| cn-block:ProxyError | 6 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ClientOSError | 3 |
| geo:ProxyError | 2 |
| speed:ClientOSError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6331 |
| ConnectionRefusedError | 962 |
| gaierror | 250 |
| OSError | 238 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.957 | prefer | 144 | 0.882 | 8419 |
| mheidari-all | 0.892 | prefer | 174 | 0.816 | 14456 |
| ermaozi | 0.828 | prefer | 17 | 0.941 | 502 |
| Au1rxx-base64 | 0.819 | prefer | 161 | 0.752 | 1751 |
| tg-ShadowsocksM | 0.707 | prefer | 14 | 0.929 | 64 |
| tg-LonUp_M | 0.392 | observe | 7 | 0.714 | 166 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 2790 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4928 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| chromego_merge | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 457 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 452 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 335 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 313 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 312 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 304 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 282 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 277 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 188 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| tg-LonUp_M | 0.714 | 5 | 2 | 7 |
| Au1rxx-base64 | 0.752 | 121 | 40 | 161 |
| mheidari-all | 0.816 | 142 | 32 | 174 |
| Surfboard-tg-mixed | 0.882 | 127 | 17 | 144 |
| tg-ShadowsocksM | 0.929 | 13 | 1 | 14 |
| ermaozi | 0.941 | 16 | 1 | 17 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14456 | yes | 4.61 | 0 |
| SoliSpirit-all | 11512 | yes | 3.67 | 0 |
| Surfboard-tg-mixed | 8419 | yes | 3.22 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.87 | 0 |
| barry-far-vless | 5907 | yes | 1.51 | 0 |
| Surfboard-tg-vless | 5726 | yes | 2.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 4928 | yes | 2.15 | 0 |
| mahdibland-V2RayAggregator | 4458 | yes | 0.16 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.24 | 0 |
| DeltaKronecker-all | 2790 | yes | 5.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 56 |
| 204 | 16 |
| cn-block | 15 |
| geo | 5 |
| speed | 2 |
