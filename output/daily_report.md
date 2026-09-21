# AutoNodes 每日报告

生成时间：2026-09-21 12:39:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 84528 |
| 去重后节点数 | 23451 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23451 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 90.1 |
| geo | 1.5 |
| probe | 219.6 |
| real_test | 233.8 |
| tcp | 38.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 49 | 28 | 21 | 57.1% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 153 | 138 | 15 | 90.2% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 38 | 25 | 13 | 65.8% |
| vless | 378 | 242 | 136 | 64.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 33 |
| 204:ProxyError | 30 |
| geo:TimeoutError | 28 |
| speed:ClientOSError | 23 |
| cn-block:TimeoutError | 20 |
| 204:TimeoutError | 19 |
| speed:TimeoutError | 15 |
| cn-block:ClientOSError | 9 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5283 |
| ConnectionRefusedError | 805 |
| gaierror | 334 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.945 | prefer | 35 | 0.886 | 16192 |
| Au1rxx-base64 | 0.919 | prefer | 271 | 0.856 | 1649 |
| DeltaKronecker-all | 0.767 | prefer | 46 | 0.696 | 6181 |
| Surfboard-tg-mixed | 0.661 | observe | 208 | 0.582 | 7246 |
| ermaozi | 0.544 | observe | 64 | 0.531 | 350 |
| Au1rxx-clash | 0.377 | observe | 2 | 1.0 | 1638 |
| tg-oneclickvpnkeys | 0.316 | observe | 2 | 1.0 | 123 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7697 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.071 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 10 | 10 |
| ermaozi | 0.531 | 34 | 30 | 64 |
| Surfboard-tg-mixed | 0.582 | 121 | 87 | 208 |
| DeltaKronecker-all | 0.696 | 32 | 14 | 46 |
| Au1rxx-base64 | 0.856 | 232 | 39 | 271 |
| mheidari-all | 0.886 | 31 | 4 | 35 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Au1rxx-clash | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16192 | yes | 5.9 | 0 |
| SoliSpirit-all | 8900 | yes | 1.92 | 0 |
| Epodonios-all | 7697 | yes | 6.37 | 0 |
| Surfboard-tg-mixed | 7246 | yes | 3.86 | 0 |
| DeltaKronecker-all | 6181 | yes | 5.06 | 0 |
| barry-far-vless | 6062 | yes | 1.26 | 0 |
| Surfboard-tg-vless | 5845 | yes | 3.59 | 0 |
| 10ium-ScrapeCategorize-Vless | 5290 | yes | 1.54 | 0 |
| mahdibland-V2RayAggregator | 4358 | yes | 3.18 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 0.97 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 64 |
| 204 | 52 |
| speed | 40 |
| cn-block | 30 |
