# AutoNodes 每日报告

生成时间：2026-10-25 05:00:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 96475 |
| 去重后节点数 | 27106 |
| TCP 可达数 | 3000 |
| 真测通过数 | 471 |
| verified 输出数 | 104 |
| global 输出数 | 300 |
| all 输出数 | 27106 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.6 |
| fetch | 5.3 |
| generate | 10.9 |
| geo | 1.5 |
| probe | 79.5 |
| real_test | 86.9 |
| tcp | 77.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 82 | 80 | 2 | 97.6% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 125 | 122 | 3 | 97.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 42 | 41 | 1 | 97.6% |
| vless | 362 | 212 | 150 | 58.6% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 97 |
| geo:ClientOSError | 28 |
| speed:ClientOSError | 15 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6279 |
| ConnectionRefusedError | 1079 |
| gaierror | 312 |
| OSError | 236 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.98 | prefer | 88 | 0.966 | 604 |
| Au1rxx-base64 | 0.926 | prefer | 321 | 0.863 | 1625 |
| Surfboard-tg-mixed | 0.835 | prefer | 14 | 1.0 | 7102 |
| mheidari-all | 0.522 | observe | 195 | 0.441 | 24115 |
| DeltaKronecker-all | 0.48 | observe | 4 | 1.0 | 3780 |
| SoliSpirit-all | 0.438 | observe | 3 | 1.0 | 10204 |
| tg-oneclickvpnkeys | 0.273 | observe | 3 | 0.667 | 107 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 179 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4911 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 499 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 390 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 385 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 268 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 246 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 245 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 134 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.441 | 86 | 109 | 195 |
| tg-oneclickvpnkeys | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.863 | 277 | 44 | 321 |
| ermaozi | 0.966 | 85 | 3 | 88 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 3 | 0 | 3 |
| DeltaKronecker-all | 1.0 | 4 | 0 | 4 |
| Surfboard-tg-mixed | 1.0 | 14 | 0 | 14 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24115 | yes | 4.71 | 0 |
| SoliSpirit-all | 10204 | yes | 1.89 | 0 |
| Epodonios-all | 7585 | yes | 2.5 | 0 |
| Surfboard-tg-mixed | 7102 | yes | 3.39 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.66 | 0 |
| barry-far-vless | 5635 | yes | 0.75 | 0 |
| Surfboard-tg-vless | 5419 | yes | 3.17 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 0.58 | 0 |
| mahdibland-V2RayAggregator | 4186 | yes | 2.56 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.95 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 97 |
| geo | 30 |
| speed | 16 |
| cn-block | 10 |
| 204 | 4 |
