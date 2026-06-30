# AutoNodes 每日报告

生成时间：2026-06-30 09:55:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75261 |
| 去重后节点数 | 23023 |
| TCP 可达数 | 3000 |
| 真测通过数 | 418 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23023 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 33.3 |
| geo | 1.4 |
| probe | 62.6 |
| real_test | 132.4 |
| tcp | 29.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 100 | 78 | 22 | 78.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 152 | 91 | 61 | 59.9% |
| vless | 395 | 206 | 189 | 52.2% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 149 |
| geo:TimeoutError | 33 |
| 204:TimeoutError | 28 |
| 204:ClientOSError | 14 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 11 |
| geo:ClientOSError | 10 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4148 |
| ConnectionRefusedError | 618 |
| gaierror | 204 |
| OSError | 132 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.754 | prefer | 46 | 0.761 | 96 |
| Surfboard-tg-mixed | 0.713 | prefer | 287 | 0.634 | 5386 |
| mheidari-all | 0.62 | observe | 233 | 0.541 | 15701 |
| DeltaKronecker-all | 0.507 | observe | 87 | 0.425 | 7352 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4139 |
| Epodonios-all | 0.255 | observe | 0 | None | 6386 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3981 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6946 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.425 | 37 | 50 | 87 |
| mheidari-all | 0.541 | 126 | 107 | 233 |
| Surfboard-tg-mixed | 0.634 | 182 | 105 | 287 |
| Au1rxx-base64 | 0.761 | 35 | 11 | 46 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15701 | yes | 3.06 | 0 |
| DeltaKronecker-all | 7352 | yes | 3.73 | 0 |
| SoliSpirit-all | 6946 | yes | 2.71 | 0 |
| Epodonios-all | 6386 | yes | 3.59 | 0 |
| Surfboard-tg-mixed | 5386 | yes | 2.4 | 0 |
| mahdibland-V2RayAggregator | 5353 | yes | 1.92 | 0 |
| barry-far-vless | 4573 | yes | 1.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4139 | yes | 1.45 | 0 |
| MatinGhanbari-all-sub | 3981 | yes | 1.33 | 0 |
| Surfboard-tg-vless | 3959 | yes | 1.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 158 |
| 204 | 53 |
| geo | 44 |
| cn-block | 18 |
