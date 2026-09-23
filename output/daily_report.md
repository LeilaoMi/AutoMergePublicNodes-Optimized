# AutoNodes 每日报告

生成时间：2026-09-23 11:22:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 96837 |
| 去重后节点数 | 26486 |
| TCP 可达数 | 3000 |
| 真测通过数 | 406 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26486 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| generate | 76.3 |
| geo | 1.5 |
| probe | 272.5 |
| real_test | 195.0 |
| tcp | 42.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 64 | 37 | 27 | 57.8% |
| hysteria2 | 20 | 20 | 0 | 100.0% |
| shadowsocks | 163 | 155 | 8 | 95.1% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 16 | 9 | 7 | 56.2% |
| vless | 258 | 180 | 78 | 69.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 32 |
| 204:TimeoutError | 22 |
| geo:ClientOSError | 16 |
| cn-block:TimeoutError | 12 |
| 204:ProxyConnectionError | 10 |
| cn-block:ClientOSError | 9 |
| geo:TimeoutError | 8 |
| speed:TimeoutError | 6 |
| speed:ClientOSError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5811 |
| ConnectionRefusedError | 977 |
| gaierror | 449 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.993 | prefer | 223 | 0.933 | 1602 |
| mheidari-all | 0.778 | prefer | 94 | 0.702 | 22242 |
| Surfboard-tg-mixed | 0.739 | prefer | 133 | 0.662 | 7036 |
| ermaozi | 0.645 | observe | 55 | 0.636 | 346 |
| DeltaKronecker-all | 0.503 | observe | 12 | 0.583 | 6471 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5131 |
| Epodonios-all | 0.255 | observe | 0 | None | 7633 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9066 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5755 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.19 | 9 | 0.222 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.222 | 2 | 7 | 9 |
| DeltaKronecker-all | 0.583 | 7 | 5 | 12 |
| ermaozi | 0.636 | 35 | 20 | 55 |
| Surfboard-tg-mixed | 0.662 | 88 | 45 | 133 |
| mheidari-all | 0.702 | 66 | 28 | 94 |
| Au1rxx-base64 | 0.933 | 208 | 15 | 223 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22242 | yes | 6.97 | 0 |
| SoliSpirit-all | 9066 | yes | 2.53 | 0 |
| Epodonios-all | 7633 | yes | 0.32 | 0 |
| Surfboard-tg-mixed | 7036 | yes | 4.58 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.53 | 0 |
| DeltaKronecker-all | 6471 | yes | 5.22 | 0 |
| barry-far-vless | 5975 | yes | 1.65 | 0 |
| Surfboard-tg-vless | 5755 | yes | 4.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 5131 | yes | 1.29 | 0 |
| mahdibland-V2RayAggregator | 4187 | yes | 3.35 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 66 |
| geo | 24 |
| cn-block | 22 |
| speed | 10 |
