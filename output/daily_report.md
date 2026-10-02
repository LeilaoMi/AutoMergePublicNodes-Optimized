# AutoNodes 每日报告

生成时间：2026-10-02 22:08:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98974 |
| 去重后节点数 | 27178 |
| TCP 可达数 | 3000 |
| 真测通过数 | 413 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27178 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| generate | 33.7 |
| geo | 0.9 |
| probe | 195.3 |
| real_test | 145.2 |
| tcp | 46.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 24 | 15 | 9 | 62.5% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 164 | 152 | 12 | 92.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 17 | 15 | 2 | 88.2% |
| vless | 243 | 211 | 32 | 86.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 18 |
| 204:ProxyConnectionError | 8 |
| 204:TimeoutError | 8 |
| 204:ProxyError | 5 |
| speed:TimeoutError | 5 |
| speed:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| geo:TimeoutError | 2 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6229 |
| ConnectionRefusedError | 1171 |
| gaierror | 532 |
| OSError | 240 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | prefer | 294 | 0.901 | 1771 |
| mheidari-all | 0.955 | prefer | 102 | 0.882 | 23213 |
| Surfboard-tg-mixed | 0.94 | prefer | 48 | 0.875 | 7321 |
| ermaozi | 0.64 | observe | 24 | 0.625 | 620 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 4981 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5276 |
| Epodonios-all | 0.255 | observe | 0 | None | 7814 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9326 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5999 |

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
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.625 | 15 | 9 | 24 |
| Surfboard-tg-mixed | 0.875 | 42 | 6 | 48 |
| mheidari-all | 0.882 | 90 | 12 | 102 |
| Au1rxx-base64 | 0.901 | 265 | 29 | 294 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23213 | yes | 6.24 | 0 |
| SoliSpirit-all | 9326 | yes | 3.43 | 0 |
| Epodonios-all | 7814 | yes | 3.73 | 0 |
| Surfboard-tg-mixed | 7321 | yes | 4.88 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.36 | 0 |
| barry-far-vless | 6241 | yes | 1.14 | 0 |
| Surfboard-tg-vless | 5999 | yes | 4.11 | 0 |
| 10ium-ScrapeCategorize-Vless | 5276 | yes | 1.38 | 0 |
| DeltaKronecker-all | 4981 | yes | 6.82 | 0 |
| mahdibland-V2RayAggregator | 4357 | yes | 3.27 | 0 |

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
| 204 | 23 |
| cn-block | 23 |
| speed | 9 |
| geo | 3 |
