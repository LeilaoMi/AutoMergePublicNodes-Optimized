# AutoNodes 每日报告

生成时间：2026-09-12 10:36:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 1/105 |
| 原始节点数 | 83079 |
| 去重后节点数 | 22882 |
| TCP 可达数 | 3000 |
| 真测通过数 | 438 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22882 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 81.7 |
| geo | 1.4 |
| probe | 267.8 |
| real_test | 245.0 |
| tcp | 37.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 64 | 32 | 32 | 50.0% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 156 | 144 | 12 | 92.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 22 | 16 | 6 | 72.7% |
| vless | 367 | 224 | 143 | 61.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 63 |
| 204:ProxyError | 27 |
| 204:TimeoutError | 17 |
| speed:TimeoutError | 17 |
| cn-block:TimeoutError | 16 |
| speed:ClientOSError | 15 |
| cn-block:ClientOSError | 13 |
| 204:ProxyConnectionError | 12 |
| geo:TimeoutError | 8 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4686 |
| ConnectionRefusedError | 903 |
| gaierror | 581 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.894 | prefer | 286 | 0.832 | 1613 |
| mheidari-all | 0.695 | observe | 94 | 0.617 | 15628 |
| Surfboard-tg-mixed | 0.676 | observe | 149 | 0.597 | 7286 |
| DeltaKronecker-all | 0.605 | observe | 38 | 0.526 | 5970 |
| ermaozi | 0.573 | observe | 52 | 0.558 | 434 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 181 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4793 |
| Epodonios-all | 0.255 | observe | 0 | None | 7695 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5895 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.23 | 12 | 0.25 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| SoliSpirit-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.25 | 3 | 9 | 12 |
| DeltaKronecker-all | 0.526 | 20 | 18 | 38 |
| ermaozi | 0.558 | 29 | 23 | 52 |
| Surfboard-tg-mixed | 0.597 | 89 | 60 | 149 |
| mheidari-all | 0.617 | 58 | 36 | 94 |
| Au1rxx-base64 | 0.832 | 238 | 48 | 286 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15628 | yes | 4.55 | 0 |
| SoliSpirit-all | 8697 | yes | 3.13 | 0 |
| Epodonios-all | 7695 | yes | 3.05 | 0 |
| Surfboard-tg-mixed | 7286 | yes | 3.7 | 0 |
| barry-far-vless | 6084 | yes | 2.08 | 0 |
| DeltaKronecker-all | 5970 | yes | 4.5 | 0 |
| Surfboard-tg-vless | 5895 | yes | 3.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 4793 | yes | 1.48 | 0 |
| mahdibland-V2RayAggregator | 4207 | yes | 0.44 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.14 | 0 |

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
| geo | 74 |
| 204 | 59 |
| speed | 32 |
| cn-block | 31 |
