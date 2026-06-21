# AutoNodes 每日报告

生成时间：2026-06-21 23:14:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 73540 |
| 去重后节点数 | 22011 |
| TCP 可达数 | 3000 |
| 真测通过数 | 752 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22011 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| generate | 27.5 |
| geo | 1.3 |
| probe | 52.2 |
| real_test | 138.0 |
| tcp | 29.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 144 | 135 | 9 | 93.8% |
| trojan | 101 | 91 | 10 | 90.1% |
| vless | 565 | 450 | 115 | 79.6% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 52 |
| geo:TimeoutError | 16 |
| cn-block:TimeoutError | 15 |
| speed:TimeoutError | 13 |
| geo:ClientOSError | 13 |
| 204:TimeoutError | 8 |
| 204:ProxyError | 8 |
| 204:ClientOSError | 7 |
| cn-block:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4213 |
| ConnectionRefusedError | 607 |
| gaierror | 136 |
| OSError | 109 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | prefer | 69 | 1.0 | 131 |
| mheidari-all | 0.98 | prefer | 329 | 0.903 | 15086 |
| Au1rxx-base64 | 0.902 | prefer | 85 | 0.906 | 135 |
| Surfboard-tg-mixed | 0.894 | prefer | 305 | 0.816 | 4776 |
| DeltaKronecker-all | 0.686 | observe | 97 | 0.608 | 6748 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 7271 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6970 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.608 | 59 | 38 | 97 |
| Surfboard-tg-mixed | 0.816 | 249 | 56 | 305 |
| mheidari-all | 0.903 | 297 | 32 | 329 |
| Au1rxx-base64 | 0.906 | 77 | 8 | 85 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 69 | 0 | 69 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15086 | yes | 3.8 | 0 |
| Epodonios-all | 7271 | yes | 2.11 | 0 |
| SoliSpirit-all | 6970 | yes | 2.45 | 0 |
| DeltaKronecker-all | 6748 | yes | 3.1 | 0 |
| Surfboard-tg-mixed | 4776 | yes | 1.73 | 0 |
| barry-far-vless | 4628 | yes | 0.99 | 0 |
| mahdibland-V2RayAggregator | 4505 | yes | 1.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 1.22 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.06 | 0 |
| Surfboard-tg-vless | 3678 | yes | 2.25 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 65 |
| geo | 29 |
| 204 | 23 |
| cn-block | 17 |
