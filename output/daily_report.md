# AutoNodes 每日报告

生成时间：2026-06-16 11:18:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 43459 |
| 去重后节点数 | 18069 |
| TCP 可达数 | 1500 |
| 真测通过数 | 244 |
| verified 输出数 | 244 |
| global 输出数 | 259 |
| all 输出数 | 18069 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.5 |
| generate | 39.5 |
| geo | 1.2 |
| real_test | 181.1 |
| tcp | 38.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 17 | 1 | 16 | 5.9% |
| shadowsocks | 266 | 63 | 203 | 23.7% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 160 | 22 | 138 | 13.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 986 | 110 | 876 | 11.2% |
| vmess | 15 | 5 | 10 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 531 |
| 204:ClientOSError | 351 |
| 204:TimeoutError | 92 |
| geo:status | 73 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 59 |
| geo:status | 40 |
| cn-block:TimeoutError | 32 |
| speed:ClientOSError | 23 |
| speed:TimeoutError | 12 |
| cn-block:ClientOSError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 6 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-62277mxa/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-v4l8h2iy/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ismw_7lq/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �5m�5�����6��ѧ~� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �^ߧ������ | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1799 |
| ConnectionRefusedError | 447 |
| gaierror | 204 |
| OSError | 27 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.898 | prefer | 46 | 0.913 | 52 |
| Au1rxx-base64 | 0.554 | observe | 78 | 0.551 | 107 |
| roosterkid-openproxylist-v2ray | 0.458 | observe | 29 | 0.448 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3345 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.215 | downweight | 840 | 0.135 | 4339 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 494 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.075 | downweight | 33 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.077 | downweight | 17 | 0.0 | 0 | 729 |
| Barabama-yudou | 0.098 | downweight | 20 | 0.05 | 0 | 166 |
| nscl5-all | 0.109 | downweight | 6 | 0.0 | 0 | 1017 |
| ninja-vless | 0.118 | downweight | 18 | 0.0 | 0 | 1791 |
| Barabama-we | 0.128 | observe | 1 | 0.0 | 0 | 23 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4484 |
| 10ium-ScrapeCategorize-Vless | 0.138 | downweight | 9 | 0.0 | 0 | 2000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.075 | 33 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.077 | 17 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.098 | 20 | 0.05 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.109 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.166 | 371 | 0.084 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.215 | 840 | 0.135 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| Barabama-we | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 6 | 6 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 9 | 9 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 17 | 17 |
| ninja-vless | 0.0 | 0 | 18 | 18 |
| moneyfly1-collectSub | 0.0 | 0 | 33 | 33 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 8110 | yes | 3.4 | 0 |
| mahdibland-V2RayAggregator | 4484 | yes | 1.07 | 0 |
| Surfboard-tg-mixed | 4339 | yes | 1.7 | 0 |
| Surfboard-tg-vless | 3345 | yes | 1.92 | 0 |
| Epodonios-all | 3000 | yes | 3.23 | 0 |
| SoliSpirit-all | 3000 | yes | 1.97 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.69 | 0 |
| mheidari-all | 2000 | yes | 3.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.59 | 0 |
| barry-far-vless | 2000 | yes | 1.41 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.059 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 974 |
| geo | 118 |
| sing-box exited 1 | 84 |
| cn-block | 45 |
| speed | 35 |
