# AutoNodes 每日报告

生成时间：2026-09-18 11:07:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83513 |
| 去重后节点数 | 22980 |
| TCP 可达数 | 3000 |
| 真测通过数 | 391 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22980 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 89.2 |
| geo | 1.4 |
| probe | 255.8 |
| real_test | 258.5 |
| tcp | 37.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 45 | 35 | 10 | 77.8% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 178 | 160 | 18 | 89.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 37 | 9 | 28 | 24.3% |
| vless | 272 | 169 | 103 | 62.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 39 |
| geo:TimeoutError | 23 |
| speed:TimeoutError | 21 |
| cn-block:TimeoutError | 19 |
| geo:ClientOSError | 18 |
| 204:ProxyError | 14 |
| cn-block:ClientOSError | 11 |
| speed:ClientOSError | 9 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5138 |
| ConnectionRefusedError | 832 |
| gaierror | 480 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.906 | prefer | 256 | 0.844 | 1622 |
| mheidari-all | 0.788 | prefer | 46 | 0.717 | 15778 |
| ermaozi | 0.76 | prefer | 45 | 0.756 | 378 |
| Surfboard-tg-mixed | 0.651 | observe | 154 | 0.571 | 7294 |
| DeltaKronecker-all | 0.484 | observe | 45 | 0.4 | 6040 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4241 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7751 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8957 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| chromego_merge | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.4 | 18 | 27 | 45 |
| Surfboard-tg-mixed | 0.571 | 88 | 66 | 154 |
| mheidari-all | 0.717 | 33 | 13 | 46 |
| ermaozi | 0.756 | 34 | 11 | 45 |
| Au1rxx-base64 | 0.844 | 216 | 40 | 256 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15778 | yes | 5.37 | 0 |
| SoliSpirit-all | 8957 | yes | 4.0 | 0 |
| Epodonios-all | 7751 | yes | 4.51 | 0 |
| Surfboard-tg-mixed | 7294 | yes | 4.16 | 0 |
| DeltaKronecker-all | 6040 | yes | 4.52 | 0 |
| barry-far-vless | 5979 | yes | 1.79 | 0 |
| Surfboard-tg-vless | 5763 | yes | 3.43 | 0 |
| 10ium-ScrapeCategorize-Vless | 5076 | yes | 2.02 | 0 |
| mahdibland-V2RayAggregator | 4241 | yes | 1.93 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 55 |
| geo | 42 |
| cn-block | 34 |
| speed | 31 |
