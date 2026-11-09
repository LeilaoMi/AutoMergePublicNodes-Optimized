# AutoNodes 每日报告

生成时间：2026-11-09 23:33:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 81722 |
| 去重后节点数 | 26721 |
| TCP 可达数 | 3000 |
| 真测通过数 | 481 |
| verified 输出数 | 49 |
| global 输出数 | 300 |
| all 输出数 | 26721 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 18.6 |
| fetch | 7.0 |
| generate | 14.2 |
| geo | 1.5 |
| probe | 97.4 |
| real_test | 81.2 |
| tcp | 79.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 19 | 18 | 1 | 94.7% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 219 | 208 | 11 | 95.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 128 | 116 | 12 | 90.6% |
| vless | 193 | 126 | 67 | 65.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 56 |
| 204:ProxyError | 8 |
| cn-block:TimeoutError | 6 |
| 204:TimeoutError | 5 |
| speed:ClientOSError | 5 |
| speed:TimeoutError | 3 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 2 |
| geo:ClientOSError | 2 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |
| cn-block:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6502 |
| ConnectionRefusedError | 977 |
| OSError | 239 |
| gaierror | 111 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.935 | prefer | 198 | 0.859 | 8250 |
| ermaozi | 0.93 | prefer | 20 | 0.95 | 518 |
| mheidari-all | 0.923 | prefer | 106 | 0.849 | 14061 |
| Au1rxx-base64 | 0.88 | prefer | 245 | 0.812 | 1751 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 2754 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11213 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6133 |

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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 435 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 430 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 313 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 291 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 290 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 282 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 260 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 255 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 179 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 166 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.812 | 199 | 46 | 245 |
| mheidari-all | 0.849 | 90 | 16 | 106 |
| Surfboard-tg-mixed | 0.859 | 170 | 28 | 198 |
| ermaozi | 0.95 | 19 | 1 | 20 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14061 | yes | 6.1 | 0 |
| SoliSpirit-all | 11213 | yes | 2.66 | 0 |
| Surfboard-tg-mixed | 8250 | yes | 4.12 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.14 | 0 |
| Surfboard-tg-vless | 6133 | yes | 4.33 | 0 |
| barry-far-vless | 6103 | yes | 0.78 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 0.55 | 0 |
| mahdibland-V2RayAggregator | 4583 | yes | 3.05 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.87 | 0 |
| DeltaKronecker-all | 2754 | yes | 6.06 | 0 |

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
| test_one_timeout | 56 |
| 204 | 14 |
| cn-block | 12 |
| speed | 9 |
| geo | 2 |
