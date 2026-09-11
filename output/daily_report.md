# AutoNodes 每日报告

生成时间：2026-09-11 11:10:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84388 |
| 去重后节点数 | 23243 |
| TCP 可达数 | 3000 |
| 真测通过数 | 483 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23243 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 77.9 |
| geo | 1.4 |
| probe | 286.6 |
| real_test | 304.0 |
| tcp | 40.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 42 | 34 | 8 | 81.0% |
| hysteria2 | 9 | 8 | 1 | 88.9% |
| shadowsocks | 166 | 149 | 17 | 89.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 26 | 15 | 11 | 57.7% |
| vless | 413 | 274 | 139 | 66.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 56 |
| 204:TimeoutError | 21 |
| speed:TimeoutError | 20 |
| 204:ProxyError | 19 |
| geo:TimeoutError | 19 |
| cn-block:TimeoutError | 13 |
| cn-block:ClientOSError | 9 |
| 204:ClientOSError | 7 |
| speed:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5715 |
| ConnectionRefusedError | 875 |
| gaierror | 373 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.938 | prefer | 283 | 0.869 | 1772 |
| mheidari-all | 0.895 | prefer | 25 | 0.84 | 15701 |
| ermaozi | 0.808 | prefer | 41 | 0.805 | 431 |
| Surfboard-tg-mixed | 0.755 | prefer | 121 | 0.678 | 7422 |
| DeltaKronecker-all | 0.609 | observe | 185 | 0.53 | 6070 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 199 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4932 |
| Epodonios-all | 0.255 | observe | 0 | None | 7889 |
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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.53 | 98 | 87 | 185 |
| Surfboard-tg-mixed | 0.678 | 82 | 39 | 121 |
| ermaozi | 0.805 | 33 | 8 | 41 |
| mheidari-all | 0.84 | 21 | 4 | 25 |
| Au1rxx-base64 | 0.869 | 246 | 37 | 283 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15701 | yes | 3.01 | 0 |
| SoliSpirit-all | 8749 | yes | 2.64 | 0 |
| Epodonios-all | 7889 | yes | 2.28 | 0 |
| Surfboard-tg-mixed | 7422 | yes | 2.73 | 0 |
| barry-far-vless | 6213 | yes | 1.84 | 0 |
| DeltaKronecker-all | 6070 | yes | 3.65 | 0 |
| Surfboard-tg-vless | 5995 | yes | 3.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4932 | yes | 1.97 | 0 |
| mahdibland-V2RayAggregator | 4223 | yes | 1.9 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.47 | 0 |

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
| geo | 78 |
| 204 | 47 |
| speed | 27 |
| cn-block | 26 |
