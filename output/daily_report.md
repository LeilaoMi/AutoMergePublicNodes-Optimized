# AutoNodes 每日报告

生成时间：2026-06-17 04:22:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/9 |
| 清理建议：优先/观察 | 1/34 |
| 原始节点数 | 43710 |
| 去重后节点数 | 18206 |
| TCP 可达数 | 1500 |
| 真测通过数 | 359 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 18206 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.4 |
| generate | 38.3 |
| geo | 1.2 |
| real_test | 215.0 |
| tcp | 39.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 13 | 1 | 12 | 7.7% |
| shadowsocks | 365 | 78 | 287 | 21.4% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 7 | 1 | 6 | 14.3% |
| trojan | 202 | 46 | 156 | 22.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 846 | 186 | 660 | 22.0% |
| vmess | 14 | 5 | 9 | 35.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 415 |
| 204:ProxyError | 375 |
| geo:status | 71 |
| 204:TimeoutError | 71 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 63 |
| speed:ClientOSError | 33 |
| speed:TimeoutError | 29 |
| cn-block:TimeoutError | 28 |
| geo:status | 18 |
| cn-block:ClientOSError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 2 |
| geo:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-96x91d8z/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| cn-block:ProxyError | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-wzqff0zo/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-es2hvdmh/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �5m�5�����6��ѧ~� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1914 |
| ConnectionRefusedError | 476 |
| gaierror | 201 |
| OSError | 35 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | prefer | 46 | 0.935 | 52 |
| roosterkid-openproxylist-v2ray | 0.627 | observe | 27 | 0.63 | 150 |
| Au1rxx-base64 | 0.516 | observe | 88 | 0.511 | 124 |
| Surfboard-tg-mixed | 0.325 | observe | 828 | 0.244 | 4546 |
| mheidari-all | 0.271 | observe | 92 | 0.185 | 2000 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3522 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| chromego_merge | 0.222 | downweight | 5 | 0.4 | 51 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| mfuu-v2ray | 0.07 | downweight | 8 | 0.0 | 0 | 233 |
| xiaoji235-airport-v2ray-all | 0.08 | downweight | 10 | 0.0 | 0 | 588 |
| moneyfly1-collectSub | 0.09 | downweight | 21 | 0.0 | 0 | 1164 |
| ts-sf | 0.091 | observe | 3 | 0.0 | 0 | 45 |
| 10ium-HighSpeed | 0.114 | observe | 4 | 0.0 | 0 | 839 |
| ninja-vless | 0.118 | downweight | 18 | 0.0 | 0 | 1791 |
| nscl5-all | 0.119 | observe | 4 | 0.0 | 0 | 967 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 20 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.128 | downweight | 17 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | mfuu-v2ray | 0.07 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.08 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.09 | 21 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.128 | 17 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.188 | 293 | 0.106 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | chromego_merge | 0.222 | 5 | 0.4 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| Au1rxx-clash | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| ts-sf | 0.0 | 0 | 3 | 3 |
| nscl5-all | 0.0 | 0 | 4 | 4 |
| 10ium-HighSpeed | 0.0 | 0 | 4 | 4 |
| mfuu-v2ray | 0.0 | 0 | 8 | 8 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 10 | 10 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 13 | 13 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 8110 | yes | 3.31 | 0 |
| Surfboard-tg-mixed | 4546 | yes | 1.78 | 0 |
| mahdibland-V2RayAggregator | 4528 | yes | 1.4 | 0 |
| Surfboard-tg-vless | 3522 | yes | 1.65 | 0 |
| Epodonios-all | 3000 | yes | 3.12 | 0 |
| SoliSpirit-all | 3000 | yes | 1.63 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.26 | 0 |
| mheidari-all | 2000 | yes | 2.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.33 | 0 |
| barry-far-vless | 2000 | yes | 1.19 | 0 |

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
| 204 | 861 |
| geo | 92 |
| sing-box exited 1 | 88 |
| speed | 62 |
| cn-block | 38 |
