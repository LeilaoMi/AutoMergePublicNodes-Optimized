# AutoNodes 每日报告

生成时间：2026-06-12 04:12:57

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/11 |
| 清理建议：优先/观察 | 1/32 |
| 原始节点数 | 39941 |
| 去重后节点数 | 15081 |
| TCP 可达数 | 1500 |
| 真测通过数 | 382 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15081 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| generate | 25.3 |
| geo | 1.2 |
| real_test | 152.0 |
| tcp | 37.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 12 | 1 | 11 | 8.3% |
| shadowsocks | 230 | 77 | 153 | 33.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 370 | 75 | 295 | 20.3% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 818 | 179 | 639 | 21.9% |
| vmess | 15 | 7 | 8 | 46.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 519 |
| 204:ProxyError | 321 |
| 204:TimeoutError | 81 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 52 |
| speed:TimeoutError | 44 |
| geo:status | 26 |
| speed:ClientOSError | 18 |
| geo:status | 16 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 4 |
| geo:TimeoutError | 4 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-qrey53q1/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-atfnx9rq/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���s�F�������>�m�s� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1760 |
| ConnectionRefusedError | 433 |
| gaierror | 197 |
| OSError | 32 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.478 | observe | 91 | 0.473 | 121 |
| roosterkid-openproxylist-v2ray | 0.446 | observe | 23 | 0.435 | 150 |
| Surfboard-tg-mixed | 0.365 | observe | 734 | 0.285 | 4083 |
| mheidari-all | 0.343 | observe | 93 | 0.258 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3039 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Epodonios-all | 0.247 | downweight | 52 | 0.154 | 3000 |
| DeltaKronecker-all | 0.209 | downweight | 339 | 0.127 | 4660 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| mfuu-v2ray | 0.074 | downweight | 9 | 0.0 | 0 | 387 |
| xiaoji235-airport-v2ray-all | 0.087 | downweight | 10 | 0.0 | 0 | 774 |
| moneyfly1-collectSub | 0.093 | downweight | 19 | 0.0 | 0 | 1164 |
| ninja-vless | 0.118 | downweight | 18 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4536 |
| SoliSpirit-all | 0.132 | downweight | 13 | 0.0 | 0 | 3000 |
| 10ium-ScrapeCategorize-Vless | 0.133 | downweight | 12 | 0.0 | 0 | 2000 |
| Barabama-yudou | 0.137 | downweight | 21 | 0.095 | 0 | 166 |
| nscl5-all | 0.169 | downweight | 8 | 0.125 | 0 | 1178 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | mfuu-v2ray | 0.074 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.087 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.093 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.133 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.137 | 21 | 0.095 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.169 | 8 | 0.125 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.209 | 339 | 0.127 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| mfuu-v2ray | 0.0 | 0 | 9 | 9 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 10 | 10 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 12 | 12 |
| SoliSpirit-all | 0.0 | 0 | 13 | 13 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 18 | 18 |
| moneyfly1-collectSub | 0.0 | 0 | 19 | 19 |
| Barabama-yudou | 0.095 | 2 | 19 | 21 |
| nscl5-all | 0.125 | 1 | 7 | 8 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 3.26 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.85 | 0 |
| Surfboard-tg-mixed | 4083 | yes | 1.7 | 0 |
| Surfboard-tg-vless | 3039 | yes | 1.04 | 0 |
| Epodonios-all | 3000 | yes | 2.63 | 0 |
| SoliSpirit-all | 3000 | yes | 1.64 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.12 | 0 |
| mheidari-all | 2000 | yes | 2.91 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.28 | 0 |
| barry-far-vless | 2000 | yes | 1.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.083 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 921 |
| sing-box exited 1 | 73 |
| speed | 62 |
| geo | 46 |
| cn-block | 16 |
