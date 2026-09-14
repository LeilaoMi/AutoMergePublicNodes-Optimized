# AutoNodes 每日报告

生成时间：2026-09-14 04:34:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/2 |
| 清理建议：优先/观察 | 2/103 |
| 原始节点数 | 89766 |
| 去重后节点数 | 25427 |
| TCP 可达数 | 3000 |
| 真测通过数 | 488 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25427 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 80.8 |
| geo | 1.4 |
| probe | 288.6 |
| real_test | 429.9 |
| tcp | 43.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 36 | 21 | 15 | 58.3% |
| hysteria2 | 24 | 22 | 2 | 91.7% |
| shadowsocks | 169 | 157 | 12 | 92.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 25 | 11 | 14 | 44.0% |
| vless | 598 | 271 | 327 | 45.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 123 |
| geo:ClientOSError | 67 |
| speed:TimeoutError | 56 |
| speed:ClientOSError | 52 |
| 204:ProxyError | 25 |
| cn-block:TimeoutError | 19 |
| cn-block:ClientOSError | 13 |
| 204:TimeoutError | 12 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5999 |
| ConnectionRefusedError | 956 |
| gaierror | 412 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.859 | prefer | 315 | 0.794 | 1684 |
| Surfboard-tg-mixed | 0.797 | prefer | 164 | 0.72 | 7482 |
| mheidari-all | 0.584 | observe | 127 | 0.504 | 15963 |
| ermaozi | 0.583 | observe | 28 | 0.571 | 417 |
| ermaozi-get_subscribe | 0.427 | observe | 9 | 0.667 | 444 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7945 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8786 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6107 |

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
| downweight | xiaoji235-airport-v2ray-all | 0.216 | 20 | 0.1 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.247 | 190 | 0.163 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 3 | 3 |
| xiaoji235-airport-v2ray-all | 0.1 | 2 | 18 | 20 |
| DeltaKronecker-all | 0.163 | 31 | 159 | 190 |
| mheidari-all | 0.504 | 64 | 63 | 127 |
| ermaozi | 0.571 | 16 | 12 | 28 |
| ermaozi-get_subscribe | 0.667 | 6 | 3 | 9 |
| Surfboard-tg-mixed | 0.72 | 118 | 46 | 164 |
| Au1rxx-base64 | 0.794 | 250 | 65 | 315 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15963 | yes | 6.25 | 0 |
| SoliSpirit-all | 8786 | yes | 3.23 | 0 |
| Epodonios-all | 7945 | yes | 3.28 | 0 |
| Surfboard-tg-mixed | 7482 | yes | 4.24 | 0 |
| barry-far-vless | 6350 | yes | 2.19 | 0 |
| Surfboard-tg-vless | 6107 | yes | 3.96 | 0 |
| DeltaKronecker-all | 5892 | yes | 5.49 | 0 |
| xiaoji235-airport-v2ray-all | 5301 | yes | 2.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4839 | yes | 2.38 | 0 |
| mahdibland-V2RayAggregator | 4222 | yes | 2.94 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 190 |
| speed | 108 |
| 204 | 40 |
| cn-block | 33 |
