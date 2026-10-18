# AutoNodes 每日报告

生成时间：2026-10-18 04:51:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99074 |
| 去重后节点数 | 27914 |
| TCP 可达数 | 3000 |
| 真测通过数 | 512 |
| verified 输出数 | 130 |
| global 输出数 | 300 |
| all 输出数 | 27914 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.5 |
| fetch | 7.2 |
| generate | 13.0 |
| geo | 1.5 |
| probe | 88.9 |
| real_test | 97.6 |
| tcp | 88.6 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 99 | 94 | 5 | 94.9% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 124 | 120 | 4 | 96.8% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 59 | 51 | 8 | 86.4% |
| vless | 378 | 232 | 146 | 61.4% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 104 |
| geo:ClientOSError | 23 |
| speed:ClientOSError | 14 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 7 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |
| cn-block:TimeoutError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7258 |
| ConnectionRefusedError | 1026 |
| OSError | 233 |
| gaierror | 155 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.989 | prefer | 99 | 0.97 | 710 |
| Au1rxx-base64 | 0.948 | prefer | 413 | 0.879 | 1776 |
| Surfboard-tg-mixed | 0.643 | observe | 10 | 0.9 | 7181 |
| DeltaKronecker-all | 0.519 | observe | 5 | 1.0 | 4999 |
| Surfboard-tg-vless | 0.372 | observe | 9 | 0.444 | 5616 |
| mheidari-all | 0.358 | observe | 142 | 0.275 | 23946 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4986 |
| Epodonios-all | 0.255 | observe | 0 | None | 7667 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9903 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.108 | observe | 2 | 0.0 | 0 | 99 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 472 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 363 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 358 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 188 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 107 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.275 | 39 | 103 | 142 |
| Surfboard-tg-vless | 0.444 | 4 | 5 | 9 |
| Au1rxx-base64 | 0.879 | 363 | 50 | 413 |
| Surfboard-tg-mixed | 0.9 | 9 | 1 | 10 |
| ermaozi | 0.97 | 96 | 3 | 99 |
| DeltaKronecker-all | 1.0 | 5 | 0 | 5 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23946 | yes | 6.24 | 0 |
| SoliSpirit-all | 9903 | yes | 5.13 | 0 |
| Epodonios-all | 7667 | yes | 5.46 | 0 |
| Surfboard-tg-mixed | 7181 | yes | 3.79 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.49 | 0 |
| barry-far-vless | 5884 | yes | 2.7 | 0 |
| Surfboard-tg-vless | 5616 | yes | 5.15 | 0 |
| DeltaKronecker-all | 4999 | yes | 6.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4986 | yes | 3.02 | 0 |
| mahdibland-V2RayAggregator | 4295 | yes | 2.08 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 104 |
| geo | 24 |
| 204 | 15 |
| speed | 15 |
| cn-block | 8 |
