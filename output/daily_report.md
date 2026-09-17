# AutoNodes 每日报告

生成时间：2026-09-17 21:18:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 84619 |
| 去重后节点数 | 23068 |
| TCP 可达数 | 3000 |
| 真测通过数 | 438 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23068 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 84.4 |
| geo | 1.4 |
| probe | 196.4 |
| real_test | 188.2 |
| tcp | 36.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 20 | 9 | 11 | 45.0% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 159 | 146 | 13 | 91.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 11 | 11 | 0 | 100.0% |
| vless | 296 | 252 | 44 | 85.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 13 |
| geo:ClientOSError | 9 |
| geo:TimeoutError | 9 |
| 204:TimeoutError | 8 |
| speed:ClientOSError | 6 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 2 |
| speed:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4494 |
| ConnectionRefusedError | 838 |
| gaierror | 391 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.989 | prefer | 31 | 0.935 | 16164 |
| Au1rxx-base64 | 0.986 | prefer | 265 | 0.925 | 1619 |
| DeltaKronecker-all | 0.893 | prefer | 121 | 0.818 | 5931 |
| Surfboard-tg-mixed | 0.886 | prefer | 65 | 0.815 | 7499 |
| ermaozi | 0.449 | observe | 16 | 0.5 | 357 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4261 |
| Epodonios-all | 0.255 | observe | 0 | None | 7954 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8875 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5936 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.234 | 5 | 0.4 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.4 | 2 | 3 | 5 |
| roosterkid-openproxylist-v2ray | 0.5 | 1 | 1 | 2 |
| ermaozi | 0.5 | 8 | 8 | 16 |
| Surfboard-tg-mixed | 0.815 | 53 | 12 | 65 |
| DeltaKronecker-all | 0.818 | 99 | 22 | 121 |
| Au1rxx-base64 | 0.925 | 245 | 20 | 265 |
| mheidari-all | 0.935 | 29 | 2 | 31 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16164 | yes | 5.32 | 0 |
| SoliSpirit-all | 8875 | yes | 4.3 | 0 |
| Epodonios-all | 7954 | yes | 3.31 | 0 |
| Surfboard-tg-mixed | 7499 | yes | 4.56 | 0 |
| barry-far-vless | 6157 | yes | 2.54 | 0 |
| Surfboard-tg-vless | 5936 | yes | 4.22 | 0 |
| DeltaKronecker-all | 5931 | yes | 4.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 5093 | yes | 2.33 | 0 |
| mahdibland-V2RayAggregator | 4261 | yes | 1.48 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.89 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 23 |
| cn-block | 19 |
| geo | 19 |
| speed | 9 |
