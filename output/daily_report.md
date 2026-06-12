# AutoNodes 每日报告

生成时间：2026-06-12 00:07:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/8 |
| 清理建议：优先/观察 | 1/35 |
| 原始节点数 | 39955 |
| 去重后节点数 | 15028 |
| TCP 可达数 | 1500 |
| 真测通过数 | 409 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15028 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 27.7 |
| geo | 1.2 |
| real_test | 150.8 |
| tcp | 34.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 6 | 1 | 5 | 16.7% |
| shadowsocks | 356 | 99 | 257 | 27.8% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 32 | 26 | 6 | 81.2% |
| trojan | 285 | 58 | 227 | 20.4% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 752 | 176 | 576 | 23.4% |
| vmess | 16 | 7 | 9 | 43.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 477 |
| 204:ProxyError | 332 |
| 204:TimeoutError | 61 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 54 |
| speed:TimeoutError | 44 |
| geo:status | 36 |
| speed:ClientOSError | 31 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 13 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| geo:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-k28c2kab/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-_45vd4o0/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-9a1g3v7c/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: վ����N]k� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1716 |
| ConnectionRefusedError | 435 |
| gaierror | 206 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.675 | observe | 71 | 0.676 | 88 |
| Surfboard-tg-mixed | 0.386 | observe | 769 | 0.306 | 4225 |
| mheidari-all | 0.317 | observe | 95 | 0.232 | 2000 |
| Epodonios-all | 0.287 | observe | 2 | 0.5 | 3000 |
| roosterkid-openproxylist-v2ray | 0.264 | observe | 29 | 0.241 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Barabama-yudou | 0.247 | observe | 4 | 0.5 | 166 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.093 | downweight | 7 | 0.0 | 0 | 729 |
| moneyfly1-collectSub | 0.101 | downweight | 11 | 0.0 | 0 | 1164 |
| nscl5-all | 0.113 | downweight | 5 | 0.0 | 0 | 984 |
| ninja-vless | 0.119 | downweight | 17 | 0.0 | 0 | 1791 |
| 10ium-HighSpeed | 0.123 | observe | 3 | 0.0 | 0 | 839 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 24 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| 10ium-ScrapeCategorize-Vless | 0.132 | downweight | 13 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4536 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.093 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.101 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.113 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.119 | 17 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.211 | 402 | 0.129 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 3 | 3 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 7 | 7 |
| moneyfly1-collectSub | 0.0 | 0 | 11 | 11 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 13 | 13 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 17 | 17 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.54 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.34 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 1.68 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.89 | 0 |
| Epodonios-all | 3000 | yes | 2.85 | 0 |
| SoliSpirit-all | 3000 | yes | 1.88 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.49 | 0 |
| mheidari-all | 2000 | yes | 2.67 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.65 | 0 |
| barry-far-vless | 2000 | yes | 1.28 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| tuic | 0.0 |
| shadowsocksr | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 870 |
| sing-box exited 1 | 79 |
| speed | 76 |
| geo | 38 |
| cn-block | 28 |
