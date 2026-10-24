# AutoNodes 每日报告

生成时间：2026-10-24 21:03:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 97014 |
| 去重后节点数 | 27063 |
| TCP 可达数 | 3000 |
| 真测通过数 | 330 |
| verified 输出数 | 81 |
| global 输出数 | 300 |
| all 输出数 | 27063 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.6 |
| fetch | 7.4 |
| generate | 14.3 |
| geo | 1.5 |
| probe | 93.7 |
| real_test | 68.3 |
| tcp | 80.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 45 | 5 | 90.0% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 115 | 111 | 4 | 96.5% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 38 | 24 | 14 | 63.2% |
| vless | 204 | 137 | 67 | 67.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 58 |
| 204:TimeoutError | 9 |
| cn-block:TimeoutError | 6 |
| geo:ClientOSError | 5 |
| 204:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ClientOSError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |
| 204:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6384 |
| ConnectionRefusedError | 1075 |
| gaierror | 293 |
| OSError | 236 |
| SSRFBlocked | 4 |
| ConnectionResetError | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.939 | prefer | 46 | 0.935 | 567 |
| Au1rxx-base64 | 0.854 | prefer | 296 | 0.791 | 1623 |
| mheidari-all | 0.83 | prefer | 62 | 0.758 | 24512 |
| Surfboard-tg-mixed | 0.352 | observe | 11 | 0.364 | 7114 |
| tg-oneclickvpnkeys | 0.324 | observe | 4 | 0.75 | 107 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4911 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3780 |
| Epodonios-all | 0.255 | observe | 0 | None | 7708 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 498 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 389 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 384 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 267 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 245 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 133 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 2 | 2 |
| Surfboard-tg-mixed | 0.364 | 4 | 7 | 11 |
| tg-oneclickvpnkeys | 0.75 | 3 | 1 | 4 |
| mheidari-all | 0.758 | 47 | 15 | 62 |
| Au1rxx-base64 | 0.791 | 234 | 62 | 296 |
| ermaozi | 0.935 | 43 | 3 | 46 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24512 | yes | 6.63 | 0 |
| SoliSpirit-all | 10157 | yes | 2.99 | 0 |
| Epodonios-all | 7708 | yes | 5.49 | 0 |
| Surfboard-tg-mixed | 7114 | yes | 3.91 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.33 | 0 |
| barry-far-vless | 5771 | yes | 1.32 | 0 |
| Surfboard-tg-vless | 5485 | yes | 3.67 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 1.65 | 0 |
| mahdibland-V2RayAggregator | 4150 | yes | 2.91 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 58 |
| 204 | 14 |
| cn-block | 11 |
| geo | 7 |
| speed | 3 |
