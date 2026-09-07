# AutoNodes 每日报告

生成时间：2026-09-07 12:10:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 94664 |
| 去重后节点数 | 24930 |
| TCP 可达数 | 3000 |
| 真测通过数 | 492 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24930 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 43.8 |
| geo | 1.4 |
| probe | 90.7 |
| real_test | 101.3 |
| tcp | 40.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 3 | 0 | 100.0% |
| http | 22 | 20 | 2 | 90.9% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 165 | 152 | 13 | 92.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 16 | 11 | 5 | 68.8% |
| vless | 393 | 281 | 112 | 71.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 38 |
| cn-block:ClientOSError | 34 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 11 |
| 204:ClientOSError | 7 |
| 204:ProxyError | 6 |
| speed:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| 204:ProxyConnectionError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5151 |
| ConnectionRefusedError | 1028 |
| gaierror | 436 |
| OSError | 238 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | prefer | 322 | 0.907 | 1781 |
| zhangkai | 0.919 | prefer | 21 | 0.952 | 144 |
| Surfboard-tg-mixed | 0.839 | prefer | 143 | 0.762 | 7247 |
| mheidari-all | 0.58 | observe | 134 | 0.5 | 21631 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 6417 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 5750 |
| tg-oneclickvpnkeys | 0.275 | observe | 3 | 0.667 | 151 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4650 |
| Epodonios-all | 0.255 | observe | 0 | None | 7707 |
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
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.5 | 67 | 67 | 134 |
| tg-oneclickvpnkeys | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.762 | 109 | 34 | 143 |
| Au1rxx-base64 | 0.907 | 292 | 30 | 322 |
| zhangkai | 0.952 | 20 | 1 | 21 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21631 | yes | 5.35 | 0 |
| SoliSpirit-all | 8442 | yes | 4.47 | 0 |
| Epodonios-all | 7707 | yes | 3.27 | 0 |
| Surfboard-tg-mixed | 7247 | yes | 3.54 | 0 |
| DeltaKronecker-all | 6417 | yes | 5.39 | 0 |
| barry-far-vless | 6245 | yes | 1.63 | 0 |
| Surfboard-tg-vless | 6030 | yes | 3.88 | 0 |
| xiaoji235-airport-v2ray-all | 5750 | yes | 1.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 4650 | yes | 2.97 | 0 |
| mahdibland-V2RayAggregator | 4138 | yes | 0.14 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 48 |
| geo | 43 |
| 204 | 31 |
| speed | 13 |
