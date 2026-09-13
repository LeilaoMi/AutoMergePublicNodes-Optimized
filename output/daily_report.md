# AutoNodes 每日报告

生成时间：2026-09-13 16:08:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 95131 |
| 去重后节点数 | 25342 |
| TCP 可达数 | 3000 |
| 真测通过数 | 432 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25342 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| generate | 90.8 |
| geo | 1.4 |
| probe | 238.8 |
| real_test | 228.4 |
| tcp | 42.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 38 | 20 | 18 | 52.6% |
| hysteria2 | 23 | 19 | 4 | 82.6% |
| shadowsocks | 159 | 149 | 10 | 93.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 16 | 14 | 2 | 87.5% |
| vless | 383 | 228 | 155 | 59.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 54 |
| cn-block:ClientOSError | 35 |
| speed:ClientOSError | 26 |
| 204:TimeoutError | 21 |
| 204:ProxyError | 18 |
| cn-block:TimeoutError | 14 |
| geo:TimeoutError | 10 |
| cn-block:ProxyError | 5 |
| 204:ClientOSError | 3 |
| 204:ProxyConnectionError | 2 |
| speed:TimeoutError | 2 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5543 |
| ConnectionRefusedError | 985 |
| gaierror | 520 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.887 | prefer | 298 | 0.822 | 1678 |
| Surfboard-tg-mixed | 0.813 | prefer | 133 | 0.737 | 7605 |
| ermaozi | 0.599 | observe | 34 | 0.588 | 382 |
| mheidari-all | 0.524 | observe | 142 | 0.444 | 20611 |
| DeltaKronecker-all | 0.43 | observe | 9 | 0.556 | 5892 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5301 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4839 |
| Epodonios-all | 0.255 | observe | 0 | None | 7899 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9265 |

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
| downweight | ermaozi-get_subscribe | 0.089 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 5 | 5 |
| mheidari-all | 0.444 | 63 | 79 | 142 |
| DeltaKronecker-all | 0.556 | 5 | 4 | 9 |
| ermaozi | 0.588 | 20 | 14 | 34 |
| Surfboard-tg-mixed | 0.737 | 98 | 35 | 133 |
| Au1rxx-base64 | 0.822 | 245 | 53 | 298 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20611 | yes | 4.97 | 0 |
| SoliSpirit-all | 9265 | yes | 4.74 | 0 |
| Epodonios-all | 7899 | yes | 6.21 | 0 |
| Surfboard-tg-mixed | 7605 | yes | 4.22 | 0 |
| barry-far-vless | 6452 | yes | 1.74 | 0 |
| Surfboard-tg-vless | 6236 | yes | 5.16 | 0 |
| DeltaKronecker-all | 5892 | yes | 5.29 | 0 |
| xiaoji235-airport-v2ray-all | 5301 | yes | 2.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 4839 | yes | 3.31 | 0 |
| mahdibland-V2RayAggregator | 4221 | yes | 0.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 64 |
| cn-block | 54 |
| 204 | 45 |
| speed | 28 |
