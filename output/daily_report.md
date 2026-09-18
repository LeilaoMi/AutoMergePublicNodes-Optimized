# AutoNodes 每日报告

生成时间：2026-09-18 20:53:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 87619 |
| 去重后节点数 | 25094 |
| TCP 可达数 | 3000 |
| 真测通过数 | 460 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25094 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 79.2 |
| geo | 1.4 |
| probe | 290.5 |
| real_test | 236.3 |
| tcp | 40.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 33 | 22 | 11 | 66.7% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 158 | 147 | 11 | 93.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 8 | 4 | 4 | 50.0% |
| vless | 425 | 265 | 160 | 62.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 42 |
| geo:ClientOSError | 39 |
| 204:TimeoutError | 28 |
| 204:ProxyError | 20 |
| cn-block:TimeoutError | 20 |
| geo:TimeoutError | 14 |
| speed:ClientOSError | 12 |
| 204:ClientOSError | 5 |
| speed:TimeoutError | 5 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5519 |
| ConnectionRefusedError | 915 |
| gaierror | 488 |
| OSError | 237 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.919 | prefer | 273 | 0.857 | 1615 |
| ermaozi | 0.828 | prefer | 25 | 0.84 | 325 |
| Surfboard-tg-mixed | 0.726 | prefer | 159 | 0.648 | 7333 |
| mheidari-all | 0.642 | observe | 176 | 0.562 | 19747 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4241 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5076 |
| Epodonios-all | 0.255 | observe | 0 | None | 7771 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8922 |

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
| downweight | ermaozi-get_subscribe | 0.136 | 8 | 0.125 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 4 | 4 |
| ermaozi-get_subscribe | 0.125 | 1 | 7 | 8 |
| mheidari-all | 0.562 | 99 | 77 | 176 |
| Surfboard-tg-mixed | 0.648 | 103 | 56 | 159 |
| ermaozi | 0.84 | 21 | 4 | 25 |
| Au1rxx-base64 | 0.857 | 234 | 39 | 273 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19747 | yes | 4.96 | 0 |
| SoliSpirit-all | 8922 | yes | 3.81 | 0 |
| Epodonios-all | 7771 | yes | 2.73 | 0 |
| Surfboard-tg-mixed | 7333 | yes | 3.63 | 0 |
| barry-far-vless | 6051 | yes | 1.97 | 0 |
| DeltaKronecker-all | 6040 | yes | 4.97 | 0 |
| Surfboard-tg-vless | 5838 | yes | 3.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 5076 | yes | 2.35 | 0 |
| mahdibland-V2RayAggregator | 4241 | yes | 1.96 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.1 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 62 |
| geo | 55 |
| 204 | 53 |
| speed | 18 |
