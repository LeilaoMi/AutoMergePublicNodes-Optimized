# AutoNodes 每日报告

生成时间：2026-06-11 10:43:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/8 |
| 清理建议：优先/观察 | 1/35 |
| 原始节点数 | 40042 |
| 去重后节点数 | 15031 |
| TCP 可达数 | 1500 |
| 真测通过数 | 300 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15031 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 26.3 |
| geo | 1.2 |
| real_test | 157.7 |
| tcp | 34.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 58 | 56 | 2 | 96.6% |
| hysteria2 | 5 | 1 | 4 | 20.0% |
| shadowsocks | 228 | 74 | 154 | 32.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 495 | 44 | 451 | 8.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 690 | 120 | 570 | 17.4% |
| vmess | 14 | 5 | 9 | 35.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 566 |
| 204:ProxyError | 309 |
| 204:TimeoutError | 140 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 44 |
| geo:status | 34 |
| geo:status | 22 |
| cn-block:TimeoutError | 20 |
| speed:ClientOSError | 16 |
| speed:TimeoutError | 10 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| geo:TimeoutError | 4 |
| geo:ClientOSError | 3 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-_gkzq8jq/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ztr9q9vc/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-a7k21hgs/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1815 |
| ConnectionRefusedError | 407 |
| gaierror | 179 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.908 | prefer | 61 | 0.918 | 75 |
| Au1rxx-base64 | 0.564 | observe | 64 | 0.562 | 90 |
| roosterkid-openproxylist-v2ray | 0.358 | observe | 14 | 0.429 | 150 |
| mheidari-all | 0.33 | observe | 106 | 0.245 | 2000 |
| Surfboard-tg-mixed | 0.296 | observe | 673 | 0.215 | 4208 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3360 |
| mfuu-v2ray | 0.187 | observe | 0 | None | 297 |
| MatinGhanbari-super-sub | 0.183 | observe | 0 | None | 199 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-yudou | 0.096 | observe | 3 | 0.0 | 0 | 166 |
| moneyfly1-collectSub | 0.105 | downweight | 9 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.109 | observe | 4 | 0.0 | 0 | 729 |
| barry-far-Sub2 | 0.11 | observe | 3 | 0.0 | 0 | 500 |
| ninja-vless | 0.112 | downweight | 23 | 0.0 | 0 | 1791 |
| nscl5-all | 0.113 | downweight | 5 | 0.0 | 0 | 984 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.129 | downweight | 15 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.129 | downweight | 15 | 0.0 | 0 | 4508 |
| 10ium-ScrapeCategorize-Vless | 0.132 | downweight | 13 | 0.0 | 0 | 2000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.105 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.112 | 23 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.113 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.145 | 472 | 0.064 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | barry-far-vless | 0.175 | 17 | 0.059 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| barry-far-Sub1 | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 3 | 3 |
| barry-far-Sub2 | 0.0 | 0 | 3 | 3 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 4 | 4 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| moneyfly1-collectSub | 0.0 | 0 | 9 | 9 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 13 | 13 |
| SoliSpirit-all | 0.0 | 0 | 15 | 15 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.68 | 0 |
| mahdibland-V2RayAggregator | 4508 | yes | 1.33 | 0 |
| Surfboard-tg-mixed | 4208 | yes | 1.96 | 0 |
| Surfboard-tg-vless | 3360 | yes | 1.54 | 0 |
| Epodonios-all | 3000 | yes | 1.85 | 0 |
| SoliSpirit-all | 3000 | yes | 1.87 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.7 | 0 |
| mheidari-all | 2000 | yes | 2.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.64 | 0 |
| barry-far-vless | 2000 | yes | 1.42 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| trojan | 0.089 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1015 |
| sing-box exited 1 | 65 |
| geo | 65 |
| cn-block | 29 |
| speed | 26 |
