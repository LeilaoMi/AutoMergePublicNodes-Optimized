# AutoNodes 每日报告

生成时间：2026-08-15 01:41:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 75507 |
| 去重后节点数 | 20655 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1182 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 20655 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 33.4 |
| geo | 0.9 |
| probe | 68.9 |
| real_test | 240.2 |
| tcp | 32.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 25 | 21 | 4 | 84.0% |
| shadowsocks | 173 | 167 | 6 | 96.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 536 | 534 | 2 | 99.6% |
| vless | 464 | 328 | 136 | 70.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 33 |
| geo:TimeoutError | 32 |
| geo:ClientOSError | 31 |
| 204:TimeoutError | 17 |
| cn-block:TimeoutError | 15 |
| speed:ClientOSError | 8 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4251 |
| ConnectionRefusedError | 801 |
| gaierror | 363 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 738 | 0.981 | 1681 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| DeltaKronecker-all | 0.848 | prefer | 257 | 0.77 | 3485 |
| Surfboard-tg-mixed | 0.75 | prefer | 183 | 0.672 | 5718 |
| mheidari-all | 0.376 | observe | 15 | 0.333 | 15517 |
| nscl5-all | 0.352 | observe | 6 | 0.5 | 2081 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 5157 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 160 |
| Epodonios-all | 0.255 | observe | 0 | None | 6388 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.333 | 5 | 10 | 15 |
| nscl5-all | 0.5 | 3 | 3 | 6 |
| Surfboard-tg-mixed | 0.672 | 123 | 60 | 183 |
| DeltaKronecker-all | 0.77 | 198 | 59 | 257 |
| Au1rxx-base64 | 0.981 | 724 | 14 | 738 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15517 | yes | 3.66 | 0 |
| SoliSpirit-all | 7639 | yes | 2.41 | 0 |
| Epodonios-all | 6388 | yes | 3.85 | 0 |
| Surfboard-tg-mixed | 5718 | yes | 3.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5157 | yes | 1.69 | 0 |
| barry-far-vless | 4744 | yes | 1.95 | 0 |
| Surfboard-tg-vless | 4415 | yes | 3.02 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.79 | 0 |
| mahdibland-V2RayAggregator | 3992 | yes | 2.62 | 0 |
| DeltaKronecker-all | 3485 | yes | 4.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 64 |
| speed | 41 |
| 204 | 23 |
| cn-block | 21 |
