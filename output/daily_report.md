# AutoNodes 每日报告

生成时间：2026-09-11 16:24:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 83892 |
| 去重后节点数 | 23240 |
| TCP 可达数 | 3000 |
| 真测通过数 | 418 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23240 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 93.7 |
| geo | 1.4 |
| probe | 265.6 |
| real_test | 235.9 |
| tcp | 39.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 37 | 25 | 12 | 67.6% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 156 | 142 | 14 | 91.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 30 | 16 | 14 | 53.3% |
| vless | 333 | 213 | 120 | 64.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 53 |
| 204:TimeoutError | 26 |
| 204:ProxyError | 24 |
| cn-block:TimeoutError | 20 |
| cn-block:ClientOSError | 14 |
| speed:ClientOSError | 10 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| speed:TimeoutError | 3 |
| geo:TimeoutError | 3 |
| 204:ServerDisconnectedError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4855 |
| ConnectionRefusedError | 905 |
| gaierror | 556 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.895 | prefer | 260 | 0.827 | 1758 |
| ermaozi | 0.796 | prefer | 30 | 0.8 | 377 |
| Surfboard-tg-mixed | 0.728 | prefer | 140 | 0.65 | 7370 |
| mheidari-all | 0.707 | prefer | 81 | 0.63 | 15708 |
| DeltaKronecker-all | 0.651 | observe | 61 | 0.574 | 6070 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4932 |
| Epodonios-all | 0.255 | observe | 0 | None | 7833 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8514 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5979 |

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
| downweight | ermaozi-get_subscribe | 0.152 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.167 | 1 | 5 | 6 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.574 | 35 | 26 | 61 |
| mheidari-all | 0.63 | 51 | 30 | 81 |
| Surfboard-tg-mixed | 0.65 | 91 | 49 | 140 |
| ermaozi | 0.8 | 24 | 6 | 30 |
| Au1rxx-base64 | 0.827 | 215 | 45 | 260 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15708 | yes | 7.31 | 0 |
| SoliSpirit-all | 8514 | yes | 4.81 | 0 |
| Epodonios-all | 7833 | yes | 3.97 | 0 |
| Surfboard-tg-mixed | 7370 | yes | 5.95 | 0 |
| barry-far-vless | 6192 | yes | 3.19 | 0 |
| DeltaKronecker-all | 6070 | yes | 5.43 | 0 |
| Surfboard-tg-vless | 5979 | yes | 4.73 | 0 |
| 10ium-ScrapeCategorize-Vless | 4932 | yes | 3.81 | 0 |
| mahdibland-V2RayAggregator | 4223 | yes | 0.5 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.5 | 0 |

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
| 204 | 56 |
| geo | 56 |
| cn-block | 37 |
| speed | 14 |
