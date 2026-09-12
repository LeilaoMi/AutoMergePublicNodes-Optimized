# AutoNodes 每日报告

生成时间：2026-09-12 20:34:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 83799 |
| 去重后节点数 | 23044 |
| TCP 可达数 | 3000 |
| 真测通过数 | 462 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23044 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| generate | 81.4 |
| geo | 1.6 |
| probe | 240.0 |
| real_test | 252.8 |
| tcp | 37.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 23 | 8 | 15 | 34.8% |
| hysteria2 | 25 | 23 | 2 | 92.0% |
| shadowsocks | 140 | 127 | 13 | 90.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 48 | 16 | 32 | 33.3% |
| vless | 393 | 286 | 107 | 72.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 43 |
| geo:ClientOSError | 42 |
| cn-block:TimeoutError | 23 |
| 204:ProxyError | 19 |
| speed:ClientOSError | 17 |
| cn-block:ClientOSError | 7 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 5 |
| geo:TimeoutError | 5 |
| 204:ProxyConnectionError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4541 |
| ConnectionRefusedError | 913 |
| gaierror | 492 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.982 | prefer | 49 | 0.918 | 15722 |
| Au1rxx-base64 | 0.893 | prefer | 322 | 0.829 | 1650 |
| DeltaKronecker-all | 0.704 | prefer | 179 | 0.626 | 5970 |
| Surfboard-tg-mixed | 0.58 | observe | 56 | 0.5 | 7382 |
| ermaozi | 0.43 | observe | 19 | 0.421 | 393 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 161 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4793 |
| Epodonios-all | 0.255 | observe | 0 | None | 7802 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8908 |

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
| downweight | ermaozi-get_subscribe | 0.163 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| ermaozi | 0.421 | 8 | 11 | 19 |
| Surfboard-tg-mixed | 0.5 | 28 | 28 | 56 |
| DeltaKronecker-all | 0.626 | 112 | 67 | 179 |
| Au1rxx-base64 | 0.829 | 267 | 55 | 322 |
| mheidari-all | 0.918 | 45 | 4 | 49 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15722 | yes | 5.6 | 0 |
| SoliSpirit-all | 8908 | yes | 3.97 | 0 |
| Epodonios-all | 7802 | yes | 3.47 | 0 |
| Surfboard-tg-mixed | 7382 | yes | 4.57 | 0 |
| barry-far-vless | 6127 | yes | 2.82 | 0 |
| Surfboard-tg-vless | 5991 | yes | 4.77 | 0 |
| DeltaKronecker-all | 5970 | yes | 5.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 4793 | yes | 3.06 | 0 |
| mahdibland-V2RayAggregator | 4295 | yes | 0.14 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.59 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 68 |
| geo | 48 |
| cn-block | 30 |
| speed | 23 |
