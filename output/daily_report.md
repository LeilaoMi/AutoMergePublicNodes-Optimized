# AutoNodes 每日报告

生成时间：2026-10-29 22:56:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 99203 |
| 去重后节点数 | 27795 |
| TCP 可达数 | 3000 |
| 真测通过数 | 519 |
| verified 输出数 | 84 |
| global 输出数 | 300 |
| all 输出数 | 27795 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 35.5 |
| fetch | 5.7 |
| generate | 11.9 |
| geo | 1.6 |
| probe | 80.1 |
| real_test | 85.2 |
| tcp | 86.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 183 | 163 | 20 | 89.1% |
| trojan | 167 | 162 | 5 | 97.0% |
| vless | 257 | 158 | 99 | 61.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 75 |
| geo:ClientOSError | 16 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 8 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 5 |
| 204:TimeoutError | 4 |
| speed:ClientOSError | 2 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6923 |
| ConnectionRefusedError | 1100 |
| gaierror | 275 |
| OSError | 238 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | prefer | 22 | 1.0 | 510 |
| Surfboard-tg-mixed | 0.953 | prefer | 100 | 0.88 | 7758 |
| Au1rxx-base64 | 0.902 | prefer | 345 | 0.835 | 1725 |
| mheidari-all | 0.752 | prefer | 175 | 0.674 | 33474 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2709 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10379 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 514 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 405 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 400 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 283 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 261 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 260 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 252 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 149 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.674 | 118 | 57 | 175 |
| Au1rxx-base64 | 0.835 | 288 | 57 | 345 |
| Surfboard-tg-mixed | 0.88 | 88 | 12 | 100 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 33474 | yes | 4.61 | 0 |
| SoliSpirit-all | 10379 | yes | 3.92 | 0 |
| Surfboard-tg-mixed | 7758 | yes | 3.18 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.46 | 0 |
| barry-far-vless | 6033 | yes | 1.79 | 0 |
| Surfboard-tg-vless | 5789 | yes | 2.6 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 2.03 | 0 |
| mahdibland-V2RayAggregator | 4444 | yes | 0.95 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.1 | 0 |
| DeltaKronecker-all | 2709 | yes | 4.56 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 75 |
| cn-block | 18 |
| geo | 16 |
| 204 | 15 |
| speed | 3 |
