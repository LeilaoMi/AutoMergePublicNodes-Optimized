# AutoNodes 每日报告

生成时间：2026-06-23 04:07:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78328 |
| 去重后节点数 | 22742 |
| TCP 可达数 | 3000 |
| 真测通过数 | 432 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22742 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 40.3 |
| geo | 1.3 |
| probe | 68.6 |
| real_test | 149.2 |
| tcp | 30.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 58 | 58 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 75 | 70 | 5 | 93.3% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 62 | 49 | 13 | 79.0% |
| vless | 906 | 247 | 659 | 27.3% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 293 |
| geo:TimeoutError | 180 |
| 204:TimeoutError | 52 |
| geo:ClientOSError | 48 |
| 204:ProxyError | 42 |
| speed:TimeoutError | 31 |
| cn-block:TimeoutError | 12 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 3 |
| geo:status | 1 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4260 |
| ConnectionRefusedError | 604 |
| gaierror | 180 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.987 | prefer | 58 | 1.0 | 95 |
| Surfboard-tg-mixed | 0.819 | prefer | 15 | 0.933 | 5421 |
| Au1rxx-base64 | 0.734 | prefer | 90 | 0.733 | 145 |
| mheidari-all | 0.64 | observe | 173 | 0.561 | 15546 |
| DeltaKronecker-all | 0.334 | observe | 769 | 0.254 | 7452 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4466 |
| Epodonios-all | 0.255 | observe | 0 | None | 8267 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7417 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.146 | observe | 2 | 0.0 | 0 | 1064 |
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
| DeltaKronecker-all | 0.254 | 195 | 574 | 769 |
| mheidari-all | 0.561 | 97 | 76 | 173 |
| Au1rxx-base64 | 0.733 | 66 | 24 | 90 |
| Surfboard-tg-mixed | 0.933 | 14 | 1 | 15 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 58 | 0 | 58 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15546 | yes | 3.21 | 0 |
| Epodonios-all | 8267 | yes | 3.8 | 0 |
| DeltaKronecker-all | 7452 | yes | 3.35 | 0 |
| SoliSpirit-all | 7417 | yes | 1.88 | 0 |
| Surfboard-tg-mixed | 5421 | yes | 2.0 | 0 |
| barry-far-vless | 5190 | yes | 1.04 | 0 |
| mahdibland-V2RayAggregator | 4547 | yes | 0.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4466 | yes | 0.85 | 0 |
| Surfboard-tg-vless | 4156 | yes | 2.14 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 325 |
| geo | 232 |
| 204 | 102 |
| cn-block | 18 |
