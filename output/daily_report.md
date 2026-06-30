# AutoNodes 每日报告

生成时间：2026-06-30 14:35:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 75035 |
| 去重后节点数 | 23114 |
| TCP 可达数 | 3000 |
| 真测通过数 | 485 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23114 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.8 |
| generate | 31.3 |
| geo | 1.4 |
| probe | 58.7 |
| real_test | 131.6 |
| tcp | 30.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 122 | 99 | 23 | 81.1% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 169 | 112 | 57 | 66.3% |
| vless | 392 | 230 | 162 | 58.7% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 128 |
| 204:TimeoutError | 24 |
| geo:TimeoutError | 17 |
| 204:ClientOSError | 16 |
| 204:ProxyError | 13 |
| geo:ClientOSError | 13 |
| cn-block:TimeoutError | 12 |
| speed:TimeoutError | 11 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4314 |
| ConnectionRefusedError | 622 |
| OSError | 132 |
| gaierror | 132 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.751 | prefer | 77 | 0.675 | 7352 |
| Surfboard-tg-mixed | 0.73 | prefer | 312 | 0.651 | 5637 |
| mheidari-all | 0.713 | prefer | 249 | 0.635 | 15693 |
| Au1rxx-base64 | 0.658 | observe | 50 | 0.66 | 103 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.303 | observe | 1 | 1.0 | 1204 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4139 |
| Epodonios-all | 0.255 | observe | 0 | None | 6322 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3977 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.635 | 158 | 91 | 249 |
| Surfboard-tg-mixed | 0.651 | 203 | 109 | 312 |
| Au1rxx-base64 | 0.66 | 33 | 17 | 50 |
| DeltaKronecker-all | 0.675 | 52 | 25 | 77 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15693 | yes | 2.51 | 0 |
| DeltaKronecker-all | 7352 | yes | 2.62 | 0 |
| SoliSpirit-all | 6506 | yes | 1.1 | 0 |
| Epodonios-all | 6322 | yes | 1.22 | 0 |
| Surfboard-tg-mixed | 5637 | yes | 1.51 | 0 |
| mahdibland-V2RayAggregator | 5353 | yes | 1.58 | 0 |
| barry-far-vless | 4531 | yes | 0.81 | 0 |
| Surfboard-tg-vless | 4204 | yes | 1.7 | 0 |
| 10ium-ScrapeCategorize-Vless | 4139 | yes | 0.95 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 0.68 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 139 |
| 204 | 53 |
| geo | 30 |
| cn-block | 21 |
