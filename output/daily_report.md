# AutoNodes 每日报告

生成时间：2026-08-01 19:22:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78665 |
| 去重后节点数 | 23513 |
| TCP 可达数 | 3000 |
| 真测通过数 | 590 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23513 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 40.4 |
| geo | 1.4 |
| probe | 58.4 |
| real_test | 149.4 |
| tcp | 34.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 146 | 146 | 0 | 100.0% |
| hysteria2 | 21 | 18 | 3 | 85.7% |
| shadowsocks | 135 | 106 | 29 | 78.5% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 28 | 26 | 2 | 92.9% |
| vless | 499 | 290 | 209 | 58.1% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 98 |
| speed:TimeoutError | 33 |
| 204:TimeoutError | 31 |
| cn-block:TimeoutError | 27 |
| geo:ClientOSError | 18 |
| speed:ClientOSError | 11 |
| 204:ProxyError | 9 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4743 |
| ConnectionRefusedError | 785 |
| gaierror | 289 |
| OSError | 223 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 148 | 1.0 | 194 |
| Au1rxx-base64 | 0.766 | prefer | 502 | 0.699 | 1692 |
| Surfboard-tg-mixed | 0.638 | observe | 75 | 0.56 | 5294 |
| DeltaKronecker-all | 0.514 | observe | 104 | 0.433 | 5502 |
| mheidari-all | 0.4 | observe | 4 | 0.75 | 16619 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 55 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5391 |
| Epodonios-all | 0.255 | observe | 0 | None | 5909 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6647 |

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
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.433 | 45 | 59 | 104 |
| Surfboard-tg-mixed | 0.56 | 42 | 33 | 75 |
| Au1rxx-base64 | 0.699 | 351 | 151 | 502 |
| mheidari-all | 0.75 | 3 | 1 | 4 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 148 | 0 | 148 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16619 | yes | 4.71 | 0 |
| SoliSpirit-all | 6647 | yes | 2.98 | 0 |
| Epodonios-all | 5909 | yes | 4.88 | 0 |
| DeltaKronecker-all | 5502 | yes | 5.14 | 0 |
| 10ium-ScrapeCategorize-Vless | 5391 | yes | 1.97 | 0 |
| Surfboard-tg-mixed | 5294 | yes | 3.58 | 0 |
| mahdibland-V2RayAggregator | 5071 | yes | 2.82 | 0 |
| barry-far-vless | 4547 | yes | 1.08 | 0 |
| Surfboard-tg-vless | 4168 | yes | 3.23 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 2.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 118 |
| speed | 46 |
| 204 | 46 |
| cn-block | 36 |
