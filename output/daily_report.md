# AutoNodes 每日报告

生成时间：2026-07-22 14:14:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82354 |
| 去重后节点数 | 22753 |
| TCP 可达数 | 3000 |
| 真测通过数 | 700 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22753 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 51.1 |
| geo | 1.3 |
| probe | 61.2 |
| real_test | 173.4 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 136 | 118 | 18 | 86.8% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 528 | 463 | 65 | 87.7% |
| vless | 256 | 77 | 179 | 30.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 81 |
| speed:ClientOSError | 61 |
| cn-block:TimeoutError | 55 |
| 204:TimeoutError | 15 |
| 204:ProxyError | 14 |
| cn-block:ClientOSError | 12 |
| geo:ClientOSError | 10 |
| speed:TimeoutError | 5 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4177 |
| ConnectionRefusedError | 691 |
| gaierror | 316 |
| OSError | 221 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.887 | prefer | 377 | 0.809 | 19287 |
| Au1rxx-base64 | 0.828 | prefer | 193 | 0.813 | 432 |
| DeltaKronecker-all | 0.712 | prefer | 123 | 0.634 | 5212 |
| Surfboard-tg-mixed | 0.608 | observe | 231 | 0.528 | 5364 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4246 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4613 |
| Epodonios-all | 0.255 | observe | 0 | None | 6476 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6830 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.528 | 122 | 109 | 231 |
| DeltaKronecker-all | 0.634 | 78 | 45 | 123 |
| mheidari-all | 0.809 | 305 | 72 | 377 |
| Au1rxx-base64 | 0.813 | 157 | 36 | 193 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19287 | yes | 3.37 | 0 |
| SoliSpirit-all | 6830 | yes | 3.51 | 0 |
| Epodonios-all | 6476 | yes | 1.66 | 0 |
| Surfboard-tg-mixed | 5364 | yes | 2.66 | 0 |
| DeltaKronecker-all | 5212 | yes | 4.12 | 0 |
| mahdibland-V2RayAggregator | 5204 | yes | 2.51 | 0 |
| barry-far-vless | 4805 | yes | 1.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 4613 | yes | 1.71 | 0 |
| Surfboard-tg-vless | 4267 | yes | 2.43 | 0 |
| xiaoji235-airport-v2ray-all | 4246 | yes | 0.78 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 92 |
| cn-block | 71 |
| speed | 68 |
| 204 | 32 |
