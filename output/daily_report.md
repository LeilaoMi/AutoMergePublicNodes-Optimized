# AutoNodes 每日报告

生成时间：2026-08-15 06:54:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78120 |
| 去重后节点数 | 22201 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1195 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22201 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 32.0 |
| geo | 1.4 |
| probe | 82.0 |
| real_test | 277.6 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 18 | 15 | 3 | 83.3% |
| shadowsocks | 134 | 126 | 8 | 94.0% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 567 | 547 | 20 | 96.5% |
| vless | 753 | 376 | 377 | 49.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 145 |
| cn-block:TimeoutError | 81 |
| geo:ClientOSError | 63 |
| speed:ClientOSError | 40 |
| speed:TimeoutError | 38 |
| 204:TimeoutError | 15 |
| cn-block:ClientOSError | 14 |
| 204:ProxyError | 8 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4658 |
| ConnectionRefusedError | 766 |
| gaierror | 268 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 811 | 0.948 | 1975 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.955 | prefer | 70 | 0.886 | 5665 |
| DeltaKronecker-all | 0.478 | observe | 578 | 0.398 | 5773 |
| nscl5-all | 0.349 | observe | 3 | 0.667 | 2081 |
| mheidari-all | 0.337 | observe | 13 | 0.308 | 15492 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 162 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5113 |
| Epodonios-all | 0.255 | observe | 0 | None | 6322 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.308 | 4 | 9 | 13 |
| DeltaKronecker-all | 0.398 | 230 | 348 | 578 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.886 | 62 | 8 | 70 |
| Au1rxx-base64 | 0.948 | 769 | 42 | 811 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15492 | yes | 4.12 | 0 |
| SoliSpirit-all | 7671 | yes | 3.83 | 0 |
| Epodonios-all | 6322 | yes | 5.74 | 0 |
| DeltaKronecker-all | 5773 | yes | 4.66 | 0 |
| Surfboard-tg-mixed | 5665 | yes | 5.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 5113 | yes | 4.07 | 0 |
| barry-far-vless | 4715 | yes | 2.31 | 0 |
| Surfboard-tg-vless | 4367 | yes | 3.45 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 2.14 | 0 |
| mahdibland-V2RayAggregator | 3935 | yes | 3.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 209 |
| cn-block | 97 |
| speed | 78 |
| 204 | 26 |
