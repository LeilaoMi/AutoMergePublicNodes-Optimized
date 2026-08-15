# AutoNodes 每日报告

生成时间：2026-08-15 12:53:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77456 |
| 去重后节点数 | 22403 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1031 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22403 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 11.6 |
| generate | 25.2 |
| geo | 1.0 |
| probe | 66.7 |
| real_test | 187.8 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 152 | 145 | 7 | 95.4% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 568 | 552 | 16 | 97.2% |
| vless | 244 | 184 | 60 | 75.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 24 |
| geo:TimeoutError | 15 |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 12 |
| geo:ClientOSError | 10 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| 204:ProxyError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4712 |
| ConnectionRefusedError | 795 |
| gaierror | 274 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 734 | 0.971 | 1659 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| mheidari-all | 0.982 | prefer | 49 | 0.918 | 15977 |
| Surfboard-tg-mixed | 0.798 | prefer | 115 | 0.722 | 5656 |
| DeltaKronecker-all | 0.778 | prefer | 84 | 0.702 | 5773 |
| nscl5-all | 0.349 | observe | 3 | 0.667 | 2081 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 160 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5113 |
| Epodonios-all | 0.255 | observe | 0 | None | 6303 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| DeltaKronecker-all | 0.702 | 59 | 25 | 84 |
| Surfboard-tg-mixed | 0.722 | 83 | 32 | 115 |
| mheidari-all | 0.918 | 45 | 4 | 49 |
| Au1rxx-base64 | 0.971 | 713 | 21 | 734 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15977 | yes | 3.2 | 0 |
| SoliSpirit-all | 7258 | yes | 2.67 | 0 |
| Epodonios-all | 6303 | yes | 4.21 | 0 |
| DeltaKronecker-all | 5773 | yes | 3.11 | 0 |
| Surfboard-tg-mixed | 5656 | yes | 3.6 | 0 |
| 10ium-ScrapeCategorize-Vless | 5113 | yes | 1.82 | 0 |
| barry-far-vless | 4711 | yes | 1.61 | 0 |
| Surfboard-tg-vless | 4372 | yes | 2.79 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.89 | 0 |
| mahdibland-V2RayAggregator | 3935 | yes | 2.03 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 28 |
| geo | 25 |
| cn-block | 18 |
| speed | 13 |
