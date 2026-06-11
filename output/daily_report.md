# AutoNodes 每日报告

生成时间：2026-06-11 20:28:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/8 |
| 清理建议：优先/观察 | 1/35 |
| 原始节点数 | 39698 |
| 去重后节点数 | 15068 |
| TCP 可达数 | 1500 |
| 真测通过数 | 265 |
| verified 输出数 | 265 |
| global 输出数 | 275 |
| all 输出数 | 15068 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.7 |
| generate | 26.2 |
| geo | 1.2 |
| real_test | 143.0 |
| tcp | 38.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 9 | 1 | 8 | 11.1% |
| shadowsocks | 219 | 63 | 156 | 28.8% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 431 | 42 | 389 | 9.7% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 770 | 110 | 660 | 14.3% |
| vmess | 16 | 7 | 9 | 43.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 571 |
| 204:ProxyError | 339 |
| 204:TimeoutError | 86 |
| geo:status | 76 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 49 |
| geo:status | 27 |
| speed:ClientOSError | 16 |
| cn-block:ClientOSError | 16 |
| cn-block:TimeoutError | 12 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:TimeoutError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| cn-block:ProxyError | 5 |
| geo:ProxyError | 4 |
| geo:TimeoutError | 3 |
| speed:ProxyError | 2 |
| geo:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-xkgrnrnx/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-j4p99k7u/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-61n1waop/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1946 |
| ConnectionRefusedError | 422 |
| gaierror | 151 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.599 | observe | 55 | 0.6 | 74 |
| roosterkid-openproxylist-v2ray | 0.351 | observe | 15 | 0.4 | 150 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 3000 |
| mheidari-all | 0.317 | observe | 91 | 0.231 | 2000 |
| Surfboard-tg-mixed | 0.258 | observe | 757 | 0.177 | 4200 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3257 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Barabama-yudou | 0.214 | observe | 2 | 0.5 | 166 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.078 | downweight | 30 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.09 | downweight | 8 | 0.0 | 0 | 729 |
| nscl5-all | 0.104 | downweight | 7 | 0.0 | 0 | 984 |
| ninja-vless | 0.112 | downweight | 23 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4536 |
| SoliSpirit-all | 0.134 | downweight | 11 | 0.0 | 0 | 3000 |
| DeltaKronecker-all | 0.144 | downweight | 437 | 0.062 | 0 | 4660 |
| 10ium-ScrapeCategorize-Vless | 0.153 | downweight | 5 | 0.0 | 0 | 2000 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.078 | 30 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.09 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.104 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.112 | 23 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.134 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.144 | 437 | 0.062 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.153 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 5 | 5 |
| nscl5-all | 0.0 | 0 | 7 | 7 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 8 | 8 |
| SoliSpirit-all | 0.0 | 0 | 11 | 11 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 23 | 23 |
| moneyfly1-collectSub | 0.0 | 0 | 30 | 30 |
| DeltaKronecker-all | 0.062 | 27 | 410 | 437 |
| Surfboard-tg-mixed | 0.177 | 134 | 623 | 757 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.68 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.35 | 0 |
| Surfboard-tg-mixed | 4200 | yes | 1.53 | 0 |
| Surfboard-tg-vless | 3257 | yes | 1.28 | 0 |
| Epodonios-all | 3000 | yes | 2.61 | 0 |
| SoliSpirit-all | 3000 | yes | 1.55 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.33 | 0 |
| mheidari-all | 2000 | yes | 2.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.28 | 0 |
| barry-far-vless | 2000 | yes | 1.07 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| trojan | 0.097 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 996 |
| geo | 112 |
| sing-box exited 1 | 69 |
| cn-block | 33 |
| speed | 25 |
