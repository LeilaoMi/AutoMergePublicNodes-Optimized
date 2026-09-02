# AutoNodes 每日报告

生成时间：2026-09-02 03:59:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 82051 |
| 去重后节点数 | 23604 |
| TCP 可达数 | 3000 |
| 真测通过数 | 750 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23604 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| generate | 28.3 |
| geo | 1.4 |
| probe | 67.2 |
| real_test | 161.7 |
| tcp | 38.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 182 | 175 | 7 | 96.2% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 61 | 46 | 15 | 75.4% |
| vless | 732 | 486 | 246 | 66.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 90 |
| speed:TimeoutError | 49 |
| geo:ClientOSError | 40 |
| cn-block:TimeoutError | 24 |
| speed:ClientOSError | 20 |
| 204:TimeoutError | 15 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 10 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 1 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4736 |
| ConnectionRefusedError | 876 |
| gaierror | 278 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.975 | prefer | 441 | 0.907 | 1736 |
| zhangkai | 0.967 | prefer | 24 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.819 | prefer | 216 | 0.741 | 6990 |
| mheidari-all | 0.701 | prefer | 246 | 0.622 | 15712 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4708 |
| Epodonios-all | 0.255 | observe | 0 | None | 7407 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7631 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5850 |
| barry-far-vless | 0.255 | observe | 0 | None | 6027 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.234 | 89 | 0.146 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.146 | 13 | 76 | 89 |
| mheidari-all | 0.622 | 153 | 93 | 246 |
| Surfboard-tg-mixed | 0.741 | 160 | 56 | 216 |
| Au1rxx-base64 | 0.907 | 400 | 41 | 441 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15712 | yes | 3.47 | 0 |
| SoliSpirit-all | 7631 | yes | 1.12 | 0 |
| Epodonios-all | 7407 | yes | 3.75 | 0 |
| DeltaKronecker-all | 7294 | yes | 2.8 | 0 |
| Surfboard-tg-mixed | 6990 | yes | 2.24 | 0 |
| barry-far-vless | 6027 | yes | 1.24 | 0 |
| Surfboard-tg-vless | 5850 | yes | 1.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4708 | yes | 0.66 | 0 |
| mahdibland-V2RayAggregator | 4159 | yes | 1.49 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.87 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 133 |
| speed | 69 |
| cn-block | 35 |
| 204 | 33 |
