# AutoNodes 每日报告

生成时间：2026-08-19 06:59:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82903 |
| 去重后节点数 | 22465 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1336 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22465 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 28.0 |
| geo | 0.8 |
| probe | 84.3 |
| real_test | 249.3 |
| tcp | 35.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 126 | 126 | 0 | 100.0% |
| hysteria2 | 20 | 16 | 4 | 80.0% |
| shadowsocks | 167 | 152 | 15 | 91.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 929 | 915 | 14 | 98.5% |
| vless | 237 | 125 | 112 | 52.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 45 |
| speed:TimeoutError | 27 |
| geo:ClientOSError | 20 |
| 204:TimeoutError | 14 |
| speed:ClientOSError | 13 |
| cn-block:TimeoutError | 10 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 5 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4364 |
| ConnectionRefusedError | 855 |
| gaierror | 414 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 803 | 0.984 | 1924 |
| zhangkai | 0.999 | prefer | 126 | 1.0 | 159 |
| mheidari-all | 0.887 | prefer | 329 | 0.809 | 16809 |
| Surfboard-tg-mixed | 0.867 | prefer | 181 | 0.79 | 6315 |
| nscl5-all | 0.4 | observe | 4 | 0.75 | 3330 |
| DeltaKronecker-all | 0.323 | observe | 35 | 0.229 | 6390 |
| Epodonios-all | 0.255 | observe | 0 | None | 7030 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7119 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4850 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.134 | observe | 1 | 0.0 | 0 | 175 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.229 | 8 | 27 | 35 |
| nscl5-all | 0.75 | 3 | 1 | 4 |
| Surfboard-tg-mixed | 0.79 | 143 | 38 | 181 |
| mheidari-all | 0.809 | 266 | 63 | 329 |
| Au1rxx-base64 | 0.984 | 790 | 13 | 803 |
| zhangkai | 1.0 | 126 | 0 | 126 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16809 | yes | 3.99 | 0 |
| SoliSpirit-all | 7119 | yes | 2.41 | 0 |
| Epodonios-all | 7030 | yes | 4.69 | 0 |
| DeltaKronecker-all | 6390 | yes | 2.67 | 0 |
| Surfboard-tg-mixed | 6315 | yes | 3.45 | 0 |
| barry-far-vless | 5173 | yes | 1.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 5067 | yes | 1.44 | 0 |
| Surfboard-tg-vless | 4850 | yes | 3.09 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.68 | 0 |
| mahdibland-V2RayAggregator | 3995 | yes | 2.5 | 0 |

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
| geo | 65 |
| speed | 40 |
| 204 | 22 |
| cn-block | 19 |
