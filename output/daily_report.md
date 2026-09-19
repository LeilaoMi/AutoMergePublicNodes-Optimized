# AutoNodes 每日报告

生成时间：2026-09-19 15:52:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 88522 |
| 去重后节点数 | 25250 |
| TCP 可达数 | 3000 |
| 真测通过数 | 495 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25250 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 83.3 |
| geo | 1.5 |
| probe | 215.5 |
| real_test | 238.7 |
| tcp | 42.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 27 | 24 | 3 | 88.9% |
| hysteria2 | 15 | 15 | 0 | 100.0% |
| shadowsocks | 154 | 145 | 9 | 94.2% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 13 | 8 | 5 | 61.5% |
| vless | 466 | 302 | 164 | 64.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 48 |
| 204:TimeoutError | 30 |
| cn-block:ClientOSError | 28 |
| speed:ClientOSError | 21 |
| geo:TimeoutError | 20 |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 12 |
| 204:ClientOSError | 5 |
| speed:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5837 |
| ConnectionRefusedError | 890 |
| gaierror | 420 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.9 | prefer | 318 | 0.836 | 1651 |
| ermaozi | 0.899 | prefer | 25 | 0.92 | 250 |
| Surfboard-tg-mixed | 0.696 | observe | 183 | 0.617 | 7296 |
| mheidari-all | 0.69 | observe | 139 | 0.612 | 19364 |
| DeltaKronecker-all | 0.515 | observe | 11 | 0.636 | 6421 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4251 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5174 |
| Epodonios-all | 0.255 | observe | 0 | None | 7933 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3995 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9336 |

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
| ermaozi-get_subscribe | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.612 | 85 | 54 | 139 |
| Surfboard-tg-mixed | 0.617 | 113 | 70 | 183 |
| DeltaKronecker-all | 0.636 | 7 | 4 | 11 |
| Au1rxx-base64 | 0.836 | 266 | 52 | 318 |
| ermaozi | 0.92 | 23 | 2 | 25 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19364 | yes | 5.55 | 0 |
| SoliSpirit-all | 9336 | yes | 4.2 | 0 |
| Epodonios-all | 7933 | yes | 3.51 | 0 |
| Surfboard-tg-mixed | 7296 | yes | 4.08 | 0 |
| DeltaKronecker-all | 6421 | yes | 4.89 | 0 |
| barry-far-vless | 6222 | yes | 1.23 | 0 |
| Surfboard-tg-vless | 5900 | yes | 5.83 | 0 |
| 10ium-ScrapeCategorize-Vless | 5174 | yes | 2.91 | 0 |
| mahdibland-V2RayAggregator | 4251 | yes | 3.2 | 0 |
| MatinGhanbari-all-sub | 3995 | yes | 4.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 69 |
| 204 | 47 |
| cn-block | 44 |
| speed | 25 |
