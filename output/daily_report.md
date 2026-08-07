# AutoNodes 每日报告

生成时间：2026-08-07 13:19:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 82701 |
| 去重后节点数 | 23372 |
| TCP 可达数 | 3000 |
| 真测通过数 | 468 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23372 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 39.5 |
| geo | 1.4 |
| probe | 48.4 |
| real_test | 106.3 |
| tcp | 35.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 22 | 19 | 3 | 86.4% |
| shadowsocks | 154 | 139 | 15 | 90.3% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 146 | 137 | 9 | 93.8% |
| vless | 250 | 149 | 101 | 59.6% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 30 |
| 204:ProxyError | 24 |
| geo:ClientOSError | 21 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 14 |
| speed:TimeoutError | 11 |
| speed:ClientOSError | 9 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4874 |
| ConnectionRefusedError | 793 |
| gaierror | 292 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.994 | prefer | 347 | 0.937 | 1509 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| DeltaKronecker-all | 0.638 | observe | 195 | 0.559 | 5326 |
| mheidari-all | 0.446 | observe | 5 | 0.8 | 17690 |
| Surfboard-tg-mixed | 0.403 | observe | 29 | 0.31 | 6364 |
| nscl5-all | 0.326 | observe | 1 | 1.0 | 1772 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5282 |
| Epodonios-all | 0.255 | observe | 0 | None | 6987 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7685 |

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
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.31 | 9 | 20 | 29 |
| DeltaKronecker-all | 0.559 | 109 | 86 | 195 |
| mheidari-all | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.937 | 325 | 22 | 347 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17690 | yes | 4.05 | 0 |
| SoliSpirit-all | 7685 | yes | 3.65 | 0 |
| Epodonios-all | 6987 | yes | 4.26 | 0 |
| Surfboard-tg-mixed | 6364 | yes | 2.66 | 0 |
| barry-far-vless | 5471 | yes | 1.11 | 0 |
| DeltaKronecker-all | 5326 | yes | 4.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 5282 | yes | 1.97 | 0 |
| mahdibland-V2RayAggregator | 5247 | yes | 3.56 | 0 |
| Surfboard-tg-vless | 5147 | yes | 3.19 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 2.07 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 51 |
| 204 | 43 |
| speed | 20 |
| cn-block | 17 |
