# AutoNodes 每日报告

生成时间：2026-06-23 09:58:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76152 |
| 去重后节点数 | 21940 |
| TCP 可达数 | 3000 |
| 真测通过数 | 350 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21940 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 35.5 |
| geo | 1.4 |
| probe | 63.4 |
| real_test | 107.5 |
| tcp | 29.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 58 | 58 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 102 | 89 | 13 | 87.3% |
| trojan | 84 | 36 | 48 | 42.9% |
| vless | 296 | 160 | 136 | 54.1% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 73 |
| 204:TimeoutError | 45 |
| cn-block:TimeoutError | 18 |
| geo:TimeoutError | 13 |
| geo:ClientOSError | 12 |
| 204:ProxyError | 10 |
| cn-block:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| 204:ClientOSError | 5 |
| speed:ProxyError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4182 |
| ConnectionRefusedError | 586 |
| gaierror | 133 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.987 | prefer | 58 | 1.0 | 95 |
| Au1rxx-base64 | 0.765 | prefer | 69 | 0.768 | 116 |
| Surfboard-tg-mixed | 0.71 | prefer | 209 | 0.632 | 5285 |
| mheidari-all | 0.615 | observe | 155 | 0.535 | 15546 |
| DeltaKronecker-all | 0.501 | observe | 55 | 0.418 | 6437 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4576 |
| Epodonios-all | 0.255 | observe | 0 | None | 7878 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7202 |

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
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 6 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.418 | 23 | 32 | 55 |
| mheidari-all | 0.535 | 83 | 72 | 155 |
| Surfboard-tg-mixed | 0.632 | 132 | 77 | 209 |
| Au1rxx-base64 | 0.768 | 53 | 16 | 69 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 58 | 0 | 58 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15546 | yes | 2.88 | 0 |
| Epodonios-all | 7878 | yes | 2.48 | 0 |
| SoliSpirit-all | 7202 | yes | 2.97 | 0 |
| DeltaKronecker-all | 6437 | yes | 3.68 | 0 |
| Surfboard-tg-mixed | 5285 | yes | 2.09 | 0 |
| barry-far-vless | 4896 | yes | 1.59 | 0 |
| 10ium-ScrapeCategorize-Vless | 4576 | yes | 1.83 | 0 |
| mahdibland-V2RayAggregator | 4477 | yes | 1.55 | 0 |
| Surfboard-tg-vless | 4084 | yes | 1.93 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.92 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 81 |
| 204 | 60 |
| cn-block | 29 |
| geo | 27 |
