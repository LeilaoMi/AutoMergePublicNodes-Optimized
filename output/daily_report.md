# AutoNodes 每日报告

生成时间：2026-09-07 04:03:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 94333 |
| 去重后节点数 | 24798 |
| TCP 可达数 | 3000 |
| 真测通过数 | 609 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24798 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 44.3 |
| geo | 1.5 |
| probe | 95.2 |
| real_test | 182.9 |
| tcp | 42.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 24 | 20 | 4 | 83.3% |
| hysteria2 | 23 | 23 | 0 | 100.0% |
| shadowsocks | 182 | 170 | 12 | 93.4% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 62 | 49 | 13 | 79.0% |
| vless | 684 | 341 | 343 | 49.9% |
| vmess | 3 | 1 | 2 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 113 |
| geo:ClientOSError | 72 |
| speed:TimeoutError | 62 |
| 204:TimeoutError | 34 |
| speed:ClientOSError | 27 |
| cn-block:ClientOSError | 27 |
| cn-block:TimeoutError | 21 |
| 204:ProxyConnectionError | 11 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 2 |
| 204:ServerDisconnectedError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6073 |
| ConnectionRefusedError | 988 |
| gaierror | 325 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.992 | prefer | 328 | 0.921 | 1835 |
| zhangkai | 0.813 | prefer | 24 | 0.833 | 144 |
| Surfboard-tg-mixed | 0.782 | prefer | 216 | 0.704 | 7284 |
| mheidari-all | 0.405 | observe | 395 | 0.324 | 21249 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 5750 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4791 |
| tg-oneclickvpnkeys | 0.316 | observe | 2 | 1.0 | 121 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 177 |
| Epodonios-all | 0.255 | observe | 0 | None | 7766 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

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
| downweight | DeltaKronecker-all | 0.181 | 14 | 0.071 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.071 | 1 | 13 | 14 |
| mheidari-all | 0.324 | 128 | 267 | 395 |
| Surfboard-tg-mixed | 0.704 | 152 | 64 | 216 |
| zhangkai | 0.833 | 20 | 4 | 24 |
| Au1rxx-base64 | 0.921 | 302 | 26 | 328 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21249 | yes | 4.93 | 0 |
| SoliSpirit-all | 8622 | yes | 5.33 | 0 |
| Epodonios-all | 7766 | yes | 3.42 | 0 |
| Surfboard-tg-mixed | 7284 | yes | 5.16 | 0 |
| barry-far-vless | 6301 | yes | 2.1 | 0 |
| Surfboard-tg-vless | 6082 | yes | 4.0 | 0 |
| DeltaKronecker-all | 5856 | yes | 6.1 | 0 |
| xiaoji235-airport-v2ray-all | 5750 | yes | 2.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 4791 | yes | 4.95 | 0 |
| mahdibland-V2RayAggregator | 4138 | yes | 0.54 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 186 |
| speed | 89 |
| 204 | 51 |
| cn-block | 50 |
