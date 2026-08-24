# AutoNodes 每日报告

生成时间：2026-08-24 01:45:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78233 |
| 去重后节点数 | 21555 |
| TCP 可达数 | 3000 |
| 真测通过数 | 747 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21555 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 26.3 |
| geo | 1.5 |
| probe | 55.8 |
| real_test | 144.5 |
| tcp | 35.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 22 | 22 | 0 | 100.0% |
| shadowsocks | 214 | 206 | 8 | 96.3% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 54 | 41 | 13 | 75.9% |
| vless | 535 | 359 | 176 | 67.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 71 |
| speed:TimeoutError | 42 |
| geo:ClientOSError | 20 |
| speed:ClientOSError | 19 |
| cn-block:TimeoutError | 15 |
| cn-block:ClientOSError | 10 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 8 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4818 |
| ConnectionRefusedError | 844 |
| gaierror | 358 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | prefer | 113 | 1.0 | 144 |
| Au1rxx-base64 | 0.983 | prefer | 448 | 0.917 | 1688 |
| Surfboard-tg-mixed | 0.867 | prefer | 158 | 0.791 | 6383 |
| DeltaKronecker-all | 0.574 | observe | 77 | 0.494 | 5415 |
| mheidari-all | 0.487 | observe | 143 | 0.406 | 14677 |
| nscl5-all | 0.352 | observe | 2 | 1.0 | 1008 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4989 |
| Epodonios-all | 0.255 | observe | 0 | None | 6993 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3989 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7072 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.406 | 58 | 85 | 143 |
| DeltaKronecker-all | 0.494 | 38 | 39 | 77 |
| Surfboard-tg-mixed | 0.791 | 125 | 33 | 158 |
| Au1rxx-base64 | 0.917 | 411 | 37 | 448 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14677 | yes | 4.11 | 0 |
| SoliSpirit-all | 7072 | yes | 4.56 | 0 |
| Epodonios-all | 6993 | yes | 4.35 | 0 |
| Surfboard-tg-mixed | 6383 | yes | 3.44 | 0 |
| barry-far-vless | 5618 | yes | 1.96 | 0 |
| DeltaKronecker-all | 5415 | yes | 4.42 | 0 |
| Surfboard-tg-vless | 5292 | yes | 1.68 | 0 |
| 10ium-ScrapeCategorize-Vless | 4989 | yes | 2.47 | 0 |
| mahdibland-V2RayAggregator | 4085 | yes | 1.35 | 0 |
| MatinGhanbari-all-sub | 3989 | yes | 2.26 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 92 |
| speed | 61 |
| cn-block | 27 |
| 204 | 18 |
