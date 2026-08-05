# AutoNodes 每日报告

生成时间：2026-08-05 14:25:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 87256 |
| 去重后节点数 | 24192 |
| TCP 可达数 | 3000 |
| 真测通过数 | 515 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24192 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 42.2 |
| geo | 1.1 |
| probe | 50.9 |
| real_test | 106.1 |
| tcp | 36.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 21 | 21 | 0 | 100.0% |
| shadowsocks | 161 | 146 | 15 | 90.7% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 158 | 154 | 4 | 97.5% |
| vless | 249 | 169 | 80 | 67.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 26 |
| 204:TimeoutError | 20 |
| geo:ClientOSError | 14 |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 8 |
| 204:ProxyError | 7 |
| 204:ClientOSError | 5 |
| speed:ClientOSError | 3 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| speed:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4804 |
| ConnectionRefusedError | 826 |
| gaierror | 354 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.998 | prefer | 422 | 0.938 | 1552 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.712 | prefer | 123 | 0.634 | 5862 |
| mheidari-all | 0.437 | observe | 40 | 0.35 | 20132 |
| DeltaKronecker-all | 0.401 | observe | 7 | 0.571 | 5316 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 6386 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 4655 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5260 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.35 | 14 | 26 | 40 |
| DeltaKronecker-all | 0.571 | 4 | 3 | 7 |
| Surfboard-tg-mixed | 0.634 | 78 | 45 | 123 |
| Au1rxx-base64 | 0.938 | 396 | 26 | 422 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20132 | yes | 5.37 | 0 |
| SoliSpirit-all | 7443 | yes | 3.75 | 0 |
| Epodonios-all | 6386 | yes | 2.66 | 0 |
| Surfboard-tg-mixed | 5862 | yes | 3.54 | 0 |
| DeltaKronecker-all | 5316 | yes | 4.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 5260 | yes | 2.34 | 0 |
| mahdibland-V2RayAggregator | 5147 | yes | 2.75 | 0 |
| barry-far-vless | 4943 | yes | 2.71 | 0 |
| Surfboard-tg-vless | 4686 | yes | 3.1 | 0 |
| xiaoji235-airport-v2ray-all | 4655 | yes | 3.46 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 40 |
| 204 | 32 |
| cn-block | 16 |
| speed | 13 |
