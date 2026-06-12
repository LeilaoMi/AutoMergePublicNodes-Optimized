# AutoNodes 每日报告

生成时间：2026-06-12 10:20:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 40228 |
| 去重后节点数 | 15001 |
| TCP 可达数 | 1500 |
| 真测通过数 | 272 |
| verified 输出数 | 272 |
| global 输出数 | 286 |
| all 输出数 | 15001 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.8 |
| generate | 27.1 |
| geo | 1.2 |
| real_test | 150.1 |
| tcp | 34.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 13 | 1 | 12 | 7.7% |
| shadowsocks | 360 | 87 | 273 | 24.2% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 7 | 1 | 6 | 14.3% |
| trojan | 153 | 24 | 129 | 15.7% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 899 | 111 | 788 | 12.3% |
| vmess | 15 | 6 | 9 | 40.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 488 |
| 204:ClientOSError | 379 |
| 204:TimeoutError | 112 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 57 |
| speed:ClientOSError | 43 |
| geo:status | 41 |
| geo:status | 30 |
| cn-block:TimeoutError | 19 |
| speed:TimeoutError | 14 |
| cn-block:ClientOSError | 13 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| geo:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |
| geo:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-sxt7qr5q/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-w6g8htcs/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-gvovyhes/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1741 |
| ConnectionRefusedError | 440 |
| gaierror | 171 |
| OSError | 33 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.531 | observe | 74 | 0.527 | 106 |
| mheidari-all | 0.28 | observe | 93 | 0.194 | 2000 |
| Surfboard-tg-mixed | 0.26 | observe | 726 | 0.179 | 4171 |
| roosterkid-openproxylist-v2ray | 0.256 | observe | 22 | 0.227 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3165 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 494 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 476 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.085 | downweight | 11 | 0.0 | 0 | 774 |
| moneyfly1-collectSub | 0.085 | downweight | 24 | 0.0 | 0 | 1164 |
| 10ium-HighSpeed | 0.095 | downweight | 8 | 0.0 | 0 | 839 |
| ninja-vless | 0.118 | downweight | 19 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4561 |
| 10ium-ScrapeCategorize-Vless | 0.133 | downweight | 12 | 0.0 | 0 | 2000 |
| SoliSpirit-all | 0.144 | downweight | 7 | 0.0 | 0 | 3000 |
| nscl5-all | 0.16 | downweight | 10 | 0.1 | 0 | 1178 |
| DeltaKronecker-all | 0.166 | downweight | 419 | 0.084 | 0 | 4706 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.085 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.085 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.095 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.133 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.144 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.16 | 10 | 0.1 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.166 | 419 | 0.084 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | barry-far-vless | 0.181 | 14 | 0.071 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 7 | 7 |
| 10ium-HighSpeed | 0.0 | 0 | 8 | 8 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 11 | 11 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 12 | 12 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 19 | 19 |
| moneyfly1-collectSub | 0.0 | 0 | 24 | 24 |
| barry-far-vless | 0.071 | 1 | 13 | 14 |
| DeltaKronecker-all | 0.084 | 35 | 384 | 419 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4706 | yes | 2.66 | 0 |
| mahdibland-V2RayAggregator | 4561 | yes | 1.43 | 0 |
| Surfboard-tg-mixed | 4171 | yes | 1.78 | 0 |
| Surfboard-tg-vless | 3165 | yes | 1.57 | 0 |
| Epodonios-all | 3000 | yes | 1.37 | 0 |
| SoliSpirit-all | 3000 | yes | 1.71 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.55 | 0 |
| mheidari-all | 2000 | yes | 2.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.46 | 0 |
| barry-far-vless | 2000 | yes | 1.29 | 0 |

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
| 204 | 979 |
| sing-box exited 1 | 79 |
| geo | 78 |
| speed | 57 |
| cn-block | 35 |
