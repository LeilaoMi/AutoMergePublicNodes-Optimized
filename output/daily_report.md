# AutoNodes 每日报告

生成时间：2026-10-22 12:10:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 5/88 |
| 原始节点数 | 95591 |
| 去重后节点数 | 26659 |
| TCP 可达数 | 3000 |
| 真测通过数 | 383 |
| verified 输出数 | 123 |
| global 输出数 | 300 |
| all 输出数 | 26659 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 35.5 |
| fetch | 6.0 |
| generate | 10.5 |
| geo | 1.6 |
| probe | 86.1 |
| real_test | 82.7 |
| tcp | 83.9 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 77 | 73 | 4 | 94.8% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 157 | 136 | 21 | 86.6% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 80 | 60 | 20 | 75.0% |
| vless | 172 | 106 | 66 | 61.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 68 |
| speed:ClientOSError | 12 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 6 |
| cn-block:TimeoutError | 6 |
| geo:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6758 |
| ConnectionRefusedError | 1006 |
| OSError | 238 |
| gaierror | 149 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.972 | prefer | 32 | 1.0 | 45 |
| ermaozi-get_subscribe | 0.884 | prefer | 49 | 0.878 | 523 |
| Au1rxx-base64 | 0.846 | prefer | 254 | 0.787 | 1519 |
| mheidari-all | 0.797 | prefer | 58 | 0.724 | 23951 |
| Surfboard-tg-mixed | 0.757 | prefer | 60 | 0.683 | 7043 |
| DeltaKronecker-all | 0.655 | observe | 38 | 0.579 | 3641 |
| ninja-vless | 0.392 | observe | 4 | 0.75 | 1791 |
| tg-oneclickvpnkeys | 0.257 | observe | 1 | 1.0 | 55 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |
| Epodonios-all | 0.255 | observe | 0 | None | 7460 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 5 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 488 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 379 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 374 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 257 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 123 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.579 | 22 | 16 | 38 |
| Surfboard-tg-mixed | 0.683 | 41 | 19 | 60 |
| mheidari-all | 0.724 | 42 | 16 | 58 |
| ninja-vless | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.787 | 200 | 54 | 254 |
| ermaozi-get_subscribe | 0.878 | 43 | 6 | 49 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 32 | 0 | 32 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23951 | yes | 4.83 | 0 |
| SoliSpirit-all | 10067 | yes | 3.09 | 0 |
| Epodonios-all | 7460 | yes | 4.29 | 0 |
| Surfboard-tg-mixed | 7043 | yes | 3.36 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.89 | 0 |
| barry-far-vless | 5666 | yes | 0.82 | 0 |
| Surfboard-tg-vless | 5382 | yes | 2.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 1.02 | 0 |
| mahdibland-V2RayAggregator | 4164 | yes | 2.48 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.28 | 0 |

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
| test_one_timeout | 68 |
| 204 | 16 |
| speed | 12 |
| cn-block | 11 |
| geo | 6 |
