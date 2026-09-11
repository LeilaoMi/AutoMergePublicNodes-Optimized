# AutoNodes 每日报告

生成时间：2026-09-11 20:55:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 83905 |
| 去重后节点数 | 23390 |
| TCP 可达数 | 3000 |
| 真测通过数 | 445 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23390 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 80.6 |
| geo | 1.4 |
| probe | 209.4 |
| real_test | 215.9 |
| tcp | 40.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 34 | 23 | 11 | 67.6% |
| hysteria2 | 25 | 23 | 2 | 92.0% |
| shadowsocks | 160 | 146 | 14 | 91.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 21 | 13 | 8 | 61.9% |
| vless | 353 | 238 | 115 | 67.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 58 |
| cn-block:TimeoutError | 21 |
| 204:TimeoutError | 20 |
| 204:ProxyError | 15 |
| speed:ClientOSError | 12 |
| cn-block:ClientOSError | 11 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 4 |
| 204:ServerDisconnectedError | 2 |
| 204:ClientOSError | 2 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5481 |
| ConnectionRefusedError | 908 |
| gaierror | 565 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.942 | prefer | 275 | 0.88 | 1630 |
| mheidari-all | 0.775 | prefer | 93 | 0.699 | 15494 |
| ermaozi | 0.748 | prefer | 28 | 0.75 | 377 |
| Surfboard-tg-mixed | 0.673 | observe | 148 | 0.595 | 7355 |
| DeltaKronecker-all | 0.658 | observe | 43 | 0.581 | 6070 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 194 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4932 |
| Epodonios-all | 0.255 | observe | 0 | None | 7810 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| downweight | ermaozi-get_subscribe | 0.162 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| DeltaKronecker-all | 0.581 | 25 | 18 | 43 |
| Surfboard-tg-mixed | 0.595 | 88 | 60 | 148 |
| mheidari-all | 0.699 | 65 | 28 | 93 |
| ermaozi | 0.75 | 21 | 7 | 28 |
| Au1rxx-base64 | 0.88 | 242 | 33 | 275 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15494 | yes | 5.32 | 0 |
| SoliSpirit-all | 9022 | yes | 4.09 | 0 |
| Epodonios-all | 7810 | yes | 3.27 | 0 |
| Surfboard-tg-mixed | 7355 | yes | 3.78 | 0 |
| barry-far-vless | 6209 | yes | 0.98 | 0 |
| DeltaKronecker-all | 6070 | yes | 5.54 | 0 |
| Surfboard-tg-vless | 5993 | yes | 4.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 4932 | yes | 1.51 | 0 |
| mahdibland-V2RayAggregator | 4223 | yes | 0.95 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.3 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 59 |
| 204 | 39 |
| cn-block | 37 |
| speed | 16 |
