# AutoNodes 每日报告

生成时间：2026-08-01 13:44:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78943 |
| 去重后节点数 | 23426 |
| TCP 可达数 | 3000 |
| 真测通过数 | 626 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23426 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 40.5 |
| geo | 1.4 |
| probe | 59.5 |
| real_test | 148.7 |
| tcp | 35.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 146 | 146 | 0 | 100.0% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 157 | 134 | 23 | 85.4% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 34 | 28 | 6 | 82.4% |
| vless | 443 | 302 | 141 | 68.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 46 |
| speed:TimeoutError | 32 |
| 204:TimeoutError | 20 |
| 204:ProxyError | 19 |
| speed:ClientOSError | 15 |
| geo:ClientOSError | 14 |
| 204:ClientOSError | 13 |
| cn-block:TimeoutError | 9 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4644 |
| ConnectionRefusedError | 776 |
| gaierror | 291 |
| OSError | 224 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.994 | prefer | 148 | 0.993 | 194 |
| Au1rxx-base64 | 0.828 | prefer | 498 | 0.761 | 1689 |
| Surfboard-tg-mixed | 0.727 | prefer | 100 | 0.65 | 5351 |
| DeltaKronecker-all | 0.712 | prefer | 36 | 0.639 | 5502 |
| mheidari-all | 0.515 | observe | 11 | 0.636 | 16460 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 5964 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 6948 |
| xiaoji235-airport-v2ray-all | 0.329 | observe | 1 | 1.0 | 1861 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 53 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.636 | 7 | 4 | 11 |
| DeltaKronecker-all | 0.639 | 23 | 13 | 36 |
| Surfboard-tg-mixed | 0.65 | 65 | 35 | 100 |
| Au1rxx-base64 | 0.761 | 379 | 119 | 498 |
| zhangkai | 0.993 | 147 | 1 | 148 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16460 | yes | 4.87 | 0 |
| SoliSpirit-all | 6948 | yes | 4.24 | 0 |
| Epodonios-all | 5964 | yes | 5.51 | 0 |
| DeltaKronecker-all | 5502 | yes | 4.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 5391 | yes | 2.11 | 0 |
| Surfboard-tg-mixed | 5351 | yes | 4.1 | 0 |
| mahdibland-V2RayAggregator | 5039 | yes | 3.12 | 0 |
| barry-far-vless | 4602 | yes | 1.57 | 0 |
| Surfboard-tg-vless | 4224 | yes | 3.3 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 60 |
| 204 | 52 |
| speed | 48 |
| cn-block | 13 |
