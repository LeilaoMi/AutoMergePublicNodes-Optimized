# AutoNodes 每日报告

生成时间：2026-10-01 13:00:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 98134 |
| 去重后节点数 | 27405 |
| TCP 可达数 | 3000 |
| 真测通过数 | 417 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27405 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 82.8 |
| geo | 1.6 |
| probe | 253.0 |
| real_test | 178.7 |
| tcp | 45.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 23 | 22 | 1 | 95.7% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 123 | 113 | 10 | 91.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 23 | 19 | 4 | 82.6% |
| vless | 383 | 240 | 143 | 62.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 91 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 14 |
| 204:ProxyError | 9 |
| geo:TimeoutError | 9 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6161 |
| ConnectionRefusedError | 1021 |
| gaierror | 378 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.96 | prefer | 20 | 1.0 | 144 |
| mheidari-all | 0.887 | prefer | 17 | 0.941 | 23162 |
| Au1rxx-base64 | 0.866 | prefer | 310 | 0.797 | 1787 |
| Surfboard-tg-mixed | 0.752 | prefer | 117 | 0.675 | 7144 |
| DeltaKronecker-all | 0.537 | observe | 103 | 0.456 | 5603 |
| ermaozi | 0.479 | observe | 6 | 1.0 | 56 |
| tg-oneclickvpnkeys | 0.314 | observe | 2 | 1.0 | 66 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5324 |
| Epodonios-all | 0.255 | observe | 0 | None | 7625 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

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
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.456 | 47 | 56 | 103 |
| Surfboard-tg-mixed | 0.675 | 79 | 38 | 117 |
| Au1rxx-base64 | 0.797 | 247 | 63 | 310 |
| mheidari-all | 0.941 | 16 | 1 | 17 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 6 | 0 | 6 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23162 | yes | 5.84 | 0 |
| SoliSpirit-all | 9489 | yes | 2.22 | 0 |
| Epodonios-all | 7625 | yes | 3.19 | 0 |
| Surfboard-tg-mixed | 7144 | yes | 3.67 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.78 | 0 |
| barry-far-vless | 6032 | yes | 1.96 | 0 |
| Surfboard-tg-vless | 5788 | yes | 3.84 | 0 |
| DeltaKronecker-all | 5603 | yes | 4.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 5324 | yes | 1.03 | 0 |
| mahdibland-V2RayAggregator | 4241 | yes | 1.34 | 0 |

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
| speed | 98 |
| cn-block | 27 |
| 204 | 23 |
| geo | 12 |
