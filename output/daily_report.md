# AutoNodes 每日报告

生成时间：2026-09-17 16:50:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 86881 |
| 去重后节点数 | 24278 |
| TCP 可达数 | 3000 |
| 真测通过数 | 445 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24278 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 79.2 |
| geo | 1.4 |
| probe | 283.0 |
| real_test | 268.3 |
| tcp | 41.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 38 | 23 | 15 | 60.5% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 162 | 149 | 13 | 92.0% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 10 | 7 | 3 | 70.0% |
| vless | 382 | 248 | 134 | 64.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 32 |
| geo:ClientOSError | 32 |
| geo:TimeoutError | 25 |
| 204:TimeoutError | 21 |
| cn-block:TimeoutError | 18 |
| speed:ClientOSError | 17 |
| speed:TimeoutError | 10 |
| cn-block:ClientOSError | 10 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5462 |
| ConnectionRefusedError | 921 |
| gaierror | 419 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.928 | prefer | 254 | 0.866 | 1619 |
| ermaozi | 0.733 | prefer | 30 | 0.733 | 357 |
| DeltaKronecker-all | 0.72 | prefer | 112 | 0.643 | 5931 |
| mheidari-all | 0.705 | prefer | 78 | 0.628 | 16008 |
| Surfboard-tg-mixed | 0.698 | observe | 129 | 0.62 | 7430 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 119 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5093 |
| Epodonios-all | 0.255 | observe | 0 | None | 7888 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9066 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.136 | 8 | 0.125 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.125 | 1 | 7 | 8 |
| Surfboard-tg-mixed | 0.62 | 80 | 49 | 129 |
| mheidari-all | 0.628 | 49 | 29 | 78 |
| DeltaKronecker-all | 0.643 | 72 | 40 | 112 |
| ermaozi | 0.733 | 22 | 8 | 30 |
| Au1rxx-base64 | 0.866 | 220 | 34 | 254 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16008 | yes | 5.04 | 0 |
| SoliSpirit-all | 9066 | yes | 4.33 | 0 |
| Epodonios-all | 7888 | yes | 5.55 | 0 |
| Surfboard-tg-mixed | 7430 | yes | 4.3 | 0 |
| barry-far-vless | 6129 | yes | 2.16 | 0 |
| DeltaKronecker-all | 5931 | yes | 5.2 | 0 |
| Surfboard-tg-vless | 5904 | yes | 3.45 | 0 |
| 10ium-ScrapeCategorize-Vless | 5093 | yes | 3.35 | 0 |
| mahdibland-V2RayAggregator | 4179 | yes | 2.02 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.47 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 58 |
| 204 | 53 |
| cn-block | 31 |
| speed | 27 |
