# AutoNodes 每日报告

生成时间：2026-07-24 19:42:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83183 |
| 去重后节点数 | 22837 |
| TCP 可达数 | 3000 |
| 真测通过数 | 708 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22837 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 39.6 |
| geo | 1.3 |
| probe | 66.6 |
| real_test | 162.0 |
| tcp | 33.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 132 | 102 | 30 | 77.3% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 513 | 439 | 74 | 85.6% |
| vless | 274 | 124 | 150 | 45.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 69 |
| geo:TimeoutError | 65 |
| cn-block:TimeoutError | 32 |
| 204:TimeoutError | 29 |
| 204:ProxyError | 17 |
| geo:ClientOSError | 11 |
| cn-block:ProxyError | 10 |
| cn-block:ClientOSError | 10 |
| speed:TimeoutError | 8 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4306 |
| ConnectionRefusedError | 698 |
| gaierror | 390 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.854 | prefer | 104 | 0.779 | 5475 |
| Au1rxx-base64 | 0.835 | prefer | 119 | 0.824 | 432 |
| mheidari-all | 0.809 | prefer | 596 | 0.73 | 19355 |
| DeltaKronecker-all | 0.603 | observe | 105 | 0.524 | 5559 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3847 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4588 |
| Epodonios-all | 0.255 | observe | 0 | None | 6668 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3967 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.524 | 55 | 50 | 105 |
| mheidari-all | 0.73 | 435 | 161 | 596 |
| Surfboard-tg-mixed | 0.779 | 81 | 23 | 104 |
| Au1rxx-base64 | 0.824 | 98 | 21 | 119 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19355 | yes | 4.56 | 0 |
| SoliSpirit-all | 6766 | yes | 2.61 | 0 |
| Epodonios-all | 6668 | yes | 3.28 | 0 |
| DeltaKronecker-all | 5559 | yes | 3.61 | 0 |
| Surfboard-tg-mixed | 5475 | yes | 2.67 | 0 |
| mahdibland-V2RayAggregator | 5027 | yes | 1.91 | 0 |
| barry-far-vless | 4905 | yes | 1.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 4588 | yes | 1.14 | 0 |
| Surfboard-tg-vless | 4271 | yes | 3.02 | 0 |
| MatinGhanbari-all-sub | 3967 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 77 |
| geo | 77 |
| cn-block | 52 |
| 204 | 50 |
