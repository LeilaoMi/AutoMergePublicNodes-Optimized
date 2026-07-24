# AutoNodes 每日报告

生成时间：2026-07-24 14:02:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 82875 |
| 去重后节点数 | 22678 |
| TCP 可达数 | 3000 |
| 真测通过数 | 775 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22678 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 39.9 |
| geo | 1.3 |
| probe | 68.9 |
| real_test | 193.1 |
| tcp | 32.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 35 | 35 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 123 | 107 | 16 | 87.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 552 | 498 | 54 | 90.2% |
| vless | 297 | 129 | 168 | 43.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 71 |
| speed:ClientOSError | 46 |
| cn-block:TimeoutError | 31 |
| 204:TimeoutError | 26 |
| 204:ProxyError | 19 |
| geo:ClientOSError | 17 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4214 |
| ConnectionRefusedError | 690 |
| gaierror | 398 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.975 | prefer | 35 | 1.0 | 61 |
| Au1rxx-base64 | 0.869 | prefer | 119 | 0.857 | 432 |
| mheidari-all | 0.822 | prefer | 684 | 0.743 | 19570 |
| DeltaKronecker-all | 0.815 | prefer | 134 | 0.739 | 5559 |
| Surfboard-tg-mixed | 0.794 | prefer | 40 | 0.725 | 5218 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3847 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4588 |
| Epodonios-all | 0.255 | observe | 0 | None | 6424 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6965 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.725 | 29 | 11 | 40 |
| DeltaKronecker-all | 0.739 | 99 | 35 | 134 |
| mheidari-all | 0.743 | 508 | 176 | 684 |
| Au1rxx-base64 | 0.857 | 102 | 17 | 119 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 35 | 0 | 35 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19570 | yes | 4.45 | 0 |
| SoliSpirit-all | 6965 | yes | 2.75 | 0 |
| Epodonios-all | 6424 | yes | 2.32 | 0 |
| DeltaKronecker-all | 5559 | yes | 3.51 | 0 |
| Surfboard-tg-mixed | 5218 | yes | 3.21 | 0 |
| mahdibland-V2RayAggregator | 5027 | yes | 2.15 | 0 |
| barry-far-vless | 4809 | yes | 1.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 4588 | yes | 1.81 | 0 |
| Surfboard-tg-vless | 4143 | yes | 1.98 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 2.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 91 |
| speed | 58 |
| 204 | 51 |
| cn-block | 40 |
