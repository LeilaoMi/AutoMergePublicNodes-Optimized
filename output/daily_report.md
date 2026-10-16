# AutoNodes 每日报告

生成时间：2026-10-16 15:18:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99232 |
| 去重后节点数 | 27717 |
| TCP 可达数 | 3000 |
| 真测通过数 | 404 |
| verified 输出数 | 77 |
| global 输出数 | 300 |
| all 输出数 | 27717 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 17.0 |
| fetch | 10.7 |
| generate | 14.0 |
| geo | 1.5 |
| probe | 94.8 |
| real_test | 80.9 |
| tcp | 85.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 57 | 2 | 96.6% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 148 | 130 | 18 | 87.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 35 | 30 | 5 | 85.7% |
| vless | 275 | 172 | 103 | 62.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 72 |
| speed:ClientOSError | 13 |
| 204:TimeoutError | 13 |
| 204:ProxyError | 10 |
| cn-block:ClientOSError | 6 |
| cn-block:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ClientOSError | 2 |
| speed:ClientPayloadError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6845 |
| ConnectionRefusedError | 1041 |
| gaierror | 271 |
| OSError | 236 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.991 | prefer | 57 | 0.982 | 618 |
| Au1rxx-base64 | 0.829 | prefer | 441 | 0.751 | 1991 |
| mheidari-all | 0.616 | observe | 26 | 0.538 | 23974 |
| Au1rxx-clash | 0.335 | observe | 1 | 1.0 | 1991 |
| Surfboard-tg-mixed | 0.32 | observe | 4 | 0.5 | 7090 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Epodonios-all | 0.255 | observe | 0 | None | 7602 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10100 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 465 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 356 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 351 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 181 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 176 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 100 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.5 | 2 | 2 | 4 |
| mheidari-all | 0.538 | 14 | 12 | 26 |
| Au1rxx-base64 | 0.751 | 331 | 110 | 441 |
| ermaozi | 0.982 | 56 | 1 | 57 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Au1rxx-clash | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23974 | yes | 6.33 | 0 |
| SoliSpirit-all | 10100 | yes | 6.04 | 0 |
| Epodonios-all | 7602 | yes | 7.53 | 0 |
| Surfboard-tg-mixed | 7090 | yes | 4.66 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.41 | 0 |
| barry-far-vless | 5822 | yes | 4.25 | 0 |
| Surfboard-tg-vless | 5572 | yes | 4.18 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 3.76 | 0 |
| DeltaKronecker-all | 4946 | yes | 7.01 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 0.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 72 |
| 204 | 27 |
| speed | 15 |
| cn-block | 13 |
| geo | 3 |
