# AutoNodes 每日报告

生成时间：2026-07-28 03:02:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84746 |
| 去重后节点数 | 23236 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1062 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23236 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 22.0 |
| generate | 30.3 |
| geo | 1.3 |
| probe | 76.6 |
| real_test | 250.6 |
| tcp | 32.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 59 | 0 | 100.0% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 167 | 155 | 12 | 92.8% |
| socks | 7 | 5 | 2 | 71.4% |
| trojan | 538 | 518 | 20 | 96.3% |
| vless | 966 | 311 | 655 | 32.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 313 |
| speed:ClientOSError | 170 |
| geo:ClientOSError | 90 |
| speed:TimeoutError | 47 |
| 204:ProxyError | 35 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 11 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4339 |
| ConnectionRefusedError | 749 |
| gaierror | 243 |
| OSError | 222 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 485 | 0.963 | 1387 |
| zhangkai | 0.987 | prefer | 59 | 1.0 | 74 |
| mheidari-all | 0.945 | prefer | 243 | 0.868 | 18500 |
| Surfboard-tg-mixed | 0.611 | observe | 30 | 0.533 | 5606 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 3959 |
| DeltaKronecker-all | 0.409 | observe | 925 | 0.329 | 5643 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4831 |
| Epodonios-all | 0.255 | observe | 0 | None | 6592 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.329 | 304 | 621 | 925 |
| Surfboard-tg-mixed | 0.533 | 16 | 14 | 30 |
| mheidari-all | 0.868 | 211 | 32 | 243 |
| Au1rxx-base64 | 0.963 | 467 | 18 | 485 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 59 | 0 | 59 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18500 | yes | 4.1 | 0 |
| Epodonios-all | 6592 | yes | 2.9 | 0 |
| SoliSpirit-all | 6500 | yes | 3.41 | 0 |
| DeltaKronecker-all | 5643 | yes | 3.81 | 0 |
| Surfboard-tg-mixed | 5606 | yes | 3.09 | 0 |
| barry-far-vless | 5025 | yes | 1.6 | 0 |
| mahdibland-V2RayAggregator | 4997 | yes | 3.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 4831 | yes | 2.41 | 0 |
| Surfboard-tg-vless | 4470 | yes | 4.5 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 2.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 403 |
| speed | 217 |
| 204 | 48 |
| cn-block | 22 |
