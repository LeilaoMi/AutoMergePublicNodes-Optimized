# AutoNodes 每日报告

生成时间：2026-09-19 10:49:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 87584 |
| 去重后节点数 | 25146 |
| TCP 可达数 | 3000 |
| 真测通过数 | 480 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25146 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 95.4 |
| geo | 1.4 |
| probe | 214.3 |
| real_test | 246.3 |
| tcp | 40.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 50 | 38 | 12 | 76.0% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 165 | 150 | 15 | 90.9% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 32 | 14 | 18 | 43.8% |
| vless | 426 | 261 | 165 | 61.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 42 |
| cn-block:ClientOSError | 34 |
| 204:TimeoutError | 32 |
| geo:TimeoutError | 26 |
| cn-block:TimeoutError | 21 |
| speed:TimeoutError | 21 |
| 204:ProxyError | 17 |
| speed:ClientOSError | 14 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5491 |
| ConnectionRefusedError | 901 |
| gaierror | 467 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.909 | prefer | 310 | 0.848 | 1569 |
| ermaozi | 0.745 | prefer | 50 | 0.74 | 358 |
| Surfboard-tg-mixed | 0.67 | observe | 225 | 0.591 | 7474 |
| mheidari-all | 0.512 | observe | 93 | 0.43 | 19088 |
| DeltaKronecker-all | 0.352 | observe | 11 | 0.364 | 6421 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4251 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| ermaozi-get_subscribe | 0.27 | observe | 1 | 1.0 | 387 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5174 |
| Epodonios-all | 0.255 | observe | 0 | None | 7699 |

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

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.364 | 4 | 7 | 11 |
| mheidari-all | 0.43 | 40 | 53 | 93 |
| Surfboard-tg-mixed | 0.591 | 133 | 92 | 225 |
| ermaozi | 0.74 | 37 | 13 | 50 |
| Au1rxx-base64 | 0.848 | 263 | 47 | 310 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19088 | yes | 3.52 | 0 |
| SoliSpirit-all | 8837 | yes | 3.25 | 0 |
| Epodonios-all | 7699 | yes | 2.25 | 0 |
| Surfboard-tg-mixed | 7474 | yes | 2.95 | 0 |
| DeltaKronecker-all | 6421 | yes | 3.78 | 0 |
| Surfboard-tg-vless | 6006 | yes | 2.78 | 0 |
| barry-far-vless | 5996 | yes | 0.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 5174 | yes | 1.02 | 0 |
| mahdibland-V2RayAggregator | 4251 | yes | 0.5 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.37 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 70 |
| cn-block | 58 |
| 204 | 51 |
| speed | 35 |
