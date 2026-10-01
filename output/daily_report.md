# AutoNodes 每日报告

生成时间：2026-10-01 05:24:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 97857 |
| 去重后节点数 | 27300 |
| TCP 可达数 | 3000 |
| 真测通过数 | 437 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27300 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| generate | 83.5 |
| geo | 1.6 |
| probe | 240.8 |
| real_test | 283.3 |
| tcp | 44.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 21 | 18 | 3 | 85.7% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 175 | 154 | 21 | 88.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 55 | 38 | 17 | 69.1% |
| vless | 432 | 205 | 227 | 47.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 82 |
| speed:ClientOSError | 58 |
| speed:TimeoutError | 44 |
| geo:ClientOSError | 30 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 13 |
| cn-block:ClientOSError | 8 |
| 204:ProxyError | 7 |
| 204:ClientOSError | 5 |
| 204:ProxyConnectionError | 2 |
| cn-block:ProxyError | 2 |
| geo:parse | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5928 |
| ConnectionRefusedError | 1023 |
| gaierror | 417 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.872 | prefer | 314 | 0.806 | 1694 |
| ermaozi | 0.807 | prefer | 19 | 0.842 | 588 |
| Surfboard-tg-mixed | 0.691 | observe | 160 | 0.613 | 7136 |
| DeltaKronecker-all | 0.612 | observe | 16 | 0.625 | 5434 |
| mheidari-all | 0.381 | observe | 191 | 0.298 | 22835 |
| tg-oneclickvpnkeys | 0.314 | observe | 2 | 1.0 | 80 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7637 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.298 | 57 | 134 | 191 |
| Surfboard-tg-mixed | 0.613 | 98 | 62 | 160 |
| DeltaKronecker-all | 0.625 | 10 | 6 | 16 |
| Au1rxx-base64 | 0.806 | 253 | 61 | 314 |
| ermaozi | 0.842 | 16 | 3 | 19 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22835 | yes | 5.71 | 0 |
| SoliSpirit-all | 9403 | yes | 3.46 | 0 |
| Epodonios-all | 7637 | yes | 1.79 | 0 |
| Surfboard-tg-mixed | 7136 | yes | 3.93 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 4.98 | 0 |
| barry-far-vless | 6001 | yes | 2.8 | 0 |
| Surfboard-tg-vless | 5815 | yes | 4.59 | 0 |
| DeltaKronecker-all | 5434 | yes | 5.83 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 2.59 | 0 |
| mahdibland-V2RayAggregator | 4183 | yes | 1.41 | 0 |

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
| geo | 113 |
| speed | 103 |
| 204 | 30 |
| cn-block | 23 |
