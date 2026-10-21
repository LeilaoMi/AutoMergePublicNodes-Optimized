# AutoNodes 每日报告

生成时间：2026-10-21 12:07:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 95764 |
| 去重后节点数 | 26911 |
| TCP 可达数 | 3000 |
| 真测通过数 | 410 |
| verified 输出数 | 118 |
| global 输出数 | 300 |
| all 输出数 | 26911 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.7 |
| fetch | 5.4 |
| generate | 11.1 |
| geo | 1.7 |
| probe | 80.6 |
| real_test | 84.4 |
| tcp | 81.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 89 | 84 | 5 | 94.4% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 155 | 138 | 17 | 89.0% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 48 | 29 | 19 | 60.4% |
| vless | 224 | 145 | 79 | 64.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 63 |
| speed:ClientOSError | 11 |
| cn-block:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| 204:ProxyError | 8 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 2 |
| 204:TimeoutError | 2 |
| speed:TimeoutError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6551 |
| ConnectionRefusedError | 1032 |
| OSError | 236 |
| gaierror | 188 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.946 | prefer | 65 | 0.938 | 516 |
| zhangkai | 0.932 | prefer | 27 | 0.963 | 31 |
| mheidari-all | 0.865 | prefer | 63 | 0.794 | 23726 |
| Au1rxx-base64 | 0.845 | prefer | 266 | 0.786 | 1541 |
| Surfboard-tg-mixed | 0.678 | observe | 105 | 0.6 | 6977 |
| DeltaKronecker-all | 0.32 | observe | 4 | 0.5 | 4067 |
| peasoft-NoMoreWalls | 0.261 | observe | 1 | 1.0 | 139 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4925 |
| Epodonios-all | 0.255 | observe | 0 | None | 7465 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.132 | observe | 1 | 0.0 | 0 | 109 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 484 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 375 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 370 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 253 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 119 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.6 | 63 | 42 | 105 |
| Au1rxx-base64 | 0.786 | 209 | 57 | 266 |
| mheidari-all | 0.794 | 50 | 13 | 63 |
| ermaozi-get_subscribe | 0.938 | 61 | 4 | 65 |
| zhangkai | 0.963 | 26 | 1 | 27 |
| peasoft-NoMoreWalls | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23726 | yes | 4.22 | 0 |
| SoliSpirit-all | 10023 | yes | 4.7 | 0 |
| Epodonios-all | 7465 | yes | 4.63 | 0 |
| Surfboard-tg-mixed | 6977 | yes | 4.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.9 | 0 |
| barry-far-vless | 5674 | yes | 2.75 | 0 |
| Surfboard-tg-vless | 5462 | yes | 3.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 4925 | yes | 2.65 | 0 |
| mahdibland-V2RayAggregator | 4127 | yes | 2.66 | 0 |
| DeltaKronecker-all | 4067 | yes | 5.01 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 63 |
| cn-block | 19 |
| 204 | 15 |
| speed | 12 |
| geo | 12 |
