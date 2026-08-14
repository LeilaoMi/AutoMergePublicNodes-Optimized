# AutoNodes 每日报告

生成时间：2026-08-14 13:22:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 81447 |
| 去重后节点数 | 23220 |
| TCP 可达数 | 3000 |
| 真测通过数 | 841 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23220 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 36.0 |
| geo | 0.8 |
| probe | 64.0 |
| real_test | 159.3 |
| tcp | 34.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 16 | 15 | 1 | 93.8% |
| shadowsocks | 138 | 129 | 9 | 93.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 351 | 342 | 9 | 97.4% |
| vless | 289 | 227 | 62 | 78.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 20 |
| speed:ClientOSError | 15 |
| geo:TimeoutError | 14 |
| cn-block:TimeoutError | 8 |
| speed:TimeoutError | 7 |
| 204:ProxyError | 6 |
| geo:ClientOSError | 5 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:40102: bind: address already in use | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4335 |
| ConnectionRefusedError | 811 |
| gaierror | 407 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 652 | 0.939 | 1959 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.804 | prefer | 103 | 0.728 | 5728 |
| DeltaKronecker-all | 0.719 | prefer | 34 | 0.647 | 5969 |
| mheidari-all | 0.446 | observe | 5 | 0.8 | 17030 |
| nscl5-all | 0.326 | observe | 1 | 1.0 | 1768 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5157 |
| Epodonios-all | 0.255 | observe | 0 | None | 6515 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7682 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.647 | 22 | 12 | 34 |
| Surfboard-tg-mixed | 0.728 | 75 | 28 | 103 |
| mheidari-all | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.939 | 612 | 40 | 652 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17030 | yes | 3.65 | 0 |
| SoliSpirit-all | 7682 | yes | 4.02 | 0 |
| Epodonios-all | 6515 | yes | 3.87 | 0 |
| DeltaKronecker-all | 5969 | yes | 3.98 | 0 |
| Surfboard-tg-mixed | 5728 | yes | 0.27 | 0 |
| mahdibland-V2RayAggregator | 5332 | yes | 2.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 5157 | yes | 2.59 | 0 |
| barry-far-vless | 4931 | yes | 0.73 | 0 |
| Surfboard-tg-vless | 4474 | yes | 2.67 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.84 | 0 |

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
| 204 | 27 |
| speed | 22 |
| geo | 19 |
| cn-block | 13 |
| sing-box exited 1 | 1 |
