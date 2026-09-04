# AutoNodes 每日报告

生成时间：2026-09-04 16:11:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84288 |
| 去重后节点数 | 23436 |
| TCP 可达数 | 3000 |
| 真测通过数 | 595 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23436 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 42.2 |
| geo | 1.2 |
| probe | 91.0 |
| real_test | 145.6 |
| tcp | 37.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 24 | 4 | 85.7% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 158 | 142 | 16 | 89.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 35 | 23 | 12 | 65.7% |
| vless | 472 | 390 | 82 | 82.6% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 30 |
| cn-block:TimeoutError | 19 |
| cn-block:ClientOSError | 14 |
| 204:ProxyError | 12 |
| speed:TimeoutError | 10 |
| geo:ClientOSError | 10 |
| 204:ProxyConnectionError | 8 |
| speed:ClientOSError | 5 |
| 204:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4538 |
| ConnectionRefusedError | 901 |
| gaierror | 402 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.986 | prefer | 356 | 0.919 | 1751 |
| mheidari-all | 0.848 | prefer | 149 | 0.772 | 15927 |
| zhangkai | 0.806 | prefer | 23 | 0.826 | 144 |
| Surfboard-tg-mixed | 0.801 | prefer | 163 | 0.724 | 7209 |
| DeltaKronecker-all | 0.661 | observe | 12 | 0.833 | 7089 |
| tg-oneclickvpnkeys | 0.443 | observe | 5 | 1.0 | 104 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4810 |
| Epodonios-all | 0.255 | observe | 0 | None | 7667 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.724 | 118 | 45 | 163 |
| mheidari-all | 0.772 | 115 | 34 | 149 |
| zhangkai | 0.826 | 19 | 4 | 23 |
| DeltaKronecker-all | 0.833 | 10 | 2 | 12 |
| Au1rxx-base64 | 0.919 | 327 | 29 | 356 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 5 | 0 | 5 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15927 | yes | 5.18 | 0 |
| SoliSpirit-all | 8718 | yes | 3.41 | 0 |
| Epodonios-all | 7667 | yes | 3.21 | 0 |
| Surfboard-tg-mixed | 7209 | yes | 4.19 | 0 |
| DeltaKronecker-all | 7089 | yes | 5.49 | 0 |
| barry-far-vless | 6339 | yes | 2.21 | 0 |
| Surfboard-tg-vless | 6091 | yes | 4.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4810 | yes | 2.54 | 0 |
| mahdibland-V2RayAggregator | 4123 | yes | 2.96 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 53 |
| cn-block | 34 |
| speed | 16 |
| geo | 12 |
