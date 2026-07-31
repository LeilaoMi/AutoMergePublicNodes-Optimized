# AutoNodes 每日报告

生成时间：2026-07-31 09:01:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 77153 |
| 去重后节点数 | 22423 |
| TCP 可达数 | 3000 |
| 真测通过数 | 361 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22423 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 36.1 |
| geo | 1.4 |
| probe | 54.8 |
| real_test | 99.0 |
| tcp | 32.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 80 | 80 | 0 | 100.0% |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 145 | 117 | 28 | 80.7% |
| socks | 10 | 6 | 4 | 60.0% |
| trojan | 45 | 38 | 7 | 84.4% |
| vless | 220 | 106 | 114 | 48.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 40 |
| 204:ProxyError | 32 |
| 204:TimeoutError | 23 |
| geo:ClientOSError | 14 |
| speed:TimeoutError | 14 |
| cn-block:ProxyError | 8 |
| speed:ClientOSError | 8 |
| cn-block:TimeoutError | 8 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4566 |
| ConnectionRefusedError | 747 |
| OSError | 221 |
| gaierror | 199 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | prefer | 81 | 1.0 | 110 |
| Au1rxx-base64 | 0.849 | prefer | 194 | 0.799 | 1319 |
| mheidari-all | 0.646 | observe | 13 | 0.769 | 16339 |
| Surfboard-tg-mixed | 0.609 | observe | 155 | 0.529 | 5242 |
| DeltaKronecker-all | 0.543 | observe | 65 | 0.462 | 5144 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 174 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 45 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5507 |
| Epodonios-all | 0.255 | observe | 0 | None | 5918 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-vless | 0.161 | observe | 3 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.462 | 30 | 35 | 65 |
| Surfboard-tg-mixed | 0.529 | 82 | 73 | 155 |
| mheidari-all | 0.769 | 10 | 3 | 13 |
| Au1rxx-base64 | 0.799 | 155 | 39 | 194 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16339 | yes | 4.05 | 0 |
| SoliSpirit-all | 6473 | yes | 1.68 | 0 |
| Epodonios-all | 5918 | yes | 4.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5507 | yes | 1.24 | 0 |
| Surfboard-tg-mixed | 5242 | yes | 3.34 | 0 |
| DeltaKronecker-all | 5144 | yes | 4.24 | 0 |
| mahdibland-V2RayAggregator | 5074 | yes | 2.12 | 0 |
| barry-far-vless | 4510 | yes | 1.0 | 0 |
| Surfboard-tg-vless | 4146 | yes | 2.83 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.45 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 59 |
| geo | 54 |
| speed | 23 |
| cn-block | 19 |
