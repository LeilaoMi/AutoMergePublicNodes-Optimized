# AutoNodes 每日报告

生成时间：2026-08-17 13:00:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83032 |
| 去重后节点数 | 23200 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1265 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23200 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 38.2 |
| geo | 0.8 |
| probe | 85.3 |
| real_test | 237.6 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 23 | 21 | 2 | 91.3% |
| shadowsocks | 139 | 132 | 7 | 95.0% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 780 | 766 | 14 | 98.2% |
| vless | 299 | 213 | 86 | 71.2% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 31 |
| speed:TimeoutError | 20 |
| geo:TimeoutError | 15 |
| 204:TimeoutError | 13 |
| speed:ClientOSError | 10 |
| geo:ClientOSError | 6 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4414 |
| ConnectionRefusedError | 839 |
| gaierror | 323 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 884 | 0.943 | 1983 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.942 | prefer | 63 | 0.873 | 6086 |
| mheidari-all | 0.933 | prefer | 284 | 0.856 | 17057 |
| DeltaKronecker-all | 0.376 | observe | 15 | 0.333 | 6368 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 194 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5085 |
| Epodonios-all | 0.255 | observe | 0 | None | 6645 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3989 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7827 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ermaozi | 0.129 | observe | 1 | 0.0 | 0 | 27 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.333 | 5 | 10 | 15 |
| mheidari-all | 0.856 | 243 | 41 | 284 |
| Surfboard-tg-mixed | 0.873 | 55 | 8 | 63 |
| Au1rxx-base64 | 0.943 | 834 | 50 | 884 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17057 | yes | 3.21 | 0 |
| SoliSpirit-all | 7827 | yes | 2.88 | 0 |
| Epodonios-all | 6645 | yes | 3.4 | 0 |
| DeltaKronecker-all | 6368 | yes | 3.56 | 0 |
| Surfboard-tg-mixed | 6086 | yes | 2.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 5085 | yes | 1.77 | 0 |
| barry-far-vless | 4992 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 4669 | yes | 1.34 | 0 |
| mahdibland-V2RayAggregator | 4046 | yes | 0.8 | 0 |
| MatinGhanbari-all-sub | 3989 | yes | 2.1 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 37 |
| speed | 30 |
| geo | 22 |
| 204 | 22 |
