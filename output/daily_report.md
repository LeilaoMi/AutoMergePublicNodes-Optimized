# AutoNodes 每日报告

生成时间：2026-09-03 20:52:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82446 |
| 去重后节点数 | 22585 |
| TCP 可达数 | 3000 |
| 真测通过数 | 508 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22585 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 29.5 |
| geo | 1.4 |
| probe | 67.1 |
| real_test | 100.5 |
| tcp | 37.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 24 | 23 | 1 | 95.8% |
| shadowsocks | 116 | 106 | 10 | 91.4% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 34 | 26 | 8 | 76.5% |
| vless | 384 | 324 | 60 | 84.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 24 |
| cn-block:TimeoutError | 20 |
| speed:ClientOSError | 8 |
| geo:ClientOSError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| 204:ProxyError | 4 |
| geo:TimeoutError | 3 |
| speed:TimeoutError | 2 |
| 204:ServerDisconnectedError | 1 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5034 |
| ConnectionRefusedError | 910 |
| gaierror | 293 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.981 | prefer | 369 | 0.913 | 1748 |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| mheidari-all | 0.866 | prefer | 96 | 0.792 | 15893 |
| DeltaKronecker-all | 0.788 | prefer | 87 | 0.713 | 6335 |
| Surfboard-tg-mixed | 0.547 | observe | 9 | 0.778 | 7177 |
| tg-oneclickvpnkeys | 0.405 | observe | 4 | 1.0 | 115 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4671 |
| Epodonios-all | 0.255 | observe | 0 | None | 7695 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8160 |

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
| DeltaKronecker-all | 0.713 | 62 | 25 | 87 |
| Surfboard-tg-mixed | 0.778 | 7 | 2 | 9 |
| mheidari-all | 0.792 | 76 | 20 | 96 |
| Au1rxx-base64 | 0.913 | 337 | 32 | 369 |
| tg-oneclickvpnkeys | 1.0 | 4 | 0 | 4 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15893 | yes | 3.63 | 0 |
| SoliSpirit-all | 8160 | yes | 2.77 | 0 |
| Epodonios-all | 7695 | yes | 2.28 | 0 |
| Surfboard-tg-mixed | 7177 | yes | 2.99 | 0 |
| DeltaKronecker-all | 6335 | yes | 3.41 | 0 |
| barry-far-vless | 6131 | yes | 1.81 | 0 |
| Surfboard-tg-vless | 5920 | yes | 2.83 | 0 |
| 10ium-ScrapeCategorize-Vless | 4671 | yes | 2.04 | 0 |
| mahdibland-V2RayAggregator | 4133 | yes | 0.76 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.9 | 0 |

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
| cn-block | 30 |
| 204 | 30 |
| geo | 10 |
| speed | 10 |
