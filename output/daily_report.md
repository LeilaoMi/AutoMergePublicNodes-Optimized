# AutoNodes 每日报告

生成时间：2026-10-04 21:17:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 99274 |
| 去重后节点数 | 27455 |
| TCP 可达数 | 3000 |
| 真测通过数 | 491 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27455 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| generate | 84.1 |
| geo | 1.1 |
| probe | 231.9 |
| real_test | 196.1 |
| tcp | 45.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 4 | 2 | 66.7% |
| http | 25 | 20 | 5 | 80.0% |
| hysteria2 | 25 | 25 | 0 | 100.0% |
| shadowsocks | 154 | 138 | 16 | 89.6% |
| socks | 5 | 1 | 4 | 20.0% |
| trojan | 82 | 77 | 5 | 93.9% |
| vless | 275 | 226 | 49 | 82.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 23 |
| geo:TimeoutError | 10 |
| 204:ProxyError | 8 |
| speed:TimeoutError | 8 |
| 204:TimeoutError | 8 |
| geo:ClientOSError | 5 |
| cn-block:ClientOSError | 5 |
| speed:ClientOSError | 4 |
| 204:ProxyConnectionError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5847 |
| ConnectionRefusedError | 1080 |
| gaierror | 538 |
| OSError | 238 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | prefer | 410 | 0.898 | 1844 |
| mheidari-all | 0.85 | prefer | 85 | 0.776 | 23222 |
| Surfboard-tg-mixed | 0.841 | prefer | 44 | 0.773 | 7257 |
| ermaozi | 0.804 | prefer | 25 | 0.8 | 653 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 5267 |
| ermaozi-get_subscribe | 0.261 | observe | 4 | 0.5 | 518 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5173 |
| Epodonios-all | 0.255 | observe | 0 | None | 7751 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9655 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.773 | 34 | 10 | 44 |
| mheidari-all | 0.776 | 66 | 19 | 85 |
| ermaozi | 0.8 | 20 | 5 | 25 |
| Au1rxx-base64 | 0.898 | 368 | 42 | 410 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23222 | yes | 6.82 | 0 |
| SoliSpirit-all | 9655 | yes | 4.92 | 0 |
| Epodonios-all | 7751 | yes | 0.36 | 0 |
| Surfboard-tg-mixed | 7257 | yes | 4.82 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.01 | 0 |
| barry-far-vless | 6058 | yes | 1.35 | 0 |
| Surfboard-tg-vless | 5820 | yes | 4.44 | 0 |
| DeltaKronecker-all | 5267 | yes | 6.98 | 0 |
| 10ium-ScrapeCategorize-Vless | 5173 | yes | 3.04 | 0 |
| mahdibland-V2RayAggregator | 4365 | yes | 3.75 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 30 |
| 204 | 22 |
| geo | 16 |
| speed | 13 |
