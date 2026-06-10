# AutoNodes 每日报告

生成时间：2026-06-10 10:08:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 43/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 39564 |
| 去重后节点数 | 15261 |
| TCP 可达数 | 1500 |
| 真测通过数 | 306 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15261 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.7 |
| generate | 23.5 |
| geo | 1.2 |
| real_test | 169.5 |
| tcp | 33.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 45 | 43 | 2 | 95.6% |
| hysteria2 | 9 | 1 | 8 | 11.1% |
| shadowsocks | 365 | 96 | 269 | 26.3% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 170 | 27 | 143 | 15.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 887 | 135 | 752 | 15.2% |
| vmess | 12 | 3 | 9 | 25.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 459 |
| 204:ProxyError | 424 |
| 204:TimeoutError | 134 |
| geo:status | 49 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 36 |
| cn-block:TimeoutError | 22 |
| geo:status | 19 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 8 |
| speed:TimeoutError | 7 |
| speed:ClientOSError | 6 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-tdjcut5_/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-orzk6mdn/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-telbw497/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1538 |
| ConnectionRefusedError | 428 |
| gaierror | 231 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.833 | prefer | 51 | 0.843 | 61 |
| Au1rxx-base64 | 0.6 | observe | 55 | 0.6 | 83 |
| roosterkid-openproxylist-v2ray | 0.4 | observe | 15 | 0.467 | 150 |
| mheidari-all | 0.344 | observe | 108 | 0.259 | 2000 |
| Surfboard-tg-mixed | 0.267 | observe | 905 | 0.187 | 4139 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3266 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Epodonios-all | 0.216 | downweight | 6 | 0.167 | 3000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| chromego_merge | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.08 | downweight | 5 | 0.0 | 0 | 166 |
| xiaoji235-airport-v2ray-all | 0.086 | downweight | 9 | 0.0 | 0 | 689 |
| moneyfly1-collectSub | 0.087 | downweight | 23 | 0.0 | 0 | 1164 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| ninja-vless | 0.128 | downweight | 10 | 0.0 | 0 | 1791 |
| mahdibland-V2RayAggregator | 0.129 | downweight | 15 | 0.0 | 0 | 4516 |
| 10ium-ScrapeCategorize-Vless | 0.138 | downweight | 9 | 0.0 | 0 | 2000 |
| SoliSpirit-all | 0.144 | downweight | 7 | 0.0 | 0 | 3000 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | Barabama-yudou | 0.08 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.086 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.087 | 23 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.128 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.144 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.168 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.171 | 273 | 0.088 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Epodonios-all | 0.216 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 5 | 5 |
| SoliSpirit-all | 0.0 | 0 | 7 | 7 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 9 | 9 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 9 | 9 |
| ninja-vless | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 15 | 15 |
| moneyfly1-collectSub | 0.0 | 0 | 23 | 23 |
| DeltaKronecker-all | 0.088 | 24 | 249 | 273 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4616 | yes | 2.56 | 0 |
| mahdibland-V2RayAggregator | 4516 | yes | 1.14 | 0 |
| Surfboard-tg-mixed | 4139 | yes | 1.42 | 0 |
| Surfboard-tg-vless | 3266 | yes | 1.51 | 0 |
| Epodonios-all | 3000 | yes | 2.48 | 0 |
| SoliSpirit-all | 3000 | yes | 1.58 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.36 | 0 |
| mheidari-all | 2000 | yes | 2.31 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.18 | 0 |
| barry-far-vless | 2000 | yes | 1.3 | 0 |

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
| 204 | 1017 |
| geo | 72 |
| sing-box exited 1 | 57 |
| cn-block | 33 |
| speed | 15 |
