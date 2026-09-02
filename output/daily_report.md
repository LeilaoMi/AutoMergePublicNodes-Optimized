# AutoNodes 每日报告

生成时间：2026-09-02 20:56:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82593 |
| 去重后节点数 | 23713 |
| TCP 可达数 | 3000 |
| 真测通过数 | 483 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23713 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 49.3 |
| geo | 1.4 |
| probe | 81.9 |
| real_test | 97.7 |
| tcp | 37.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 19 | 4 | 82.6% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 90 | 84 | 6 | 93.3% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 29 | 26 | 3 | 89.7% |
| vless | 410 | 335 | 75 | 81.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 17 |
| cn-block:TimeoutError | 17 |
| geo:ClientOSError | 14 |
| cn-block:ClientOSError | 11 |
| speed:ClientOSError | 8 |
| 204:ProxyError | 7 |
| 204:ProxyConnectionError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 2 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4734 |
| ConnectionRefusedError | 930 |
| gaierror | 275 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | prefer | 346 | 0.913 | 1798 |
| mheidari-all | 0.851 | prefer | 103 | 0.777 | 15504 |
| zhangkai | 0.766 | prefer | 23 | 0.783 | 144 |
| DeltaKronecker-all | 0.743 | prefer | 90 | 0.667 | 7295 |
| Surfboard-tg-mixed | 0.606 | observe | 9 | 0.889 | 7091 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 131 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4765 |
| Epodonios-all | 0.255 | observe | 0 | None | 7530 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7745 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.667 | 60 | 30 | 90 |
| mheidari-all | 0.777 | 80 | 23 | 103 |
| zhangkai | 0.783 | 18 | 5 | 23 |
| Surfboard-tg-mixed | 0.889 | 8 | 1 | 9 |
| Au1rxx-base64 | 0.913 | 316 | 30 | 346 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15504 | yes | 4.84 | 0 |
| SoliSpirit-all | 7745 | yes | 3.82 | 0 |
| Epodonios-all | 7530 | yes | 5.2 | 0 |
| DeltaKronecker-all | 7295 | yes | 4.3 | 0 |
| Surfboard-tg-mixed | 7091 | yes | 3.73 | 0 |
| barry-far-vless | 6223 | yes | 4.35 | 0 |
| Surfboard-tg-vless | 6013 | yes | 5.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4765 | yes | 2.64 | 0 |
| mahdibland-V2RayAggregator | 4066 | yes | 1.51 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 2.71 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 34 |
| cn-block | 32 |
| geo | 17 |
| speed | 8 |
