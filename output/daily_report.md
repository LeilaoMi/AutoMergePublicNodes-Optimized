# AutoNodes 每日报告

生成时间：2026-09-26 11:17:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 96784 |
| 去重后节点数 | 26417 |
| TCP 可达数 | 3000 |
| 真测通过数 | 367 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26417 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| generate | 96.3 |
| geo | 1.5 |
| probe | 212.1 |
| real_test | 207.2 |
| tcp | 43.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 38 | 11 | 27 | 28.9% |
| hysteria2 | 21 | 18 | 3 | 85.7% |
| shadowsocks | 161 | 136 | 25 | 84.5% |
| socks | 6 | 2 | 4 | 33.3% |
| trojan | 34 | 30 | 4 | 88.2% |
| vless | 232 | 167 | 65 | 72.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 27 |
| cn-block:TimeoutError | 24 |
| 204:ProxyError | 23 |
| cn-block:ClientOSError | 11 |
| 204:ProxyConnectionError | 10 |
| geo:TimeoutError | 9 |
| cn-block:ProxyError | 8 |
| speed:TimeoutError | 8 |
| speed:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6331 |
| ConnectionRefusedError | 955 |
| gaierror | 292 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.958 | prefer | 238 | 0.895 | 1660 |
| Surfboard-tg-mixed | 0.757 | prefer | 128 | 0.68 | 7247 |
| mheidari-all | 0.727 | prefer | 83 | 0.651 | 22392 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4355 |
| ermaozi | 0.282 | observe | 39 | 0.256 | 352 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| DeltaKronecker-all | 0.259 | observe | 3 | 0.333 | 5512 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5242 |
| Epodonios-all | 0.255 | observe | 0 | None | 7713 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3995 |

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
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.256 | 10 | 29 | 39 |
| DeltaKronecker-all | 0.333 | 1 | 2 | 3 |
| mheidari-all | 0.651 | 54 | 29 | 83 |
| Surfboard-tg-mixed | 0.68 | 87 | 41 | 128 |
| Au1rxx-base64 | 0.895 | 213 | 25 | 238 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22392 | yes | 6.21 | 0 |
| SoliSpirit-all | 8992 | yes | 2.64 | 0 |
| Epodonios-all | 7713 | yes | 3.36 | 0 |
| Surfboard-tg-mixed | 7247 | yes | 4.4 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.13 | 0 |
| barry-far-vless | 6071 | yes | 1.0 | 0 |
| Surfboard-tg-vless | 5840 | yes | 3.67 | 0 |
| DeltaKronecker-all | 5512 | yes | 6.24 | 0 |
| 10ium-ScrapeCategorize-Vless | 5242 | yes | 1.27 | 0 |
| mahdibland-V2RayAggregator | 4355 | yes | 3.01 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 62 |
| cn-block | 43 |
| speed | 12 |
| geo | 11 |
