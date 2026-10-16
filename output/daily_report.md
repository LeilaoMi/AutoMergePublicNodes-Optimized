# AutoNodes 每日报告

生成时间：2026-10-16 21:26:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 99390 |
| 去重后节点数 | 27723 |
| TCP 可达数 | 3000 |
| 真测通过数 | 453 |
| verified 输出数 | 91 |
| global 输出数 | 300 |
| all 输出数 | 27723 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.1 |
| fetch | 4.5 |
| generate | 8.3 |
| geo | 1.5 |
| probe | 69.1 |
| real_test | 83.6 |
| tcp | 89.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 63 | 60 | 3 | 95.2% |
| hysteria2 | 16 | 13 | 3 | 81.2% |
| shadowsocks | 155 | 144 | 11 | 92.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 37 | 35 | 2 | 94.6% |
| vless | 281 | 200 | 81 | 71.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 53 |
| speed:ClientOSError | 13 |
| 204:ProxyError | 8 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 6 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7361 |
| ConnectionRefusedError | 1021 |
| OSError | 233 |
| gaierror | 140 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.976 | prefer | 60 | 0.967 | 618 |
| Au1rxx-base64 | 0.892 | prefer | 451 | 0.814 | 1995 |
| mheidari-all | 0.799 | prefer | 30 | 0.733 | 23910 |
| Surfboard-tg-mixed | 0.349 | observe | 3 | 0.667 | 7222 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Surfboard-tg-vless | 0.259 | observe | 3 | 0.333 | 5648 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1995 |
| Epodonios-all | 0.255 | observe | 0 | None | 7598 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 467 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 358 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 353 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 178 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 102 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-vless | 0.333 | 1 | 2 | 3 |
| tg-oneclickvpnkeys | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.733 | 22 | 8 | 30 |
| Au1rxx-base64 | 0.814 | 367 | 84 | 451 |
| ermaozi | 0.967 | 58 | 2 | 60 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23910 | yes | 3.29 | 0 |
| SoliSpirit-all | 10078 | yes | 2.45 | 0 |
| Epodonios-all | 7598 | yes | 3.69 | 0 |
| Surfboard-tg-mixed | 7222 | yes | 2.16 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.8 | 0 |
| barry-far-vless | 5818 | yes | 1.29 | 0 |
| Surfboard-tg-vless | 5648 | yes | 2.91 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 1.4 | 0 |
| DeltaKronecker-all | 4946 | yes | 2.88 | 0 |
| mahdibland-V2RayAggregator | 4255 | yes | 1.86 | 0 |

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
| test_one_timeout | 53 |
| 204 | 16 |
| speed | 15 |
| cn-block | 12 |
| geo | 5 |
