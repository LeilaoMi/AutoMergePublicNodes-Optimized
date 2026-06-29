# AutoNodes 每日报告

生成时间：2026-06-29 20:11:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 75589 |
| 去重后节点数 | 23098 |
| TCP 可达数 | 3000 |
| 真测通过数 | 452 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23098 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 36.4 |
| geo | 1.4 |
| probe | 57.0 |
| real_test | 131.4 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 104 | 80 | 24 | 76.9% |
| socks | 17 | 14 | 3 | 82.4% |
| trojan | 124 | 53 | 71 | 42.7% |
| vless | 380 | 260 | 120 | 68.4% |
| vmess | 7 | 7 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 95 |
| 204:ProxyError | 24 |
| 204:TimeoutError | 22 |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 12 |
| geo:TimeoutError | 11 |
| 204:ClientOSError | 11 |
| geo:ClientOSError | 9 |
| geo:ProxyError | 8 |
| cn-block:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4338 |
| ConnectionRefusedError | 647 |
| gaierror | 201 |
| OSError | 131 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.803 | prefer | 38 | 0.816 | 79 |
| mheidari-all | 0.761 | prefer | 249 | 0.683 | 15724 |
| Surfboard-tg-mixed | 0.722 | prefer | 305 | 0.643 | 5575 |
| DeltaKronecker-all | 0.495 | observe | 39 | 0.41 | 7004 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4653 |
| Epodonios-all | 0.255 | observe | 0 | None | 6449 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3980 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RayRootFree | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.41 | 16 | 23 | 39 |
| Surfboard-tg-mixed | 0.643 | 196 | 109 | 305 |
| mheidari-all | 0.683 | 170 | 79 | 249 |
| Au1rxx-base64 | 0.816 | 31 | 7 | 38 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15724 | yes | 2.84 | 0 |
| DeltaKronecker-all | 7004 | yes | 3.01 | 0 |
| SoliSpirit-all | 6727 | yes | 1.79 | 0 |
| Epodonios-all | 6449 | yes | 3.57 | 0 |
| Surfboard-tg-mixed | 5575 | yes | 2.99 | 0 |
| mahdibland-V2RayAggregator | 5353 | yes | 1.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4653 | yes | 0.64 | 0 |
| barry-far-vless | 4569 | yes | 0.78 | 0 |
| Surfboard-tg-vless | 4058 | yes | 1.75 | 0 |
| MatinGhanbari-all-sub | 3980 | yes | 0.89 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 109 |
| 204 | 57 |
| geo | 28 |
| cn-block | 24 |
