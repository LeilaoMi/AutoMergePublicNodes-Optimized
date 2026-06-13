# AutoNodes 每日报告

生成时间：2026-06-13 09:22:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 40116 |
| 去重后节点数 | 15386 |
| TCP 可达数 | 1500 |
| 真测通过数 | 268 |
| verified 输出数 | 268 |
| global 输出数 | 283 |
| all 输出数 | 15386 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.7 |
| generate | 24.9 |
| geo | 1.2 |
| real_test | 160.8 |
| tcp | 36.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 13 | 1 | 12 | 7.7% |
| shadowsocks | 365 | 79 | 286 | 21.6% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 20 | 13 | 7 | 65.0% |
| trojan | 136 | 17 | 119 | 12.5% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 896 | 108 | 788 | 12.1% |
| vmess | 17 | 8 | 9 | 47.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 519 |
| 204:ClientOSError | 310 |
| 204:TimeoutError | 97 |
| geo:status | 72 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 58 |
| geo:status | 57 |
| speed:ClientOSError | 44 |
| speed:TimeoutError | 22 |
| cn-block:TimeoutError | 19 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 6 |
| geo:ProxyError | 3 |
| geo:TimeoutError | 2 |
| geo:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-z55ia5qo/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-y5mjcgur/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-38vlccbv/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1928 |
| ConnectionRefusedError | 429 |
| gaierror | 165 |
| OSError | 33 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | prefer | 46 | 0.935 | 52 |
| Au1rxx-base64 | 0.527 | observe | 84 | 0.524 | 106 |
| roosterkid-openproxylist-v2ray | 0.45 | observe | 25 | 0.44 | 150 |
| Surfboard-tg-mixed | 0.257 | observe | 653 | 0.176 | 4171 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3114 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.226 | downweight | 94 | 0.138 | 2000 |
| 10ium-HighSpeed | 0.209 | observe | 0 | None | 839 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.072 | downweight | 37 | 0.0 | 0 | 1164 |
| nscl5-all | 0.101 | downweight | 10 | 0.0 | 0 | 1119 |
| ninja-vless | 0.12 | downweight | 16 | 0.0 | 0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.125 | downweight | 15 | 0.067 | 0 | 666 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4566 |
| Barabama-yudou | 0.137 | downweight | 21 | 0.095 | 0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.141 | downweight | 8 | 0.0 | 0 | 2000 |
| SoliSpirit-all | 0.148 | downweight | 6 | 0.0 | 0 | 3000 |
| DeltaKronecker-all | 0.165 | downweight | 471 | 0.083 | 0 | 4955 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.072 | 37 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.101 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.12 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.125 | 15 | 0.067 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.137 | 21 | 0.095 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.141 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.148 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.165 | 471 | 0.083 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mheidari-all | 0.226 | 94 | 0.138 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 6 | 6 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 8 | 8 |
| nscl5-all | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| ninja-vless | 0.0 | 0 | 16 | 16 |
| moneyfly1-collectSub | 0.0 | 0 | 37 | 37 |
| xiaoji235-airport-v2ray-all | 0.067 | 1 | 14 | 15 |
| DeltaKronecker-all | 0.083 | 39 | 432 | 471 |
| Barabama-yudou | 0.095 | 2 | 19 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4955 | yes | 2.32 | 0 |
| mahdibland-V2RayAggregator | 4566 | yes | 1.26 | 0 |
| Surfboard-tg-mixed | 4171 | yes | 1.55 | 0 |
| Surfboard-tg-vless | 3114 | yes | 1.64 | 0 |
| Epodonios-all | 3000 | yes | 1.45 | 0 |
| SoliSpirit-all | 3000 | yes | 1.01 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.86 | 0 |
| mheidari-all | 2000 | yes | 2.43 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.77 | 0 |
| barry-far-vless | 2000 | yes | 1.38 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.077 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 926 |
| geo | 136 |
| sing-box exited 1 | 77 |
| speed | 67 |
| cn-block | 26 |
