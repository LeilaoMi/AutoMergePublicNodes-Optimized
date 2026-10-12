# AutoNodes 每日报告

生成时间：2026-10-12 05:41:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 1/106 |
| 原始节点数 | 99742 |
| 去重后节点数 | 27632 |
| TCP 可达数 | 3000 |
| 真测通过数 | 546 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27632 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 84.0 |
| geo | 1.4 |
| probe | 444.7 |
| real_test | 591.9 |
| tcp | 47.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 51 | 34 | 17 | 66.7% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 130 | 120 | 10 | 92.3% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 174 | 167 | 7 | 96.0% |
| vless | 507 | 204 | 303 | 40.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 160 |
| speed:TimeoutError | 43 |
| geo:ClientOSError | 35 |
| 204:ProxyError | 26 |
| cn-block:TimeoutError | 22 |
| speed:ClientOSError | 22 |
| 204:TimeoutError | 12 |
| cn-block:ClientOSError | 12 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6549 |
| ConnectionRefusedError | 1049 |
| gaierror | 402 |
| OSError | 239 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.978 | prefer | 389 | 0.907 | 1810 |
| ermaozi | 0.683 | observe | 53 | 0.66 | 708 |
| DeltaKronecker-all | 0.505 | observe | 250 | 0.424 | 5372 |
| Surfboard-tg-mixed | 0.349 | observe | 3 | 0.667 | 7200 |
| mheidari-all | 0.342 | observe | 185 | 0.259 | 23656 |
| ermaozi-get_subscribe | 0.279 | observe | 1 | 1.0 | 600 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7699 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9920 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.259 | 48 | 137 | 185 |
| DeltaKronecker-all | 0.424 | 106 | 144 | 250 |
| ermaozi | 0.66 | 35 | 18 | 53 |
| Surfboard-tg-mixed | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.907 | 353 | 36 | 389 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23656 | yes | 5.4 | 0 |
| SoliSpirit-all | 9920 | yes | 1.54 | 0 |
| Epodonios-all | 7699 | yes | 4.88 | 0 |
| Surfboard-tg-mixed | 7200 | yes | 2.91 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.01 | 0 |
| barry-far-vless | 5961 | yes | 1.13 | 0 |
| Surfboard-tg-vless | 5717 | yes | 3.22 | 0 |
| DeltaKronecker-all | 5372 | yes | 4.42 | 0 |
| 10ium-ScrapeCategorize-Vless | 5099 | yes | 0.83 | 0 |
| mahdibland-V2RayAggregator | 4284 | yes | 2.35 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 197 |
| speed | 67 |
| 204 | 39 |
| cn-block | 36 |
