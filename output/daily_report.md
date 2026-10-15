# AutoNodes 每日报告

生成时间：2026-10-15 16:47:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 100051 |
| 去重后节点数 | 27919 |
| TCP 可达数 | 3000 |
| 真测通过数 | 89 |
| verified 输出数 | 89 |
| global 输出数 | 94 |
| all 输出数 | 27919 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.7 |
| fetch | 7.8 |
| generate | 14.2 |
| geo | 1.5 |
| probe | 113.3 |
| real_test | 72.7 |
| tcp | 84.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 69 | 67 | 2 | 97.1% |
| hysteria2 | 13 | 11 | 2 | 84.6% |
| shadowsocks | 131 | 93 | 38 | 71.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 8 | 5 | 3 | 62.5% |
| vless | 170 | 98 | 72 | 57.6% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 80 |
| speed:ClientOSError | 11 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 5 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6405 |
| ConnectionRefusedError | 1032 |
| gaierror | 315 |
| OSError | 236 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.984 | prefer | 69 | 0.971 | 659 |
| Au1rxx-base64 | 0.709 | prefer | 308 | 0.64 | 1767 |
| mheidari-all | 0.633 | observe | 14 | 0.714 | 24080 |
| Surfboard-tg-mixed | 0.391 | observe | 2 | 1.0 | 7281 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5089 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5147 |
| Epodonios-all | 0.255 | observe | 0 | None | 7794 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10074 |

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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 455 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 346 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 341 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 224 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 171 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 166 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 90 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.64 | 197 | 111 | 308 |
| mheidari-all | 0.714 | 10 | 4 | 14 |
| ermaozi | 0.971 | 67 | 2 | 69 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24080 | yes | 6.34 | 0 |
| SoliSpirit-all | 10074 | yes | 5.83 | 0 |
| Epodonios-all | 7794 | yes | 6.64 | 0 |
| Surfboard-tg-mixed | 7281 | yes | 5.66 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 4.11 | 0 |
| barry-far-vless | 5961 | yes | 3.47 | 0 |
| Surfboard-tg-vless | 5707 | yes | 4.26 | 0 |
| DeltaKronecker-all | 5147 | yes | 11.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 5089 | yes | 3.25 | 0 |
| mahdibland-V2RayAggregator | 4338 | yes | 3.22 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 80 |
| 204 | 14 |
| speed | 12 |
| cn-block | 8 |
| geo | 4 |
