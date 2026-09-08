# AutoNodes 每日报告

生成时间：2026-09-08 04:06:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 91631 |
| 去重后节点数 | 25396 |
| TCP 可达数 | 3000 |
| 真测通过数 | 694 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25396 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 50.1 |
| geo | 1.6 |
| probe | 99.0 |
| real_test | 197.1 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 9 | 5 | 4 | 55.6% |
| http | 58 | 58 | 0 | 100.0% |
| hysteria2 | 23 | 22 | 1 | 95.7% |
| shadowsocks | 182 | 172 | 10 | 94.5% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 63 | 46 | 17 | 73.0% |
| vless | 908 | 386 | 522 | 42.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 190 |
| speed:TimeoutError | 85 |
| geo:ClientOSError | 81 |
| speed:ClientOSError | 56 |
| cn-block:ClientOSError | 53 |
| 204:TimeoutError | 24 |
| cn-block:TimeoutError | 24 |
| 204:ProxyError | 22 |
| 204:ClientOSError | 16 |
| 204:ProxyConnectionError | 1 |
| cn-block:ProxyError | 1 |
| 204:ServerDisconnectedError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5530 |
| ConnectionRefusedError | 973 |
| gaierror | 453 |
| OSError | 237 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.994 | prefer | 40 | 1.0 | 450 |
| Au1rxx-base64 | 0.985 | prefer | 360 | 0.914 | 1833 |
| ermaozi-get_subscribe | 0.94 | prefer | 19 | 1.0 | 470 |
| Surfboard-tg-mixed | 0.919 | prefer | 85 | 0.847 | 7392 |
| DeltaKronecker-all | 0.457 | observe | 59 | 0.373 | 6417 |
| mheidari-all | 0.389 | observe | 672 | 0.308 | 22287 |
| tg-oneclickvpnkeys | 0.313 | observe | 8 | 0.5 | 196 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7885 |
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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.308 | 207 | 465 | 672 |
| DeltaKronecker-all | 0.373 | 22 | 37 | 59 |
| tg-oneclickvpnkeys | 0.5 | 4 | 4 | 8 |
| Surfboard-tg-mixed | 0.847 | 72 | 13 | 85 |
| Au1rxx-base64 | 0.914 | 329 | 31 | 360 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22287 | yes | 5.85 | 0 |
| SoliSpirit-all | 8682 | yes | 2.13 | 0 |
| Epodonios-all | 7885 | yes | 3.9 | 0 |
| Surfboard-tg-mixed | 7392 | yes | 4.32 | 0 |
| barry-far-vless | 6444 | yes | 1.71 | 0 |
| DeltaKronecker-all | 6417 | yes | 5.66 | 0 |
| Surfboard-tg-vless | 6186 | yes | 3.67 | 0 |
| xiaoji235-airport-v2ray-all | 5750 | yes | 3.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 4650 | yes | 1.44 | 0 |
| mahdibland-V2RayAggregator | 4218 | yes | 3.16 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 272 |
| speed | 141 |
| cn-block | 78 |
| 204 | 64 |
