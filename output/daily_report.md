# AutoNodes 每日报告

生成时间：2026-08-07 19:08:29

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 82638 |
| 去重后节点数 | 23519 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23519 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 36.5 |
| geo | 1.4 |
| probe | 56.4 |
| real_test | 104.4 |
| tcp | 36.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 19 | 1 | 95.0% |
| hysteria2 | 24 | 23 | 1 | 95.8% |
| shadowsocks | 153 | 134 | 19 | 87.6% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 139 | 138 | 1 | 99.3% |
| vless | 232 | 137 | 95 | 59.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 29 |
| 204:TimeoutError | 25 |
| geo:ClientOSError | 15 |
| geo:TimeoutError | 13 |
| cn-block:TimeoutError | 9 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5011 |
| ConnectionRefusedError | 821 |
| gaierror | 299 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.989 | prefer | 350 | 0.931 | 1506 |
| zhangkai | 0.91 | prefer | 20 | 0.95 | 25 |
| DeltaKronecker-all | 0.605 | observe | 175 | 0.526 | 5326 |
| Surfboard-tg-mixed | 0.556 | observe | 12 | 0.667 | 6368 |
| ninja-vless | 0.457 | observe | 7 | 0.714 | 1791 |
| mheidari-all | 0.401 | observe | 7 | 0.571 | 17684 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5282 |
| Epodonios-all | 0.255 | observe | 0 | None | 7096 |
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
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 9 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.526 | 92 | 83 | 175 |
| mheidari-all | 0.571 | 4 | 3 | 7 |
| Surfboard-tg-mixed | 0.667 | 8 | 4 | 12 |
| ninja-vless | 0.714 | 5 | 2 | 7 |
| Au1rxx-base64 | 0.931 | 326 | 24 | 350 |
| zhangkai | 0.95 | 19 | 1 | 20 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17684 | yes | 5.27 | 0 |
| SoliSpirit-all | 7593 | yes | 3.13 | 0 |
| Epodonios-all | 7096 | yes | 5.53 | 0 |
| Surfboard-tg-mixed | 6368 | yes | 2.88 | 0 |
| barry-far-vless | 5504 | yes | 2.45 | 0 |
| DeltaKronecker-all | 5326 | yes | 4.3 | 0 |
| 10ium-ScrapeCategorize-Vless | 5282 | yes | 2.22 | 0 |
| mahdibland-V2RayAggregator | 5175 | yes | 2.44 | 0 |
| Surfboard-tg-vless | 5103 | yes | 3.56 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 2.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 59 |
| geo | 29 |
| speed | 18 |
| cn-block | 14 |
