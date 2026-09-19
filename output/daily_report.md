# AutoNodes 每日报告

生成时间：2026-09-19 04:15:53

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 82099 |
| 去重后节点数 | 23205 |
| TCP 可达数 | 3000 |
| 真测通过数 | 548 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23205 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 72.7 |
| geo | 1.4 |
| probe | 267.2 |
| real_test | 328.3 |
| tcp | 38.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 60 | 41 | 19 | 68.3% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 167 | 162 | 5 | 97.0% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 51 | 32 | 19 | 62.7% |
| vless | 522 | 293 | 229 | 56.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 94 |
| speed:TimeoutError | 46 |
| geo:ClientOSError | 31 |
| speed:ClientOSError | 30 |
| 204:ProxyError | 26 |
| cn-block:TimeoutError | 24 |
| cn-block:ClientOSError | 12 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5179 |
| ConnectionRefusedError | 821 |
| gaierror | 437 |
| OSError | 15 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.946 | prefer | 317 | 0.88 | 1703 |
| ermaozi | 0.769 | prefer | 51 | 0.765 | 358 |
| Surfboard-tg-mixed | 0.739 | prefer | 247 | 0.66 | 7266 |
| mheidari-all | 0.506 | observe | 113 | 0.425 | 13937 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4241 |
| ermaozi-get_subscribe | 0.288 | observe | 11 | 0.364 | 387 |
| 10ium-ScrapeCategorize-Vless | 0.259 | observe | 3 | 0.333 | 5076 |
| DeltaKronecker-all | 0.257 | observe | 77 | 0.169 | 6040 |
| Epodonios-all | 0.255 | observe | 0 | None | 7793 |
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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.169 | 13 | 64 | 77 |
| 10ium-ScrapeCategorize-Vless | 0.333 | 1 | 2 | 3 |
| ermaozi-get_subscribe | 0.364 | 4 | 7 | 11 |
| mheidari-all | 0.425 | 48 | 65 | 113 |
| Surfboard-tg-mixed | 0.66 | 163 | 84 | 247 |
| ermaozi | 0.765 | 39 | 12 | 51 |
| Au1rxx-base64 | 0.88 | 279 | 38 | 317 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 13937 | yes | 5.25 | 0 |
| SoliSpirit-all | 8930 | yes | 2.93 | 0 |
| Epodonios-all | 7793 | yes | 2.17 | 0 |
| Surfboard-tg-mixed | 7266 | yes | 4.22 | 0 |
| barry-far-vless | 6112 | yes | 0.82 | 0 |
| DeltaKronecker-all | 6040 | yes | 3.68 | 0 |
| Surfboard-tg-vless | 5822 | yes | 3.73 | 0 |
| 10ium-ScrapeCategorize-Vless | 5076 | yes | 2.49 | 0 |
| mahdibland-V2RayAggregator | 4241 | yes | 3.23 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.37 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 125 |
| speed | 77 |
| cn-block | 37 |
| 204 | 34 |
