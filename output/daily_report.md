# AutoNodes 每日报告

生成时间：2026-11-19 20:53:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 83175 |
| 去重后节点数 | 27828 |
| TCP 可达数 | 3000 |
| 真测通过数 | 416 |
| verified 输出数 | 65 |
| global 输出数 | 300 |
| all 输出数 | 27828 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 35.9 |
| fetch | 4.9 |
| generate | 11.0 |
| geo | 1.4 |
| probe | 76.9 |
| real_test | 80.0 |
| tcp | 83.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 26 | 25 | 1 | 96.2% |
| hysteria2 | 10 | 8 | 2 | 80.0% |
| shadowsocks | 266 | 244 | 22 | 91.7% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 58 | 19 | 39 | 32.8% |
| vless | 172 | 121 | 51 | 70.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 56 |
| 204:ProxyError | 34 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 5 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 1 |
| speed:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6539 |
| ConnectionRefusedError | 1004 |
| OSError | 239 |
| gaierror | 180 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.981 | prefer | 24 | 1.0 | 491 |
| mheidari-all | 0.928 | prefer | 77 | 0.857 | 14706 |
| Surfboard-tg-mixed | 0.857 | prefer | 272 | 0.779 | 8602 |
| Au1rxx-base64 | 0.784 | prefer | 145 | 0.717 | 1751 |
| roosterkid-openproxylist-v2ray | 0.55 | observe | 11 | 0.818 | 150 |
| tg-LonUp_M | 0.407 | observe | 4 | 1.0 | 179 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2728 |
| mahdibland-V2RayAggregator | 0.287 | observe | 2 | 0.5 | 4507 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4935 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 460 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 455 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 338 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 316 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 315 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 307 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 285 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 280 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mahdibland-V2RayAggregator | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.717 | 104 | 41 | 145 |
| Surfboard-tg-mixed | 0.779 | 212 | 60 | 272 |
| roosterkid-openproxylist-v2ray | 0.818 | 9 | 2 | 11 |
| mheidari-all | 0.857 | 66 | 11 | 77 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 4 | 0 | 4 |
| ermaozi | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14706 | yes | 4.43 | 0 |
| SoliSpirit-all | 12076 | yes | 2.88 | 0 |
| Surfboard-tg-mixed | 8602 | yes | 3.9 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.21 | 0 |
| Surfboard-tg-vless | 5937 | yes | 3.38 | 0 |
| barry-far-vless | 5868 | yes | 1.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 4935 | yes | 1.73 | 0 |
| mahdibland-V2RayAggregator | 4507 | yes | 2.09 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.8 | 0 |
| DeltaKronecker-all | 2728 | yes | 3.95 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 56 |
| 204 | 43 |
| cn-block | 11 |
| speed | 3 |
| geo | 3 |
