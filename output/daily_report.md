# AutoNodes 每日报告

生成时间：2026-06-14 01:18:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/12 |
| 清理建议：优先/观察 | 1/31 |
| 原始节点数 | 40280 |
| 去重后节点数 | 15578 |
| TCP 可达数 | 1500 |
| 真测通过数 | 376 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15578 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| generate | 19.9 |
| geo | 1.2 |
| real_test | 184.7 |
| tcp | 36.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 7 | 1 | 6 | 14.3% |
| shadowsocks | 370 | 84 | 286 | 22.7% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 160 | 38 | 122 | 23.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 891 | 202 | 689 | 22.7% |
| vmess | 17 | 7 | 10 | 41.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 400 |
| 204:ProxyError | 341 |
| speed:TimeoutError | 95 |
| 204:TimeoutError | 75 |
| geo:status | 72 |
| speed:ClientOSError | 52 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 35 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:TimeoutError | 8 |
| cn-block:ClientOSError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| geo:TimeoutError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: decode public_key: illegal base64 data at input byte 44 | 2 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-vp4qms7k/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-q5xvwfv1/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-nalapbx7/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1873 |
| ConnectionRefusedError | 444 |
| gaierror | 205 |
| OSError | 34 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.938 | prefer | 45 | 0.956 | 52 |
| roosterkid-openproxylist-v2ray | 0.574 | observe | 35 | 0.571 | 150 |
| Au1rxx-base64 | 0.442 | observe | 108 | 0.435 | 135 |
| Surfboard-tg-mixed | 0.377 | observe | 658 | 0.296 | 4199 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| mheidari-all | 0.288 | observe | 104 | 0.202 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3299 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| DeltaKronecker-all | 0.205 | downweight | 342 | 0.123 | 4955 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| ts-sf | 0.057 | downweight | 11 | 0.0 | 0 | 58 |
| Barabama-we | 0.069 | downweight | 6 | 0.0 | 0 | 23 |
| moneyfly1-collectSub | 0.07 | downweight | 41 | 0.0 | 0 | 1164 |
| nscl5-all | 0.103 | downweight | 9 | 0.0 | 0 | 1119 |
| ermaozi | 0.105 | observe | 2 | 0.0 | 0 | 29 |
| 10ium-HighSpeed | 0.107 | downweight | 5 | 0.0 | 0 | 839 |
| ninja-vless | 0.118 | downweight | 18 | 0.0 | 0 | 1791 |
| SoliSpirit-all | 0.126 | downweight | 19 | 0.0 | 0 | 3000 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 0.13 | downweight | 13 | 0.077 | 0 | 675 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ts-sf | 0.057 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-we | 0.069 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.07 | 41 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.103 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.107 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.126 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.13 | 13 | 0.077 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Au1rxx-clash | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.0 | 0 | 2 | 2 |
| 10ium-HighSpeed | 0.0 | 0 | 5 | 5 |
| Barabama-we | 0.0 | 0 | 6 | 6 |
| nscl5-all | 0.0 | 0 | 9 | 9 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 9 | 9 |
| ts-sf | 0.0 | 0 | 11 | 11 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| ninja-vless | 0.0 | 0 | 18 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4955 | yes | 2.83 | 0 |
| mahdibland-V2RayAggregator | 4566 | yes | 1.56 | 0 |
| Surfboard-tg-mixed | 4199 | yes | 1.5 | 0 |
| Surfboard-tg-vless | 3299 | yes | 0.82 | 0 |
| Epodonios-all | 3000 | yes | 2.21 | 0 |
| SoliSpirit-all | 3000 | yes | 2.05 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.89 | 0 |
| mheidari-all | 2000 | yes | 2.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.55 | 0 |
| barry-far-vless | 2000 | yes | 1.4 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 816 |
| speed | 147 |
| geo | 75 |
| sing-box exited 1 | 69 |
| cn-block | 17 |
