# AutoNodes 每日报告

生成时间：2026-10-14 17:01:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 3/91 |
| 原始节点数 | 98394 |
| 去重后节点数 | 27341 |
| TCP 可达数 | 3000 |
| 真测通过数 | 63 |
| verified 输出数 | 63 |
| global 输出数 | 73 |
| all 输出数 | 27341 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 34.6 |
| fetch | 7.9 |
| generate | 13.3 |
| geo | 1.5 |
| probe | 107.7 |
| real_test | 70.5 |
| tcp | 89.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 27 | 1 | 96.4% |
| hysteria2 | 8 | 7 | 1 | 87.5% |
| shadowsocks | 127 | 106 | 21 | 83.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 8 | 2 | 6 | 25.0% |
| vless | 162 | 95 | 67 | 58.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 59 |
| geo:ClientOSError | 9 |
| speed:ClientOSError | 8 |
| cn-block:TimeoutError | 7 |
| 204:TimeoutError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |
| 204:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7503 |
| ConnectionRefusedError | 996 |
| OSError | 230 |
| gaierror | 51 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.915 | prefer | 20 | 0.95 | 144 |
| mheidari-all | 0.788 | prefer | 70 | 0.714 | 23968 |
| Au1rxx-base64 | 0.766 | prefer | 185 | 0.697 | 1780 |
| Surfboard-tg-mixed | 0.695 | observe | 50 | 0.62 | 7210 |
| ermaozi-get_subscribe | 0.57 | observe | 8 | 1.0 | 515 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7543 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 451 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 342 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 337 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 189 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 167 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 162 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 86 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.62 | 31 | 19 | 50 |
| Au1rxx-base64 | 0.697 | 129 | 56 | 185 |
| mheidari-all | 0.714 | 50 | 20 | 70 |
| zhangkai | 0.95 | 19 | 1 | 20 |
| ermaozi-get_subscribe | 1.0 | 8 | 0 | 8 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23968 | yes | 5.16 | 0 |
| SoliSpirit-all | 9997 | yes | 2.88 | 0 |
| Epodonios-all | 7543 | yes | 5.62 | 0 |
| Surfboard-tg-mixed | 7210 | yes | 7.35 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 5.16 | 0 |
| barry-far-vless | 5831 | yes | 4.44 | 0 |
| Surfboard-tg-vless | 5726 | yes | 4.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 4.23 | 0 |
| DeltaKronecker-all | 4803 | yes | 5.18 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 2.16 | 0 |

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
| test_one_timeout | 59 |
| cn-block | 14 |
| geo | 9 |
| speed | 8 |
| 204 | 7 |
