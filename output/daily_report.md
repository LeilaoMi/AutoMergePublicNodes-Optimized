# AutoNodes 每日报告

生成时间：2026-11-12 07:29:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83686 |
| 去重后节点数 | 26699 |
| TCP 可达数 | 3000 |
| 真测通过数 | 429 |
| verified 输出数 | 79 |
| global 输出数 | 300 |
| all 输出数 | 26699 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 34.8 |
| fetch | 6.0 |
| generate | 11.1 |
| geo | 1.6 |
| probe | 86.0 |
| real_test | 75.0 |
| tcp | 83.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 72 | 71 | 1 | 98.6% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 204 | 178 | 26 | 87.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 109 | 87 | 22 | 79.8% |
| vless | 136 | 79 | 57 | 58.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 53 |
| 204:ProxyError | 19 |
| speed:ClientOSError | 8 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 4 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |
| geo:ClientOSError | 2 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6580 |
| ConnectionRefusedError | 950 |
| OSError | 234 |
| gaierror | 113 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.997 | prefer | 72 | 0.986 | 596 |
| Surfboard-tg-mixed | 0.901 | prefer | 143 | 0.825 | 8783 |
| Au1rxx-base64 | 0.871 | prefer | 199 | 0.804 | 1751 |
| mheidari-all | 0.735 | prefer | 117 | 0.658 | 14005 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| peasoft-NoMoreWalls | 0.26 | observe | 1 | 1.0 | 130 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4981 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2629 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11526 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 443 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 438 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 321 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 299 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 298 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 290 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 268 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 263 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 187 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 174 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.658 | 77 | 40 | 117 |
| Au1rxx-base64 | 0.804 | 160 | 39 | 199 |
| Surfboard-tg-mixed | 0.825 | 118 | 25 | 143 |
| ermaozi | 0.986 | 71 | 1 | 72 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| peasoft-NoMoreWalls | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14005 | yes | 3.04 | 0 |
| SoliSpirit-all | 11526 | yes | 2.65 | 0 |
| Surfboard-tg-mixed | 8783 | yes | 3.69 | 0 |
| barry-far-vless | 6775 | yes | 1.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.25 | 0 |
| Surfboard-tg-vless | 6596 | yes | 3.42 | 0 |
| 10ium-ScrapeCategorize-Vless | 4981 | yes | 0.91 | 0 |
| mahdibland-V2RayAggregator | 4595 | yes | 2.48 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.43 | 0 |
| DeltaKronecker-all | 2629 | yes | 2.76 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 53 |
| 204 | 27 |
| cn-block | 12 |
| speed | 9 |
| geo | 6 |
