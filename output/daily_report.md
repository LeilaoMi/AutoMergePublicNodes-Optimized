# AutoNodes 每日报告

生成时间：2026-11-20 07:34:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 82463 |
| 去重后节点数 | 27651 |
| TCP 可达数 | 3000 |
| 真测通过数 | 430 |
| verified 输出数 | 60 |
| global 输出数 | 300 |
| all 输出数 | 27651 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 23.8 |
| fetch | 6.9 |
| generate | 15.5 |
| geo | 1.5 |
| probe | 97.6 |
| real_test | 63.2 |
| tcp | 81.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 11 | 8 | 3 | 72.7% |
| shadowsocks | 258 | 230 | 28 | 89.1% |
| socks | 6 | 6 | 0 | 100.0% |
| trojan | 54 | 34 | 20 | 63.0% |
| vless | 170 | 135 | 35 | 79.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 44 |
| 204:ProxyError | 14 |
| cn-block:ClientOSError | 9 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| 204:TimeoutError | 3 |
| geo:ProxyError | 2 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6239 |
| ConnectionRefusedError | 976 |
| gaierror | 260 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.98 | prefer | 24 | 1.0 | 469 |
| Surfboard-tg-mixed | 0.948 | prefer | 142 | 0.873 | 8500 |
| mheidari-all | 0.933 | prefer | 189 | 0.857 | 14360 |
| Au1rxx-base64 | 0.831 | prefer | 165 | 0.764 | 1751 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4935 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2728 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 11813 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5726 |
| barry-far-vless | 0.255 | observe | 0 | None | 6117 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 139 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| ripaojiedian-freenode | 0.175 | observe | 0 | None | 0 | 12 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 461 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 456 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 339 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 317 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 316 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 308 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 286 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 281 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.764 | 126 | 39 | 165 |
| mheidari-all | 0.857 | 162 | 27 | 189 |
| Surfboard-tg-mixed | 0.873 | 124 | 18 | 142 |
| ermaozi | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14360 | yes | 4.57 | 0 |
| SoliSpirit-all | 11813 | yes | 5.77 | 0 |
| Surfboard-tg-mixed | 8500 | yes | 4.89 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.99 | 0 |
| barry-far-vless | 6117 | yes | 3.15 | 0 |
| Surfboard-tg-vless | 5726 | yes | 4.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 4935 | yes | 3.37 | 0 |
| mahdibland-V2RayAggregator | 4501 | yes | 3.18 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.71 | 0 |
| DeltaKronecker-all | 2728 | yes | 5.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 44 |
| 204 | 23 |
| cn-block | 15 |
| geo | 2 |
| speed | 2 |
