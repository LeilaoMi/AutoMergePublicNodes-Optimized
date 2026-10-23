# AutoNodes 每日报告

生成时间：2026-10-23 21:35:57

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 92424 |
| 去重后节点数 | 24537 |
| TCP 可达数 | 3000 |
| 真测通过数 | 330 |
| verified 输出数 | 83 |
| global 输出数 | 300 |
| all 输出数 | 24537 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.4 |
| fetch | 6.8 |
| generate | 11.7 |
| geo | 1.5 |
| probe | 87.5 |
| real_test | 70.7 |
| tcp | 74.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 55 | 51 | 4 | 92.7% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 113 | 107 | 6 | 94.7% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 22 | 22 | 0 | 100.0% |
| vless | 207 | 143 | 64 | 69.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 50 |
| cn-block:TimeoutError | 8 |
| 204:TimeoutError | 6 |
| geo:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| speed:ClientOSError | 2 |
| speed:ProxyError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6208 |
| ConnectionRefusedError | 1057 |
| OSError | 237 |
| gaierror | 235 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.947 | prefer | 51 | 0.941 | 555 |
| Au1rxx-base64 | 0.86 | prefer | 268 | 0.799 | 1594 |
| mheidari-all | 0.826 | prefer | 57 | 0.754 | 23638 |
| Surfboard-tg-mixed | 0.749 | prefer | 13 | 0.923 | 7184 |
| roosterkid-openproxylist-v2ray | 0.433 | observe | 8 | 0.75 | 150 |
| Surfboard-tg-vless | 0.391 | observe | 2 | 1.0 | 5437 |
| 10ium-HighSpeed | 0.345 | observe | 2 | 1.0 | 839 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10312 |
| tg-oneclickvpnkeys | 0.324 | observe | 4 | 0.75 | 92 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 175 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 494 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 385 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 380 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 263 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 129 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.75 | 3 | 1 | 4 |
| roosterkid-openproxylist-v2ray | 0.75 | 6 | 2 | 8 |
| mheidari-all | 0.754 | 43 | 14 | 57 |
| Au1rxx-base64 | 0.799 | 214 | 54 | 268 |
| Surfboard-tg-mixed | 0.923 | 12 | 1 | 13 |
| ermaozi | 0.941 | 48 | 3 | 51 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23638 | yes | 5.34 | 0 |
| SoliSpirit-all | 10312 | yes | 3.25 | 0 |
| Epodonios-all | 7680 | yes | 3.61 | 0 |
| Surfboard-tg-mixed | 7184 | yes | 3.4 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.2 | 0 |
| barry-far-vless | 5798 | yes | 1.42 | 0 |
| Surfboard-tg-vless | 5437 | yes | 3.17 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 1.61 | 0 |
| mahdibland-V2RayAggregator | 4117 | yes | 2.95 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.32 | 0 |

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
| test_one_timeout | 50 |
| cn-block | 11 |
| 204 | 10 |
| geo | 3 |
| speed | 3 |
