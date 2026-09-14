# AutoNodes 每日报告

生成时间：2026-09-14 21:52:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 89958 |
| 去重后节点数 | 25660 |
| TCP 可达数 | 3000 |
| 真测通过数 | 468 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25660 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| generate | 79.1 |
| geo | 1.4 |
| probe | 278.7 |
| real_test | 223.4 |
| tcp | 41.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 35 | 22 | 13 | 62.9% |
| hysteria2 | 28 | 26 | 2 | 92.9% |
| shadowsocks | 169 | 156 | 13 | 92.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 18 | 6 | 12 | 33.3% |
| vless | 371 | 255 | 116 | 68.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 53 |
| geo:ClientOSError | 36 |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 13 |
| speed:ClientOSError | 7 |
| speed:TimeoutError | 4 |
| geo:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5976 |
| ConnectionRefusedError | 946 |
| gaierror | 378 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.993 | prefer | 311 | 0.926 | 1752 |
| Surfboard-tg-mixed | 0.721 | prefer | 90 | 0.644 | 7602 |
| mheidari-all | 0.612 | observe | 186 | 0.532 | 21195 |
| ermaozi | 0.61 | observe | 35 | 0.6 | 393 |
| ermaozi-get_subscribe | 0.272 | observe | 1 | 1.0 | 427 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 135 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4914 |
| Epodonios-all | 0.255 | observe | 0 | None | 7941 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8691 |

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
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.532 | 99 | 87 | 186 |
| ermaozi | 0.6 | 21 | 14 | 35 |
| Surfboard-tg-mixed | 0.644 | 58 | 32 | 90 |
| Au1rxx-base64 | 0.926 | 288 | 23 | 311 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21195 | yes | 2.64 | 0 |
| SoliSpirit-all | 8691 | yes | 1.35 | 0 |
| Epodonios-all | 7941 | yes | 3.74 | 0 |
| Surfboard-tg-mixed | 7602 | yes | 3.09 | 0 |
| barry-far-vless | 6284 | yes | 0.45 | 0 |
| Surfboard-tg-vless | 6098 | yes | 2.24 | 0 |
| DeltaKronecker-all | 5972 | yes | 3.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 4914 | yes | 0.6 | 0 |
| mahdibland-V2RayAggregator | 4099 | yes | 1.53 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.64 | 0 |

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
| cn-block | 70 |
| geo | 41 |
| 204 | 35 |
| speed | 12 |
