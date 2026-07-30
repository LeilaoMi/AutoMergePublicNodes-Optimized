# AutoNodes 每日报告

生成时间：2026-07-30 14:20:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78844 |
| 去重后节点数 | 22974 |
| TCP 可达数 | 3000 |
| 真测通过数 | 473 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22974 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 46.6 |
| geo | 1.4 |
| probe | 56.3 |
| real_test | 120.1 |
| tcp | 32.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 129 | 108 | 21 | 83.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 30 | 25 | 5 | 83.3% |
| vless | 359 | 213 | 146 | 59.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 55 |
| geo:ClientOSError | 30 |
| speed:TimeoutError | 25 |
| 204:TimeoutError | 21 |
| 204:ProxyError | 15 |
| speed:ClientOSError | 13 |
| cn-block:TimeoutError | 7 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4615 |
| ConnectionRefusedError | 742 |
| OSError | 225 |
| gaierror | 192 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | prefer | 113 | 1.0 | 129 |
| Au1rxx-base64 | 0.869 | prefer | 262 | 0.813 | 1460 |
| DeltaKronecker-all | 0.62 | observe | 159 | 0.541 | 5759 |
| Surfboard-tg-mixed | 0.618 | observe | 104 | 0.538 | 5443 |
| mheidari-all | 0.446 | observe | 5 | 0.8 | 16526 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5342 |
| Epodonios-all | 0.255 | observe | 0 | None | 6193 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6515 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.538 | 56 | 48 | 104 |
| DeltaKronecker-all | 0.541 | 86 | 73 | 159 |
| mheidari-all | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.813 | 213 | 49 | 262 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16526 | yes | 4.91 | 0 |
| SoliSpirit-all | 6515 | yes | 3.47 | 0 |
| Epodonios-all | 6193 | yes | 2.81 | 0 |
| DeltaKronecker-all | 5759 | yes | 5.03 | 0 |
| Surfboard-tg-mixed | 5443 | yes | 4.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 5342 | yes | 2.31 | 0 |
| mahdibland-V2RayAggregator | 5029 | yes | 2.65 | 0 |
| barry-far-vless | 4667 | yes | 1.25 | 0 |
| Surfboard-tg-vless | 4288 | yes | 3.29 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 2.58 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 87 |
| speed | 39 |
| 204 | 37 |
| cn-block | 12 |
