# AutoNodes 每日报告

生成时间：2026-09-04 20:41:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 84229 |
| 去重后节点数 | 23541 |
| TCP 可达数 | 3000 |
| 真测通过数 | 584 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23541 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 39.4 |
| geo | 1.3 |
| probe | 73.6 |
| real_test | 129.9 |
| tcp | 38.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 28 | 28 | 0 | 100.0% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 173 | 153 | 20 | 88.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 25 | 22 | 3 | 88.0% |
| vless | 474 | 364 | 110 | 76.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 26 |
| 204:TimeoutError | 25 |
| geo:ClientOSError | 23 |
| cn-block:ClientOSError | 18 |
| speed:ClientOSError | 13 |
| geo:TimeoutError | 9 |
| 204:ProxyError | 7 |
| speed:TimeoutError | 7 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5159 |
| ConnectionRefusedError | 889 |
| gaierror | 365 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.962 | prefer | 21 | 1.0 | 144 |
| Au1rxx-base64 | 0.915 | prefer | 346 | 0.847 | 1756 |
| mheidari-all | 0.882 | prefer | 124 | 0.806 | 16096 |
| Surfboard-tg-mixed | 0.81 | prefer | 183 | 0.732 | 7342 |
| DeltaKronecker-all | 0.81 | prefer | 35 | 0.743 | 7089 |
| tg-oneclickvpnkeys | 0.589 | observe | 9 | 1.0 | 118 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4810 |
| Epodonios-all | 0.255 | observe | 0 | None | 7798 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| Surfboard-tg-mixed | 0.732 | 134 | 49 | 183 |
| DeltaKronecker-all | 0.743 | 26 | 9 | 35 |
| mheidari-all | 0.806 | 100 | 24 | 124 |
| Au1rxx-base64 | 0.847 | 293 | 53 | 346 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 9 | 0 | 9 |
| zhangkai | 1.0 | 21 | 0 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16096 | yes | 3.66 | 0 |
| SoliSpirit-all | 8118 | yes | 2.77 | 0 |
| Epodonios-all | 7798 | yes | 1.92 | 0 |
| Surfboard-tg-mixed | 7342 | yes | 2.7 | 0 |
| DeltaKronecker-all | 7089 | yes | 5.59 | 0 |
| barry-far-vless | 6376 | yes | 2.59 | 0 |
| Surfboard-tg-vless | 6159 | yes | 2.84 | 0 |
| 10ium-ScrapeCategorize-Vless | 4810 | yes | 2.21 | 0 |
| mahdibland-V2RayAggregator | 4095 | yes | 0.71 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.04 | 0 |

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
| cn-block | 47 |
| 204 | 35 |
| geo | 34 |
| speed | 20 |
