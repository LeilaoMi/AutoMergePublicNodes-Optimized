# AutoNodes 每日报告

生成时间：2026-10-16 06:55:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 99726 |
| 去重后节点数 | 27907 |
| TCP 可达数 | 3000 |
| 真测通过数 | 505 |
| verified 输出数 | 39 |
| global 输出数 | 300 |
| all 输出数 | 27907 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 23.4 |
| fetch | 8.0 |
| generate | 14.5 |
| geo | 1.5 |
| probe | 115.1 |
| real_test | 97.1 |
| tcp | 84.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 92 | 84 | 8 | 91.3% |
| hysteria2 | 17 | 15 | 2 | 88.2% |
| shadowsocks | 156 | 145 | 11 | 92.9% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 49 | 34 | 15 | 69.4% |
| vless | 324 | 225 | 99 | 69.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 64 |
| speed:ClientOSError | 22 |
| geo:ClientOSError | 14 |
| cn-block:ClientOSError | 10 |
| 204:TimeoutError | 8 |
| speed:ProxyError | 5 |
| cn-block:ProxyError | 4 |
| cn-block:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| 204:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6708 |
| ConnectionRefusedError | 1026 |
| OSError | 238 |
| gaierror | 202 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.941 | prefer | 90 | 0.922 | 693 |
| Au1rxx-base64 | 0.89 | prefer | 478 | 0.812 | 1992 |
| mheidari-all | 0.58 | observe | 20 | 0.5 | 23985 |
| Surfboard-tg-mixed | 0.529 | observe | 47 | 0.447 | 7054 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 5147 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7651 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 461 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 352 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 347 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 96 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.447 | 21 | 26 | 47 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.5 | 10 | 10 | 20 |
| Au1rxx-base64 | 0.812 | 388 | 90 | 478 |
| ermaozi | 0.922 | 83 | 7 | 90 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23985 | yes | 6.82 | 0 |
| SoliSpirit-all | 10060 | yes | 5.72 | 0 |
| Epodonios-all | 7651 | yes | 7.17 | 0 |
| Surfboard-tg-mixed | 7054 | yes | 4.77 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.61 | 0 |
| barry-far-vless | 5882 | yes | 1.48 | 0 |
| Surfboard-tg-vless | 5573 | yes | 4.97 | 0 |
| DeltaKronecker-all | 5147 | yes | 7.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 1.27 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 0.17 | 0 |

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
| test_one_timeout | 64 |
| speed | 27 |
| cn-block | 18 |
| 204 | 14 |
| geo | 14 |
