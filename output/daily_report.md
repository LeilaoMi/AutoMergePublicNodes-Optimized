# AutoNodes 每日报告

生成时间：2026-10-16 06:07:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/2 |
| 清理建议：优先/观察 | 2/90 |
| 原始节点数 | 99583 |
| 去重后节点数 | 27920 |
| TCP 可达数 | 3000 |
| 真测通过数 | 507 |
| verified 输出数 | 21 |
| global 输出数 | 300 |
| all 输出数 | 27920 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.2 |
| fetch | 8.0 |
| generate | 14.0 |
| geo | 1.5 |
| probe | 95.3 |
| real_test | 109.2 |
| tcp | 85.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 90 | 88 | 2 | 97.8% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 151 | 140 | 11 | 92.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 46 | 40 | 6 | 87.0% |
| vless | 408 | 224 | 184 | 54.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 140 |
| geo:ClientOSError | 20 |
| speed:ClientOSError | 16 |
| cn-block:ClientOSError | 11 |
| 204:TimeoutError | 5 |
| 204:ProxyError | 3 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| geo:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6913 |
| ConnectionRefusedError | 1027 |
| OSError | 240 |
| gaierror | 229 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 89 | 0.989 | 693 |
| Au1rxx-base64 | 0.883 | prefer | 490 | 0.804 | 1992 |
| Surfboard-tg-mixed | 0.515 | observe | 11 | 0.636 | 7054 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7651 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9906 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5573 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.131 | observe | 1 | 0.0 | 0 | 79 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 458 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 349 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 344 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 174 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 169 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 93 | 连续死亡次数 >= 2 |
| downweight | DeltaKronecker-all | 0.193 | 10 | 0.1 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mheidari-all | 0.233 | 109 | 0.147 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.1 | 1 | 9 | 10 |
| mheidari-all | 0.147 | 16 | 93 | 109 |
| Surfboard-tg-mixed | 0.636 | 7 | 4 | 11 |
| Au1rxx-base64 | 0.804 | 394 | 96 | 490 |
| ermaozi | 0.989 | 88 | 1 | 89 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23985 | yes | 6.38 | 0 |
| SoliSpirit-all | 9906 | yes | 5.98 | 0 |
| Epodonios-all | 7651 | yes | 6.61 | 0 |
| Surfboard-tg-mixed | 7054 | yes | 4.59 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.89 | 0 |
| barry-far-vless | 5882 | yes | 1.24 | 0 |
| Surfboard-tg-vless | 5573 | yes | 4.83 | 0 |
| DeltaKronecker-all | 5147 | yes | 7.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 3.07 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 1.26 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_drop_50pct | verified output dropped from 99 to 21 |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 140 |
| geo | 23 |
| speed | 18 |
| cn-block | 14 |
| 204 | 11 |
