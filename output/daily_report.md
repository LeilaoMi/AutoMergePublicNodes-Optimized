# AutoNodes 每日报告

生成时间：2026-07-15 13:57:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76174 |
| 去重后节点数 | 22913 |
| TCP 可达数 | 3000 |
| 真测通过数 | 279 |
| verified 输出数 | 279 |
| global 输出数 | 290 |
| all 输出数 | 22913 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 44.5 |
| geo | 1.3 |
| probe | 46.7 |
| real_test | 82.9 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 52 | 40 | 12 | 76.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 216 | 185 | 31 | 85.6% |
| vless | 75 | 9 | 66 | 12.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 43 |
| speed:ClientOSError | 20 |
| 204:TimeoutError | 14 |
| speed:TimeoutError | 8 |
| cn-block:TimeoutError | 7 |
| 204:ProxyError | 6 |
| cn-block:ProxyError | 4 |
| geo:ClientOSError | 3 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4346 |
| ConnectionRefusedError | 665 |
| gaierror | 271 |
| OSError | 209 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.853 | prefer | 170 | 0.776 | 16029 |
| Surfboard-tg-mixed | 0.801 | prefer | 59 | 0.729 | 5463 |
| DeltaKronecker-all | 0.622 | observe | 116 | 0.543 | 6421 |
| nscl5-all | 0.321 | observe | 3 | 0.667 | 1300 |
| Au1rxx-base64 | 0.317 | observe | 2 | 1.0 | 149 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6619 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3979 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7237 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.543 | 63 | 53 | 116 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.729 | 43 | 16 | 59 |
| mheidari-all | 0.776 | 132 | 38 | 170 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Au1rxx-base64 | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16029 | yes | 3.23 | 0 |
| SoliSpirit-all | 7237 | yes | 3.65 | 0 |
| Epodonios-all | 6619 | yes | 3.43 | 0 |
| DeltaKronecker-all | 6421 | yes | 3.23 | 0 |
| Surfboard-tg-mixed | 5463 | yes | 1.92 | 0 |
| mahdibland-V2RayAggregator | 5187 | yes | 0.54 | 0 |
| barry-far-vless | 4859 | yes | 0.87 | 0 |
| Surfboard-tg-vless | 4283 | yes | 2.18 | 0 |
| MatinGhanbari-all-sub | 3979 | yes | 1.14 | 0 |
| 10ium-ScrapeCategorize-Vless | 3759 | yes | 1.04 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 46 |
| speed | 29 |
| 204 | 22 |
| cn-block | 14 |
