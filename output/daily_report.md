# AutoNodes 每日报告

生成时间：2026-07-18 13:33:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 81014 |
| 去重后节点数 | 22082 |
| TCP 可达数 | 3000 |
| 真测通过数 | 860 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22082 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 33.7 |
| geo | 0.8 |
| probe | 68.3 |
| real_test | 204.0 |
| tcp | 31.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 155 | 137 | 18 | 88.4% |
| socks | 10 | 7 | 3 | 70.0% |
| trojan | 665 | 587 | 78 | 88.3% |
| vless | 319 | 89 | 230 | 27.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 134 |
| speed:ClientOSError | 60 |
| 204:TimeoutError | 39 |
| cn-block:TimeoutError | 32 |
| geo:ClientOSError | 27 |
| 204:ProxyError | 13 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4179 |
| ConnectionRefusedError | 701 |
| gaierror | 271 |
| OSError | 217 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.883 | prefer | 449 | 0.804 | 19072 |
| nscl5-all | 0.862 | prefer | 21 | 0.81 | 1976 |
| Au1rxx-base64 | 0.834 | prefer | 132 | 0.833 | 150 |
| DeltaKronecker-all | 0.73 | prefer | 224 | 0.652 | 4096 |
| Surfboard-tg-mixed | 0.662 | observe | 321 | 0.583 | 5677 |
| xiaoji235-airport-v2ray-all | 0.438 | observe | 3 | 1.0 | 4321 |
| Epodonios-all | 0.255 | observe | 0 | None | 6767 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7013 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.583 | 187 | 134 | 321 |
| DeltaKronecker-all | 0.652 | 146 | 78 | 224 |
| mheidari-all | 0.804 | 361 | 88 | 449 |
| nscl5-all | 0.81 | 17 | 4 | 21 |
| Au1rxx-base64 | 0.833 | 110 | 22 | 132 |
| xiaoji235-airport-v2ray-all | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19072 | yes | 3.67 | 0 |
| SoliSpirit-all | 7013 | yes | 2.43 | 0 |
| Epodonios-all | 6767 | yes | 0.59 | 0 |
| Surfboard-tg-mixed | 5677 | yes | 2.24 | 0 |
| mahdibland-V2RayAggregator | 5334 | yes | 1.66 | 0 |
| barry-far-vless | 4927 | yes | 1.07 | 0 |
| 10ium-ScrapeCategorize-Vless | 4371 | yes | 1.27 | 0 |
| xiaoji235-airport-v2ray-all | 4321 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 4291 | yes | 1.94 | 0 |
| DeltaKronecker-all | 4096 | yes | 3.93 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 164 |
| speed | 71 |
| 204 | 57 |
| cn-block | 37 |
