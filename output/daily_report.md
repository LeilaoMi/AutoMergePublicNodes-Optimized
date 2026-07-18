# AutoNodes 每日报告

生成时间：2026-07-18 02:59:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 98/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82736 |
| 去重后节点数 | 25440 |
| TCP 可达数 | 3000 |
| 真测通过数 | 756 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25440 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 26.4 |
| geo | 1.3 |
| probe | 63.6 |
| real_test | 178.8 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 150 | 139 | 11 | 92.7% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 442 | 430 | 12 | 97.3% |
| vless | 555 | 141 | 414 | 25.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 224 |
| geo:TimeoutError | 97 |
| geo:ClientOSError | 39 |
| speed:TimeoutError | 37 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 12 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4740 |
| ConnectionRefusedError | 690 |
| gaierror | 264 |
| OSError | 217 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| nscl5-all | 0.954 | prefer | 19 | 0.947 | 1976 |
| Au1rxx-base64 | 0.886 | prefer | 123 | 0.886 | 149 |
| mheidari-all | 0.757 | prefer | 534 | 0.678 | 16573 |
| Surfboard-tg-mixed | 0.676 | observe | 337 | 0.596 | 5500 |
| xiaoji235-airport-v2ray-all | 0.547 | observe | 9 | 0.778 | 4321 |
| DeltaKronecker-all | 0.255 | observe | 135 | 0.17 | 8967 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4428 |
| Epodonios-all | 0.255 | observe | 0 | None | 6707 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.17 | 23 | 112 | 135 |
| Surfboard-tg-mixed | 0.596 | 201 | 136 | 337 |
| mheidari-all | 0.678 | 362 | 172 | 534 |
| xiaoji235-airport-v2ray-all | 0.778 | 7 | 2 | 9 |
| Au1rxx-base64 | 0.886 | 109 | 14 | 123 |
| nscl5-all | 0.947 | 18 | 1 | 19 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16573 | yes | 3.96 | 0 |
| DeltaKronecker-all | 8967 | yes | 4.59 | 0 |
| SoliSpirit-all | 6869 | yes | 2.45 | 0 |
| Epodonios-all | 6707 | yes | 1.14 | 0 |
| Surfboard-tg-mixed | 5500 | yes | 2.74 | 0 |
| mahdibland-V2RayAggregator | 5263 | yes | 0.96 | 0 |
| barry-far-vless | 4834 | yes | 1.18 | 0 |
| 10ium-ScrapeCategorize-Vless | 4428 | yes | 1.48 | 0 |
| xiaoji235-airport-v2ray-all | 4321 | yes | 0.78 | 0 |
| Surfboard-tg-vless | 4227 | yes | 2.98 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 261 |
| geo | 136 |
| cn-block | 22 |
| 204 | 21 |
