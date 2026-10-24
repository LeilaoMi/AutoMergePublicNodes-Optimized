# AutoNodes 每日报告

生成时间：2026-10-24 16:08:49

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 93158 |
| 去重后节点数 | 24623 |
| TCP 可达数 | 3000 |
| 真测通过数 | 297 |
| verified 输出数 | 65 |
| global 输出数 | 300 |
| all 输出数 | 24623 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 22.1 |
| fetch | 5.2 |
| generate | 9.6 |
| geo | 1.4 |
| probe | 77.6 |
| real_test | 64.8 |
| tcp | 77.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 46 | 42 | 4 | 91.3% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 109 | 100 | 9 | 91.7% |
| socks | 4 | 0 | 4 | 0.0% |
| trojan | 10 | 9 | 1 | 90.0% |
| vless | 188 | 135 | 53 | 71.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 43 |
| 204:ProxyError | 6 |
| 204:TimeoutError | 5 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:TimeoutError | 2 |
| speed:ClientOSError | 2 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6386 |
| ConnectionRefusedError | 1041 |
| OSError | 239 |
| gaierror | 177 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.934 | prefer | 43 | 0.93 | 567 |
| Au1rxx-base64 | 0.879 | prefer | 258 | 0.818 | 1587 |
| mheidari-all | 0.753 | prefer | 50 | 0.68 | 24286 |
| Surfboard-tg-vless | 0.519 | observe | 5 | 1.0 | 5474 |
| Surfboard-tg-mixed | 0.373 | observe | 5 | 0.6 | 7219 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4911 |
| Epodonios-all | 0.255 | observe | 0 | None | 7679 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ermaozi-get_subscribe | 0.144 | observe | 1 | 0.0 | 0 | 410 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 497 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 388 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 383 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 132 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.6 | 3 | 2 | 5 |
| mheidari-all | 0.68 | 34 | 16 | 50 |
| Au1rxx-base64 | 0.818 | 211 | 47 | 258 |
| ermaozi | 0.93 | 40 | 3 | 43 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24286 | yes | 3.1 | 0 |
| SoliSpirit-all | 10364 | yes | 5.24 | 0 |
| Epodonios-all | 7679 | yes | 3.78 | 0 |
| Surfboard-tg-mixed | 7219 | yes | 4.58 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.23 | 0 |
| barry-far-vless | 5757 | yes | 3.82 | 0 |
| Surfboard-tg-vless | 5474 | yes | 4.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 2.15 | 0 |
| mahdibland-V2RayAggregator | 4150 | yes | 0.72 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.22 | 0 |

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
| test_one_timeout | 43 |
| 204 | 15 |
| cn-block | 9 |
| geo | 3 |
| speed | 2 |
