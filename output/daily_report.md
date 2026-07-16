# AutoNodes 每日报告

生成时间：2026-07-16 14:10:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79344 |
| 去重后节点数 | 24515 |
| TCP 可达数 | 3000 |
| 真测通过数 | 500 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24515 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 29.8 |
| geo | 1.1 |
| probe | 48.1 |
| real_test | 110.8 |
| tcp | 33.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 147 | 129 | 18 | 87.8% |
| socks | 8 | 5 | 3 | 62.5% |
| trojan | 334 | 307 | 27 | 91.9% |
| vless | 81 | 17 | 64 | 21.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 33 |
| speed:ClientOSError | 30 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 8 |
| geo:ClientOSError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| cn-block:TimeoutError | 4 |
| speed:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4570 |
| ConnectionRefusedError | 656 |
| gaierror | 243 |
| OSError | 220 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.924 | prefer | 120 | 0.85 | 16416 |
| Au1rxx-base64 | 0.906 | prefer | 128 | 0.906 | 150 |
| Surfboard-tg-mixed | 0.899 | prefer | 92 | 0.826 | 5430 |
| DeltaKronecker-all | 0.802 | prefer | 232 | 0.724 | 8462 |
| xiaoji235-airport-v2ray-all | 0.325 | observe | 1 | 1.0 | 1757 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4470 |
| Epodonios-all | 0.255 | observe | 0 | None | 6545 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7282 |

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
| tg-LonUp_M | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.724 | 168 | 64 | 232 |
| Surfboard-tg-mixed | 0.826 | 76 | 16 | 92 |
| mheidari-all | 0.85 | 102 | 18 | 120 |
| Au1rxx-base64 | 0.906 | 116 | 12 | 128 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16416 | yes | 2.98 | 0 |
| DeltaKronecker-all | 8462 | yes | 16.05 | 0 |
| SoliSpirit-all | 7282 | yes | 2.11 | 0 |
| Epodonios-all | 6545 | yes | 1.43 | 0 |
| Surfboard-tg-mixed | 5430 | yes | 1.76 | 0 |
| mahdibland-V2RayAggregator | 5262 | yes | 1.84 | 0 |
| barry-far-vless | 4817 | yes | 1.18 | 0 |
| 10ium-ScrapeCategorize-Vless | 4470 | yes | 1.34 | 0 |
| Surfboard-tg-vless | 4211 | yes | 1.26 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 39 |
| speed | 32 |
| 204 | 27 |
| cn-block | 14 |
