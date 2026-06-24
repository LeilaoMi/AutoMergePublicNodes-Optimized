# AutoNodes 每日报告

生成时间：2026-06-24 04:08:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77147 |
| 去重后节点数 | 22469 |
| TCP 可达数 | 3000 |
| 真测通过数 | 553 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22469 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 22.0 |
| geo | 1.4 |
| probe | 49.7 |
| real_test | 110.0 |
| tcp | 29.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 50 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 133 | 125 | 8 | 94.0% |
| socks | 16 | 15 | 1 | 93.8% |
| trojan | 253 | 186 | 67 | 73.5% |
| vless | 290 | 171 | 119 | 59.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 104 |
| geo:TimeoutError | 46 |
| 204:TimeoutError | 13 |
| cn-block:TimeoutError | 8 |
| cn-block:ClientOSError | 5 |
| geo:ClientOSError | 5 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 3 |
| speed:ProxyError | 1 |
| 204:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 3979 |
| ConnectionRefusedError | 629 |
| gaierror | 258 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | prefer | 50 | 1.0 | 73 |
| mheidari-all | 0.904 | prefer | 32 | 0.844 | 15816 |
| Surfboard-tg-mixed | 0.89 | prefer | 309 | 0.812 | 5496 |
| Au1rxx-base64 | 0.796 | prefer | 79 | 0.797 | 135 |
| DeltaKronecker-all | 0.658 | observe | 273 | 0.579 | 6437 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1140 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4576 |
| Epodonios-all | 0.255 | observe | 0 | None | 8143 |

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
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 9 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.579 | 158 | 115 | 273 |
| Au1rxx-base64 | 0.797 | 63 | 16 | 79 |
| Surfboard-tg-mixed | 0.812 | 251 | 58 | 309 |
| mheidari-all | 0.844 | 27 | 5 | 32 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 50 | 0 | 50 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15816 | yes | 3.67 | 0 |
| Epodonios-all | 8143 | yes | 2.43 | 0 |
| SoliSpirit-all | 7676 | yes | 1.52 | 0 |
| DeltaKronecker-all | 6437 | yes | 3.58 | 0 |
| Surfboard-tg-mixed | 5496 | yes | 2.09 | 0 |
| barry-far-vless | 4932 | yes | 1.68 | 0 |
| mahdibland-V2RayAggregator | 4664 | yes | 1.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 4576 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 4190 | yes | 1.92 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 110 |
| geo | 54 |
| 204 | 17 |
| cn-block | 14 |
