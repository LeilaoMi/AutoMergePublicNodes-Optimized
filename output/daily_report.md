# AutoNodes 每日报告

生成时间：2026-08-07 07:28:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 89705 |
| 去重后节点数 | 24235 |
| TCP 可达数 | 3000 |
| 真测通过数 | 456 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24235 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 29.2 |
| geo | 1.3 |
| probe | 52.1 |
| real_test | 114.6 |
| tcp | 35.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 168 | 150 | 18 | 89.3% |
| socks | 12 | 5 | 7 | 41.7% |
| trojan | 164 | 150 | 14 | 91.5% |
| vless | 227 | 111 | 116 | 48.9% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 47 |
| geo:ClientOSError | 38 |
| 204:TimeoutError | 14 |
| speed:TimeoutError | 13 |
| 204:ProxyError | 12 |
| cn-block:TimeoutError | 10 |
| speed:ClientOSError | 9 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4662 |
| ConnectionRefusedError | 828 |
| gaierror | 348 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.979 | prefer | 381 | 0.929 | 1300 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| DeltaKronecker-all | 0.564 | observe | 29 | 0.483 | 5326 |
| Surfboard-tg-mixed | 0.526 | observe | 128 | 0.445 | 6241 |
| mheidari-all | 0.3 | observe | 48 | 0.208 | 20715 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 5184 |
| Epodonios-all | 0.255 | observe | 0 | None | 6873 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7440 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4967 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.208 | 10 | 38 | 48 |
| Surfboard-tg-mixed | 0.445 | 57 | 71 | 128 |
| DeltaKronecker-all | 0.483 | 14 | 15 | 29 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.929 | 354 | 27 | 381 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20715 | yes | 5.56 | 0 |
| SoliSpirit-all | 7440 | yes | 3.86 | 0 |
| Epodonios-all | 6873 | yes | 4.48 | 0 |
| Surfboard-tg-mixed | 6241 | yes | 2.92 | 0 |
| DeltaKronecker-all | 5326 | yes | 3.57 | 0 |
| barry-far-vless | 5297 | yes | 1.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5282 | yes | 2.92 | 0 |
| mahdibland-V2RayAggregator | 5247 | yes | 2.49 | 0 |
| xiaoji235-airport-v2ray-all | 5184 | yes | 2.68 | 0 |
| Surfboard-tg-vless | 4967 | yes | 4.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 87 |
| 204 | 32 |
| speed | 22 |
| cn-block | 15 |
