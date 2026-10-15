# AutoNodes 每日报告

生成时间：2026-10-15 04:09:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 98808 |
| 去重后节点数 | 27524 |
| TCP 可达数 | 3000 |
| 真测通过数 | 62 |
| verified 输出数 | 62 |
| global 输出数 | 72 |
| all 输出数 | 27524 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.0 |
| fetch | 4.4 |
| generate | 7.8 |
| geo | 1.5 |
| probe | 86.8 |
| real_test | 85.5 |
| tcp | 87.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 59 | 0 | 100.0% |
| hysteria2 | 12 | 10 | 2 | 83.3% |
| shadowsocks | 138 | 126 | 12 | 91.3% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 11 | 7 | 4 | 63.6% |
| vless | 328 | 192 | 136 | 58.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 102 |
| speed:ClientOSError | 15 |
| geo:ClientOSError | 14 |
| cn-block:ClientOSError | 8 |
| 204:ProxyError | 6 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| cn-block:TimeoutError | 2 |
| speed:TimeoutError | 2 |
| 204:TimeoutError | 2 |
| geo:ProxyError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7063 |
| ConnectionRefusedError | 1025 |
| OSError | 234 |
| gaierror | 185 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.996 | prefer | 61 | 0.984 | 703 |
| Au1rxx-base64 | 0.832 | prefer | 388 | 0.771 | 1576 |
| mheidari-all | 0.449 | observe | 101 | 0.366 | 23886 |
| Surfboard-tg-mixed | 0.32 | observe | 4 | 0.5 | 7169 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7681 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9917 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 453 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 344 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 339 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 169 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 164 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 88 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.366 | 37 | 64 | 101 |
| Surfboard-tg-mixed | 0.5 | 2 | 2 | 4 |
| Au1rxx-base64 | 0.771 | 299 | 89 | 388 |
| ermaozi | 0.984 | 60 | 1 | 61 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23886 | yes | 3.49 | 0 |
| SoliSpirit-all | 9917 | yes | 1.98 | 0 |
| Epodonios-all | 7681 | yes | 3.6 | 0 |
| Surfboard-tg-mixed | 7169 | yes | 3.73 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.22 | 0 |
| barry-far-vless | 5978 | yes | 0.56 | 0 |
| Surfboard-tg-vless | 5728 | yes | 2.24 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 1.48 | 0 |
| DeltaKronecker-all | 4803 | yes | 3.63 | 0 |
| mahdibland-V2RayAggregator | 4271 | yes | 1.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 102 |
| speed | 18 |
| geo | 15 |
| cn-block | 12 |
| 204 | 10 |
