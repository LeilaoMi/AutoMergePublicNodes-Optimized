# AutoNodes 每日报告

生成时间：2026-10-18 16:04:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/1 |
| 清理建议：优先/观察 | 3/89 |
| 原始节点数 | 98093 |
| 去重后节点数 | 27755 |
| TCP 可达数 | 3000 |
| 真测通过数 | 362 |
| verified 输出数 | 143 |
| global 输出数 | 300 |
| all 输出数 | 27755 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.9 |
| fetch | 7.4 |
| generate | 14.2 |
| geo | 1.6 |
| probe | 102.9 |
| real_test | 73.5 |
| tcp | 82.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 34 | 30 | 4 | 88.2% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 137 | 122 | 15 | 89.1% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 40 | 20 | 20 | 50.0% |
| vless | 262 | 181 | 81 | 69.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 50 |
| geo:ClientOSError | 22 |
| 204:TimeoutError | 17 |
| speed:ClientOSError | 11 |
| 204:ProxyError | 6 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6875 |
| ConnectionRefusedError | 1048 |
| gaierror | 331 |
| OSError | 235 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.919 | prefer | 311 | 0.852 | 1729 |
| mheidari-all | 0.908 | prefer | 27 | 0.852 | 23775 |
| ermaozi | 0.863 | prefer | 35 | 0.857 | 639 |
| Surfboard-tg-mixed | 0.599 | observe | 79 | 0.519 | 7095 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 175 |
| peasoft-NoMoreWalls | 0.26 | observe | 1 | 1.0 | 123 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4983 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10058 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5602 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.174 | downweight | 30 | 0.067 | 0 | 4750 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 474 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 365 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 360 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 109 | 连续死亡次数 >= 2 |
| downweight | DeltaKronecker-all | 0.174 | 30 | 0.067 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.067 | 2 | 28 | 30 |
| Epodonios-all | 0.25 | 1 | 3 | 4 |
| Surfboard-tg-mixed | 0.519 | 41 | 38 | 79 |
| mheidari-all | 0.852 | 23 | 4 | 27 |
| Au1rxx-base64 | 0.852 | 265 | 46 | 311 |
| ermaozi | 0.857 | 30 | 5 | 35 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| peasoft-NoMoreWalls | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23775 | yes | 6.41 | 0 |
| SoliSpirit-all | 10058 | yes | 4.57 | 0 |
| Epodonios-all | 7485 | yes | 5.7 | 0 |
| Surfboard-tg-mixed | 7095 | yes | 4.21 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.03 | 0 |
| barry-far-vless | 5815 | yes | 0.97 | 0 |
| Surfboard-tg-vless | 5602 | yes | 3.97 | 0 |
| 10ium-ScrapeCategorize-Vless | 4983 | yes | 1.22 | 0 |
| DeltaKronecker-all | 4750 | yes | 6.34 | 0 |
| mahdibland-V2RayAggregator | 4246 | yes | 3.51 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 50 |
| 204 | 25 |
| geo | 24 |
| cn-block | 13 |
| speed | 12 |
