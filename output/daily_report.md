# AutoNodes 每日报告

生成时间：2026-11-03 19:43:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 2/88 |
| 原始节点数 | 83456 |
| 去重后节点数 | 26791 |
| TCP 可达数 | 3000 |
| 真测通过数 | 362 |
| verified 输出数 | 37 |
| global 输出数 | 300 |
| all 输出数 | 26791 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 20.5 |
| fetch | 7.2 |
| generate | 14.4 |
| geo | 1.5 |
| probe | 99.3 |
| real_test | 74.9 |
| tcp | 78.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 21 | 0 | 100.0% |
| hysteria2 | 15 | 11 | 4 | 73.3% |
| shadowsocks | 189 | 164 | 25 | 86.8% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 68 | 46 | 22 | 67.6% |
| vless | 245 | 120 | 125 | 49.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 86 |
| geo:ClientOSError | 40 |
| 204:TimeoutError | 15 |
| 204:ProxyError | 14 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| speed:ClientOSError | 3 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6048 |
| ConnectionRefusedError | 964 |
| OSError | 233 |
| gaierror | 192 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.978 | prefer | 20 | 1.0 | 592 |
| Au1rxx-base64 | 0.783 | prefer | 266 | 0.714 | 1751 |
| mheidari-all | 0.673 | observe | 244 | 0.594 | 15211 |
| Surfboard-tg-mixed | 0.401 | observe | 7 | 0.571 | 8613 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 122 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5017 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2526 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
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
| disable | tg-Letiranbreath | 0.0 | 0 | None | 418 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 413 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 296 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 274 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 273 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 265 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 162 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 149 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.571 | 4 | 3 | 7 |
| mheidari-all | 0.594 | 145 | 99 | 244 |
| Au1rxx-base64 | 0.714 | 190 | 76 | 266 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15211 | yes | 5.05 | 0 |
| SoliSpirit-all | 10863 | yes | 3.08 | 0 |
| Surfboard-tg-mixed | 8613 | yes | 4.02 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.53 | 0 |
| barry-far-vless | 6302 | yes | 0.98 | 0 |
| Surfboard-tg-vless | 6089 | yes | 4.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 5017 | yes | 1.77 | 0 |
| mahdibland-V2RayAggregator | 4753 | yes | 0.84 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.61 | 0 |
| DeltaKronecker-all | 2526 | yes | 6.05 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 86 |
| geo | 40 |
| 204 | 32 |
| cn-block | 13 |
| speed | 7 |
