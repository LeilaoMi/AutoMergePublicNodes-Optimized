# AutoNodes 每日报告

生成时间：2026-11-08 22:21:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81580 |
| 去重后节点数 | 26785 |
| TCP 可达数 | 3000 |
| 真测通过数 | 494 |
| verified 输出数 | 84 |
| global 输出数 | 300 |
| all 输出数 | 26785 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 34.3 |
| fetch | 5.2 |
| generate | 11.3 |
| geo | 1.5 |
| probe | 80.3 |
| real_test | 75.6 |
| tcp | 81.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 57 | 56 | 1 | 98.2% |
| hysteria2 | 14 | 11 | 3 | 78.6% |
| shadowsocks | 223 | 206 | 17 | 92.4% |
| trojan | 123 | 109 | 14 | 88.6% |
| vless | 164 | 112 | 52 | 68.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 50 |
| 204:ProxyError | 13 |
| speed:TimeoutError | 8 |
| cn-block:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| 204:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6367 |
| ConnectionRefusedError | 1013 |
| OSError | 235 |
| gaierror | 144 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.99 | prefer | 57 | 0.982 | 586 |
| mheidari-all | 0.964 | prefer | 93 | 0.892 | 13955 |
| Surfboard-tg-mixed | 0.917 | prefer | 194 | 0.84 | 8189 |
| Au1rxx-base64 | 0.875 | prefer | 234 | 0.808 | 1751 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5035 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3024 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10983 |

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
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 431 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 426 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 309 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 287 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 286 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 278 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 256 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 251 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 175 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 162 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.808 | 189 | 45 | 234 |
| Surfboard-tg-mixed | 0.84 | 163 | 31 | 194 |
| mheidari-all | 0.892 | 83 | 10 | 93 |
| ermaozi | 0.982 | 56 | 1 | 57 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13955 | yes | 4.48 | 0 |
| SoliSpirit-all | 10983 | yes | 2.88 | 0 |
| Surfboard-tg-mixed | 8189 | yes | 2.93 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.52 | 0 |
| barry-far-vless | 6123 | yes | 1.91 | 0 |
| Surfboard-tg-vless | 5913 | yes | 2.7 | 0 |
| 10ium-ScrapeCategorize-Vless | 5035 | yes | 1.36 | 0 |
| mahdibland-V2RayAggregator | 4597 | yes | 2.27 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.98 | 0 |
| DeltaKronecker-all | 3024 | yes | 4.45 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 50 |
| 204 | 17 |
| speed | 8 |
| cn-block | 8 |
| geo | 4 |
