# AutoNodes 每日报告

生成时间：2026-09-08 21:09:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 84956 |
| 去重后节点数 | 22773 |
| TCP 可达数 | 3000 |
| 真测通过数 | 527 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22773 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 87.7 |
| geo | 1.4 |
| probe | 236.2 |
| real_test | 283.2 |
| tcp | 37.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 33 | 23 | 10 | 69.7% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 164 | 152 | 12 | 92.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 34 | 21 | 13 | 61.8% |
| vless | 382 | 312 | 70 | 81.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 27 |
| geo:ClientOSError | 21 |
| 204:ProxyError | 16 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| geo:TimeoutError | 4 |
| speed:ClientOSError | 4 |
| cn-block:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4704 |
| ConnectionRefusedError | 870 |
| gaierror | 489 |
| OSError | 27 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 291 | 0.942 | 1700 |
| DeltaKronecker-all | 0.92 | prefer | 23 | 0.87 | 6097 |
| Surfboard-tg-mixed | 0.814 | prefer | 167 | 0.737 | 7370 |
| mheidari-all | 0.811 | prefer | 117 | 0.735 | 16416 |
| ermaozi | 0.702 | prefer | 33 | 0.697 | 409 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7999 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8578 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6089 |

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
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.697 | 23 | 10 | 33 |
| mheidari-all | 0.735 | 86 | 31 | 117 |
| Surfboard-tg-mixed | 0.737 | 123 | 44 | 167 |
| DeltaKronecker-all | 0.87 | 20 | 3 | 23 |
| Au1rxx-base64 | 0.942 | 274 | 17 | 291 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16416 | yes | 5.09 | 0 |
| SoliSpirit-all | 8578 | yes | 2.45 | 0 |
| Epodonios-all | 7999 | yes | 0.82 | 0 |
| Surfboard-tg-mixed | 7370 | yes | 4.12 | 0 |
| barry-far-vless | 6497 | yes | 2.15 | 0 |
| DeltaKronecker-all | 6097 | yes | 5.95 | 0 |
| Surfboard-tg-vless | 6089 | yes | 4.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 1.17 | 0 |
| mahdibland-V2RayAggregator | 4219 | yes | 0.18 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.48 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 47 |
| cn-block | 26 |
| geo | 25 |
| speed | 9 |
