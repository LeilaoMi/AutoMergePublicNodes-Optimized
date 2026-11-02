# AutoNodes 每日报告

生成时间：2026-11-02 06:30:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 2/88 |
| 原始节点数 | 82989 |
| 去重后节点数 | 26848 |
| TCP 可达数 | 3000 |
| 真测通过数 | 369 |
| verified 输出数 | 41 |
| global 输出数 | 300 |
| all 输出数 | 26848 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.0 |
| fetch | 5.5 |
| generate | 11.2 |
| geo | 1.5 |
| probe | 81.2 |
| real_test | 81.5 |
| tcp | 81.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 18 | 18 | 0 | 100.0% |
| hysteria2 | 16 | 13 | 3 | 81.2% |
| shadowsocks | 115 | 108 | 7 | 93.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 102 | 94 | 8 | 92.2% |
| vless | 304 | 136 | 168 | 44.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 74 |
| geo:ClientOSError | 57 |
| 204:ProxyError | 16 |
| cn-block:ProxyError | 9 |
| cn-block:TimeoutError | 8 |
| geo:ProxyError | 6 |
| 204:TimeoutError | 6 |
| speed:ClientOSError | 6 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6187 |
| ConnectionRefusedError | 934 |
| OSError | 232 |
| gaierror | 134 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.89 | prefer | 18 | 1.0 | 43 |
| Au1rxx-base64 | 0.87 | prefer | 308 | 0.802 | 1751 |
| mheidari-all | 0.521 | observe | 220 | 0.441 | 15216 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| Surfboard-tg-mixed | 0.352 | observe | 6 | 0.5 | 8273 |
| xiaoji235-airport-v2ray-all | 0.32 | observe | 4 | 0.5 | 6752 |
| ermaozi-get_subscribe | 0.277 | observe | 1 | 1.0 | 547 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3716 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 415 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 410 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 270 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 262 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 159 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 146 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.441 | 97 | 123 | 220 |
| xiaoji235-airport-v2ray-all | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.5 | 3 | 3 | 6 |
| Au1rxx-base64 | 0.802 | 247 | 61 | 308 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 18 | 0 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15216 | yes | 3.83 | 0 |
| SoliSpirit-all | 10657 | yes | 1.06 | 0 |
| Surfboard-tg-mixed | 8273 | yes | 4.02 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.31 | 0 |
| barry-far-vless | 6036 | yes | 0.58 | 0 |
| Surfboard-tg-vless | 5823 | yes | 2.7 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 0.75 | 0 |
| mahdibland-V2RayAggregator | 4726 | yes | 2.46 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.81 | 0 |
| DeltaKronecker-all | 3716 | yes | 4.4 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 74 |
| geo | 63 |
| 204 | 23 |
| cn-block | 21 |
| speed | 8 |
