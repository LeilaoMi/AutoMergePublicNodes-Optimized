# AutoNodes 每日报告

生成时间：2026-08-03 19:49:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 84754 |
| 去重后节点数 | 25181 |
| TCP 可达数 | 3000 |
| 真测通过数 | 478 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25181 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 31.2 |
| geo | 1.7 |
| probe | 56.8 |
| real_test | 126.8 |
| tcp | 37.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 67 | 67 | 0 | 100.0% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 129 | 102 | 27 | 79.1% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 64 | 61 | 3 | 95.3% |
| vless | 426 | 226 | 200 | 53.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 118 |
| 204:TimeoutError | 36 |
| speed:TimeoutError | 23 |
| geo:ClientOSError | 15 |
| 204:ProxyError | 11 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 7 |
| speed:ClientOSError | 7 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| geo:parse | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5006 |
| ConnectionRefusedError | 805 |
| gaierror | 302 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 67 | 1.0 | 92 |
| Au1rxx-base64 | 0.782 | prefer | 525 | 0.714 | 1718 |
| Surfboard-tg-mixed | 0.673 | observe | 25 | 0.6 | 5168 |
| mheidari-all | 0.446 | observe | 8 | 0.625 | 18750 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 5127 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 57 |
| DeltaKronecker-all | 0.256 | observe | 83 | 0.169 | 6205 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5285 |
| Epodonios-all | 0.255 | observe | 0 | None | 5757 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.169 | 14 | 69 | 83 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.6 | 15 | 10 | 25 |
| mheidari-all | 0.625 | 5 | 3 | 8 |
| Au1rxx-base64 | 0.714 | 375 | 150 | 525 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 67 | 0 | 67 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18750 | yes | 4.81 | 0 |
| SoliSpirit-all | 6825 | yes | 2.54 | 0 |
| DeltaKronecker-all | 6205 | yes | 4.87 | 0 |
| Epodonios-all | 5757 | yes | 3.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 5285 | yes | 0.85 | 0 |
| Surfboard-tg-mixed | 5168 | yes | 4.3 | 0 |
| mahdibland-V2RayAggregator | 5152 | yes | 2.59 | 0 |
| xiaoji235-airport-v2ray-all | 5127 | yes | 1.65 | 0 |
| barry-far-vless | 4498 | yes | 0.99 | 0 |
| Surfboard-tg-vless | 4147 | yes | 2.91 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 134 |
| 204 | 50 |
| speed | 31 |
| cn-block | 19 |
