# AutoNodes 每日报告

生成时间：2026-11-15 06:53:29

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 4/84 |
| 原始节点数 | 83136 |
| 去重后节点数 | 27053 |
| TCP 可达数 | 3000 |
| 真测通过数 | 449 |
| verified 输出数 | 67 |
| global 输出数 | 300 |
| all 输出数 | 27053 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.3 |
| fetch | 6.9 |
| generate | 15.0 |
| geo | 1.5 |
| probe | 95.9 |
| real_test | 78.0 |
| tcp | 78.5 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 0 | 2 | 0.0% |
| http | 40 | 38 | 2 | 95.0% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 224 | 204 | 20 | 91.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 118 | 101 | 17 | 85.6% |
| vless | 150 | 94 | 56 | 62.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 54 |
| 204:ProxyError | 12 |
| 204:TimeoutError | 6 |
| 204:ClientOSError | 5 |
| speed:ClientOSError | 5 |
| cn-block:ProxyError | 5 |
| speed:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| speed:TimeoutError | 2 |
| geo:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6024 |
| ConnectionRefusedError | 975 |
| gaierror | 257 |
| OSError | 240 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.944 | prefer | 167 | 0.868 | 9013 |
| ermaozi | 0.93 | prefer | 41 | 0.927 | 576 |
| mheidari-all | 0.863 | prefer | 127 | 0.787 | 13787 |
| Au1rxx-base64 | 0.86 | prefer | 203 | 0.793 | 1751 |
| xiaoji235-airport-v2ray-all | 0.446 | observe | 8 | 0.625 | 6752 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2652 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4966 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11652 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6319 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-VmessProtocol | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-freeiranianv2rey | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 451 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 446 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 329 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 307 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 306 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 298 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 276 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 271 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 182 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.625 | 5 | 3 | 8 |
| mheidari-all | 0.787 | 100 | 27 | 127 |
| Au1rxx-base64 | 0.793 | 161 | 42 | 203 |
| Surfboard-tg-mixed | 0.868 | 145 | 22 | 167 |
| ermaozi | 0.927 | 38 | 3 | 41 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13787 | yes | 5.23 | 0 |
| SoliSpirit-all | 11652 | yes | 2.56 | 0 |
| Surfboard-tg-mixed | 9013 | yes | 3.88 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.0 | 0 |
| barry-far-vless | 6500 | yes | 1.05 | 0 |
| Surfboard-tg-vless | 6319 | yes | 4.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 4966 | yes | 1.42 | 0 |
| mahdibland-V2RayAggregator | 4584 | yes | 3.14 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.17 | 0 |
| DeltaKronecker-all | 2652 | yes | 6.41 | 0 |

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
| test_one_timeout | 54 |
| 204 | 23 |
| speed | 10 |
| cn-block | 8 |
| geo | 2 |
