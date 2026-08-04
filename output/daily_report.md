# AutoNodes 每日报告

生成时间：2026-08-04 03:18:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 85773 |
| 去重后节点数 | 24690 |
| TCP 可达数 | 3000 |
| 真测通过数 | 739 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24690 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 36.0 |
| geo | 1.4 |
| probe | 59.0 |
| real_test | 175.9 |
| tcp | 36.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 67 | 67 | 0 | 100.0% |
| hysteria2 | 20 | 20 | 0 | 100.0% |
| shadowsocks | 163 | 156 | 7 | 95.7% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 110 | 96 | 14 | 87.3% |
| vless | 801 | 397 | 404 | 49.6% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 181 |
| speed:TimeoutError | 83 |
| speed:ClientOSError | 62 |
| geo:ClientOSError | 59 |
| cn-block:TimeoutError | 22 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 6 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4609 |
| ConnectionRefusedError | 806 |
| gaierror | 357 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 67 | 1.0 | 92 |
| Au1rxx-base64 | 0.941 | prefer | 631 | 0.875 | 1681 |
| Surfboard-tg-mixed | 0.584 | observe | 127 | 0.504 | 5262 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 57 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5285 |
| Epodonios-all | 0.255 | observe | 0 | None | 5848 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6833 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4123 |
| barry-far-vless | 0.255 | observe | 0 | None | 4484 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.202 | 47 | 0.106 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.106 | 5 | 42 | 47 |
| mheidari-all | 0.172 | 50 | 241 | 291 |
| Surfboard-tg-mixed | 0.504 | 64 | 63 | 127 |
| Au1rxx-base64 | 0.875 | 552 | 79 | 631 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 67 | 0 | 67 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19963 | yes | 5.32 | 0 |
| SoliSpirit-all | 6833 | yes | 4.61 | 0 |
| DeltaKronecker-all | 6205 | yes | 5.19 | 0 |
| Epodonios-all | 5848 | yes | 4.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 5285 | yes | 2.78 | 0 |
| Surfboard-tg-mixed | 5262 | yes | 4.68 | 0 |
| mahdibland-V2RayAggregator | 5152 | yes | 2.45 | 0 |
| xiaoji235-airport-v2ray-all | 5127 | yes | 3.3 | 0 |
| barry-far-vless | 4484 | yes | 2.45 | 0 |
| Surfboard-tg-vless | 4123 | yes | 3.28 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 241 |
| speed | 145 |
| cn-block | 25 |
| 204 | 17 |
