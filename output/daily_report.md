# AutoNodes 每日报告

生成时间：2026-07-30 02:51:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77441 |
| 去重后节点数 | 22597 |
| TCP 可达数 | 3000 |
| 真测通过数 | 582 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22597 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| generate | 34.8 |
| geo | 1.4 |
| probe | 52.5 |
| real_test | 133.7 |
| tcp | 31.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 70 | 70 | 0 | 100.0% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 236 | 217 | 19 | 91.9% |
| socks | 15 | 12 | 3 | 80.0% |
| trojan | 79 | 63 | 16 | 79.7% |
| vless | 501 | 205 | 296 | 40.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 186 |
| geo:ClientOSError | 41 |
| speed:TimeoutError | 39 |
| speed:ClientOSError | 28 |
| cn-block:TimeoutError | 21 |
| 204:ProxyError | 8 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4152 |
| ConnectionRefusedError | 742 |
| gaierror | 314 |
| OSError | 223 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | prefer | 70 | 1.0 | 84 |
| Au1rxx-base64 | 0.971 | prefer | 290 | 0.924 | 1255 |
| Surfboard-tg-mixed | 0.716 | prefer | 174 | 0.638 | 5390 |
| mheidari-all | 0.447 | observe | 28 | 0.357 | 16333 |
| DeltaKronecker-all | 0.426 | observe | 348 | 0.345 | 5519 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 5118 |
| xiaoji235-airport-v2ray-all | 0.282 | observe | 2 | 0.5 | 1861 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 6124 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.345 | 120 | 228 | 348 |
| mheidari-all | 0.357 | 10 | 18 | 28 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.638 | 111 | 63 | 174 |
| Au1rxx-base64 | 0.924 | 268 | 22 | 290 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 70 | 0 | 70 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16333 | yes | 4.36 | 0 |
| SoliSpirit-all | 6420 | yes | 3.9 | 0 |
| Epodonios-all | 6124 | yes | 2.3 | 0 |
| DeltaKronecker-all | 5519 | yes | 4.83 | 0 |
| Surfboard-tg-mixed | 5390 | yes | 3.31 | 0 |
| 10ium-ScrapeCategorize-Vless | 5118 | yes | 2.39 | 0 |
| mahdibland-V2RayAggregator | 5076 | yes | 2.49 | 0 |
| barry-far-vless | 4688 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 4279 | yes | 3.46 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.13 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 228 |
| speed | 67 |
| cn-block | 24 |
| 204 | 16 |
