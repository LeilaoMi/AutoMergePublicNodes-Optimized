# AutoNodes 每日报告

生成时间：2026-07-25 13:52:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78946 |
| 去重后节点数 | 22525 |
| TCP 可达数 | 3000 |
| 真测通过数 | 821 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22525 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 36.9 |
| geo | 1.1 |
| probe | 65.2 |
| real_test | 180.3 |
| tcp | 31.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 76 | 76 | 0 | 100.0% |
| hysteria2 | 8 | 8 | 0 | 100.0% |
| shadowsocks | 135 | 112 | 23 | 83.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 613 | 557 | 56 | 90.9% |
| vless | 177 | 66 | 111 | 37.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 57 |
| speed:ClientOSError | 40 |
| cn-block:TimeoutError | 27 |
| 204:ProxyError | 20 |
| 204:TimeoutError | 15 |
| geo:ClientOSError | 8 |
| cn-block:ClientOSError | 8 |
| cn-block:ProxyError | 6 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4098 |
| ConnectionRefusedError | 687 |
| gaierror | 333 |
| OSError | 220 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 76 | 1.0 | 119 |
| Au1rxx-base64 | 0.92 | prefer | 293 | 0.891 | 803 |
| mheidari-all | 0.858 | prefer | 399 | 0.779 | 17158 |
| DeltaKronecker-all | 0.792 | prefer | 182 | 0.714 | 5838 |
| Surfboard-tg-mixed | 0.775 | prefer | 57 | 0.702 | 5379 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 180 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4879 |
| Epodonios-all | 0.255 | observe | 0 | None | 6540 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 183 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.702 | 40 | 17 | 57 |
| DeltaKronecker-all | 0.714 | 130 | 52 | 182 |
| mheidari-all | 0.779 | 311 | 88 | 399 |
| Au1rxx-base64 | 0.891 | 261 | 32 | 293 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17158 | yes | 3.57 | 0 |
| Epodonios-all | 6540 | yes | 4.56 | 0 |
| SoliSpirit-all | 6338 | yes | 2.66 | 0 |
| DeltaKronecker-all | 5838 | yes | 3.48 | 0 |
| Surfboard-tg-mixed | 5379 | yes | 2.36 | 0 |
| mahdibland-V2RayAggregator | 5009 | yes | 2.0 | 0 |
| 10ium-ScrapeCategorize-Vless | 4879 | yes | 1.56 | 0 |
| barry-far-vless | 4746 | yes | 1.34 | 0 |
| Surfboard-tg-vless | 4058 | yes | 3.01 | 0 |
| MatinGhanbari-all-sub | 3969 | yes | 1.92 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 67 |
| speed | 45 |
| cn-block | 41 |
| 204 | 39 |
