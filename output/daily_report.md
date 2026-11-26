# AutoNodes 每日报告

生成时间：2026-11-26 08:40:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 85/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 78785 |
| 去重后节点数 | 27338 |
| TCP 可达数 | 3000 |
| 真测通过数 | 320 |
| verified 输出数 | 54 |
| global 输出数 | 300 |
| all 输出数 | 27338 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.2 |
| fetch | 4.7 |
| generate | 11.2 |
| geo | 1.4 |
| probe | 78.0 |
| real_test | 63.5 |
| tcp | 80.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 4 | 1 | 80.0% |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 8 | 7 | 1 | 87.5% |
| shadowsocks | 217 | 189 | 28 | 87.1% |
| socks | 7 | 7 | 0 | 100.0% |
| trojan | 45 | 15 | 30 | 33.3% |
| vless | 130 | 85 | 45 | 65.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 45 |
| 204:ProxyError | 28 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| geo:ProxyError | 3 |
| speed:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6863 |
| ConnectionRefusedError | 1036 |
| OSError | 243 |
| gaierror | 214 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.975 | prefer | 22 | 1.0 | 406 |
| Au1rxx-base64 | 0.831 | prefer | 136 | 0.765 | 1751 |
| mheidari-all | 0.83 | prefer | 58 | 0.759 | 14817 |
| Surfboard-tg-mixed | 0.805 | prefer | 209 | 0.727 | 8442 |
| ermaozi-get_subscribe | 0.381 | observe | 5 | 0.8 | 363 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11584 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5447 |
| barry-far-vless | 0.255 | observe | 0 | None | 5694 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 473 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 468 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 351 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 329 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 328 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 320 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 298 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.727 | 152 | 57 | 209 |
| mheidari-all | 0.759 | 44 | 14 | 58 |
| Au1rxx-base64 | 0.765 | 104 | 32 | 136 |
| ermaozi-get_subscribe | 0.8 | 4 | 1 | 5 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14817 | yes | 2.57 | 0 |
| SoliSpirit-all | 11584 | yes | 1.36 | 0 |
| Surfboard-tg-mixed | 8442 | yes | 4.15 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.9 | 0 |
| barry-far-vless | 5694 | yes | 0.76 | 0 |
| Surfboard-tg-vless | 5447 | yes | 2.97 | 0 |
| 10ium-ScrapeCategorize-Vless | 4958 | yes | 1.04 | 0 |
| mahdibland-V2RayAggregator | 4485 | yes | 0.49 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.54 | 0 |
| ninja-vless | 1791 | yes | 2.24 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 45 |
| 204 | 41 |
| cn-block | 13 |
| geo | 3 |
| speed | 3 |
