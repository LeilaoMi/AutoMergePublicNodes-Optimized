# AutoNodes 每日报告

生成时间：2026-10-23 05:07:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 96386 |
| 去重后节点数 | 26819 |
| TCP 可达数 | 3000 |
| 真测通过数 | 429 |
| verified 输出数 | 175 |
| global 输出数 | 300 |
| all 输出数 | 26819 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.6 |
| fetch | 4.2 |
| generate | 8.9 |
| geo | 1.6 |
| probe | 68.2 |
| real_test | 82.8 |
| tcp | 82.2 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 104 | 100 | 4 | 96.2% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 117 | 112 | 5 | 95.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 46 | 44 | 2 | 95.7% |
| vless | 296 | 161 | 135 | 54.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 88 |
| speed:ClientOSError | 21 |
| geo:ClientOSError | 18 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| 204:TimeoutError | 3 |
| geo:ProxyError | 2 |
| geo:TimeoutError | 2 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6641 |
| ConnectionRefusedError | 1031 |
| OSError | 238 |
| gaierror | 178 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.986 | prefer | 103 | 0.971 | 609 |
| Au1rxx-base64 | 0.878 | prefer | 259 | 0.819 | 1536 |
| Surfboard-tg-mixed | 0.749 | prefer | 13 | 0.923 | 6999 |
| mheidari-all | 0.621 | observe | 183 | 0.541 | 23958 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| DeltaKronecker-all | 0.37 | observe | 16 | 0.312 | 3641 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10110 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |
| Epodonios-all | 0.255 | observe | 0 | None | 7509 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 491 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 382 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 377 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 260 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 126 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.312 | 5 | 11 | 16 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.541 | 99 | 84 | 183 |
| Au1rxx-base64 | 0.819 | 212 | 47 | 259 |
| Surfboard-tg-mixed | 0.923 | 12 | 1 | 13 |
| ermaozi | 0.971 | 100 | 3 | 103 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23958 | yes | 3.39 | 0 |
| SoliSpirit-all | 10110 | yes | 1.56 | 0 |
| Epodonios-all | 7509 | yes | 3.5 | 0 |
| Surfboard-tg-mixed | 6999 | yes | 0.18 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.28 | 0 |
| barry-far-vless | 5666 | yes | 0.59 | 0 |
| Surfboard-tg-vless | 5447 | yes | 2.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 0.81 | 0 |
| mahdibland-V2RayAggregator | 4230 | yes | 1.84 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.68 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 88 |
| speed | 22 |
| geo | 22 |
| cn-block | 8 |
| 204 | 8 |
