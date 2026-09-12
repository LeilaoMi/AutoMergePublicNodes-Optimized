# AutoNodes 每日报告

生成时间：2026-09-12 04:18:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83274 |
| 去重后节点数 | 23411 |
| TCP 可达数 | 3000 |
| 真测通过数 | 546 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23411 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 77.3 |
| geo | 1.4 |
| probe | 367.3 |
| real_test | 426.4 |
| tcp | 40.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 56 | 41 | 15 | 73.2% |
| hysteria2 | 24 | 23 | 1 | 95.8% |
| shadowsocks | 180 | 170 | 10 | 94.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 19 | 13 | 6 | 68.4% |
| vless | 625 | 296 | 329 | 47.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 118 |
| geo:ClientOSError | 93 |
| speed:TimeoutError | 44 |
| speed:ClientOSError | 36 |
| cn-block:TimeoutError | 26 |
| 204:ProxyError | 20 |
| cn-block:ClientOSError | 15 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5535 |
| ConnectionRefusedError | 902 |
| gaierror | 503 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.948 | prefer | 317 | 0.883 | 1681 |
| ermaozi | 0.74 | prefer | 52 | 0.731 | 434 |
| Surfboard-tg-mixed | 0.719 | prefer | 192 | 0.641 | 7263 |
| mheidari-all | 0.58 | observe | 112 | 0.5 | 15597 |
| ermaozi-get_subscribe | 0.338 | observe | 4 | 0.75 | 459 |
| DeltaKronecker-all | 0.281 | observe | 227 | 0.198 | 6070 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 194 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4932 |
| Epodonios-all | 0.255 | observe | 0 | None | 7719 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.198 | 45 | 182 | 227 |
| mheidari-all | 0.5 | 56 | 56 | 112 |
| Surfboard-tg-mixed | 0.641 | 123 | 69 | 192 |
| ermaozi | 0.731 | 38 | 14 | 52 |
| ermaozi-get_subscribe | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.883 | 280 | 37 | 317 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15597 | yes | 3.57 | 0 |
| SoliSpirit-all | 8500 | yes | 3.48 | 0 |
| Epodonios-all | 7719 | yes | 2.4 | 0 |
| Surfboard-tg-mixed | 7263 | yes | 3.07 | 0 |
| barry-far-vless | 6106 | yes | 0.88 | 0 |
| DeltaKronecker-all | 6070 | yes | 3.91 | 0 |
| Surfboard-tg-vless | 5889 | yes | 2.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4932 | yes | 1.24 | 0 |
| mahdibland-V2RayAggregator | 4223 | yes | 2.06 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.72 | 0 |

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
| geo | 211 |
| speed | 80 |
| cn-block | 42 |
| 204 | 30 |
