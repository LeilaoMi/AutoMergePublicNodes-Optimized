# AutoNodes 每日报告

生成时间：2026-07-10 14:44:29

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75777 |
| 去重后节点数 | 23709 |
| TCP 可达数 | 3000 |
| 真测通过数 | 338 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23709 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 37.2 |
| geo | 1.4 |
| probe | 50.8 |
| real_test | 112.8 |
| tcp | 31.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 127 | 112 | 15 | 88.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 183 | 103 | 80 | 56.3% |
| vless | 192 | 79 | 113 | 41.1% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 72 |
| geo:TimeoutError | 29 |
| 204:ProxyError | 18 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 14 |
| cn-block:ProxyError | 13 |
| geo:ClientOSError | 13 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 9 |
| cn-block:ClientOSError | 8 |
| speed:ProxyError | 6 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4453 |
| ConnectionRefusedError | 664 |
| gaierror | 205 |
| OSError | 192 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.785 | prefer | 19 | 0.842 | 50 |
| mheidari-all | 0.729 | prefer | 75 | 0.653 | 16259 |
| Surfboard-tg-mixed | 0.669 | observe | 278 | 0.59 | 5542 |
| DeltaKronecker-all | 0.605 | observe | 137 | 0.526 | 7600 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1148 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4165 |
| Epodonios-all | 0.255 | observe | 0 | None | 6344 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6409 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.526 | 72 | 65 | 137 |
| Surfboard-tg-mixed | 0.59 | 164 | 114 | 278 |
| mheidari-all | 0.653 | 49 | 26 | 75 |
| Au1rxx-base64 | 0.842 | 16 | 3 | 19 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16259 | yes | 3.01 | 0 |
| DeltaKronecker-all | 7600 | yes | 3.31 | 0 |
| SoliSpirit-all | 6409 | yes | 2.12 | 0 |
| Epodonios-all | 6344 | yes | 0.59 | 0 |
| Surfboard-tg-mixed | 5542 | yes | 2.35 | 0 |
| mahdibland-V2RayAggregator | 5391 | yes | 0.69 | 0 |
| barry-far-vless | 4670 | yes | 1.45 | 0 |
| Surfboard-tg-vless | 4182 | yes | 3.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 4165 | yes | 1.61 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 87 |
| geo | 44 |
| 204 | 43 |
| cn-block | 35 |
