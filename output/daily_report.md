# AutoNodes 每日报告

生成时间：2026-06-12 00:22:20

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
| 真测通过数 | 410 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15022 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.7 |
| generate | 24.2 |
| geo | 1.2 |
| real_test | 152.9 |
| tcp | 35.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 5 | 1 | 4 | 20.0% |
| shadowsocks | 357 | 103 | 254 | 28.9% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 29 | 26 | 3 | 89.7% |
| trojan | 333 | 63 | 270 | 18.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 707 | 168 | 539 | 23.8% |
| vmess | 16 | 7 | 9 | 43.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 486 |
| 204:ProxyError | 336 |
| 204:TimeoutError | 67 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 53 |
| geo:status | 34 |
| speed:ClientOSError | 33 |
| speed:TimeoutError | 33 |
| cn-block:TimeoutError | 12 |
| cn-block:ClientOSError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 4 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-id8rz1gf/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-424qnwnc/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-hj63zuks/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ݽ5k����^�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٽv��{��u�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1793 |
| ConnectionRefusedError | 427 |
| gaierror | 188 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.623 | observe | 69 | 0.623 | 88 |
| Surfboard-tg-mixed | 0.405 | observe | 719 | 0.324 | 4225 |
| mheidari-all | 0.358 | observe | 95 | 0.274 | 2000 |
| roosterkid-openproxylist-v2ray | 0.306 | observe | 28 | 0.286 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| DeltaKronecker-all | 0.21 | downweight | 437 | 0.128 | 4660 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.077 | downweight | 16 | 0.0 | 0 | 729 |
| moneyfly1-collectSub | 0.096 | downweight | 15 | 0.0 | 0 | 1164 |
| nscl5-all | 0.113 | downweight | 5 | 0.0 | 0 | 984 |
| 10ium-ScrapeCategorize-Vless | 0.127 | downweight | 18 | 0.0 | 0 | 2000 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 24 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| ninja-vless | 0.13 | downweight | 9 | 0.0 | 0 | 1791 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4536 |
| Barabama-yudou | 0.137 | downweight | 21 | 0.095 | 0 | 166 |
| SoliSpirit-all | 0.138 | downweight | 9 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.077 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.096 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.113 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.127 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.13 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.137 | 21 | 0.095 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.21 | 437 | 0.128 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| ninja-vless | 0.0 | 0 | 9 | 9 |
| SoliSpirit-all | 0.0 | 0 | 9 | 9 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| moneyfly1-collectSub | 0.0 | 0 | 15 | 15 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 16 | 16 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 18 | 18 |
| Barabama-yudou | 0.095 | 2 | 19 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.63 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.19 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 1.64 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.39 | 0 |
| Epodonios-all | 3000 | yes | 2.57 | 0 |
| SoliSpirit-all | 3000 | yes | 1.77 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.5 | 0 |
| mheidari-all | 2000 | yes | 2.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.5 | 0 |
| barry-far-vless | 2000 | yes | 1.14 | 0 |

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
| 204 | 889 |
| sing-box exited 1 | 78 |
| speed | 66 |
| geo | 34 |
| cn-block | 23 |
