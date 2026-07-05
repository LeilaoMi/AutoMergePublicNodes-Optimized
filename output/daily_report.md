# AutoNodes 每日报告

生成时间：2026-07-05 13:55:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 80046 |
| 去重后节点数 | 23893 |
| TCP 可达数 | 3000 |
| 真测通过数 | 308 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23893 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 29.4 |
| geo | 1.3 |
| probe | 53.2 |
| real_test | 74.4 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 124 | 108 | 16 | 87.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 174 | 148 | 26 | 85.1% |
| vless | 35 | 7 | 28 | 20.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 21 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 9 |
| geo:TimeoutError | 8 |
| 204:TimeoutError | 7 |
| geo:ClientOSError | 6 |
| cn-block:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4324 |
| ConnectionRefusedError | 787 |
| gaierror | 176 |
| OSError | 157 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.869 | prefer | 88 | 0.795 | 16415 |
| DeltaKronecker-all | 0.862 | prefer | 117 | 0.786 | 7739 |
| Surfboard-tg-mixed | 0.858 | prefer | 106 | 0.783 | 6156 |
| Au1rxx-base64 | 0.843 | prefer | 29 | 0.862 | 114 |
| nscl5-all | 0.364 | observe | 2 | 1.0 | 1323 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4662 |
| Epodonios-all | 0.255 | observe | 0 | None | 7257 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7136 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.783 | 83 | 23 | 106 |
| DeltaKronecker-all | 0.786 | 92 | 25 | 117 |
| mheidari-all | 0.795 | 70 | 18 | 88 |
| Au1rxx-base64 | 0.862 | 25 | 4 | 29 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16415 | yes | 3.74 | 0 |
| DeltaKronecker-all | 7739 | yes | 3.77 | 0 |
| Epodonios-all | 7257 | yes | 1.99 | 0 |
| SoliSpirit-all | 7136 | yes | 1.87 | 0 |
| Surfboard-tg-mixed | 6156 | yes | 1.79 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 1.56 | 0 |
| barry-far-vless | 5319 | yes | 1.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4662 | yes | 1.54 | 0 |
| Surfboard-tg-vless | 4608 | yes | 2.24 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.33 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 26 |
| speed | 21 |
| geo | 15 |
| cn-block | 9 |
