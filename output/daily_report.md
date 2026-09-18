# AutoNodes 每日报告

生成时间：2026-09-18 16:20:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 83896 |
| 去重后节点数 | 23095 |
| TCP 可达数 | 3000 |
| 真测通过数 | 399 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23095 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 78.8 |
| geo | 1.4 |
| probe | 275.5 |
| real_test | 223.4 |
| tcp | 38.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 33 | 22 | 11 | 66.7% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 165 | 147 | 18 | 89.1% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 2 | 1 | 1 | 50.0% |
| vless | 304 | 213 | 91 | 70.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 24 |
| 204:ProxyError | 18 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 15 |
| geo:TimeoutError | 15 |
| cn-block:ClientOSError | 12 |
| speed:ClientOSError | 11 |
| 204:ProxyConnectionError | 5 |
| cn-block:ProxyError | 3 |
| speed:TimeoutError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5216 |
| ConnectionRefusedError | 818 |
| gaierror | 435 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | prefer | 257 | 0.899 | 1596 |
| ermaozi | 0.828 | prefer | 25 | 0.84 | 325 |
| mheidari-all | 0.747 | prefer | 64 | 0.672 | 15758 |
| Surfboard-tg-mixed | 0.742 | prefer | 146 | 0.664 | 7397 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4241 |
| DeltaKronecker-all | 0.314 | observe | 18 | 0.222 | 6040 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5076 |
| Epodonios-all | 0.255 | observe | 0 | None | 7860 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| ermaozi-get_subscribe | 0.125 | 1 | 7 | 8 |
| DeltaKronecker-all | 0.222 | 4 | 14 | 18 |
| Surfboard-tg-mixed | 0.664 | 97 | 49 | 146 |
| mheidari-all | 0.672 | 43 | 21 | 64 |
| ermaozi | 0.84 | 21 | 4 | 25 |
| Au1rxx-base64 | 0.899 | 231 | 26 | 257 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15758 | yes | 4.56 | 0 |
| SoliSpirit-all | 8960 | yes | 4.77 | 0 |
| Epodonios-all | 7860 | yes | 4.95 | 0 |
| Surfboard-tg-mixed | 7397 | yes | 4.18 | 0 |
| barry-far-vless | 6127 | yes | 0.75 | 0 |
| DeltaKronecker-all | 6040 | yes | 5.54 | 0 |
| Surfboard-tg-vless | 5909 | yes | 3.79 | 0 |
| 10ium-ScrapeCategorize-Vless | 5076 | yes | 2.73 | 0 |
| mahdibland-V2RayAggregator | 4241 | yes | 2.91 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 40 |
| 204 | 39 |
| cn-block | 30 |
| speed | 13 |
