# AutoNodes 每日报告

生成时间：2026-10-02 05:16:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98630 |
| 去重后节点数 | 27538 |
| TCP 可达数 | 3000 |
| 真测通过数 | 460 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27538 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| generate | 85.2 |
| geo | 1.5 |
| probe | 321.7 |
| real_test | 400.1 |
| tcp | 46.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 24 | 23 | 1 | 95.8% |
| hysteria2 | 24 | 24 | 0 | 100.0% |
| shadowsocks | 173 | 158 | 15 | 91.3% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 42 | 28 | 14 | 66.7% |
| vless | 508 | 222 | 286 | 43.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 151 |
| speed:TimeoutError | 66 |
| geo:ClientOSError | 29 |
| 204:ProxyError | 22 |
| speed:ClientOSError | 17 |
| cn-block:TimeoutError | 11 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 6 |
| 204:ProxyConnectionError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6121 |
| ConnectionRefusedError | 1053 |
| gaierror | 493 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.987 | prefer | 267 | 0.921 | 1731 |
| Surfboard-tg-mixed | 0.919 | prefer | 60 | 0.85 | 7165 |
| ermaozi | 0.914 | prefer | 25 | 0.92 | 618 |
| mheidari-all | 0.41 | observe | 416 | 0.329 | 23308 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 5324 |
| DeltaKronecker-all | 0.263 | observe | 8 | 0.25 | 5603 |
| Epodonios-all | 0.255 | observe | 0 | None | 7654 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9200 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5778 |

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
| DeltaKronecker-all | 0.25 | 2 | 6 | 8 |
| mheidari-all | 0.329 | 137 | 279 | 416 |
| Surfboard-tg-mixed | 0.85 | 51 | 9 | 60 |
| ermaozi | 0.92 | 23 | 2 | 25 |
| Au1rxx-base64 | 0.921 | 246 | 21 | 267 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23308 | yes | 6.4 | 0 |
| SoliSpirit-all | 9200 | yes | 5.29 | 0 |
| Epodonios-all | 7654 | yes | 3.46 | 0 |
| Surfboard-tg-mixed | 7165 | yes | 3.83 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.74 | 0 |
| barry-far-vless | 6015 | yes | 4.0 | 0 |
| Surfboard-tg-vless | 5778 | yes | 4.78 | 0 |
| DeltaKronecker-all | 5603 | yes | 6.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 5324 | yes | 3.77 | 0 |
| mahdibland-V2RayAggregator | 4310 | yes | 3.53 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 180 |
| speed | 84 |
| 204 | 35 |
| cn-block | 19 |
