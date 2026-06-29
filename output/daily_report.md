# AutoNodes 每日报告

生成时间：2026-06-29 04:31:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75950 |
| 去重后节点数 | 22966 |
| TCP 可达数 | 3000 |
| 真测通过数 | 660 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22966 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 24.8 |
| geo | 1.4 |
| probe | 54.1 |
| real_test | 140.1 |
| tcp | 30.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 131 | 119 | 12 | 90.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 98 | 79 | 19 | 80.6% |
| vless | 729 | 420 | 309 | 57.6% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 134 |
| speed:ClientOSError | 112 |
| geo:ClientOSError | 47 |
| speed:TimeoutError | 15 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| 204:TimeoutError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4183 |
| ConnectionRefusedError | 650 |
| gaierror | 249 |
| OSError | 131 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.92 | prefer | 367 | 0.842 | 16006 |
| Surfboard-tg-mixed | 0.796 | prefer | 262 | 0.718 | 5165 |
| Au1rxx-base64 | 0.655 | observe | 41 | 0.659 | 86 |
| DeltaKronecker-all | 0.413 | observe | 292 | 0.332 | 6788 |
| nscl5-all | 0.358 | observe | 2 | 1.0 | 1166 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7662 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Parsashonam | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.332 | 97 | 195 | 292 |
| Au1rxx-base64 | 0.659 | 27 | 14 | 41 |
| Surfboard-tg-mixed | 0.718 | 188 | 74 | 262 |
| mheidari-all | 0.842 | 309 | 58 | 367 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16006 | yes | 2.91 | 0 |
| Epodonios-all | 7662 | yes | 2.0 | 0 |
| SoliSpirit-all | 6991 | yes | 3.23 | 0 |
| DeltaKronecker-all | 6788 | yes | 3.16 | 0 |
| mahdibland-V2RayAggregator | 5325 | yes | 1.53 | 0 |
| Surfboard-tg-mixed | 5165 | yes | 2.18 | 0 |
| barry-far-vless | 4390 | yes | 1.98 | 0 |
| 10ium-ScrapeCategorize-Vless | 4327 | yes | 1.81 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.45 | 0 |
| Surfboard-tg-vless | 3804 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 181 |
| speed | 127 |
| cn-block | 19 |
| 204 | 14 |
