# AutoNodes 每日报告

生成时间：2026-08-18 06:59:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 91021 |
| 去重后节点数 | 23861 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1271 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23861 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 36.7 |
| geo | 1.0 |
| probe | 77.5 |
| real_test | 257.0 |
| tcp | 36.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 23 | 19 | 4 | 82.6% |
| shadowsocks | 169 | 152 | 17 | 89.9% |
| socks | 7 | 4 | 3 | 57.1% |
| trojan | 864 | 844 | 20 | 97.7% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 441 | 124 | 317 | 28.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 111 |
| speed:TimeoutError | 93 |
| geo:ClientOSError | 61 |
| 204:TimeoutError | 29 |
| speed:ClientOSError | 28 |
| cn-block:TimeoutError | 24 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| 204:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4345 |
| ConnectionRefusedError | 893 |
| gaierror | 408 |
| OSError | 222 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.934 | prefer | 135 | 0.859 | 6138 |
| Au1rxx-base64 | 0.896 | prefer | 814 | 0.84 | 1408 |
| mheidari-all | 0.705 | prefer | 539 | 0.625 | 21284 |
| nscl5-all | 0.4 | observe | 4 | 0.75 | 2992 |
| DeltaKronecker-all | 0.344 | observe | 12 | 0.333 | 5725 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5068 |
| Epodonios-all | 0.255 | observe | 0 | None | 6730 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3986 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6856 |

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
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.333 | 4 | 8 | 12 |
| mheidari-all | 0.625 | 337 | 202 | 539 |
| nscl5-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.84 | 684 | 130 | 814 |
| Surfboard-tg-mixed | 0.859 | 116 | 19 | 135 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21284 | yes | 3.5 | 0 |
| SoliSpirit-all | 6856 | yes | 1.35 | 0 |
| Epodonios-all | 6730 | yes | 1.84 | 0 |
| xiaoji235-airport-v2ray-all | 6329 | yes | 1.01 | 0 |
| Surfboard-tg-mixed | 6138 | yes | 2.27 | 0 |
| DeltaKronecker-all | 5725 | yes | 3.24 | 0 |
| barry-far-vless | 5074 | yes | 1.19 | 0 |
| 10ium-ScrapeCategorize-Vless | 5068 | yes | 0.79 | 0 |
| Surfboard-tg-vless | 4777 | yes | 2.11 | 0 |
| mahdibland-V2RayAggregator | 4045 | yes | 0.79 | 0 |

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
| geo | 172 |
| speed | 123 |
| 204 | 36 |
| cn-block | 31 |
