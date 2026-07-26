# AutoNodes 每日报告

生成时间：2026-07-26 19:25:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83971 |
| 去重后节点数 | 22078 |
| TCP 可达数 | 3000 |
| 真测通过数 | 725 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22078 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 42.7 |
| geo | 1.3 |
| probe | 75.0 |
| real_test | 189.0 |
| tcp | 32.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 7 | 6 | 1 | 85.7% |
| http | 76 | 76 | 0 | 100.0% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 99 | 73 | 26 | 73.7% |
| socks | 6 | 2 | 4 | 33.3% |
| trojan | 409 | 383 | 26 | 93.6% |
| vless | 552 | 174 | 378 | 31.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 145 |
| geo:TimeoutError | 99 |
| 204:ProxyError | 54 |
| geo:ClientOSError | 41 |
| 204:TimeoutError | 40 |
| cn-block:TimeoutError | 21 |
| speed:TimeoutError | 13 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 8 |
| cn-block:ProxyError | 4 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4383 |
| ConnectionRefusedError | 705 |
| gaierror | 303 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.991 | prefer | 76 | 1.0 | 86 |
| Au1rxx-base64 | 0.978 | prefer | 435 | 0.92 | 1507 |
| mheidari-all | 0.858 | prefer | 97 | 0.784 | 19379 |
| tg-oneclickvpnkeys | 0.456 | observe | 7 | 0.857 | 164 |
| Surfboard-tg-mixed | 0.423 | observe | 65 | 0.338 | 5460 |
| DeltaKronecker-all | 0.383 | observe | 474 | 0.302 | 4320 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.259 | observe | 3 | 0.333 | 3959 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 6631 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.302 | 143 | 331 | 474 |
| xiaoji235-airport-v2ray-all | 0.333 | 1 | 2 | 3 |
| Surfboard-tg-mixed | 0.338 | 22 | 43 | 65 |
| mheidari-all | 0.784 | 76 | 21 | 97 |
| tg-oneclickvpnkeys | 0.857 | 6 | 1 | 7 |
| Au1rxx-base64 | 0.92 | 400 | 35 | 435 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 76 | 0 | 76 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19379 | yes | 5.13 | 0 |
| Epodonios-all | 6631 | yes | 2.69 | 0 |
| SoliSpirit-all | 6557 | yes | 2.39 | 0 |
| Surfboard-tg-mixed | 5460 | yes | 3.63 | 0 |
| mahdibland-V2RayAggregator | 5003 | yes | 2.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 1.03 | 0 |
| barry-far-vless | 4894 | yes | 1.21 | 0 |
| DeltaKronecker-all | 4320 | yes | 5.11 | 0 |
| Surfboard-tg-vless | 4238 | yes | 2.99 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.48 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 159 |
| geo | 141 |
| 204 | 102 |
| cn-block | 33 |
