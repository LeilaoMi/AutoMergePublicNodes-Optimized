# AutoNodes 每日报告

生成时间：2026-10-16 14:42:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99222 |
| 去重后节点数 | 27685 |
| TCP 可达数 | 3000 |
| 真测通过数 | 343 |
| verified 输出数 | 50 |
| global 输出数 | 300 |
| all 输出数 | 27685 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 34.0 |
| fetch | 4.7 |
| generate | 8.7 |
| geo | 1.5 |
| probe | 65.6 |
| real_test | 82.9 |
| tcp | 91.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 60 | 57 | 3 | 95.0% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 136 | 103 | 33 | 75.7% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 28 | 19 | 9 | 67.9% |
| vless | 229 | 152 | 77 | 66.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 73 |
| speed:ClientOSError | 12 |
| 204:ProxyError | 9 |
| geo:ClientOSError | 7 |
| cn-block:TimeoutError | 7 |
| 204:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7608 |
| ConnectionRefusedError | 1005 |
| OSError | 232 |
| gaierror | 56 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.959 | prefer | 59 | 0.949 | 618 |
| Au1rxx-base64 | 0.789 | prefer | 384 | 0.711 | 1991 |
| mheidari-all | 0.461 | observe | 11 | 0.545 | 23974 |
| DeltaKronecker-all | 0.4 | observe | 4 | 0.75 | 4946 |
| Surfboard-tg-mixed | 0.391 | observe | 2 | 1.0 | 7090 |
| ninja-vless | 0.291 | observe | 5 | 0.4 | 1791 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1991 |
| Epodonios-all | 0.255 | observe | 0 | None | 7568 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 463 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 354 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 349 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 179 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 174 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 98 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.4 | 2 | 3 | 5 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.545 | 6 | 5 | 11 |
| Au1rxx-base64 | 0.711 | 273 | 111 | 384 |
| DeltaKronecker-all | 0.75 | 3 | 1 | 4 |
| ermaozi | 0.949 | 56 | 3 | 59 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23974 | yes | 4.84 | 0 |
| SoliSpirit-all | 10094 | yes | 3.14 | 0 |
| Epodonios-all | 7568 | yes | 3.71 | 0 |
| Surfboard-tg-mixed | 7090 | yes | 1.65 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.09 | 0 |
| barry-far-vless | 5827 | yes | 0.71 | 0 |
| Surfboard-tg-vless | 5572 | yes | 1.53 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 1.06 | 0 |
| DeltaKronecker-all | 4946 | yes | 3.75 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 1.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 73 |
| 204 | 16 |
| speed | 14 |
| cn-block | 13 |
| geo | 9 |
