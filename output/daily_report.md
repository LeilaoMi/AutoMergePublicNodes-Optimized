# AutoNodes 每日报告

生成时间：2026-11-05 07:05:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82241 |
| 去重后节点数 | 26663 |
| TCP 可达数 | 3000 |
| 真测通过数 | 398 |
| verified 输出数 | 36 |
| global 输出数 | 300 |
| all 输出数 | 26663 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.8 |
| fetch | 7.1 |
| generate | 14.9 |
| geo | 1.6 |
| probe | 98.7 |
| real_test | 78.5 |
| tcp | 79.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 18 | 2 | 90.0% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 204 | 195 | 9 | 95.6% |
| socks | 4 | 4 | 0 | 100.0% |
| trojan | 67 | 58 | 9 | 86.6% |
| vless | 195 | 115 | 80 | 59.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 66 |
| 204:ProxyError | 12 |
| 204:TimeoutError | 5 |
| cn-block:TimeoutError | 5 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6214 |
| ConnectionRefusedError | 969 |
| OSError | 233 |
| gaierror | 156 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.963 | prefer | 58 | 0.897 | 8675 |
| ermaozi | 0.898 | prefer | 19 | 0.947 | 555 |
| mheidari-all | 0.866 | prefer | 185 | 0.789 | 14576 |
| Au1rxx-base64 | 0.843 | prefer | 236 | 0.775 | 1751 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2526 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10857 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.133 | observe | 1 | 0.0 | 0 | 139 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 422 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 417 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 300 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 278 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 277 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 269 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 247 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 166 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 153 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.775 | 183 | 53 | 236 |
| mheidari-all | 0.789 | 146 | 39 | 185 |
| Surfboard-tg-mixed | 0.897 | 52 | 6 | 58 |
| ermaozi | 0.947 | 18 | 1 | 19 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14576 | yes | 6.34 | 0 |
| SoliSpirit-all | 10857 | yes | 1.93 | 0 |
| Surfboard-tg-mixed | 8675 | yes | 3.76 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.66 | 0 |
| barry-far-vless | 6243 | yes | 1.14 | 0 |
| Surfboard-tg-vless | 6030 | yes | 4.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 1.47 | 0 |
| mahdibland-V2RayAggregator | 4612 | yes | 3.28 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.23 | 0 |
| DeltaKronecker-all | 2526 | yes | 6.4 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 66 |
| 204 | 20 |
| cn-block | 10 |
| geo | 4 |
| speed | 1 |
