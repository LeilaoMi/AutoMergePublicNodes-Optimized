# AutoNodes 每日报告

生成时间：2026-06-07 14:00:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/9 |
| 清理建议：优先/观察 | 0/35 |
| 原始节点数 | 40146 |
| 去重后节点数 | 15518 |
| TCP 可达数 | 1500 |
| 真测通过数 | 240 |
| verified 输出数 | 240 |
| global 输出数 | 259 |
| all 输出数 | 15518 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.5 |
| generate | 23.8 |
| geo | 1.4 |
| real_test | 136.2 |
| tcp | 40.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 7 | 14 | 33.3% |
| hysteria2 | 15 | 1 | 14 | 6.7% |
| shadowsocks | 339 | 76 | 263 | 22.4% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 265 | 29 | 236 | 10.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 830 | 118 | 712 | 14.2% |
| vmess | 19 | 9 | 10 | 47.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 541 |
| 204:ClientOSError | 424 |
| 204:TimeoutError | 93 |
| geo:status | 60 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 30 |
| speed:TimeoutError | 20 |
| cn-block:ClientOSError | 13 |
| geo:status | 13 |
| cn-block:TimeoutError | 10 |
| speed:ClientOSError | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| geo:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| speed:ProxyError | 4 |
| geo:ProxyError | 4 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ݽ5k����^�� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-gdv8omlp/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-9iwbgyp4/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1984 |
| ConnectionRefusedError | 446 |
| gaierror | 150 |
| OSError | 25 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.465 | observe | 63 | 0.46 | 93 |
| roosterkid-openproxylist-v2ray | 0.393 | observe | 16 | 0.438 | 150 |
| mheidari-all | 0.359 | observe | 84 | 0.274 | 2000 |
| snakem982 | 0.335 | observe | 22 | 0.318 | 47 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3552 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.249 | downweight | 848 | 0.169 | 4512 |
| 10ium-HighSpeed | 0.209 | observe | 0 | None | 839 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.072 | downweight | 38 | 0.0 | 0 | 1164 |
| 10ium-ScrapeCategorize-Vless | 0.109 | downweight | 32 | 0.0 | 0 | 2000 |
| nscl5-all | 0.114 | downweight | 5 | 0.0 | 0 | 1013 |
| ninja-vless | 0.12 | downweight | 16 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4612 |
| xiaoji235-airport-v2ray-all | 0.132 | downweight | 12 | 0.083 | 0 | 646 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| Epodonios-all | 0.17 | observe | 3 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.072 | 38 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.109 | 32 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.114 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.12 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.132 | 12 | 0.083 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.173 | 331 | 0.091 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.249 | 848 | 0.169 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 3 | 3 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 16 | 16 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 32 | 32 |
| moneyfly1-collectSub | 0.0 | 0 | 38 | 38 |
| xiaoji235-airport-v2ray-all | 0.083 | 1 | 11 | 12 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 4612 | yes | 1.25 | 0 |
| DeltaKronecker-all | 4578 | yes | 2.04 | 0 |
| Surfboard-tg-mixed | 4512 | yes | 1.18 | 0 |
| Surfboard-tg-vless | 3552 | yes | 1.36 | 0 |
| Epodonios-all | 3000 | yes | 2.38 | 0 |
| SoliSpirit-all | 3000 | yes | 1.75 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.2 | 0 |
| mheidari-all | 2000 | yes | 2.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.11 | 0 |
| barry-far-vless | 2000 | yes | 0.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.067 |
| tuic | 0.0 |
| shadowsocksr | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1058 |
| geo | 84 |
| sing-box exited 1 | 57 |
| speed | 33 |
| cn-block | 28 |
