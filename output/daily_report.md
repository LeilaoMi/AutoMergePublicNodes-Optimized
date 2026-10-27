# AutoNodes 每日报告

生成时间：2026-10-27 22:30:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 4/88 |
| 原始节点数 | 97513 |
| 去重后节点数 | 26753 |
| TCP 可达数 | 3000 |
| 真测通过数 | 459 |
| verified 输出数 | 85 |
| global 输出数 | 300 |
| all 输出数 | 26753 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.5 |
| fetch | 7.1 |
| generate | 14.1 |
| geo | 1.5 |
| probe | 89.6 |
| real_test | 76.9 |
| tcp | 78.4 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 28 | 0 | 100.0% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 169 | 160 | 9 | 94.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 71 | 70 | 1 | 98.6% |
| vless | 244 | 187 | 57 | 76.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 41 |
| 204:ProxyError | 6 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| geo:ClientOSError | 4 |
| geo:TimeoutError | 1 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6249 |
| ConnectionRefusedError | 1099 |
| gaierror | 348 |
| OSError | 239 |
| SSRFBlocked | 5 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.988 | prefer | 28 | 1.0 | 535 |
| Surfboard-tg-mixed | 0.951 | prefer | 60 | 0.883 | 7532 |
| Au1rxx-base64 | 0.947 | prefer | 375 | 0.88 | 1730 |
| mheidari-all | 0.849 | prefer | 50 | 0.78 | 24397 |
| DeltaKronecker-all | 0.352 | observe | 6 | 0.5 | 3052 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10927 |
| roosterkid-openproxylist-v2ray | 0.326 | observe | 4 | 0.75 | 150 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 508 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 399 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 394 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 277 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 255 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 254 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 246 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 224 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 143 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.5 | 3 | 3 | 6 |
| roosterkid-openproxylist-v2ray | 0.75 | 3 | 1 | 4 |
| mheidari-all | 0.78 | 39 | 11 | 50 |
| Au1rxx-base64 | 0.88 | 330 | 45 | 375 |
| Surfboard-tg-mixed | 0.883 | 53 | 7 | 60 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 28 | 0 | 28 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24397 | yes | 5.77 | 0 |
| SoliSpirit-all | 10927 | yes | 4.96 | 0 |
| Surfboard-tg-mixed | 7532 | yes | 3.88 | 0 |
| Epodonios-all | 7530 | yes | 6.12 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 5538 | yes | 3.46 | 0 |
| barry-far-vless | 5531 | yes | 1.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 2.5 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 3.54 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.8 | 0 |

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
| test_one_timeout | 41 |
| 204 | 11 |
| cn-block | 9 |
| geo | 6 |
| speed | 1 |
