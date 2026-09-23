# AutoNodes 每日报告

生成时间：2026-09-23 16:43:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 97200 |
| 去重后节点数 | 26542 |
| TCP 可达数 | 3000 |
| 真测通过数 | 436 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26542 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| generate | 84.4 |
| geo | 1.6 |
| probe | 267.0 |
| real_test | 184.2 |
| tcp | 43.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 36 | 25 | 11 | 69.4% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 170 | 154 | 16 | 90.6% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 5 | 4 | 1 | 80.0% |
| vless | 378 | 233 | 145 | 61.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 48 |
| geo:ClientOSError | 37 |
| 204:TimeoutError | 30 |
| cn-block:TimeoutError | 22 |
| 204:ProxyError | 18 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 3 |
| speed:ClientOSError | 2 |
| geo:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6223 |
| ConnectionRefusedError | 960 |
| gaierror | 317 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.99 | prefer | 273 | 0.927 | 1665 |
| ermaozi | 0.793 | prefer | 30 | 0.8 | 291 |
| Surfboard-tg-mixed | 0.604 | observe | 61 | 0.525 | 7138 |
| mheidari-all | 0.599 | observe | 237 | 0.519 | 22163 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 6471 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 88 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5131 |
| Epodonios-all | 0.255 | observe | 0 | None | 7512 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| downweight | ermaozi-get_subscribe | 0.141 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.143 | 1 | 6 | 7 |
| mheidari-all | 0.519 | 123 | 114 | 237 |
| Surfboard-tg-mixed | 0.525 | 32 | 29 | 61 |
| ermaozi | 0.8 | 24 | 6 | 30 |
| Au1rxx-base64 | 0.927 | 253 | 20 | 273 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22163 | yes | 4.29 | 0 |
| SoliSpirit-all | 9407 | yes | 2.86 | 0 |
| Epodonios-all | 7512 | yes | 4.69 | 0 |
| Surfboard-tg-mixed | 7138 | yes | 3.29 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.58 | 0 |
| DeltaKronecker-all | 6471 | yes | 4.28 | 0 |
| barry-far-vless | 6042 | yes | 1.63 | 0 |
| Surfboard-tg-vless | 5827 | yes | 0.38 | 0 |
| 10ium-ScrapeCategorize-Vless | 5131 | yes | 2.25 | 0 |
| mahdibland-V2RayAggregator | 4187 | yes | 1.34 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 70 |
| 204 | 52 |
| geo | 42 |
| speed | 11 |
