# AutoNodes 每日报告

生成时间：2026-08-01 03:33:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78571 |
| 去重后节点数 | 22863 |
| TCP 可达数 | 3000 |
| 真测通过数 | 619 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22863 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 30.3 |
| geo | 1.4 |
| probe | 53.6 |
| real_test | 129.6 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 80 | 80 | 0 | 100.0% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 160 | 154 | 6 | 96.2% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 41 | 33 | 8 | 80.5% |
| vless | 512 | 332 | 180 | 64.8% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 57 |
| geo:TimeoutError | 56 |
| speed:ClientOSError | 36 |
| geo:ClientOSError | 13 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4683 |
| ConnectionRefusedError | 752 |
| OSError | 224 |
| gaierror | 198 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 80 | 1.0 | 110 |
| Au1rxx-base64 | 0.938 | prefer | 529 | 0.873 | 1664 |
| Surfboard-tg-mixed | 0.573 | observe | 15 | 0.6 | 5365 |
| DeltaKronecker-all | 0.504 | observe | 57 | 0.421 | 5144 |
| mheidari-all | 0.406 | observe | 127 | 0.323 | 16450 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 6122 |
| nscl5-all | 0.305 | observe | 1 | 1.0 | 1258 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5507 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.152 | observe | 4 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| mheidari-all | 0.323 | 41 | 86 | 127 |
| DeltaKronecker-all | 0.421 | 24 | 33 | 57 |
| Surfboard-tg-mixed | 0.6 | 9 | 6 | 15 |
| Au1rxx-base64 | 0.873 | 462 | 67 | 529 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16450 | yes | 4.24 | 0 |
| SoliSpirit-all | 6657 | yes | 4.84 | 0 |
| Epodonios-all | 6122 | yes | 5.14 | 0 |
| 10ium-ScrapeCategorize-Vless | 5507 | yes | 3.14 | 0 |
| Surfboard-tg-mixed | 5365 | yes | 3.46 | 0 |
| DeltaKronecker-all | 5144 | yes | 5.55 | 0 |
| mahdibland-V2RayAggregator | 5081 | yes | 1.58 | 0 |
| barry-far-vless | 4596 | yes | 2.92 | 0 |
| Surfboard-tg-vless | 4239 | yes | 3.27 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.22 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 93 |
| geo | 69 |
| 204 | 19 |
| cn-block | 17 |
