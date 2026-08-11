# AutoNodes 每日报告

生成时间：2026-08-11 07:20:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84663 |
| 去重后节点数 | 24209 |
| TCP 可达数 | 3000 |
| 真测通过数 | 495 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24209 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 29.9 |
| geo | 1.3 |
| probe | 51.0 |
| real_test | 106.8 |
| tcp | 36.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 49 | 49 | 0 | 100.0% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 155 | 140 | 15 | 90.3% |
| socks | 9 | 5 | 4 | 55.6% |
| trojan | 142 | 127 | 15 | 89.4% |
| vless | 304 | 158 | 146 | 52.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 46 |
| geo:ClientOSError | 44 |
| speed:TimeoutError | 29 |
| 204:TimeoutError | 18 |
| speed:ClientOSError | 17 |
| 204:ProxyError | 11 |
| cn-block:TimeoutError | 5 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5020 |
| ConnectionRefusedError | 806 |
| gaierror | 275 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.983 | prefer | 49 | 1.0 | 67 |
| Au1rxx-base64 | 0.949 | prefer | 380 | 0.895 | 1409 |
| Surfboard-tg-mixed | 0.792 | prefer | 102 | 0.716 | 6265 |
| DeltaKronecker-all | 0.397 | observe | 39 | 0.308 | 5522 |
| mheidari-all | 0.29 | observe | 103 | 0.204 | 20272 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5419 |
| Epodonios-all | 0.255 | observe | 0 | None | 6871 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7470 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5103 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.204 | 21 | 82 | 103 |
| DeltaKronecker-all | 0.308 | 12 | 27 | 39 |
| Surfboard-tg-mixed | 0.716 | 73 | 29 | 102 |
| Au1rxx-base64 | 0.895 | 340 | 40 | 380 |
| zhangkai | 1.0 | 49 | 0 | 49 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20272 | yes | 4.16 | 0 |
| SoliSpirit-all | 7470 | yes | 2.67 | 0 |
| Epodonios-all | 6871 | yes | 4.54 | 0 |
| Surfboard-tg-mixed | 6265 | yes | 2.67 | 0 |
| DeltaKronecker-all | 5522 | yes | 4.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 5419 | yes | 2.41 | 0 |
| barry-far-vless | 5410 | yes | 2.06 | 0 |
| mahdibland-V2RayAggregator | 5209 | yes | 1.42 | 0 |
| Surfboard-tg-vless | 5103 | yes | 2.49 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.21 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 91 |
| speed | 46 |
| 204 | 32 |
| cn-block | 12 |
