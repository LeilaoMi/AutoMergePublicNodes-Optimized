# AutoNodes 每日报告

生成时间：2026-10-16 16:52:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/1 |
| 清理建议：优先/观察 | 3/89 |
| 原始节点数 | 99080 |
| 去重后节点数 | 27737 |
| TCP 可达数 | 3000 |
| 真测通过数 | 409 |
| verified 输出数 | 81 |
| global 输出数 | 300 |
| all 输出数 | 27737 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 17.4 |
| fetch | 7.8 |
| generate | 14.0 |
| geo | 1.6 |
| probe | 95.5 |
| real_test | 89.4 |
| tcp | 86.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 58 | 1 | 98.3% |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 141 | 121 | 20 | 85.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 36 | 32 | 4 | 88.9% |
| vless | 279 | 184 | 95 | 65.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 70 |
| speed:ClientOSError | 15 |
| 204:ProxyError | 12 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 5 |
| geo:ClientOSError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7009 |
| ConnectionRefusedError | 1038 |
| OSError | 237 |
| gaierror | 233 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.991 | prefer | 58 | 0.983 | 618 |
| Au1rxx-base64 | 0.833 | prefer | 444 | 0.755 | 1991 |
| mheidari-all | 0.762 | prefer | 20 | 0.7 | 23974 |
| Surfboard-tg-mixed | 0.391 | observe | 2 | 1.0 | 7090 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 79 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1991 |
| Epodonios-all | 0.255 | observe | 0 | None | 7602 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| peasoft-NoMoreWalls | 0.133 | observe | 1 | 0.0 | 0 | 143 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| DeltaKronecker-all | 0.153 | downweight | 5 | 0.0 | 0 | 4946 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 466 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 357 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 352 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 182 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 101 | 连续死亡次数 >= 2 |
| downweight | DeltaKronecker-all | 0.153 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| peasoft-NoMoreWalls | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 5 | 5 |
| mheidari-all | 0.7 | 14 | 6 | 20 |
| Au1rxx-base64 | 0.755 | 335 | 109 | 444 |
| ermaozi | 0.983 | 57 | 1 | 58 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23974 | yes | 5.67 | 0 |
| SoliSpirit-all | 9917 | yes | 2.86 | 0 |
| Epodonios-all | 7602 | yes | 6.88 | 0 |
| Surfboard-tg-mixed | 7090 | yes | 7.67 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 4.22 | 0 |
| barry-far-vless | 5822 | yes | 2.2 | 0 |
| Surfboard-tg-vless | 5572 | yes | 4.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 4.6 | 0 |
| DeltaKronecker-all | 4946 | yes | 7.7 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 2.16 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 70 |
| 204 | 22 |
| speed | 16 |
| cn-block | 9 |
| geo | 6 |
