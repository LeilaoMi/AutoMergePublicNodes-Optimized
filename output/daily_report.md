# AutoNodes 每日报告

生成时间：2026-09-10 16:21:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 91096 |
| 去重后节点数 | 24439 |
| TCP 可达数 | 3000 |
| 真测通过数 | 444 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24439 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 83.4 |
| geo | 1.5 |
| probe | 272.2 |
| real_test | 291.7 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 28 | 21 | 7 | 75.0% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 149 | 137 | 12 | 91.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 31 | 23 | 8 | 74.2% |
| vless | 361 | 242 | 119 | 67.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 46 |
| 204:TimeoutError | 22 |
| cn-block:ClientOSError | 19 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 15 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| geo:TimeoutError | 4 |
| 204:ProxyConnectionError | 2 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5208 |
| ConnectionRefusedError | 976 |
| gaierror | 453 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.948 | prefer | 273 | 0.883 | 1693 |
| Surfboard-tg-mixed | 0.849 | prefer | 132 | 0.773 | 7191 |
| ermaozi | 0.824 | prefer | 24 | 0.833 | 405 |
| mheidari-all | 0.599 | observe | 152 | 0.52 | 19266 |
| tg-oneclickvpnkeys | 0.264 | observe | 1 | 1.0 | 214 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4995 |
| Epodonios-all | 0.255 | observe | 0 | None | 7902 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8955 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5790 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 4 | 4 |
| ermaozi-get_subscribe | 0.25 | 1 | 3 | 4 |
| mheidari-all | 0.52 | 79 | 73 | 152 |
| Surfboard-tg-mixed | 0.773 | 102 | 30 | 132 |
| ermaozi | 0.833 | 20 | 4 | 24 |
| Au1rxx-base64 | 0.883 | 241 | 32 | 273 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19266 | yes | 5.68 | 0 |
| SoliSpirit-all | 8955 | yes | 4.26 | 0 |
| Epodonios-all | 7902 | yes | 6.28 | 0 |
| Surfboard-tg-mixed | 7191 | yes | 4.29 | 0 |
| barry-far-vless | 6248 | yes | 2.36 | 0 |
| DeltaKronecker-all | 5853 | yes | 5.75 | 0 |
| Surfboard-tg-vless | 5790 | yes | 3.7 | 0 |
| 10ium-ScrapeCategorize-Vless | 4995 | yes | 1.91 | 0 |
| mahdibland-V2RayAggregator | 4358 | yes | 2.09 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.64 | 0 |

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
| geo | 52 |
| 204 | 40 |
| cn-block | 35 |
| speed | 20 |
