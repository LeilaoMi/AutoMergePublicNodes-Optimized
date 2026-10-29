# AutoNodes 每日报告

生成时间：2026-10-29 13:24:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 99866 |
| 去重后节点数 | 28371 |
| TCP 可达数 | 3000 |
| 真测通过数 | 402 |
| verified 输出数 | 71 |
| global 输出数 | 300 |
| all 输出数 | 28371 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.8 |
| fetch | 4.4 |
| generate | 9.7 |
| geo | 1.6 |
| probe | 73.3 |
| real_test | 87.0 |
| tcp | 92.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 21 | 2 | 91.3% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 167 | 146 | 21 | 87.4% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 128 | 101 | 27 | 78.9% |
| vless | 216 | 122 | 94 | 56.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 82 |
| geo:ClientOSError | 19 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 10 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 6 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |
| speed:ClientOSError | 1 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7421 |
| ConnectionRefusedError | 1078 |
| OSError | 240 |
| gaierror | 170 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.87 | prefer | 310 | 0.803 | 1723 |
| ermaozi | 0.739 | prefer | 30 | 0.733 | 510 |
| mheidari-all | 0.738 | prefer | 71 | 0.662 | 34088 |
| Surfboard-tg-mixed | 0.705 | prefer | 134 | 0.627 | 7779 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2709 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10415 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5820 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 513 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 404 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 399 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 282 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 260 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 259 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 251 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 224 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 148 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.627 | 84 | 50 | 134 |
| mheidari-all | 0.662 | 47 | 24 | 71 |
| ermaozi | 0.733 | 22 | 8 | 30 |
| Au1rxx-base64 | 0.803 | 249 | 61 | 310 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34088 | yes | 3.84 | 0 |
| SoliSpirit-all | 10415 | yes | 1.52 | 0 |
| Surfboard-tg-mixed | 7779 | yes | 1.94 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.23 | 0 |
| barry-far-vless | 6035 | yes | 0.78 | 0 |
| Surfboard-tg-vless | 5820 | yes | 2.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 0.67 | 0 |
| mahdibland-V2RayAggregator | 4444 | yes | 1.71 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.55 | 0 |
| DeltaKronecker-all | 2709 | yes | 3.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 82 |
| 204 | 23 |
| geo | 22 |
| cn-block | 15 |
| speed | 2 |
