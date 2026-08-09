# AutoNodes 每日报告

生成时间：2026-08-09 13:06:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 85362 |
| 去重后节点数 | 23924 |
| TCP 可达数 | 3000 |
| 真测通过数 | 483 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23924 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 28.8 |
| geo | 1.4 |
| probe | 51.3 |
| real_test | 112.5 |
| tcp | 36.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 21 | 0 | 100.0% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 141 | 137 | 4 | 97.2% |
| socks | 17 | 13 | 4 | 76.5% |
| trojan | 132 | 126 | 6 | 95.5% |
| vless | 266 | 164 | 102 | 61.7% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 25 |
| 204:TimeoutError | 21 |
| speed:TimeoutError | 17 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 13 |
| speed:ClientOSError | 11 |
| geo:TimeoutError | 8 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4964 |
| ConnectionRefusedError | 834 |
| gaierror | 292 |
| OSError | 228 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.989 | prefer | 403 | 0.923 | 1704 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.778 | prefer | 104 | 0.702 | 6480 |
| mheidari-all | 0.33 | observe | 70 | 0.243 | 20170 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 77 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5505 |
| Epodonios-all | 0.255 | observe | 0 | None | 7128 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7369 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5320 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.243 | 17 | 53 | 70 |
| Surfboard-tg-mixed | 0.702 | 73 | 31 | 104 |
| Au1rxx-base64 | 0.923 | 372 | 31 | 403 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20170 | yes | 4.62 | 0 |
| SoliSpirit-all | 7369 | yes | 2.56 | 0 |
| Epodonios-all | 7128 | yes | 4.84 | 0 |
| Surfboard-tg-mixed | 6480 | yes | 3.49 | 0 |
| barry-far-vless | 5659 | yes | 0.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 5505 | yes | 1.32 | 0 |
| Surfboard-tg-vless | 5320 | yes | 3.67 | 0 |
| mahdibland-V2RayAggregator | 5130 | yes | 2.83 | 0 |
| DeltaKronecker-all | 4998 | yes | 4.79 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 37 |
| geo | 33 |
| speed | 29 |
| cn-block | 18 |
