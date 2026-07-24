# AutoNodes 每日报告

生成时间：2026-07-24 03:24:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83696 |
| 去重后节点数 | 23126 |
| TCP 可达数 | 3000 |
| 真测通过数 | 859 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23126 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 36.1 |
| geo | 1.4 |
| probe | 64.4 |
| real_test | 211.0 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 35 | 1 | 97.2% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 154 | 144 | 10 | 93.5% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 685 | 582 | 103 | 85.0% |
| vless | 449 | 91 | 358 | 20.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 206 |
| cn-block:TimeoutError | 71 |
| speed:ClientOSError | 61 |
| speed:TimeoutError | 44 |
| 204:ProxyError | 38 |
| geo:ClientOSError | 37 |
| cn-block:ClientOSError | 5 |
| 204:TimeoutError | 3 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 3 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4133 |
| ConnectionRefusedError | 700 |
| gaierror | 408 |
| OSError | 217 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | prefer | 36 | 0.972 | 61 |
| Surfboard-tg-mixed | 0.912 | prefer | 99 | 0.838 | 5375 |
| DeltaKronecker-all | 0.822 | prefer | 153 | 0.745 | 5572 |
| Au1rxx-base64 | 0.759 | prefer | 199 | 0.744 | 432 |
| mheidari-all | 0.645 | observe | 840 | 0.565 | 20024 |
| 10ium-HighSpeed | 0.345 | observe | 2 | 1.0 | 839 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 3843 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4757 |
| Epodonios-all | 0.255 | observe | 0 | None | 6509 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.565 | 475 | 365 | 840 |
| Au1rxx-base64 | 0.744 | 148 | 51 | 199 |
| DeltaKronecker-all | 0.745 | 114 | 39 | 153 |
| Surfboard-tg-mixed | 0.838 | 83 | 16 | 99 |
| zhangkai | 0.972 | 35 | 1 | 36 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20024 | yes | 4.04 | 0 |
| SoliSpirit-all | 6957 | yes | 3.18 | 0 |
| Epodonios-all | 6509 | yes | 1.88 | 0 |
| DeltaKronecker-all | 5572 | yes | 3.98 | 0 |
| Surfboard-tg-mixed | 5375 | yes | 2.55 | 0 |
| mahdibland-V2RayAggregator | 4971 | yes | 2.13 | 0 |
| 10ium-ScrapeCategorize-Vless | 4757 | yes | 2.43 | 0 |
| barry-far-vless | 4750 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 4163 | yes | 2.04 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 2.86 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 245 |
| speed | 108 |
| cn-block | 79 |
| 204 | 42 |
