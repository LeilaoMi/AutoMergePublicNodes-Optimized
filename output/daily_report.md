# AutoNodes 每日报告

生成时间：2026-10-16 06:25:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/1 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99736 |
| 去重后节点数 | 27922 |
| TCP 可达数 | 3000 |
| 真测通过数 | 495 |
| verified 输出数 | 18 |
| global 输出数 | 300 |
| all 输出数 | 27922 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.4 |
| fetch | 8.3 |
| generate | 14.4 |
| geo | 1.5 |
| probe | 108.2 |
| real_test | 107.4 |
| tcp | 87.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 90 | 87 | 3 | 96.7% |
| hysteria2 | 15 | 10 | 5 | 66.7% |
| shadowsocks | 154 | 141 | 13 | 91.6% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 60 | 45 | 15 | 75.0% |
| vless | 318 | 210 | 108 | 66.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 81 |
| speed:ClientOSError | 16 |
| geo:ClientOSError | 13 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 6 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6851 |
| ConnectionRefusedError | 1015 |
| OSError | 239 |
| gaierror | 170 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.984 | prefer | 89 | 0.966 | 693 |
| Au1rxx-base64 | 0.878 | prefer | 465 | 0.8 | 1992 |
| mheidari-all | 0.642 | observe | 30 | 0.567 | 23985 |
| Surfboard-tg-mixed | 0.488 | observe | 47 | 0.404 | 7054 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 79 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7651 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10060 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.145 | downweight | 5 | 0.0 | 0 | 1791 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 459 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 350 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 345 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 175 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 170 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 94 | 连续死亡次数 >= 2 |
| downweight | ninja-vless | 0.145 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 5 | 5 |
| Surfboard-tg-mixed | 0.404 | 19 | 28 | 47 |
| mheidari-all | 0.567 | 17 | 13 | 30 |
| Au1rxx-base64 | 0.8 | 372 | 93 | 465 |
| ermaozi | 0.966 | 86 | 3 | 89 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23985 | yes | 6.84 | 0 |
| SoliSpirit-all | 10060 | yes | 5.68 | 0 |
| Epodonios-all | 7651 | yes | 7.14 | 0 |
| Surfboard-tg-mixed | 7054 | yes | 5.78 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.62 | 0 |
| barry-far-vless | 5882 | yes | 3.13 | 0 |
| Surfboard-tg-vless | 5573 | yes | 5.54 | 0 |
| DeltaKronecker-all | 5147 | yes | 7.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 2.85 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 3.87 | 0 |

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
| test_one_timeout | 81 |
| speed | 26 |
| 204 | 13 |
| geo | 13 |
| cn-block | 12 |
