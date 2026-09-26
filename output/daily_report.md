# AutoNodes 每日报告

生成时间：2026-09-26 16:18:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 96747 |
| 去重后节点数 | 26321 |
| TCP 可达数 | 3000 |
| 真测通过数 | 345 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26321 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 77.0 |
| geo | 1.5 |
| probe | 239.0 |
| real_test | 213.0 |
| tcp | 43.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 21 | 8 | 13 | 38.1% |
| hysteria2 | 19 | 17 | 2 | 89.5% |
| shadowsocks | 153 | 125 | 28 | 81.7% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 13 | 8 | 5 | 61.5% |
| vless | 243 | 184 | 59 | 75.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 26 |
| 204:TimeoutError | 26 |
| 204:ProxyError | 13 |
| cn-block:ClientOSError | 13 |
| speed:TimeoutError | 9 |
| 204:ProxyConnectionError | 8 |
| geo:TimeoutError | 5 |
| speed:ClientOSError | 4 |
| geo:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6043 |
| ConnectionRefusedError | 946 |
| gaierror | 317 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.936 | prefer | 268 | 0.873 | 1642 |
| mheidari-all | 0.742 | prefer | 63 | 0.667 | 22551 |
| Surfboard-tg-mixed | 0.694 | observe | 99 | 0.616 | 7263 |
| ermaozi | 0.426 | observe | 19 | 0.421 | 296 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5242 |
| Epodonios-all | 0.255 | observe | 0 | None | 7742 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8947 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5823 |
| barry-far-vless | 0.255 | observe | 0 | None | 6056 |

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
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| ermaozi-get_subscribe | 0.0 | 0 | 2 | 2 |
| ermaozi | 0.421 | 8 | 11 | 19 |
| Surfboard-tg-mixed | 0.616 | 61 | 38 | 99 |
| mheidari-all | 0.667 | 42 | 21 | 63 |
| Au1rxx-base64 | 0.873 | 234 | 34 | 268 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22551 | yes | 6.38 | 0 |
| SoliSpirit-all | 8947 | yes | 2.34 | 0 |
| Epodonios-all | 7742 | yes | 3.11 | 0 |
| Surfboard-tg-mixed | 7263 | yes | 4.6 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.81 | 0 |
| barry-far-vless | 6056 | yes | 1.06 | 0 |
| Surfboard-tg-vless | 5823 | yes | 3.81 | 0 |
| DeltaKronecker-all | 5512 | yes | 5.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 5242 | yes | 0.76 | 0 |
| mahdibland-V2RayAggregator | 4355 | yes | 2.72 | 0 |

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
| 204 | 49 |
| cn-block | 41 |
| speed | 13 |
| geo | 8 |
