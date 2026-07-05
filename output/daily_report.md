# AutoNodes 每日报告

生成时间：2026-07-05 19:29:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78323 |
| 去重后节点数 | 24054 |
| TCP 可达数 | 3000 |
| 真测通过数 | 278 |
| verified 输出数 | 278 |
| global 输出数 | 292 |
| all 输出数 | 24054 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 44.1 |
| geo | 1.3 |
| probe | 48.5 |
| real_test | 81.0 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 111 | 98 | 13 | 88.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 169 | 122 | 47 | 72.2% |
| vless | 42 | 13 | 29 | 31.0% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 19 |
| 204:ProxyError | 16 |
| geo:TimeoutError | 11 |
| 204:ClientOSError | 10 |
| cn-block:ClientOSError | 7 |
| cn-block:TimeoutError | 7 |
| geo:ClientOSError | 5 |
| 204:TimeoutError | 4 |
| speed:TimeoutError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4397 |
| ConnectionRefusedError | 783 |
| gaierror | 183 |
| OSError | 155 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.842 | prefer | 82 | 0.768 | 5733 |
| Au1rxx-base64 | 0.825 | prefer | 26 | 0.846 | 91 |
| mheidari-all | 0.787 | prefer | 97 | 0.711 | 16129 |
| DeltaKronecker-all | 0.771 | prefer | 121 | 0.694 | 7739 |
| nscl5-all | 0.411 | observe | 3 | 1.0 | 1323 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4662 |
| Epodonios-all | 0.255 | observe | 0 | None | 7047 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.694 | 84 | 37 | 121 |
| mheidari-all | 0.711 | 69 | 28 | 97 |
| Surfboard-tg-mixed | 0.768 | 63 | 19 | 82 |
| Au1rxx-base64 | 0.846 | 22 | 4 | 26 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 3 | 0 | 3 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16129 | yes | 4.16 | 0 |
| DeltaKronecker-all | 7739 | yes | 3.0 | 0 |
| Epodonios-all | 7047 | yes | 1.39 | 0 |
| SoliSpirit-all | 6940 | yes | 1.88 | 0 |
| Surfboard-tg-mixed | 5733 | yes | 2.78 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 1.77 | 0 |
| barry-far-vless | 4982 | yes | 2.11 | 0 |
| 10ium-ScrapeCategorize-Vless | 4662 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4405 | yes | 2.14 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.4 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| speed | 25 |
| geo | 19 |
| cn-block | 16 |
