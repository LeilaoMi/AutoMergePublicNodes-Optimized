# AutoNodes 每日报告

生成时间：2026-11-13 18:26:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83175 |
| 去重后节点数 | 26889 |
| TCP 可达数 | 3000 |
| 真测通过数 | 362 |
| verified 输出数 | 68 |
| global 输出数 | 300 |
| all 输出数 | 26889 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 17.9 |
| fetch | 5.1 |
| generate | 10.6 |
| geo | 1.4 |
| probe | 78.8 |
| real_test | 68.4 |
| tcp | 78.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 55 | 53 | 2 | 96.4% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 215 | 188 | 27 | 87.4% |
| trojan | 85 | 40 | 45 | 47.1% |
| vless | 114 | 69 | 45 | 60.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| 204:ProxyError | 33 |
| speed:ClientOSError | 13 |
| cn-block:ProxyError | 11 |
| 204:TimeoutError | 9 |
| geo:ProxyError | 3 |
| speed:TimeoutError | 2 |
| cn-block:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6043 |
| ConnectionRefusedError | 965 |
| gaierror | 247 |
| OSError | 239 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.971 | prefer | 55 | 0.964 | 590 |
| Surfboard-tg-mixed | 0.845 | prefer | 147 | 0.769 | 8804 |
| Au1rxx-base64 | 0.807 | prefer | 173 | 0.74 | 1751 |
| mheidari-all | 0.722 | prefer | 104 | 0.644 | 14267 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4900 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2734 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11395 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6228 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.111 | observe | 2 | 0.0 | 0 | 169 |
| ermaozi-get_subscribe | 0.145 | observe | 1 | 0.0 | 0 | 442 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 446 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 441 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 324 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 302 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 301 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 293 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.644 | 67 | 37 | 104 |
| Au1rxx-base64 | 0.74 | 128 | 45 | 173 |
| Surfboard-tg-mixed | 0.769 | 113 | 34 | 147 |
| ermaozi | 0.964 | 53 | 2 | 55 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14267 | yes | 3.57 | 0 |
| SoliSpirit-all | 11395 | yes | 2.42 | 0 |
| Surfboard-tg-mixed | 8804 | yes | 2.93 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.99 | 0 |
| barry-far-vless | 6409 | yes | 0.97 | 0 |
| Surfboard-tg-vless | 6228 | yes | 2.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 4900 | yes | 0.56 | 0 |
| mahdibland-V2RayAggregator | 4624 | yes | 2.23 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.05 | 0 |
| DeltaKronecker-all | 2734 | yes | 4.0 | 0 |

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
| 204 | 44 |
| test_one_timeout | 44 |
| speed | 15 |
| cn-block | 14 |
| geo | 4 |
