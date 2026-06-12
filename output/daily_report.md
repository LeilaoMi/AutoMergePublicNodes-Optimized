# AutoNodes 每日报告

生成时间：2026-06-12 00:17:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/9 |
| 清理建议：优先/观察 | 1/34 |
| 原始节点数 | 39955 |
| 去重后节点数 | 15022 |
| TCP 可达数 | 1500 |
| 真测通过数 | 390 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15022 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.7 |
| generate | 26.3 |
| geo | 1.3 |
| real_test | 183.8 |
| tcp | 36.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 5 | 1 | 4 | 20.0% |
| shadowsocks | 351 | 102 | 249 | 29.1% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 29 | 25 | 4 | 86.2% |
| trojan | 131 | 45 | 86 | 34.4% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 915 | 168 | 747 | 18.4% |
| vmess | 16 | 7 | 9 | 43.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 335 |
| 204:ClientOSError | 334 |
| speed:TimeoutError | 133 |
| speed:ClientOSError | 110 |
| 204:TimeoutError | 61 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 53 |
| geo:status | 35 |
| cn-block:ClientOSError | 12 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:TimeoutError | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 4 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-agl912a5/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-scrd0ol4/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-_wu3tnrn/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1854 |
| ConnectionRefusedError | 421 |
| gaierror | 168 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.634 | observe | 71 | 0.634 | 88 |
| Surfboard-tg-mixed | 0.405 | observe | 691 | 0.324 | 4225 |
| mheidari-all | 0.364 | observe | 93 | 0.28 | 2000 |
| Epodonios-all | 0.287 | observe | 2 | 0.5 | 3000 |
| roosterkid-openproxylist-v2ray | 0.273 | observe | 28 | 0.25 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 501 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.072 | downweight | 38 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.102 | downweight | 5 | 0.0 | 0 | 729 |
| nscl5-all | 0.104 | downweight | 7 | 0.0 | 0 | 984 |
| Barabama-we | 0.105 | observe | 2 | 0.0 | 0 | 23 |
| ninja-vless | 0.107 | downweight | 26 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4536 |
| Barabama-yudou | 0.137 | downweight | 21 | 0.095 | 0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.141 | downweight | 8 | 0.0 | 0 | 2000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.072 | 38 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.102 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.104 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.107 | 26 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.137 | 21 | 0.095 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.141 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.18 | 436 | 0.099 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| Barabama-we | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 5 | 5 |
| nscl5-all | 0.0 | 0 | 7 | 7 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 8 | 8 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 26 | 26 |
| moneyfly1-collectSub | 0.0 | 0 | 38 | 38 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.18 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.55 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 1.38 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.91 | 0 |
| Epodonios-all | 3000 | yes | 2.44 | 0 |
| SoliSpirit-all | 3000 | yes | 1.88 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.44 | 0 |
| mheidari-all | 2000 | yes | 2.87 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.59 | 0 |
| barry-far-vless | 2000 | yes | 1.25 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 730 |
| speed | 243 |
| sing-box exited 1 | 77 |
| geo | 38 |
| cn-block | 22 |
