# AutoNodes 每日报告

生成时间：2026-10-20 21:47:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 94518 |
| 去重后节点数 | 26436 |
| TCP 可达数 | 3000 |
| 真测通过数 | 353 |
| verified 输出数 | 94 |
| global 输出数 | 300 |
| all 输出数 | 26436 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.1 |
| fetch | 4.0 |
| generate | 7.9 |
| geo | 1.4 |
| probe | 66.3 |
| real_test | 64.8 |
| tcp | 82.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 31 | 31 | 0 | 100.0% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 109 | 105 | 4 | 96.3% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 40 | 35 | 5 | 87.5% |
| vless | 220 | 173 | 47 | 78.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 27 |
| speed:ClientOSError | 12 |
| 204:ProxyError | 7 |
| geo:ClientOSError | 6 |
| cn-block:TimeoutError | 3 |
| geo:TimeoutError | 1 |
| cn-block:ProxyError | 1 |
| 204:TimeoutError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6624 |
| ConnectionRefusedError | 1005 |
| OSError | 234 |
| gaierror | 168 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | prefer | 27 | 1.0 | 31 |
| mheidari-all | 0.934 | prefer | 94 | 0.862 | 23621 |
| Au1rxx-base64 | 0.921 | prefer | 258 | 0.868 | 1401 |
| Surfboard-tg-mixed | 0.66 | observe | 16 | 0.688 | 6945 |
| DeltaKronecker-all | 0.53 | observe | 10 | 0.7 | 3519 |
| tg-oneclickvpnkeys | 0.403 | observe | 4 | 1.0 | 74 |
| SoliSpirit-all | 0.391 | observe | 2 | 1.0 | 9871 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4967 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 482 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 373 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 368 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 251 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 117 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.688 | 11 | 5 | 16 |
| DeltaKronecker-all | 0.7 | 7 | 3 | 10 |
| mheidari-all | 0.862 | 81 | 13 | 94 |
| Au1rxx-base64 | 0.868 | 224 | 34 | 258 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23621 | yes | 3.29 | 0 |
| SoliSpirit-all | 9871 | yes | 1.95 | 0 |
| Epodonios-all | 7425 | yes | 2.41 | 0 |
| Surfboard-tg-mixed | 6945 | yes | 1.86 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.32 | 0 |
| barry-far-vless | 5701 | yes | 0.7 | 0 |
| Surfboard-tg-vless | 5487 | yes | 1.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 4967 | yes | 0.58 | 0 |
| mahdibland-V2RayAggregator | 4127 | yes | 1.62 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 27 |
| speed | 12 |
| 204 | 8 |
| geo | 7 |
| cn-block | 5 |
