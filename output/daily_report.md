# AutoNodes 每日报告

生成时间：2026-11-03 07:03:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 17/1 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 81802 |
| 去重后节点数 | 26687 |
| TCP 可达数 | 3000 |
| 真测通过数 | 392 |
| verified 输出数 | 34 |
| global 输出数 | 300 |
| all 输出数 | 26687 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 22.2 |
| fetch | 7.2 |
| generate | 15.1 |
| geo | 1.5 |
| probe | 98.1 |
| real_test | 67.8 |
| tcp | 78.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 21 | 20 | 1 | 95.2% |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 164 | 146 | 18 | 89.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 138 | 101 | 37 | 73.2% |
| vless | 191 | 112 | 79 | 58.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 79 |
| geo:ClientOSError | 28 |
| 204:ProxyError | 17 |
| 204:TimeoutError | 5 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 2 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5961 |
| ConnectionRefusedError | 974 |
| OSError | 233 |
| gaierror | 223 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 43 |
| Au1rxx-base64 | 0.909 | prefer | 283 | 0.841 | 1751 |
| mheidari-all | 0.887 | prefer | 55 | 0.818 | 14871 |
| Surfboard-tg-mixed | 0.694 | observe | 138 | 0.616 | 8355 |
| ninja-vless | 0.383 | observe | 2 | 1.0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4941 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2726 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10703 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| peasoft-NoMoreWalls | 0.039 | downweight | 30 | 0.0 | 0 | 200 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 417 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 412 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 295 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 273 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 272 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 264 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 161 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 148 | 连续死亡次数 >= 2 |
| downweight | peasoft-NoMoreWalls | 0.039 | 30 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| peasoft-NoMoreWalls | 0.0 | 0 | 30 | 30 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.616 | 85 | 53 | 138 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.818 | 45 | 10 | 55 |
| Au1rxx-base64 | 0.841 | 238 | 45 | 283 |
| ninja-vless | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14871 | yes | 5.5 | 0 |
| SoliSpirit-all | 10703 | yes | 2.34 | 0 |
| Surfboard-tg-mixed | 8355 | yes | 4.48 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.1 | 0 |
| barry-far-vless | 6133 | yes | 1.26 | 0 |
| Surfboard-tg-vless | 5917 | yes | 3.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 4941 | yes | 1.54 | 0 |
| mahdibland-V2RayAggregator | 4734 | yes | 1.55 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.91 | 0 |
| DeltaKronecker-all | 2726 | yes | 5.16 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 79 |
| geo | 28 |
| 204 | 25 |
| cn-block | 6 |
| speed | 2 |
