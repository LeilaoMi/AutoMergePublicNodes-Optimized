# AutoNodes 每日报告

生成时间：2026-06-26 09:42:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 82588 |
| 去重后节点数 | 22700 |
| TCP 可达数 | 3000 |
| 真测通过数 | 351 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22700 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 42.5 |
| geo | 1.3 |
| probe | 64.6 |
| real_test | 117.1 |
| tcp | 30.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 97 | 83 | 14 | 85.6% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 113 | 50 | 63 | 44.2% |
| vless | 284 | 175 | 109 | 61.6% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 73 |
| 204:TimeoutError | 38 |
| cn-block:TimeoutError | 23 |
| geo:TimeoutError | 13 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 9 |
| geo:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4308 |
| ConnectionRefusedError | 639 |
| gaierror | 168 |
| OSError | 119 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Au1rxx-base64 | 0.89 | prefer | 42 | 0.905 | 96 |
| mheidari-all | 0.729 | prefer | 189 | 0.651 | 16243 |
| Surfboard-tg-mixed | 0.661 | observe | 189 | 0.582 | 5153 |
| DeltaKronecker-all | 0.605 | observe | 78 | 0.526 | 12590 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1175 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4567 |
| Epodonios-all | 0.255 | observe | 0 | None | 7806 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3985 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.526 | 41 | 37 | 78 |
| Surfboard-tg-mixed | 0.582 | 110 | 79 | 189 |
| mheidari-all | 0.651 | 123 | 66 | 189 |
| Au1rxx-base64 | 0.905 | 38 | 4 | 42 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16243 | yes | 3.47 | 0 |
| DeltaKronecker-all | 12590 | yes | 4.07 | 0 |
| Epodonios-all | 7806 | yes | 2.03 | 0 |
| SoliSpirit-all | 7302 | yes | 2.99 | 0 |
| mahdibland-V2RayAggregator | 5185 | yes | 2.45 | 0 |
| Surfboard-tg-mixed | 5153 | yes | 2.2 | 0 |
| barry-far-vless | 4575 | yes | 1.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4567 | yes | 1.86 | 0 |
| MatinGhanbari-all-sub | 3985 | yes | 1.58 | 0 |
| Surfboard-tg-vless | 3827 | yes | 2.33 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 80 |
| 204 | 57 |
| cn-block | 29 |
| geo | 20 |
