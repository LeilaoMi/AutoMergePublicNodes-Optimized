# AutoNodes 每日报告

生成时间：2026-08-18 18:51:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 93066 |
| 去重后节点数 | 24084 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1197 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24084 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 39.8 |
| geo | 1.0 |
| probe | 72.6 |
| real_test | 257.4 |
| tcp | 36.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 102 | 90 | 12 | 88.2% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 823 | 817 | 6 | 99.3% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 218 | 148 | 70 | 67.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 40 |
| speed:TimeoutError | 14 |
| 204:TimeoutError | 10 |
| cn-block:TimeoutError | 9 |
| geo:TimeoutError | 6 |
| speed:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4759 |
| ConnectionRefusedError | 917 |
| gaierror | 312 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 755 | 0.976 | 1643 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.997 | prefer | 34 | 0.941 | 6301 |
| mheidari-all | 0.889 | prefer | 365 | 0.811 | 22150 |
| nscl5-all | 0.438 | observe | 3 | 1.0 | 2992 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 5725 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5068 |
| Epodonios-all | 0.255 | observe | 0 | None | 6927 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.811 | 296 | 69 | 365 |
| Surfboard-tg-mixed | 0.941 | 32 | 2 | 34 |
| Au1rxx-base64 | 0.976 | 737 | 18 | 755 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22150 | yes | 5.31 | 0 |
| SoliSpirit-all | 7150 | yes | 3.94 | 0 |
| Epodonios-all | 6927 | yes | 2.05 | 0 |
| xiaoji235-airport-v2ray-all | 6329 | yes | 1.53 | 0 |
| Surfboard-tg-mixed | 6301 | yes | 4.69 | 0 |
| DeltaKronecker-all | 5725 | yes | 5.36 | 0 |
| barry-far-vless | 5149 | yes | 2.0 | 0 |
| 10ium-ScrapeCategorize-Vless | 5068 | yes | 3.27 | 0 |
| Surfboard-tg-vless | 4855 | yes | 3.6 | 0 |
| mahdibland-V2RayAggregator | 4035 | yes | 2.95 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 47 |
| speed | 18 |
| cn-block | 14 |
| 204 | 13 |
