# AutoNodes 每日报告

生成时间：2026-08-25 07:00:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78337 |
| 去重后节点数 | 22287 |
| TCP 可达数 | 3000 |
| 真测通过数 | 685 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22287 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 30.8 |
| geo | 1.4 |
| probe | 54.4 |
| real_test | 134.5 |
| tcp | 35.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 222 | 205 | 17 | 92.3% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 89 | 74 | 15 | 83.1% |
| vless | 502 | 359 | 143 | 71.5% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 54 |
| 204:TimeoutError | 23 |
| speed:TimeoutError | 21 |
| speed:ClientOSError | 20 |
| cn-block:TimeoutError | 19 |
| geo:ClientOSError | 16 |
| 204:ClientOSError | 9 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4782 |
| ConnectionRefusedError | 810 |
| gaierror | 353 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | prefer | 24 | 1.0 | 144 |
| Au1rxx-base64 | 0.925 | prefer | 508 | 0.858 | 1700 |
| Surfboard-tg-mixed | 0.824 | prefer | 154 | 0.747 | 6465 |
| mheidari-all | 0.803 | prefer | 63 | 0.73 | 14480 |
| DeltaKronecker-all | 0.651 | observe | 110 | 0.573 | 6340 |
| 10ium-ScrapeCategorize-Vless | 0.287 | observe | 2 | 0.5 | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 6925 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3989 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6957 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5306 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.573 | 63 | 47 | 110 |
| mheidari-all | 0.73 | 46 | 17 | 63 |
| Surfboard-tg-mixed | 0.747 | 115 | 39 | 154 |
| Au1rxx-base64 | 0.858 | 436 | 72 | 508 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14480 | yes | 4.55 | 0 |
| SoliSpirit-all | 6957 | yes | 4.81 | 0 |
| Epodonios-all | 6925 | yes | 4.82 | 0 |
| Surfboard-tg-mixed | 6465 | yes | 4.12 | 0 |
| DeltaKronecker-all | 6340 | yes | 5.14 | 0 |
| barry-far-vless | 5525 | yes | 2.99 | 0 |
| Surfboard-tg-vless | 5306 | yes | 3.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 3.03 | 0 |
| mahdibland-V2RayAggregator | 4119 | yes | 1.5 | 0 |
| MatinGhanbari-all-sub | 3989 | yes | 3.35 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 71 |
| speed | 43 |
| 204 | 36 |
| cn-block | 28 |
