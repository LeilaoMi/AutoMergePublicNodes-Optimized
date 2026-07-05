# AutoNodes 每日报告

生成时间：2026-07-05 04:02:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78644 |
| 去重后节点数 | 23862 |
| TCP 可达数 | 3000 |
| 真测通过数 | 451 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23862 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 24.6 |
| geo | 1.6 |
| probe | 43.3 |
| real_test | 87.4 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 146 | 131 | 15 | 89.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 263 | 242 | 21 | 92.0% |
| vless | 113 | 31 | 82 | 27.4% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 45 |
| speed:ClientOSError | 35 |
| 204:ClientOSError | 8 |
| geo:ClientOSError | 7 |
| cn-block:TimeoutError | 7 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 4 |
| 204:TimeoutError | 3 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:34986: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4503 |
| ConnectionRefusedError | 789 |
| OSError | 155 |
| gaierror | 82 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.954 | prefer | 85 | 0.882 | 16452 |
| Surfboard-tg-mixed | 0.872 | prefer | 157 | 0.796 | 5979 |
| Au1rxx-base64 | 0.805 | prefer | 58 | 0.81 | 125 |
| DeltaKronecker-all | 0.798 | prefer | 232 | 0.72 | 7309 |
| nscl5-all | 0.308 | observe | 1 | 1.0 | 1323 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 6981 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3983 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6984 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.72 | 167 | 65 | 232 |
| Surfboard-tg-mixed | 0.796 | 125 | 32 | 157 |
| Au1rxx-base64 | 0.81 | 47 | 11 | 58 |
| mheidari-all | 0.882 | 75 | 10 | 85 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16452 | yes | 3.7 | 0 |
| DeltaKronecker-all | 7309 | yes | 3.78 | 0 |
| SoliSpirit-all | 6984 | yes | 2.49 | 0 |
| Epodonios-all | 6981 | yes | 1.77 | 0 |
| Surfboard-tg-mixed | 5979 | yes | 2.55 | 0 |
| mahdibland-V2RayAggregator | 5366 | yes | 0.36 | 0 |
| barry-far-vless | 5089 | yes | 2.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 4424 | yes | 2.7 | 0 |
| MatinGhanbari-all-sub | 3983 | yes | 2.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 52 |
| speed | 41 |
| 204 | 13 |
| cn-block | 12 |
| sing-box exited 1 | 1 |
