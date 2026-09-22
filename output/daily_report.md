# AutoNodes 每日报告

生成时间：2026-09-22 04:28:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/3 |
| 清理建议：优先/观察 | 1/103 |
| 原始节点数 | 91704 |
| 去重后节点数 | 25163 |
| TCP 可达数 | 3000 |
| 真测通过数 | 569 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25163 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 80.8 |
| geo | 1.5 |
| probe | 299.1 |
| real_test | 309.3 |
| tcp | 42.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 49 | 31 | 18 | 63.3% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 168 | 162 | 6 | 96.4% |
| socks | 5 | 1 | 4 | 20.0% |
| trojan | 35 | 26 | 9 | 74.3% |
| vless | 671 | 330 | 341 | 49.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 88 |
| geo:ClientOSError | 71 |
| speed:ClientOSError | 60 |
| cn-block:ClientOSError | 40 |
| 204:ProxyError | 37 |
| speed:TimeoutError | 35 |
| cn-block:TimeoutError | 19 |
| 204:TimeoutError | 18 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5905 |
| ConnectionRefusedError | 931 |
| gaierror | 315 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.907 | prefer | 305 | 0.843 | 1658 |
| Surfboard-tg-mixed | 0.673 | observe | 229 | 0.594 | 7121 |
| ermaozi | 0.623 | observe | 49 | 0.612 | 369 |
| mheidari-all | 0.582 | observe | 275 | 0.502 | 19852 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7572 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8704 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5672 |
| barry-far-vless | 0.255 | observe | 0 | None | 5888 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | 10ium-ScrapeCategorize-Vless | 0.148 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.163 | 70 | 0.071 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ermaozi-get_subscribe | 0.235 | 5 | 0.4 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 6 | 6 |
| DeltaKronecker-all | 0.071 | 5 | 65 | 70 |
| ermaozi-get_subscribe | 0.4 | 2 | 3 | 5 |
| mheidari-all | 0.502 | 138 | 137 | 275 |
| Surfboard-tg-mixed | 0.594 | 136 | 93 | 229 |
| ermaozi | 0.612 | 30 | 19 | 49 |
| Au1rxx-base64 | 0.843 | 257 | 48 | 305 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19852 | yes | 5.91 | 0 |
| SoliSpirit-all | 8704 | yes | 3.29 | 0 |
| Epodonios-all | 7572 | yes | 6.22 | 0 |
| Surfboard-tg-mixed | 7121 | yes | 3.71 | 0 |
| DeltaKronecker-all | 6181 | yes | 5.2 | 0 |
| barry-far-vless | 5888 | yes | 2.35 | 0 |
| Surfboard-tg-vless | 5672 | yes | 3.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 5290 | yes | 2.14 | 0 |
| mahdibland-V2RayAggregator | 4344 | yes | 2.2 | 0 |
| xiaoji235-airport-v2ray-all | 4242 | yes | 2.92 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 161 |
| speed | 95 |
| 204 | 61 |
| cn-block | 61 |
