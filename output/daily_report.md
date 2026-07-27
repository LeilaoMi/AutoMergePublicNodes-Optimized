# AutoNodes 每日报告

生成时间：2026-07-27 14:53:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 85525 |
| 去重后节点数 | 22983 |
| TCP 可达数 | 3000 |
| 真测通过数 | 698 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22983 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 40.7 |
| geo | 1.4 |
| probe | 63.2 |
| real_test | 172.0 |
| tcp | 32.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 4 | 1 | 80.0% |
| http | 59 | 58 | 1 | 98.3% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 149 | 134 | 15 | 89.9% |
| socks | 6 | 2 | 4 | 33.3% |
| trojan | 457 | 388 | 69 | 84.9% |
| vless | 252 | 101 | 151 | 40.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 60 |
| speed:ClientOSError | 45 |
| cn-block:TimeoutError | 29 |
| 204:ProxyError | 28 |
| 204:TimeoutError | 22 |
| geo:ClientOSError | 20 |
| speed:TimeoutError | 10 |
| cn-block:ProxyError | 9 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 4 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4410 |
| ConnectionRefusedError | 715 |
| gaierror | 295 |
| OSError | 223 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.988 | prefer | 415 | 0.93 | 1507 |
| zhangkai | 0.97 | prefer | 59 | 0.983 | 74 |
| mheidari-all | 0.779 | prefer | 121 | 0.702 | 19227 |
| DeltaKronecker-all | 0.623 | observe | 138 | 0.543 | 5643 |
| Surfboard-tg-mixed | 0.535 | observe | 196 | 0.454 | 5641 |
| tg-oneclickvpnkeys | 0.371 | observe | 5 | 0.8 | 131 |
| xiaoji235-airport-v2ray-all | 0.259 | observe | 3 | 0.333 | 3959 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4831 |
| Epodonios-all | 0.255 | observe | 0 | None | 6520 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.333 | 1 | 2 | 3 |
| Surfboard-tg-mixed | 0.454 | 89 | 107 | 196 |
| DeltaKronecker-all | 0.543 | 75 | 63 | 138 |
| mheidari-all | 0.702 | 85 | 36 | 121 |
| tg-oneclickvpnkeys | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.93 | 386 | 29 | 415 |
| zhangkai | 0.983 | 58 | 1 | 59 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19227 | yes | 4.45 | 0 |
| SoliSpirit-all | 6628 | yes | 2.85 | 0 |
| Epodonios-all | 6520 | yes | 2.2 | 0 |
| DeltaKronecker-all | 5643 | yes | 5.19 | 0 |
| Surfboard-tg-mixed | 5641 | yes | 3.03 | 0 |
| mahdibland-V2RayAggregator | 5017 | yes | 3.71 | 0 |
| barry-far-vless | 4866 | yes | 3.02 | 0 |
| 10ium-ScrapeCategorize-Vless | 4831 | yes | 0.98 | 0 |
| Surfboard-tg-vless | 4484 | yes | 2.83 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 1.41 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 84 |
| speed | 58 |
| 204 | 54 |
| cn-block | 46 |
