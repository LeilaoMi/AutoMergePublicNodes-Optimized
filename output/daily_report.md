# AutoNodes 每日报告

生成时间：2026-06-22 00:49:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 73174 |
| 去重后节点数 | 22101 |
| TCP 可达数 | 3000 |
| 真测通过数 | 581 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22101 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 20.4 |
| geo | 1.3 |
| probe | 45.7 |
| real_test | 107.2 |
| tcp | 29.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 63 | 58 | 5 | 92.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 228 | 185 | 43 | 81.1% |
| vless | 410 | 261 | 149 | 63.7% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 73 |
| speed:ClientOSError | 70 |
| speed:TimeoutError | 20 |
| geo:ClientOSError | 10 |
| cn-block:TimeoutError | 6 |
| 204:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| 204:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4137 |
| ConnectionRefusedError | 594 |
| gaierror | 189 |
| OSError | 109 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | prefer | 69 | 1.0 | 131 |
| Au1rxx-base64 | 0.847 | prefer | 42 | 0.857 | 149 |
| mheidari-all | 0.829 | prefer | 425 | 0.751 | 15086 |
| DeltaKronecker-all | 0.731 | prefer | 227 | 0.652 | 6748 |
| Surfboard-tg-mixed | 0.53 | observe | 10 | 0.7 | 4738 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 7244 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3978 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6793 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.152 | observe | 2 | 0.0 | 0 | 1204 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
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
| nscl5-all | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.652 | 148 | 79 | 227 |
| Surfboard-tg-mixed | 0.7 | 7 | 3 | 10 |
| mheidari-all | 0.751 | 319 | 106 | 425 |
| Au1rxx-base64 | 0.857 | 36 | 6 | 42 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 69 | 0 | 69 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15086 | yes | 3.65 | 0 |
| Epodonios-all | 7244 | yes | 2.47 | 0 |
| SoliSpirit-all | 6793 | yes | 1.68 | 0 |
| DeltaKronecker-all | 6748 | yes | 3.46 | 0 |
| Surfboard-tg-mixed | 4738 | yes | 2.08 | 0 |
| barry-far-vless | 4524 | yes | 1.33 | 0 |
| mahdibland-V2RayAggregator | 4505 | yes | 1.63 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 1.16 | 0 |
| MatinGhanbari-all-sub | 3978 | yes | 1.41 | 0 |
| Surfboard-tg-vless | 3632 | yes | 1.76 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 90 |
| geo | 83 |
| 204 | 12 |
| cn-block | 12 |
