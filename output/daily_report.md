# AutoNodes 每日报告

生成时间：2026-08-10 02:15:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 86295 |
| 去重后节点数 | 23966 |
| TCP 可达数 | 3000 |
| 真测通过数 | 583 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23966 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 44.5 |
| geo | 1.4 |
| probe | 52.5 |
| real_test | 138.9 |
| tcp | 34.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 24 | 21 | 3 | 87.5% |
| shadowsocks | 159 | 153 | 6 | 96.2% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 144 | 131 | 13 | 91.0% |
| vless | 623 | 249 | 374 | 40.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 152 |
| speed:TimeoutError | 80 |
| geo:ClientOSError | 73 |
| speed:ClientOSError | 31 |
| cn-block:TimeoutError | 28 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 11 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 2 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| geo:status | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4067 |
| ConnectionRefusedError | 848 |
| gaierror | 417 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | prefer | 457 | 0.893 | 1716 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.662 | observe | 156 | 0.583 | 6683 |
| tg-oneclickvpnkeys | 0.402 | observe | 4 | 1.0 | 44 |
| nscl5-all | 0.313 | observe | 1 | 1.0 | 1442 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| mheidari-all | 0.258 | observe | 296 | 0.176 | 20202 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5505 |
| Epodonios-all | 0.255 | observe | 0 | None | 7220 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.236 | 43 | 0.14 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.14 | 6 | 37 | 43 |
| mheidari-all | 0.176 | 52 | 244 | 296 |
| Surfboard-tg-mixed | 0.583 | 91 | 65 | 156 |
| Au1rxx-base64 | 0.893 | 408 | 49 | 457 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 4 | 0 | 4 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20202 | yes | 4.6 | 0 |
| SoliSpirit-all | 7672 | yes | 4.57 | 0 |
| Epodonios-all | 7220 | yes | 2.66 | 0 |
| Surfboard-tg-mixed | 6683 | yes | 3.46 | 0 |
| barry-far-vless | 5808 | yes | 1.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 5505 | yes | 1.86 | 0 |
| Surfboard-tg-vless | 5494 | yes | 3.65 | 0 |
| mahdibland-V2RayAggregator | 5189 | yes | 2.87 | 0 |
| DeltaKronecker-all | 4998 | yes | 4.92 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.94 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 229 |
| speed | 111 |
| cn-block | 32 |
| 204 | 25 |
