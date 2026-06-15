# AutoNodes 每日报告

生成时间：2026-06-15 21:02:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/11 |
| 清理建议：优先/观察 | 1/32 |
| 原始节点数 | 41019 |
| 去重后节点数 | 16137 |
| TCP 可达数 | 1500 |
| 真测通过数 | 254 |
| verified 输出数 | 254 |
| global 输出数 | 258 |
| all 输出数 | 16137 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| generate | 36.9 |
| geo | 1.2 |
| real_test | 208.5 |
| tcp | 37.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 17 | 2 | 15 | 11.8% |
| shadowsocks | 370 | 62 | 308 | 16.8% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 9 | 0 | 9 | 0.0% |
| trojan | 201 | 37 | 164 | 18.4% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 837 | 107 | 730 | 12.8% |
| vmess | 13 | 4 | 9 | 30.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 433 |
| 204:ProxyError | 416 |
| 204:TimeoutError | 104 |
| geo:status | 99 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 61 |
| geo:status | 56 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 11 |
| speed:ClientOSError | 10 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:TimeoutError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 4 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 3 |
| geo:ProxyError | 3 |
| geo:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ir3qseza/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-mv2zru1p/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �5m�5�����6��ѧ~� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1881 |
| ConnectionRefusedError | 462 |
| gaierror | 182 |
| OSError | 27 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | prefer | 46 | 0.935 | 52 |
| Au1rxx-base64 | 0.511 | observe | 77 | 0.506 | 112 |
| roosterkid-openproxylist-v2ray | 0.441 | observe | 21 | 0.429 | 150 |
| mfuu-v2ray | 0.263 | observe | 1 | 1.0 | 205 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3429 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.232 | downweight | 761 | 0.151 | 4405 |
| Epodonios-all | 0.232 | downweight | 110 | 0.145 | 3000 |
| mheidari-all | 0.21 | downweight | 90 | 0.122 | 2000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.074 | downweight | 20 | 0.0 | 0 | 703 |
| moneyfly1-collectSub | 0.076 | downweight | 32 | 0.0 | 0 | 1164 |
| 10ium-HighSpeed | 0.107 | downweight | 5 | 0.0 | 0 | 839 |
| Barabama-yudou | 0.11 | observe | 2 | 0.0 | 0 | 166 |
| ninja-vless | 0.122 | downweight | 14 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| nscl5-all | 0.13 | observe | 3 | 0.0 | 0 | 1019 |
| 10ium-ScrapeCategorize-Vless | 0.13 | downweight | 14 | 0.0 | 0 | 2000 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4560 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.074 | 20 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.076 | 32 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.107 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.122 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.156 | 275 | 0.073 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mheidari-all | 0.21 | 90 | 0.122 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.232 | 761 | 0.151 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 3 | 3 |
| 10ium-HighSpeed | 0.0 | 0 | 5 | 5 |
| ninja-vless | 0.0 | 0 | 14 | 14 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 14 | 14 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 20 | 20 |
| moneyfly1-collectSub | 0.0 | 0 | 32 | 32 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 5458 | yes | 3.32 | 0 |
| mahdibland-V2RayAggregator | 4560 | yes | 1.61 | 0 |
| Surfboard-tg-mixed | 4405 | yes | 2.37 | 0 |
| Surfboard-tg-vless | 3429 | yes | 1.81 | 0 |
| Epodonios-all | 3000 | yes | 2.24 | 0 |
| SoliSpirit-all | 3000 | yes | 1.78 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.32 | 0 |
| mheidari-all | 2000 | yes | 3.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.53 | 0 |
| barry-far-vless | 2000 | yes | 0.91 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 953 |
| geo | 161 |
| sing-box exited 1 | 86 |
| cn-block | 28 |
| speed | 18 |
