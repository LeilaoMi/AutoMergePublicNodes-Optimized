# AutoNodes 每日报告

生成时间：2026-11-08 13:43:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81840 |
| 去重后节点数 | 26970 |
| TCP 可达数 | 3000 |
| 真测通过数 | 447 |
| verified 输出数 | 68 |
| global 输出数 | 300 |
| all 输出数 | 26970 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.5 |
| fetch | 6.7 |
| generate | 14.5 |
| geo | 1.5 |
| probe | 97.5 |
| real_test | 73.2 |
| tcp | 76.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 55 | 55 | 0 | 100.0% |
| hysteria2 | 16 | 13 | 3 | 81.2% |
| shadowsocks | 211 | 198 | 13 | 93.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 112 | 84 | 28 | 75.0% |
| vless | 138 | 97 | 41 | 70.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 45 |
| 204:ProxyError | 16 |
| cn-block:ProxyError | 6 |
| cn-block:TimeoutError | 5 |
| 204:TimeoutError | 4 |
| geo:ProxyError | 3 |
| speed:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| speed:ClientOSError | 1 |
| speed:ProxyError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5883 |
| ConnectionRefusedError | 1029 |
| gaierror | 256 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 55 | 1.0 | 586 |
| Au1rxx-base64 | 0.903 | prefer | 219 | 0.836 | 1751 |
| Surfboard-tg-mixed | 0.89 | prefer | 172 | 0.814 | 8136 |
| mheidari-all | 0.871 | prefer | 84 | 0.798 | 14420 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 3024 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5035 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10990 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5786 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 430 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 425 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 308 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 286 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 285 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 277 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 255 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 250 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 174 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 161 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.798 | 67 | 17 | 84 |
| Surfboard-tg-mixed | 0.814 | 140 | 32 | 172 |
| Au1rxx-base64 | 0.836 | 183 | 36 | 219 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 55 | 0 | 55 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14420 | yes | 4.87 | 0 |
| SoliSpirit-all | 10990 | yes | 2.29 | 0 |
| Surfboard-tg-mixed | 8136 | yes | 4.35 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.08 | 0 |
| barry-far-vless | 5999 | yes | 1.13 | 0 |
| Surfboard-tg-vless | 5786 | yes | 3.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 5035 | yes | 0.79 | 0 |
| mahdibland-V2RayAggregator | 4635 | yes | 3.06 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.88 | 0 |
| DeltaKronecker-all | 3024 | yes | 5.98 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 45 |
| 204 | 22 |
| cn-block | 12 |
| speed | 4 |
| geo | 3 |
