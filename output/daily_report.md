# AutoNodes 每日报告

生成时间：2026-10-31 21:49:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 80795 |
| 去重后节点数 | 26337 |
| TCP 可达数 | 3000 |
| 真测通过数 | 509 |
| verified 输出数 | 99 |
| global 输出数 | 300 |
| all 输出数 | 26337 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 27.7 |
| fetch | 8.7 |
| generate | 12.4 |
| geo | 1.6 |
| probe | 94.4 |
| real_test | 84.2 |
| tcp | 75.6 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 21 | 20 | 1 | 95.2% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 171 | 155 | 16 | 90.6% |
| trojan | 187 | 177 | 10 | 94.7% |
| vless | 228 | 144 | 84 | 63.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 41 |
| geo:ClientOSError | 39 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| cn-block:TimeoutError | 5 |
| 204:TimeoutError | 4 |
| speed:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5543 |
| ConnectionRefusedError | 961 |
| gaierror | 273 |
| OSError | 235 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.959 | prefer | 97 | 0.887 | 14850 |
| Au1rxx-base64 | 0.931 | prefer | 330 | 0.864 | 1751 |
| zhangkai | 0.877 | prefer | 19 | 0.947 | 43 |
| Surfboard-tg-mixed | 0.754 | prefer | 170 | 0.676 | 7936 |
| DeltaKronecker-all | 0.391 | observe | 2 | 1.0 | 2848 |
| ermaozi-get_subscribe | 0.328 | observe | 2 | 1.0 | 412 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| peasoft-NoMoreWalls | 0.264 | observe | 1 | 1.0 | 227 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4970 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 520 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 411 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 406 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 289 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 267 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 258 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 155 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.676 | 115 | 55 | 170 |
| Au1rxx-base64 | 0.864 | 285 | 45 | 330 |
| mheidari-all | 0.887 | 86 | 11 | 97 |
| zhangkai | 0.947 | 18 | 1 | 19 |
| peasoft-NoMoreWalls | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| DeltaKronecker-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14850 | yes | 5.32 | 0 |
| SoliSpirit-all | 10505 | yes | 4.83 | 0 |
| Surfboard-tg-mixed | 7936 | yes | 4.13 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.93 | 0 |
| barry-far-vless | 5849 | yes | 2.63 | 0 |
| Surfboard-tg-vless | 5636 | yes | 3.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4970 | yes | 2.54 | 0 |
| mahdibland-V2RayAggregator | 4635 | yes | 3.11 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.02 | 0 |
| DeltaKronecker-all | 2848 | yes | 5.79 | 0 |

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
| test_one_timeout | 41 |
| geo | 40 |
| 204 | 16 |
| cn-block | 12 |
| speed | 4 |
