# AutoNodes 每日报告

生成时间：2026-10-21 05:05:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 95380 |
| 去重后节点数 | 26617 |
| TCP 可达数 | 3000 |
| 真测通过数 | 445 |
| verified 输出数 | 118 |
| global 输出数 | 300 |
| all 输出数 | 26617 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.9 |
| fetch | 6.8 |
| generate | 12.6 |
| geo | 1.6 |
| probe | 91.7 |
| real_test | 88.6 |
| tcp | 83.2 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 91 | 86 | 5 | 94.5% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 123 | 119 | 4 | 96.7% |
| socks | 5 | 5 | 0 | 100.0% |
| trojan | 48 | 46 | 2 | 95.8% |
| vless | 326 | 185 | 141 | 56.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 102 |
| geo:ClientOSError | 21 |
| speed:ClientOSError | 18 |
| 204:ProxyError | 3 |
| cn-block:ClientOSError | 2 |
| speed:ProxyError | 1 |
| cn-block:TimeoutError | 1 |
| 204:TimeoutError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6784 |
| ConnectionRefusedError | 1022 |
| OSError | 233 |
| gaierror | 127 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.959 | prefer | 63 | 0.952 | 516 |
| zhangkai | 0.932 | prefer | 27 | 0.963 | 31 |
| Au1rxx-base64 | 0.922 | prefer | 277 | 0.866 | 1451 |
| Surfboard-tg-mixed | 0.835 | prefer | 14 | 1.0 | 7115 |
| mheidari-all | 0.575 | observe | 198 | 0.495 | 23653 |
| SoliSpirit-all | 0.391 | observe | 2 | 1.0 | 10017 |
| roosterkid-openproxylist-v2ray | 0.372 | observe | 5 | 0.8 | 150 |
| ermaozi | 0.314 | observe | 2 | 1.0 | 76 |
| DeltaKronecker-all | 0.291 | observe | 12 | 0.25 | 3519 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 5 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 483 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 374 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 369 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 252 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 118 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.25 | 3 | 9 | 12 |
| mheidari-all | 0.495 | 98 | 100 | 198 |
| tg-oneclickvpnkeys | 0.667 | 2 | 1 | 3 |
| roosterkid-openproxylist-v2ray | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.866 | 240 | 37 | 277 |
| ermaozi-get_subscribe | 0.952 | 60 | 3 | 63 |
| zhangkai | 0.963 | 26 | 1 | 27 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23653 | yes | 4.73 | 0 |
| SoliSpirit-all | 10017 | yes | 3.13 | 0 |
| Epodonios-all | 7598 | yes | 4.91 | 0 |
| Surfboard-tg-mixed | 7115 | yes | 3.34 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.76 | 0 |
| barry-far-vless | 5764 | yes | 1.17 | 0 |
| Surfboard-tg-vless | 5552 | yes | 3.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 4967 | yes | 0.7 | 0 |
| mahdibland-V2RayAggregator | 4127 | yes | 2.93 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.99 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 102 |
| geo | 22 |
| speed | 20 |
| 204 | 5 |
| cn-block | 3 |
