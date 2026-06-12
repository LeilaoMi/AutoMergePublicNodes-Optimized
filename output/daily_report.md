# AutoNodes 每日报告

生成时间：2026-06-12 20:16:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/13 |
| 清理建议：优先/观察 | 1/30 |
| 原始节点数 | 40347 |
| 去重后节点数 | 15278 |
| TCP 可达数 | 1500 |
| 真测通过数 | 258 |
| verified 输出数 | 258 |
| global 输出数 | 264 |
| all 输出数 | 15278 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.6 |
| generate | 23.6 |
| geo | 1.2 |
| real_test | 153.2 |
| tcp | 37.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 12 | 1 | 11 | 8.3% |
| shadowsocks | 350 | 74 | 276 | 21.1% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 135 | 20 | 115 | 14.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 931 | 116 | 815 | 12.5% |
| vmess | 17 | 5 | 12 | 29.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 448 |
| 204:ClientOSError | 405 |
| 204:TimeoutError | 129 |
| geo:status | 73 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 62 |
| geo:status | 53 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:TimeoutError | 6 |
| speed:ClientOSError | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 4 |
| geo:ProxyError | 4 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-j738h3g2/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-3z3q97_4/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-jvjsmtz5/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1870 |
| ConnectionRefusedError | 451 |
| gaierror | 173 |
| OSError | 34 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.917 | prefer | 45 | 0.933 | 52 |
| Au1rxx-base64 | 0.566 | observe | 71 | 0.563 | 108 |
| roosterkid-openproxylist-v2ray | 0.338 | observe | 17 | 0.353 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.242 | downweight | 78 | 0.154 | 2000 |
| Surfboard-tg-mixed | 0.24 | downweight | 768 | 0.159 | 4374 |
| Epodonios-all | 0.223 | downweight | 47 | 0.128 | 3000 |
| Surfboard-tg-vless | 0.199 | downweight | 40 | 0.1 | 3279 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 484 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.049 | downweight | 64 | 0.0 | 0 | 839 |
| moneyfly1-collectSub | 0.073 | downweight | 36 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.089 | downweight | 9 | 0.0 | 0 | 774 |
| ermaozi | 0.091 | observe | 3 | 0.0 | 0 | 29 |
| nscl5-all | 0.108 | downweight | 8 | 0.0 | 0 | 1178 |
| Barabama-yudou | 0.11 | observe | 2 | 0.0 | 0 | 166 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.129 | downweight | 15 | 0.0 | 0 | 4561 |
| ninja-vless | 0.133 | downweight | 8 | 0.0 | 0 | 1791 |
| SoliSpirit-all | 0.134 | downweight | 11 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | 10ium-HighSpeed | 0.049 | 64 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.073 | 36 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.089 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.108 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.133 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.134 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.136 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.18 | 267 | 0.097 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-vless | 0.199 | 40 | 0.1 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 2 | 2 |
| ermaozi | 0.0 | 0 | 3 | 3 |
| ninja-vless | 0.0 | 0 | 8 | 8 |
| nscl5-all | 0.0 | 0 | 8 | 8 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 9 | 9 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 10 | 10 |
| SoliSpirit-all | 0.0 | 0 | 11 | 11 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 15 | 15 |
| moneyfly1-collectSub | 0.0 | 0 | 36 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4706 | yes | 2.54 | 0 |
| mahdibland-V2RayAggregator | 4561 | yes | 1.53 | 0 |
| Surfboard-tg-mixed | 4374 | yes | 1.32 | 0 |
| Surfboard-tg-vless | 3279 | yes | 0.82 | 0 |
| Epodonios-all | 3000 | yes | 1.47 | 0 |
| SoliSpirit-all | 3000 | yes | 1.57 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.28 | 0 |
| mheidari-all | 2000 | yes | 2.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.4 | 0 |
| barry-far-vless | 2000 | yes | 1.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.083 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 982 |
| geo | 135 |
| sing-box exited 1 | 85 |
| cn-block | 28 |
| speed | 12 |
