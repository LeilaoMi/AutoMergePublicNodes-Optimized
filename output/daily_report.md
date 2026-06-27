# AutoNodes 每日报告

生成时间：2026-06-27 19:41:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76527 |
| 去重后节点数 | 23143 |
| TCP 可达数 | 3000 |
| 真测通过数 | 348 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23143 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 36.4 |
| geo | 1.4 |
| probe | 56.7 |
| real_test | 102.2 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 2 | 2 | 50.0% |
| shadowsocks | 104 | 79 | 25 | 76.0% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 96 | 35 | 61 | 36.5% |
| vless | 307 | 190 | 117 | 61.9% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 82 |
| 204:TimeoutError | 24 |
| cn-block:TimeoutError | 23 |
| 204:ClientOSError | 18 |
| geo:TimeoutError | 18 |
| 204:ProxyError | 16 |
| geo:ClientOSError | 8 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4423 |
| ConnectionRefusedError | 657 |
| gaierror | 143 |
| OSError | 140 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.795 | prefer | 46 | 0.804 | 95 |
| Surfboard-tg-mixed | 0.768 | prefer | 213 | 0.69 | 5026 |
| mheidari-all | 0.601 | observe | 165 | 0.521 | 16060 |
| DeltaKronecker-all | 0.524 | observe | 88 | 0.443 | 6822 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1186 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 7776 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3980 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.147 | observe | 2 | 0.0 | 0 | 1084 |
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
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.443 | 39 | 49 | 88 |
| mheidari-all | 0.521 | 86 | 79 | 165 |
| Surfboard-tg-mixed | 0.69 | 147 | 66 | 213 |
| Au1rxx-base64 | 0.804 | 37 | 9 | 46 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16060 | yes | 3.0 | 0 |
| Epodonios-all | 7776 | yes | 3.65 | 0 |
| SoliSpirit-all | 7278 | yes | 2.31 | 0 |
| DeltaKronecker-all | 6822 | yes | 3.92 | 0 |
| mahdibland-V2RayAggregator | 5287 | yes | 1.63 | 0 |
| Surfboard-tg-mixed | 5026 | yes | 2.13 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 1.57 | 0 |
| barry-far-vless | 4576 | yes | 1.26 | 0 |
| MatinGhanbari-all-sub | 3980 | yes | 1.37 | 0 |
| Surfboard-tg-vless | 3682 | yes | 1.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 91 |
| 204 | 58 |
| cn-block | 29 |
| geo | 27 |
