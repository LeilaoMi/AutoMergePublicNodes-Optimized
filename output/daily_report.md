# AutoNodes 每日报告

生成时间：2026-07-16 08:27:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78890 |
| 去重后节点数 | 24434 |
| TCP 可达数 | 3000 |
| 真测通过数 | 440 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24434 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 32.2 |
| geo | 0.8 |
| probe | 52.5 |
| real_test | 132.7 |
| tcp | 32.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 77 | 64 | 13 | 83.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 399 | 322 | 77 | 80.7% |
| vless | 116 | 10 | 106 | 8.6% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 70 |
| 204:TimeoutError | 35 |
| speed:ClientOSError | 25 |
| cn-block:TimeoutError | 18 |
| 204:ProxyError | 12 |
| speed:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 5 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4638 |
| ConnectionRefusedError | 642 |
| OSError | 214 |
| gaierror | 172 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | prefer | 99 | 0.98 | 149 |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.814 | prefer | 122 | 0.738 | 16602 |
| Surfboard-tg-mixed | 0.665 | observe | 39 | 0.59 | 5419 |
| DeltaKronecker-all | 0.649 | observe | 337 | 0.57 | 8462 |
| xiaoji235-airport-v2ray-all | 0.325 | observe | 1 | 1.0 | 1757 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4470 |
| Epodonios-all | 0.255 | observe | 0 | None | 6507 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6810 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.57 | 192 | 145 | 337 |
| Surfboard-tg-mixed | 0.59 | 23 | 16 | 39 |
| mheidari-all | 0.738 | 90 | 32 | 122 |
| Au1rxx-base64 | 0.98 | 97 | 2 | 99 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16602 | yes | 4.01 | 0 |
| DeltaKronecker-all | 8462 | yes | 3.12 | 0 |
| SoliSpirit-all | 6810 | yes | 2.42 | 0 |
| Epodonios-all | 6507 | yes | 1.02 | 0 |
| Surfboard-tg-mixed | 5419 | yes | 2.15 | 0 |
| mahdibland-V2RayAggregator | 5262 | yes | 0.84 | 0 |
| barry-far-vless | 4742 | yes | 2.14 | 0 |
| 10ium-ScrapeCategorize-Vless | 4470 | yes | 1.77 | 0 |
| Surfboard-tg-vless | 4150 | yes | 2.32 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 1.97 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.086 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 80 |
| 204 | 53 |
| speed | 35 |
| cn-block | 30 |
