# AutoNodes 每日报告

生成时间：2026-07-04 13:49:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78542 |
| 去重后节点数 | 23660 |
| TCP 可达数 | 3000 |
| 真测通过数 | 300 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23660 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| generate | 34.8 |
| geo | 1.4 |
| probe | 49.8 |
| real_test | 91.6 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 110 | 95 | 15 | 86.4% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 207 | 139 | 68 | 67.1% |
| vless | 47 | 18 | 29 | 38.3% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 24 |
| 204:TimeoutError | 19 |
| 204:ProxyError | 17 |
| geo:TimeoutError | 17 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| geo:ClientOSError | 3 |
| speed:TimeoutError | 2 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4558 |
| ConnectionRefusedError | 677 |
| OSError | 152 |
| gaierror | 62 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.804 | prefer | 74 | 0.73 | 16374 |
| Au1rxx-base64 | 0.799 | prefer | 42 | 0.81 | 94 |
| Surfboard-tg-mixed | 0.794 | prefer | 89 | 0.719 | 6003 |
| DeltaKronecker-all | 0.727 | prefer | 165 | 0.648 | 7309 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 7174 |
| nscl5-all | 0.303 | observe | 1 | 1.0 | 1189 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 180 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.648 | 107 | 58 | 165 |
| Surfboard-tg-mixed | 0.719 | 64 | 25 | 89 |
| mheidari-all | 0.73 | 54 | 20 | 74 |
| Au1rxx-base64 | 0.81 | 34 | 8 | 42 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16374 | yes | 2.59 | 0 |
| DeltaKronecker-all | 7309 | yes | 3.09 | 0 |
| SoliSpirit-all | 7174 | yes | 1.81 | 0 |
| Epodonios-all | 6895 | yes | 1.46 | 0 |
| Surfboard-tg-mixed | 6003 | yes | 2.05 | 0 |
| mahdibland-V2RayAggregator | 5333 | yes | 0.82 | 0 |
| barry-far-vless | 5028 | yes | 0.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 0.84 | 0 |
| Surfboard-tg-vless | 4552 | yes | 1.56 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 0.92 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 42 |
| speed | 26 |
| cn-block | 23 |
| geo | 22 |
