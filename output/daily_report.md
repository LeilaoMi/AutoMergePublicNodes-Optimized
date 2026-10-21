# AutoNodes 每日报告

生成时间：2026-10-21 17:27:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 92/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 96402 |
| 去重后节点数 | 26917 |
| TCP 可达数 | 3000 |
| 真测通过数 | 300 |
| verified 输出数 | 75 |
| global 输出数 | 300 |
| all 输出数 | 26917 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.9 |
| fetch | 7.3 |
| generate | 13.9 |
| geo | 1.5 |
| probe | 96.5 |
| real_test | 63.9 |
| tcp | 81.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 41 | 39 | 2 | 95.1% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 104 | 91 | 13 | 87.5% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 32 | 29 | 3 | 90.6% |
| vless | 196 | 128 | 68 | 65.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 43 |
| speed:ClientOSError | 15 |
| geo:ClientOSError | 8 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 4 |
| 204:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6500 |
| ConnectionRefusedError | 1048 |
| OSError | 237 |
| gaierror | 233 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | prefer | 27 | 1.0 | 31 |
| mheidari-all | 0.856 | prefer | 83 | 0.783 | 24102 |
| Au1rxx-base64 | 0.83 | prefer | 234 | 0.769 | 1566 |
| ermaozi-get_subscribe | 0.703 | prefer | 12 | 1.0 | 385 |
| Surfboard-tg-mixed | 0.543 | observe | 13 | 0.615 | 7070 |
| DeltaKronecker-all | 0.352 | observe | 11 | 0.364 | 4067 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4925 |
| Epodonios-all | 0.255 | observe | 0 | None | 7559 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.107 | observe | 2 | 0.0 | 0 | 82 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 485 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 376 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 371 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 254 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 223 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 120 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.364 | 4 | 7 | 11 |
| tg-LonUp_M | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.615 | 8 | 5 | 13 |
| Au1rxx-base64 | 0.769 | 180 | 54 | 234 |
| mheidari-all | 0.783 | 65 | 18 | 83 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |
| ermaozi-get_subscribe | 1.0 | 12 | 0 | 12 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24102 | yes | 5.87 | 0 |
| SoliSpirit-all | 10000 | yes | 3.25 | 0 |
| Epodonios-all | 7559 | yes | 6.16 | 0 |
| Surfboard-tg-mixed | 7070 | yes | 0.45 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.93 | 0 |
| barry-far-vless | 5768 | yes | 0.84 | 0 |
| Surfboard-tg-vless | 5554 | yes | 3.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4925 | yes | 1.16 | 0 |
| mahdibland-V2RayAggregator | 4127 | yes | 3.34 | 0 |
| DeltaKronecker-all | 4067 | yes | 6.74 | 0 |

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
| test_one_timeout | 43 |
| speed | 15 |
| 204 | 11 |
| cn-block | 11 |
| geo | 8 |
