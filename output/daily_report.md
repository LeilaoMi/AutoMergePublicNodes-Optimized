# AutoNodes 每日报告

生成时间：2026-08-08 13:02:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 83600 |
| 去重后节点数 | 23665 |
| TCP 可达数 | 3000 |
| 真测通过数 | 411 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23665 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 37.0 |
| geo | 1.1 |
| probe | 50.9 |
| real_test | 87.2 |
| tcp | 34.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 25 | 23 | 2 | 92.0% |
| shadowsocks | 160 | 144 | 16 | 90.0% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 136 | 131 | 5 | 96.3% |
| vless | 184 | 87 | 97 | 47.3% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 29 |
| 204:TimeoutError | 28 |
| geo:TimeoutError | 18 |
| cn-block:TimeoutError | 13 |
| speed:ClientOSError | 11 |
| speed:TimeoutError | 10 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4738 |
| ConnectionRefusedError | 825 |
| gaierror | 380 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.996 | prefer | 342 | 0.939 | 1488 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.676 | observe | 87 | 0.598 | 6570 |
| mheidari-all | 0.438 | observe | 3 | 1.0 | 17827 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 196 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| DeltaKronecker-all | 0.257 | observe | 77 | 0.169 | 5347 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5450 |
| Epodonios-all | 0.255 | observe | 0 | None | 7203 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.169 | 13 | 64 | 77 |
| Surfboard-tg-mixed | 0.598 | 52 | 35 | 87 |
| Au1rxx-base64 | 0.939 | 321 | 21 | 342 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| mheidari-all | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17827 | yes | 4.35 | 0 |
| SoliSpirit-all | 7636 | yes | 2.77 | 0 |
| Epodonios-all | 7203 | yes | 2.75 | 0 |
| Surfboard-tg-mixed | 6570 | yes | 3.87 | 0 |
| barry-far-vless | 5686 | yes | 1.24 | 0 |
| 10ium-ScrapeCategorize-Vless | 5450 | yes | 1.73 | 0 |
| Surfboard-tg-vless | 5374 | yes | 3.32 | 0 |
| DeltaKronecker-all | 5347 | yes | 4.9 | 0 |
| mahdibland-V2RayAggregator | 5162 | yes | 2.55 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.81 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 48 |
| 204 | 35 |
| speed | 21 |
| cn-block | 17 |
