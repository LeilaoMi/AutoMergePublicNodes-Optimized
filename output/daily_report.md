# AutoNodes 每日报告

生成时间：2026-07-23 03:30:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 81981 |
| 去重后节点数 | 22675 |
| TCP 可达数 | 3000 |
| 真测通过数 | 677 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22675 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 35.4 |
| geo | 1.3 |
| probe | 73.1 |
| real_test | 192.6 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 35 | 1 | 97.2% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 145 | 131 | 14 | 90.3% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 416 | 368 | 48 | 88.5% |
| vless | 625 | 135 | 490 | 21.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 272 |
| speed:ClientOSError | 93 |
| cn-block:TimeoutError | 57 |
| speed:TimeoutError | 52 |
| geo:ClientOSError | 47 |
| 204:TimeoutError | 9 |
| cn-block:ClientOSError | 7 |
| geo:ProxyError | 5 |
| 204:ProxyError | 5 |
| speed:ProxyError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4565 |
| ConnectionRefusedError | 698 |
| OSError | 218 |
| gaierror | 149 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | prefer | 36 | 0.972 | 61 |
| Au1rxx-base64 | 0.753 | prefer | 206 | 0.738 | 432 |
| mheidari-all | 0.581 | observe | 729 | 0.501 | 19379 |
| DeltaKronecker-all | 0.555 | observe | 242 | 0.475 | 5212 |
| Surfboard-tg-mixed | 0.482 | observe | 14 | 0.5 | 5286 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4399 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4613 |
| Epodonios-all | 0.255 | observe | 0 | None | 6359 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.475 | 115 | 127 | 242 |
| Surfboard-tg-mixed | 0.5 | 7 | 7 | 14 |
| mheidari-all | 0.501 | 365 | 364 | 729 |
| Au1rxx-base64 | 0.738 | 152 | 54 | 206 |
| zhangkai | 0.972 | 35 | 1 | 36 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19379 | yes | 3.61 | 0 |
| SoliSpirit-all | 6912 | yes | 2.47 | 0 |
| Epodonios-all | 6359 | yes | 1.86 | 0 |
| Surfboard-tg-mixed | 5286 | yes | 2.58 | 0 |
| DeltaKronecker-all | 5212 | yes | 3.95 | 0 |
| mahdibland-V2RayAggregator | 4954 | yes | 1.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 4613 | yes | 1.44 | 0 |
| barry-far-vless | 4602 | yes | 0.89 | 0 |
| xiaoji235-airport-v2ray-all | 4399 | yes | 1.23 | 0 |
| Surfboard-tg-vless | 4008 | yes | 2.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 324 |
| speed | 148 |
| cn-block | 66 |
| 204 | 16 |
