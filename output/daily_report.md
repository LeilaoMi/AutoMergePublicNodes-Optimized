# AutoNodes 每日报告

生成时间：2026-10-18 20:59:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 97460 |
| 去重后节点数 | 27664 |
| TCP 可达数 | 3000 |
| 真测通过数 | 347 |
| verified 输出数 | 143 |
| global 输出数 | 300 |
| all 输出数 | 27664 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.3 |
| fetch | 7.5 |
| generate | 14.1 |
| geo | 1.5 |
| probe | 99.9 |
| real_test | 74.1 |
| tcp | 76.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 35 | 35 | 0 | 100.0% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 116 | 108 | 8 | 93.1% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 23 | 18 | 5 | 78.3% |
| vless | 244 | 177 | 67 | 72.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 40 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 10 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 3 |
| 204:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6599 |
| ConnectionRefusedError | 1041 |
| gaierror | 396 |
| OSError | 240 |
| SSRFBlocked | 7 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | prefer | 36 | 1.0 | 639 |
| Au1rxx-base64 | 0.892 | prefer | 280 | 0.825 | 1727 |
| mheidari-all | 0.822 | prefer | 91 | 0.747 | 23629 |
| DeltaKronecker-all | 0.53 | observe | 10 | 0.7 | 4750 |
| Surfboard-tg-mixed | 0.503 | observe | 12 | 0.583 | 7036 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| SoliSpirit-all | 0.287 | observe | 2 | 0.5 | 9755 |
| roosterkid-openproxylist-v2ray | 0.275 | observe | 3 | 0.667 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4983 |
| Epodonios-all | 0.255 | observe | 0 | None | 7503 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 475 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 366 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 361 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 110 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| SoliSpirit-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.583 | 7 | 5 | 12 |
| roosterkid-openproxylist-v2ray | 0.667 | 2 | 1 | 3 |
| DeltaKronecker-all | 0.7 | 7 | 3 | 10 |
| mheidari-all | 0.747 | 68 | 23 | 91 |
| Au1rxx-base64 | 0.825 | 231 | 49 | 280 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23629 | yes | 6.62 | 0 |
| SoliSpirit-all | 9755 | yes | 3.81 | 0 |
| Epodonios-all | 7503 | yes | 5.83 | 0 |
| Surfboard-tg-mixed | 7036 | yes | 4.73 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.08 | 0 |
| barry-far-vless | 5766 | yes | 0.52 | 0 |
| Surfboard-tg-vless | 5553 | yes | 4.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4983 | yes | 0.79 | 0 |
| DeltaKronecker-all | 4750 | yes | 7.2 | 0 |
| mahdibland-V2RayAggregator | 4246 | yes | 3.46 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 40 |
| speed | 14 |
| 204 | 12 |
| geo | 8 |
| cn-block | 8 |
