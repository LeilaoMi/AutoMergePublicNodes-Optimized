# AutoNodes 每日报告

生成时间：2026-07-03 14:24:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77345 |
| 去重后节点数 | 22900 |
| TCP 可达数 | 3000 |
| 真测通过数 | 295 |
| verified 输出数 | 295 |
| global 输出数 | 300 |
| all 输出数 | 22900 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| generate | 18.6 |
| geo | 1.6 |
| probe | 44.2 |
| real_test | 81.1 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 88 | 73 | 15 | 83.0% |
| socks | 3 | 3 | 0 | 100.0% |
| trojan | 185 | 138 | 47 | 74.6% |
| vless | 165 | 38 | 127 | 23.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 88 |
| geo:TimeoutError | 37 |
| 204:ProxyError | 13 |
| 204:ClientOSError | 8 |
| cn-block:ProxyError | 7 |
| geo:ProxyError | 7 |
| speed:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| geo:ClientOSError | 5 |
| 204:TimeoutError | 5 |
| cn-block:TimeoutError | 5 |
| speed:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4393 |
| ConnectionRefusedError | 663 |
| gaierror | 172 |
| OSError | 152 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.843 | prefer | 23 | 0.87 | 79 |
| Surfboard-tg-mixed | 0.767 | prefer | 94 | 0.691 | 5871 |
| mheidari-all | 0.622 | observe | 15 | 0.667 | 16032 |
| DeltaKronecker-all | 0.593 | observe | 312 | 0.513 | 6997 |
| nscl5-all | 0.403 | observe | 3 | 1.0 | 1114 |
| tg-ConfigV2rayNG | 0.263 | observe | 1 | 1.0 | 200 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4368 |
| Epodonios-all | 0.255 | observe | 0 | None | 6926 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 12 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.513 | 160 | 152 | 312 |
| mheidari-all | 0.667 | 10 | 5 | 15 |
| Surfboard-tg-mixed | 0.691 | 65 | 29 | 94 |
| Au1rxx-base64 | 0.87 | 20 | 3 | 23 |
| tg-ConfigV2rayNG | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 3 | 0 | 3 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16032 | yes | 3.14 | 0 |
| SoliSpirit-all | 7164 | yes | 1.91 | 0 |
| DeltaKronecker-all | 6997 | yes | 3.22 | 0 |
| Epodonios-all | 6926 | yes | 0.56 | 0 |
| Surfboard-tg-mixed | 5871 | yes | 1.86 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 0.39 | 0 |
| barry-far-vless | 5041 | yes | 1.21 | 0 |
| Surfboard-tg-vless | 4477 | yes | 2.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 4368 | yes | 1.68 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.52 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 97 |
| geo | 49 |
| 204 | 26 |
| cn-block | 17 |
