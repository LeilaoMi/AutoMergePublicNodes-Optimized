# AutoNodes 每日报告

生成时间：2026-11-07 13:21:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 82306 |
| 去重后节点数 | 26976 |
| TCP 可达数 | 3000 |
| 真测通过数 | 343 |
| verified 输出数 | 68 |
| global 输出数 | 300 |
| all 输出数 | 26976 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 20.1 |
| fetch | 4.9 |
| generate | 10.6 |
| geo | 1.4 |
| probe | 79.7 |
| real_test | 64.0 |
| tcp | 78.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 3 | 0 | 100.0% |
| http | 19 | 18 | 1 | 94.7% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 154 | 148 | 6 | 96.1% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 82 | 71 | 11 | 86.6% |
| vless | 160 | 91 | 69 | 56.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 46 |
| 204:ProxyError | 22 |
| 204:TimeoutError | 10 |
| cn-block:TimeoutError | 4 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| 204:ServerDisconnectedError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6102 |
| ConnectionRefusedError | 1018 |
| gaierror | 241 |
| OSError | 235 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.896 | prefer | 19 | 0.947 | 515 |
| Au1rxx-base64 | 0.873 | prefer | 237 | 0.806 | 1751 |
| mheidari-all | 0.833 | prefer | 152 | 0.757 | 14331 |
| DeltaKronecker-all | 0.646 | observe | 13 | 0.769 | 2734 |
| Surfboard-tg-mixed | 0.465 | observe | 7 | 0.714 | 8637 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 6752 |
| ermaozi-get_subscribe | 0.326 | observe | 2 | 1.0 | 366 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 176 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4866 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 427 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 422 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 305 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 283 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 282 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 274 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 252 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 247 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 171 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 158 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.714 | 5 | 2 | 7 |
| mheidari-all | 0.757 | 115 | 37 | 152 |
| DeltaKronecker-all | 0.769 | 10 | 3 | 13 |
| Au1rxx-base64 | 0.806 | 191 | 46 | 237 |
| ermaozi | 0.947 | 18 | 1 | 19 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14331 | yes | 2.65 | 0 |
| SoliSpirit-all | 11009 | yes | 2.96 | 0 |
| Surfboard-tg-mixed | 8637 | yes | 3.71 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.21 | 0 |
| barry-far-vless | 6359 | yes | 2.28 | 0 |
| Surfboard-tg-vless | 6148 | yes | 3.0 | 0 |
| 10ium-ScrapeCategorize-Vless | 4866 | yes | 2.64 | 0 |
| mahdibland-V2RayAggregator | 4522 | yes | 2.2 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.5 | 0 |
| DeltaKronecker-all | 2734 | yes | 4.27 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 46 |
| 204 | 34 |
| cn-block | 8 |
| geo | 2 |
