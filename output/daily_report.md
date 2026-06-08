# AutoNodes 每日报告

生成时间：2026-06-08 20:24:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/12 |
| 清理建议：优先/观察 | 0/32 |
| 原始节点数 | 39075 |
| 去重后节点数 | 15611 |
| TCP 可达数 | 1500 |
| 真测通过数 | 249 |
| verified 输出数 | 249 |
| global 输出数 | 258 |
| all 输出数 | 15611 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.5 |
| generate | 25.1 |
| geo | 1.2 |
| real_test | 151.1 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 35 | 29 | 6 | 82.9% |
| hysteria2 | 13 | 1 | 12 | 7.7% |
| shadowsocks | 347 | 75 | 272 | 21.6% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 256 | 25 | 231 | 9.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 816 | 107 | 709 | 13.1% |
| vmess | 18 | 9 | 9 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 467 |
| 204:ClientOSError | 444 |
| 204:TimeoutError | 120 |
| geo:status | 93 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 43 |
| speed:ClientOSError | 14 |
| geo:status | 14 |
| speed:TimeoutError | 12 |
| cn-block:ClientOSError | 9 |
| cn-block:TimeoutError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 2 |
| geo:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-n92io6bo/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-nq5jhf_q/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-i5vovutb/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���s�F�������>�m�s� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2070 |
| ConnectionRefusedError | 415 |
| gaierror | 141 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.676 | observe | 44 | 0.682 | 62 |
| Au1rxx-base64 | 0.531 | observe | 51 | 0.529 | 69 |
| roosterkid-openproxylist-v2ray | 0.521 | observe | 13 | 0.692 | 150 |
| mheidari-all | 0.327 | observe | 95 | 0.242 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.242 | downweight | 701 | 0.161 | 4007 |
| Surfboard-tg-vless | 0.218 | downweight | 92 | 0.13 | 3035 |
| Barabama-yudou | 0.214 | observe | 2 | 0.5 | 166 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.077 | downweight | 31 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.08 | downweight | 10 | 0.0 | 0 | 584 |
| 10ium-HighSpeed | 0.092 | downweight | 9 | 0.0 | 0 | 839 |
| nscl5-all | 0.106 | downweight | 6 | 0.0 | 0 | 957 |
| ninja-vless | 0.115 | downweight | 21 | 0.0 | 0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.117 | downweight | 25 | 0.0 | 0 | 2000 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| Epodonios-all | 0.128 | downweight | 16 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.129 | downweight | 15 | 0.0 | 0 | 4521 |
| chromego_merge | 0.13 | observe | 1 | 0.0 | 0 | 53 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.077 | 31 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.08 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.092 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.106 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.115 | 21 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.117 | 25 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Epodonios-all | 0.128 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.136 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.178 | 356 | 0.096 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| ts-sf | 0.0 | 0 | 1 | 1 |
| chromego_merge | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 6 | 6 |
| 10ium-HighSpeed | 0.0 | 0 | 9 | 9 |
| SoliSpirit-all | 0.0 | 0 | 10 | 10 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 15 | 15 |
| Epodonios-all | 0.0 | 0 | 16 | 16 |
| ninja-vless | 0.0 | 0 | 21 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4760 | yes | 2.48 | 0 |
| mahdibland-V2RayAggregator | 4521 | yes | 0.57 | 0 |
| Surfboard-tg-mixed | 4007 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 3035 | yes | 1.17 | 0 |
| Epodonios-all | 3000 | yes | 2.39 | 0 |
| SoliSpirit-all | 3000 | yes | 1.96 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.28 | 0 |
| mheidari-all | 2000 | yes | 2.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.34 | 0 |
| barry-far-vless | 2000 | yes | 1.22 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| trojan | 0.098 |
| hysteria2 | 0.077 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1031 |
| geo | 110 |
| sing-box exited 1 | 64 |
| speed | 27 |
| cn-block | 19 |
