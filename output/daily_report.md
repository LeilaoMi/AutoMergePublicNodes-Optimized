# AutoNodes 每日报告

生成时间：2026-10-16 11:41:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99280 |
| 去重后节点数 | 27669 |
| TCP 可达数 | 3000 |
| 真测通过数 | 469 |
| verified 输出数 | 21 |
| global 输出数 | 300 |
| all 输出数 | 27669 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 27.0 |
| fetch | 6.0 |
| generate | 11.0 |
| geo | 1.5 |
| probe | 86.1 |
| real_test | 92.2 |
| tcp | 86.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 88 | 86 | 2 | 97.7% |
| hysteria2 | 17 | 13 | 4 | 76.5% |
| shadowsocks | 147 | 124 | 23 | 84.4% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 33 | 29 | 4 | 87.9% |
| vless | 311 | 215 | 96 | 69.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 70 |
| speed:ClientOSError | 15 |
| 204:TimeoutError | 11 |
| geo:ClientOSError | 9 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 4 |
| 204:ClientOSError | 4 |
| speed:ProxyError | 3 |
| speed:TimeoutError | 2 |
| cn-block:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7062 |
| ConnectionRefusedError | 1023 |
| OSError | 237 |
| gaierror | 231 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 86 | 0.988 | 693 |
| Au1rxx-base64 | 0.848 | prefer | 473 | 0.77 | 1990 |
| mheidari-all | 0.58 | observe | 26 | 0.5 | 23871 |
| Surfboard-tg-mixed | 0.465 | observe | 7 | 0.714 | 7090 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1990 |
| Epodonios-all | 0.255 | observe | 0 | None | 7568 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10088 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| DeltaKronecker-all | 0.17 | observe | 3 | 0.0 | 0 | 4946 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 462 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 353 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 348 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 178 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 173 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 97 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 3 | 3 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.5 | 13 | 13 | 26 |
| Surfboard-tg-mixed | 0.714 | 5 | 2 | 7 |
| Au1rxx-base64 | 0.77 | 364 | 109 | 473 |
| ermaozi | 0.988 | 85 | 1 | 86 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23871 | yes | 4.65 | 0 |
| SoliSpirit-all | 10088 | yes | 3.47 | 0 |
| Epodonios-all | 7568 | yes | 4.87 | 0 |
| Surfboard-tg-mixed | 7090 | yes | 3.64 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.48 | 0 |
| barry-far-vless | 5827 | yes | 1.44 | 0 |
| Surfboard-tg-vless | 5572 | yes | 3.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 1.16 | 0 |
| DeltaKronecker-all | 4946 | yes | 4.64 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 2.7 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_drop_50pct | verified output dropped from 43 to 21 |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 70 |
| speed | 20 |
| 204 | 19 |
| cn-block | 12 |
| geo | 9 |
