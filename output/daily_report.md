# AutoNodes 每日报告

生成时间：2026-10-15 11:16:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 99769 |
| 去重后节点数 | 27864 |
| TCP 可达数 | 3000 |
| 真测通过数 | 100 |
| verified 输出数 | 100 |
| global 输出数 | 104 |
| all 输出数 | 27864 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.7 |
| fetch | 6.6 |
| generate | 11.2 |
| geo | 1.5 |
| probe | 101.4 |
| real_test | 71.5 |
| tcp | 88.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 80 | 75 | 5 | 93.8% |
| hysteria2 | 9 | 7 | 2 | 77.8% |
| shadowsocks | 124 | 106 | 18 | 85.5% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 7 | 5 | 2 | 71.4% |
| vless | 158 | 100 | 58 | 63.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 53 |
| speed:ClientOSError | 7 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 6 |
| 204:TimeoutError | 6 |
| geo:ClientOSError | 4 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7244 |
| ConnectionRefusedError | 1013 |
| OSError | 233 |
| gaierror | 169 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.956 | prefer | 81 | 0.938 | 703 |
| Au1rxx-base64 | 0.821 | prefer | 274 | 0.752 | 1769 |
| mheidari-all | 0.671 | observe | 20 | 0.6 | 24005 |
| Surfboard-tg-mixed | 0.337 | observe | 7 | 0.429 | 7139 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5089 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5147 |
| Epodonios-all | 0.255 | observe | 0 | None | 7652 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10113 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5693 |

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
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 454 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 345 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 340 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 223 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 170 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 165 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 89 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.429 | 3 | 4 | 7 |
| mheidari-all | 0.6 | 12 | 8 | 20 |
| Au1rxx-base64 | 0.752 | 206 | 68 | 274 |
| ermaozi | 0.938 | 76 | 5 | 81 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24005 | yes | 5.8 | 0 |
| SoliSpirit-all | 10113 | yes | 3.33 | 0 |
| Epodonios-all | 7652 | yes | 5.19 | 0 |
| Surfboard-tg-mixed | 7139 | yes | 3.79 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.87 | 0 |
| barry-far-vless | 5924 | yes | 2.29 | 0 |
| Surfboard-tg-vless | 5693 | yes | 4.0 | 0 |
| DeltaKronecker-all | 5147 | yes | 5.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 5089 | yes | 2.49 | 0 |
| mahdibland-V2RayAggregator | 4338 | yes | 2.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 53 |
| 204 | 14 |
| speed | 7 |
| cn-block | 7 |
| geo | 5 |
