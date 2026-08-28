# AutoNodes 每日报告

生成时间：2026-08-28 22:07:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77033 |
| 去重后节点数 | 20891 |
| TCP 可达数 | 3000 |
| 真测通过数 | 630 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 20891 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 44.3 |
| geo | 1.4 |
| probe | 61.9 |
| real_test | 131.2 |
| tcp | 34.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 28 | 0 | 100.0% |
| hysteria2 | 27 | 24 | 3 | 88.9% |
| shadowsocks | 176 | 164 | 12 | 93.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 22 | 21 | 1 | 95.5% |
| vless | 475 | 389 | 86 | 81.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 23 |
| cn-block:TimeoutError | 20 |
| geo:ClientOSError | 18 |
| 204:ProxyError | 10 |
| speed:ClientOSError | 8 |
| speed:TimeoutError | 7 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4624 |
| ConnectionRefusedError | 894 |
| gaierror | 442 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 352 | 0.949 | 1776 |
| zhangkai | 0.967 | prefer | 24 | 1.0 | 144 |
| mheidari-all | 0.949 | prefer | 82 | 0.878 | 14493 |
| DeltaKronecker-all | 0.889 | prefer | 87 | 0.816 | 4065 |
| Surfboard-tg-mixed | 0.758 | prefer | 181 | 0.68 | 6713 |
| tg-oneclickvpnkeys | 0.445 | observe | 5 | 1.0 | 140 |
| nscl5-all | 0.279 | observe | 1 | 1.0 | 594 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4725 |
| Epodonios-all | 0.255 | observe | 0 | None | 6861 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.68 | 123 | 58 | 181 |
| DeltaKronecker-all | 0.816 | 71 | 16 | 87 |
| mheidari-all | 0.878 | 72 | 10 | 82 |
| Au1rxx-base64 | 0.949 | 334 | 18 | 352 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 5 | 0 | 5 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14493 | yes | 5.0 | 0 |
| SoliSpirit-all | 7878 | yes | 4.6 | 0 |
| Epodonios-all | 6861 | yes | 3.95 | 0 |
| Surfboard-tg-mixed | 6713 | yes | 3.77 | 0 |
| Surfboard-tg-vless | 5540 | yes | 3.44 | 0 |
| barry-far-vless | 5468 | yes | 3.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4725 | yes | 3.57 | 0 |
| mahdibland-V2RayAggregator | 4081 | yes | 3.51 | 0 |
| DeltaKronecker-all | 4065 | yes | 5.16 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 3.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 37 |
| cn-block | 29 |
| geo | 20 |
| speed | 17 |
