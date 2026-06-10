# AutoNodes 每日报告

生成时间：2026-06-10 20:36:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/9 |
| 清理建议：优先/观察 | 1/34 |
| 原始节点数 | 39568 |
| 去重后节点数 | 15284 |
| TCP 可达数 | 1500 |
| 真测通过数 | 265 |
| verified 输出数 | 265 |
| global 输出数 | 271 |
| all 输出数 | 15284 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 28.7 |
| geo | 1.2 |
| real_test | 159.0 |
| tcp | 35.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 58 | 55 | 3 | 94.8% |
| hysteria2 | 11 | 1 | 10 | 9.1% |
| shadowsocks | 355 | 69 | 286 | 19.4% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 6 | 0 | 6 | 0.0% |
| trojan | 143 | 7 | 136 | 4.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 904 | 130 | 774 | 14.4% |
| vmess | 14 | 3 | 11 | 21.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 490 |
| 204:ClientOSError | 382 |
| 204:TimeoutError | 142 |
| geo:status | 74 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 42 |
| geo:status | 28 |
| cn-block:ClientOSError | 14 |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| speed:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| geo:TimeoutError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-n6doqgp5/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ed8ev5im/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-94uegkkn/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: վ����N]k� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1762 |
| ConnectionRefusedError | 431 |
| gaierror | 190 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.878 | prefer | 62 | 0.887 | 75 |
| Au1rxx-base64 | 0.575 | observe | 54 | 0.574 | 88 |
| roosterkid-openproxylist-v2ray | 0.415 | observe | 20 | 0.4 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3262 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.242 | downweight | 881 | 0.161 | 4236 |
| mheidari-all | 0.223 | downweight | 96 | 0.135 | 2000 |
| Epodonios-all | 0.207 | observe | 1 | 0.0 | 3000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.086 | downweight | 9 | 0.0 | 0 | 689 |
| moneyfly1-collectSub | 0.108 | downweight | 8 | 0.0 | 0 | 1164 |
| ninja-vless | 0.117 | downweight | 20 | 0.0 | 0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.122 | downweight | 22 | 0.0 | 0 | 2000 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.128 | downweight | 17 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4508 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| DeltaKronecker-all | 0.138 | downweight | 292 | 0.055 | 0 | 4616 |
| nscl5-all | 0.143 | observe | 2 | 0.0 | 0 | 989 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.086 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.108 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.117 | 20 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.122 | 22 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.128 | 17 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.138 | 292 | 0.055 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mheidari-all | 0.223 | 96 | 0.135 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.242 | 881 | 0.161 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 2 | 2 |
| moneyfly1-collectSub | 0.0 | 0 | 8 | 8 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 9 | 9 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| SoliSpirit-all | 0.0 | 0 | 17 | 17 |
| ninja-vless | 0.0 | 0 | 20 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4616 | yes | 3.11 | 0 |
| mahdibland-V2RayAggregator | 4508 | yes | 1.37 | 0 |
| Surfboard-tg-mixed | 4236 | yes | 2.07 | 0 |
| Surfboard-tg-vless | 3262 | yes | 1.63 | 0 |
| Epodonios-all | 3000 | yes | 1.3 | 0 |
| SoliSpirit-all | 3000 | yes | 1.48 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.02 | 0 |
| mheidari-all | 2000 | yes | 2.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.21 | 0 |
| barry-far-vless | 2000 | yes | 0.84 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.091 |
| trojan | 0.049 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1014 |
| geo | 108 |
| sing-box exited 1 | 66 |
| cn-block | 31 |
| speed | 16 |
