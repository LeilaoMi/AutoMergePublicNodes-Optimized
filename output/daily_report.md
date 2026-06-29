# AutoNodes 每日报告

生成时间：2026-06-29 11:16:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76490 |
| 去重后节点数 | 23087 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23087 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 49.4 |
| geo | 1.3 |
| probe | 59.9 |
| real_test | 123.4 |
| tcp | 30.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 110 | 84 | 26 | 76.4% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 105 | 46 | 59 | 43.8% |
| vless | 388 | 281 | 107 | 72.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 70 |
| 204:ProxyError | 22 |
| 204:ClientOSError | 18 |
| 204:TimeoutError | 17 |
| cn-block:TimeoutError | 17 |
| geo:TimeoutError | 16 |
| speed:TimeoutError | 11 |
| cn-block:ClientOSError | 8 |
| geo:ClientOSError | 7 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 3 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4105 |
| ConnectionRefusedError | 654 |
| gaierror | 275 |
| OSError | 132 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.826 | prefer | 282 | 0.748 | 15787 |
| Au1rxx-base64 | 0.82 | prefer | 36 | 0.833 | 95 |
| Surfboard-tg-mixed | 0.707 | prefer | 239 | 0.628 | 5303 |
| DeltaKronecker-all | 0.571 | observe | 53 | 0.491 | 7004 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1166 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4653 |
| Epodonios-all | 0.255 | observe | 0 | None | 7391 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 179 |
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
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.491 | 26 | 27 | 53 |
| Surfboard-tg-mixed | 0.628 | 150 | 89 | 239 |
| mheidari-all | 0.748 | 211 | 71 | 282 |
| Au1rxx-base64 | 0.833 | 30 | 6 | 36 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15787 | yes | 4.07 | 0 |
| Epodonios-all | 7391 | yes | 3.13 | 0 |
| SoliSpirit-all | 7178 | yes | 2.45 | 0 |
| DeltaKronecker-all | 7004 | yes | 3.43 | 0 |
| Surfboard-tg-mixed | 5303 | yes | 1.96 | 0 |
| mahdibland-V2RayAggregator | 5278 | yes | 1.47 | 0 |
| 10ium-ScrapeCategorize-Vless | 4653 | yes | 2.03 | 0 |
| barry-far-vless | 4344 | yes | 1.79 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.64 | 0 |
| Surfboard-tg-vless | 3969 | yes | 2.57 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 84 |
| 204 | 57 |
| cn-block | 28 |
| geo | 25 |
