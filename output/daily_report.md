# AutoNodes 每日报告

生成时间：2026-10-14 21:33:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 4/90 |
| 原始节点数 | 98750 |
| 去重后节点数 | 27406 |
| TCP 可达数 | 3000 |
| 真测通过数 | 69 |
| verified 输出数 | 69 |
| global 输出数 | 74 |
| all 输出数 | 27406 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 31.3 |
| fetch | 4.6 |
| generate | 8.6 |
| geo | 1.6 |
| probe | 89.0 |
| real_test | 67.0 |
| tcp | 86.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 131 | 124 | 7 | 94.7% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 4 | 2 | 2 | 50.0% |
| vless | 202 | 133 | 69 | 65.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 45 |
| geo:ClientOSError | 11 |
| speed:ClientOSError | 9 |
| 204:TimeoutError | 5 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6857 |
| ConnectionRefusedError | 1011 |
| OSError | 234 |
| gaierror | 155 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| mheidari-all | 0.905 | prefer | 78 | 0.833 | 23828 |
| Au1rxx-base64 | 0.853 | prefer | 210 | 0.786 | 1761 |
| Surfboard-tg-mixed | 0.709 | prefer | 60 | 0.633 | 7197 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7716 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10189 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5754 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 452 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 343 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 338 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 168 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 163 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 87 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.633 | 38 | 22 | 60 |
| Au1rxx-base64 | 0.786 | 165 | 45 | 210 |
| mheidari-all | 0.833 | 65 | 13 | 78 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23828 | yes | 3.77 | 0 |
| SoliSpirit-all | 10189 | yes | 2.66 | 0 |
| Epodonios-all | 7716 | yes | 4.1 | 0 |
| Surfboard-tg-mixed | 7197 | yes | 3.0 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 0.87 | 0 |
| barry-far-vless | 5978 | yes | 0.44 | 0 |
| Surfboard-tg-vless | 5754 | yes | 2.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 2.46 | 0 |
| DeltaKronecker-all | 4803 | yes | 4.01 | 0 |
| mahdibland-V2RayAggregator | 4271 | yes | 2.09 | 0 |

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
| geo | 11 |
| speed | 9 |
| 204 | 9 |
| cn-block | 8 |
