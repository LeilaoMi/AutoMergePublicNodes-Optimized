# AutoNodes 每日报告

生成时间：2026-11-01 18:04:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 89/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 3/87 |
| 原始节点数 | 82878 |
| 去重后节点数 | 26787 |
| TCP 可达数 | 3000 |
| 真测通过数 | 388 |
| verified 输出数 | 82 |
| global 输出数 | 300 |
| all 输出数 | 26787 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.1 |
| fetch | 4.4 |
| generate | 9.8 |
| geo | 1.4 |
| probe | 71.0 |
| real_test | 81.6 |
| tcp | 78.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 74 | 73 | 1 | 98.6% |
| hysteria2 | 14 | 11 | 3 | 78.6% |
| shadowsocks | 143 | 129 | 14 | 90.2% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 97 | 66 | 31 | 68.0% |
| vless | 242 | 108 | 134 | 44.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 80 |
| geo:ClientOSError | 58 |
| 204:ProxyError | 15 |
| 204:TimeoutError | 7 |
| cn-block:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 4 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6090 |
| ConnectionRefusedError | 954 |
| OSError | 238 |
| gaierror | 155 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.985 | prefer | 55 | 0.982 | 499 |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 43 |
| Au1rxx-base64 | 0.804 | prefer | 284 | 0.736 | 1751 |
| Surfboard-tg-mixed | 0.66 | observe | 117 | 0.581 | 8239 |
| mheidari-all | 0.465 | observe | 94 | 0.383 | 15458 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3716 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10659 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 171 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 413 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 408 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 291 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 269 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 268 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 260 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 157 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 144 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.383 | 36 | 58 | 94 |
| Surfboard-tg-mixed | 0.581 | 68 | 49 | 117 |
| Au1rxx-base64 | 0.736 | 209 | 75 | 284 |
| ermaozi-get_subscribe | 0.982 | 54 | 1 | 55 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15458 | yes | 3.61 | 0 |
| SoliSpirit-all | 10659 | yes | 2.88 | 0 |
| Surfboard-tg-mixed | 8239 | yes | 2.53 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.34 | 0 |
| barry-far-vless | 5873 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 5773 | yes | 2.26 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 1.66 | 0 |
| mahdibland-V2RayAggregator | 4680 | yes | 0.68 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.7 | 0 |
| DeltaKronecker-all | 3716 | yes | 3.45 | 0 |

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
| test_one_timeout | 80 |
| geo | 62 |
| 204 | 26 |
| cn-block | 15 |
| speed | 1 |
