# AutoNodes 每日报告

生成时间：2026-10-09 13:10:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 98198 |
| 去重后节点数 | 27459 |
| TCP 可达数 | 3000 |
| 真测通过数 | 414 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27459 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| generate | 97.5 |
| geo | 1.5 |
| probe | 358.2 |
| real_test | 367.9 |
| tcp | 47.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 7 | 2 | 5 | 28.6% |
| http | 61 | 28 | 33 | 45.9% |
| hysteria2 | 15 | 11 | 4 | 73.3% |
| shadowsocks | 130 | 104 | 26 | 80.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 124 | 99 | 25 | 79.8% |
| vless | 250 | 169 | 81 | 67.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 37 |
| 204:ProxyError | 35 |
| cn-block:TimeoutError | 35 |
| speed:TimeoutError | 13 |
| geo:TimeoutError | 12 |
| speed:ClientOSError | 11 |
| cn-block:ClientOSError | 9 |
| geo:ClientOSError | 9 |
| cn-block:ProxyError | 7 |
| 204:ProxyConnectionError | 3 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6282 |
| ConnectionRefusedError | 1002 |
| gaierror | 406 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.984 | prefer | 293 | 0.915 | 1810 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| mheidari-all | 0.803 | prefer | 45 | 0.733 | 23165 |
| Surfboard-tg-mixed | 0.68 | observe | 53 | 0.604 | 7139 |
| DeltaKronecker-all | 0.472 | observe | 128 | 0.391 | 5154 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4984 |
| Epodonios-all | 0.255 | observe | 0 | None | 7541 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10038 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.19 | 46 | 0.152 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.152 | 7 | 39 | 46 |
| DeltaKronecker-all | 0.391 | 50 | 78 | 128 |
| Surfboard-tg-mixed | 0.604 | 32 | 21 | 53 |
| mheidari-all | 0.733 | 33 | 12 | 45 |
| Au1rxx-base64 | 0.915 | 268 | 25 | 293 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23165 | yes | 6.38 | 0 |
| SoliSpirit-all | 10038 | yes | 6.24 | 0 |
| Epodonios-all | 7541 | yes | 4.19 | 0 |
| Surfboard-tg-mixed | 7139 | yes | 6.67 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.84 | 0 |
| barry-far-vless | 5830 | yes | 2.05 | 0 |
| Surfboard-tg-vless | 5578 | yes | 4.68 | 0 |
| DeltaKronecker-all | 5154 | yes | 5.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4984 | yes | 0.85 | 0 |
| mahdibland-V2RayAggregator | 4362 | yes | 3.88 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 78 |
| cn-block | 51 |
| speed | 25 |
| geo | 22 |
