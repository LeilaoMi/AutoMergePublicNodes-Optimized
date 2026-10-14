# AutoNodes 每日报告

生成时间：2026-10-14 10:50:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 4/90 |
| 原始节点数 | 98335 |
| 去重后节点数 | 27212 |
| TCP 可达数 | 3000 |
| 真测通过数 | 73 |
| verified 输出数 | 73 |
| global 输出数 | 80 |
| all 输出数 | 27212 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| generate | 59.7 |
| geo | 1.6 |
| probe | 111.0 |
| real_test | 84.4 |
| tcp | 118.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 0 | 2 | 0.0% |
| http | 76 | 74 | 2 | 97.4% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 129 | 119 | 10 | 92.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 24 | 11 | 13 | 45.8% |
| vless | 185 | 104 | 81 | 56.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 50 |
| geo:ClientOSError | 12 |
| 204:ProxyError | 9 |
| speed:ClientOSError | 9 |
| cn-block:ClientOSError | 7 |
| 204:ProxyConnectionError | 6 |
| geo:TimeoutError | 6 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:TimeoutError | 2 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6242 |
| ConnectionRefusedError | 1039 |
| gaierror | 356 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.976 | prefer | 60 | 0.967 | 598 |
| mheidari-all | 0.88 | prefer | 68 | 0.809 | 23983 |
| zhangkai | 0.861 | prefer | 17 | 1.0 | 144 |
| Au1rxx-base64 | 0.786 | prefer | 205 | 0.717 | 1786 |
| Surfboard-tg-mixed | 0.65 | observe | 84 | 0.571 | 7056 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7616 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10026 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 446 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 337 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 332 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 193 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 162 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 157 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 81 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.571 | 48 | 36 | 84 |
| Au1rxx-base64 | 0.717 | 147 | 58 | 205 |
| mheidari-all | 0.809 | 55 | 13 | 68 |
| ermaozi-get_subscribe | 0.967 | 58 | 2 | 60 |
| zhangkai | 1.0 | 17 | 0 | 17 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23983 | yes | 5.71 | 0 |
| SoliSpirit-all | 10026 | yes | 3.04 | 0 |
| Epodonios-all | 7616 | yes | 6.58 | 0 |
| Surfboard-tg-mixed | 7056 | yes | 4.44 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.93 | 0 |
| barry-far-vless | 5831 | yes | 0.87 | 0 |
| Surfboard-tg-vless | 5579 | yes | 4.19 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 0.54 | 0 |
| DeltaKronecker-all | 4803 | yes | 6.32 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 3.23 | 0 |

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
| test_one_timeout | 50 |
| 204 | 20 |
| geo | 19 |
| cn-block | 12 |
| speed | 9 |
