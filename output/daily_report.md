# AutoNodes 每日报告

生成时间：2026-10-26 05:04:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 2/90 |
| 原始节点数 | 98294 |
| 去重后节点数 | 27405 |
| TCP 可达数 | 3000 |
| 真测通过数 | 494 |
| verified 输出数 | 117 |
| global 输出数 | 300 |
| all 输出数 | 27405 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.2 |
| fetch | 7.2 |
| generate | 14.2 |
| geo | 1.7 |
| probe | 91.8 |
| real_test | 90.7 |
| tcp | 85.4 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 104 | 102 | 2 | 98.1% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 131 | 121 | 10 | 92.4% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 37 | 34 | 3 | 91.9% |
| vless | 371 | 224 | 147 | 60.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 85 |
| speed:ClientOSError | 27 |
| geo:ClientOSError | 20 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 4 |
| geo:ProxyError | 3 |
| 204:TimeoutError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| speed:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6990 |
| ConnectionRefusedError | 1050 |
| OSError | 234 |
| gaierror | 182 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.998 | prefer | 105 | 0.981 | 643 |
| Au1rxx-base64 | 0.872 | prefer | 362 | 0.807 | 1674 |
| mheidari-all | 0.606 | observe | 152 | 0.526 | 24290 |
| Surfboard-tg-mixed | 0.57 | observe | 11 | 0.727 | 7351 |
| DeltaKronecker-all | 0.455 | observe | 22 | 0.364 | 3849 |
| roosterkid-openproxylist-v2ray | 0.364 | observe | 3 | 1.0 | 150 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 7848 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 20 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 503 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 394 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 389 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 272 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 250 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 249 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 138 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.364 | 8 | 14 | 22 |
| mheidari-all | 0.526 | 80 | 72 | 152 |
| Surfboard-tg-mixed | 0.727 | 8 | 3 | 11 |
| Au1rxx-base64 | 0.807 | 292 | 70 | 362 |
| ermaozi | 0.981 | 103 | 2 | 105 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24290 | yes | 6.32 | 0 |
| SoliSpirit-all | 10571 | yes | 2.44 | 0 |
| Epodonios-all | 7848 | yes | 6.66 | 0 |
| Surfboard-tg-mixed | 7351 | yes | 4.54 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.01 | 0 |
| barry-far-vless | 5884 | yes | 0.57 | 0 |
| Surfboard-tg-vless | 5665 | yes | 4.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 0.8 | 0 |
| mahdibland-V2RayAggregator | 4228 | yes | 3.32 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 85 |
| speed | 29 |
| geo | 23 |
| cn-block | 15 |
| 204 | 10 |
