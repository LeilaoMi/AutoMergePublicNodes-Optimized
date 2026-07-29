# AutoNodes 每日报告

生成时间：2026-07-29 19:28:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79381 |
| 去重后节点数 | 22734 |
| TCP 可达数 | 3000 |
| 真测通过数 | 431 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22734 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 40.9 |
| geo | 1.3 |
| probe | 54.0 |
| real_test | 111.4 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 70 | 70 | 0 | 100.0% |
| hysteria2 | 15 | 11 | 4 | 73.3% |
| shadowsocks | 200 | 150 | 50 | 75.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 34 | 29 | 5 | 85.3% |
| vless | 253 | 169 | 84 | 66.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 36 |
| 204:TimeoutError | 33 |
| cn-block:TimeoutError | 30 |
| speed:TimeoutError | 16 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 6 |
| speed:ClientOSError | 6 |
| geo:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4146 |
| ConnectionRefusedError | 735 |
| gaierror | 328 |
| OSError | 223 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 70 | 1.0 | 84 |
| Au1rxx-base64 | 0.815 | prefer | 289 | 0.761 | 1384 |
| Surfboard-tg-mixed | 0.722 | prefer | 118 | 0.644 | 5853 |
| DeltaKronecker-all | 0.712 | prefer | 85 | 0.635 | 5519 |
| mheidari-all | 0.679 | observe | 11 | 0.909 | 16105 |
| xiaoji235-airport-v2ray-all | 0.329 | observe | 1 | 1.0 | 1861 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5118 |
| Epodonios-all | 0.255 | observe | 0 | None | 6489 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6586 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.635 | 54 | 31 | 85 |
| Surfboard-tg-mixed | 0.644 | 76 | 42 | 118 |
| Au1rxx-base64 | 0.761 | 220 | 69 | 289 |
| mheidari-all | 0.909 | 10 | 1 | 11 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 70 | 0 | 70 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16105 | yes | 4.01 | 0 |
| SoliSpirit-all | 6586 | yes | 3.65 | 0 |
| Epodonios-all | 6489 | yes | 1.38 | 0 |
| Surfboard-tg-mixed | 5853 | yes | 2.95 | 0 |
| DeltaKronecker-all | 5519 | yes | 4.45 | 0 |
| 10ium-ScrapeCategorize-Vless | 5118 | yes | 2.65 | 0 |
| mahdibland-V2RayAggregator | 5076 | yes | 1.46 | 0 |
| barry-far-vless | 4922 | yes | 1.56 | 0 |
| Surfboard-tg-vless | 4561 | yes | 2.57 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 1.8 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 43 |
| geo | 41 |
| cn-block | 38 |
| speed | 22 |
