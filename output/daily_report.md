# AutoNodes 每日报告

生成时间：2026-09-19 20:31:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 91254 |
| 去重后节点数 | 25369 |
| TCP 可达数 | 3000 |
| 真测通过数 | 459 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25369 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.8 |
| generate | 75.1 |
| geo | 1.3 |
| probe | 226.0 |
| real_test | 208.6 |
| tcp | 42.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 27 | 24 | 3 | 88.9% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 146 | 135 | 11 | 92.5% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 11 | 8 | 3 | 72.7% |
| vless | 422 | 276 | 146 | 65.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 42 |
| geo:TimeoutError | 33 |
| cn-block:ClientOSError | 26 |
| 204:TimeoutError | 20 |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 11 |
| speed:ClientOSError | 7 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5721 |
| ConnectionRefusedError | 902 |
| gaierror | 373 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.915 | prefer | 303 | 0.851 | 1650 |
| ermaozi | 0.899 | prefer | 25 | 0.92 | 250 |
| Surfboard-tg-mixed | 0.728 | prefer | 157 | 0.65 | 7211 |
| mheidari-all | 0.631 | observe | 125 | 0.552 | 19269 |
| DeltaKronecker-all | 0.372 | observe | 9 | 0.444 | 6421 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4251 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5174 |
| Epodonios-all | 0.255 | observe | 0 | None | 7761 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| DeltaKronecker-all | 0.444 | 4 | 5 | 9 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.552 | 69 | 56 | 125 |
| Surfboard-tg-mixed | 0.65 | 102 | 55 | 157 |
| Au1rxx-base64 | 0.851 | 258 | 45 | 303 |
| ermaozi | 0.92 | 23 | 2 | 25 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19269 | yes | 2.68 | 0 |
| SoliSpirit-all | 9098 | yes | 2.21 | 0 |
| Epodonios-all | 7761 | yes | 3.56 | 0 |
| Surfboard-tg-mixed | 7211 | yes | 2.27 | 0 |
| DeltaKronecker-all | 6421 | yes | 2.35 | 0 |
| barry-far-vless | 6077 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 5765 | yes | 2.36 | 0 |
| 10ium-ScrapeCategorize-Vless | 5174 | yes | 1.02 | 0 |
| mahdibland-V2RayAggregator | 4251 | yes | 1.49 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.05 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 76 |
| cn-block | 42 |
| 204 | 33 |
| speed | 13 |
