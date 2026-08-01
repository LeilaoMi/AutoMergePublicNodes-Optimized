# AutoNodes 每日报告

生成时间：2026-08-01 08:33:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78775 |
| 去重后节点数 | 23169 |
| TCP 可达数 | 3000 |
| 真测通过数 | 642 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23169 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 39.0 |
| geo | 1.3 |
| probe | 60.2 |
| real_test | 168.6 |
| tcp | 34.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 156 | 156 | 0 | 100.0% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 147 | 110 | 37 | 74.8% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 46 | 42 | 4 | 91.3% |
| vless | 650 | 312 | 338 | 48.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 147 |
| speed:TimeoutError | 70 |
| geo:ClientOSError | 56 |
| speed:ClientOSError | 38 |
| 204:TimeoutError | 25 |
| 204:ProxyError | 18 |
| cn-block:TimeoutError | 10 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 8 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4542 |
| ConnectionRefusedError | 751 |
| gaierror | 297 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 158 | 1.0 | 228 |
| Au1rxx-base64 | 0.796 | prefer | 461 | 0.731 | 1655 |
| Surfboard-tg-mixed | 0.62 | observe | 85 | 0.541 | 5316 |
| mheidari-all | 0.43 | observe | 9 | 0.556 | 16723 |
| DeltaKronecker-all | 0.389 | observe | 309 | 0.307 | 5502 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5391 |
| Epodonios-all | 0.255 | observe | 0 | None | 5937 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6670 |

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
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.307 | 95 | 214 | 309 |
| Surfboard-tg-mixed | 0.541 | 46 | 39 | 85 |
| mheidari-all | 0.556 | 5 | 4 | 9 |
| Au1rxx-base64 | 0.731 | 337 | 124 | 461 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 158 | 0 | 158 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16723 | yes | 4.82 | 0 |
| SoliSpirit-all | 6670 | yes | 3.33 | 0 |
| Epodonios-all | 5937 | yes | 4.99 | 0 |
| DeltaKronecker-all | 5502 | yes | 5.05 | 0 |
| 10ium-ScrapeCategorize-Vless | 5391 | yes | 1.85 | 0 |
| Surfboard-tg-mixed | 5316 | yes | 3.39 | 0 |
| mahdibland-V2RayAggregator | 5039 | yes | 3.05 | 0 |
| barry-far-vless | 4552 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4168 | yes | 5.23 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.96 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 204 |
| speed | 108 |
| 204 | 51 |
| cn-block | 20 |
