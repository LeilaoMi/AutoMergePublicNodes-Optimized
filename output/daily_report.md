# AutoNodes 每日报告

生成时间：2026-08-02 19:24:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 81361 |
| 去重后节点数 | 22680 |
| TCP 可达数 | 3000 |
| 真测通过数 | 634 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22680 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.6 |
| generate | 38.6 |
| geo | 1.5 |
| probe | 64.1 |
| real_test | 176.7 |
| tcp | 34.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 143 | 143 | 0 | 100.0% |
| hysteria2 | 20 | 18 | 2 | 90.0% |
| shadowsocks | 128 | 101 | 27 | 78.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 27 | 25 | 2 | 92.6% |
| vless | 613 | 344 | 269 | 56.1% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 102 |
| 204:TimeoutError | 48 |
| 204:ProxyError | 43 |
| speed:TimeoutError | 29 |
| cn-block:TimeoutError | 22 |
| geo:ClientOSError | 19 |
| speed:ClientOSError | 15 |
| 204:ClientOSError | 8 |
| cn-block:ProxyError | 7 |
| geo:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4695 |
| ConnectionRefusedError | 772 |
| gaierror | 313 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 143 | 1.0 | 344 |
| Au1rxx-base64 | 0.774 | prefer | 533 | 0.709 | 1651 |
| DeltaKronecker-all | 0.542 | observe | 117 | 0.462 | 3437 |
| Surfboard-tg-mixed | 0.477 | observe | 129 | 0.395 | 5222 |
| mheidari-all | 0.418 | observe | 10 | 0.5 | 18817 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 3833 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 56 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5486 |
| Epodonios-all | 0.255 | observe | 0 | None | 5783 |

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
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.395 | 51 | 78 | 129 |
| DeltaKronecker-all | 0.462 | 54 | 63 | 117 |
| mheidari-all | 0.5 | 5 | 5 | 10 |
| Au1rxx-base64 | 0.709 | 378 | 155 | 533 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 143 | 0 | 143 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18817 | yes | 5.62 | 0 |
| SoliSpirit-all | 7117 | yes | 3.52 | 0 |
| Epodonios-all | 5783 | yes | 2.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 5486 | yes | 1.74 | 0 |
| Surfboard-tg-mixed | 5222 | yes | 5.81 | 0 |
| mahdibland-V2RayAggregator | 5208 | yes | 3.44 | 0 |
| barry-far-vless | 4490 | yes | 1.62 | 0 |
| Surfboard-tg-vless | 4122 | yes | 3.68 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.45 | 0 |
| xiaoji235-airport-v2ray-all | 3833 | yes | 2.45 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 125 |
| 204 | 99 |
| speed | 47 |
| cn-block | 32 |
