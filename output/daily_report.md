# AutoNodes 每日报告

生成时间：2026-06-07 19:28:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 0/34 |
| 原始节点数 | 39691 |
| 去重后节点数 | 15325 |
| TCP 可达数 | 1500 |
| 真测通过数 | 159 |
| verified 输出数 | 159 |
| global 输出数 | 167 |
| all 输出数 | 15325 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| generate | 25.8 |
| geo | 1.1 |
| real_test | 150.2 |
| tcp | 41.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 7 | 16 | 30.4% |
| hysteria2 | 11 | 0 | 11 | 0.0% |
| shadowsocks | 329 | 67 | 262 | 20.4% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 166 | 7 | 159 | 4.2% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 941 | 70 | 871 | 7.4% |
| vmess | 19 | 8 | 11 | 42.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 615 |
| 204:ClientOSError | 349 |
| 204:TimeoutError | 170 |
| geo:status | 70 |
| speed:TimeoutError | 37 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 31 |
| speed:ClientOSError | 17 |
| cn-block:TimeoutError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| geo:status | 8 |
| cn-block:ClientOSError | 7 |
| geo:TimeoutError | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-u43r103k/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-i6qqwo_w/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-w18cr1uf/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���s�F�������>�m�s� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: վ����N]k� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: s��m� | ���o� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2134 |
| ConnectionRefusedError | 443 |
| gaierror | 141 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.486 | observe | 79 | 0.481 | 102 |
| roosterkid-openproxylist-v2ray | 0.351 | observe | 15 | 0.4 | 150 |
| mheidari-all | 0.34 | observe | 75 | 0.253 | 2000 |
| snakem982 | 0.335 | observe | 25 | 0.32 | 47 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3345 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 482 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.073 | downweight | 36 | 0.0 | 0 | 1164 |
| Barabama-we | 0.074 | downweight | 5 | 0.0 | 0 | 23 |
| xiaoji235-airport-v2ray-all | 0.094 | downweight | 6 | 0.0 | 0 | 646 |
| Pawdroid | 0.104 | observe | 2 | 0.0 | 0 | 6 |
| 10ium-HighSpeed | 0.104 | downweight | 69 | 0.058 | 0 | 839 |
| Barabama-yudou | 0.11 | observe | 2 | 0.0 | 0 | 166 |
| ninja-vless | 0.117 | downweight | 20 | 0.0 | 0 | 1791 |
| nscl5-all | 0.121 | observe | 4 | 0.0 | 0 | 1013 |
| 10ium-ScrapeCategorize-Vless | 0.123 | downweight | 21 | 0.0 | 0 | 2000 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 20 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.073 | 36 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-we | 0.074 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.094 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.104 | 69 | 0.058 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.117 | 20 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.123 | 21 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.134 | 425 | 0.052 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.136 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.171 | 690 | 0.09 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 2 | 2 |
| Pawdroid | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 4 | 4 |
| Barabama-we | 0.0 | 0 | 5 | 5 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 6 | 6 |
| SoliSpirit-all | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 20 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 4615 | yes | 1.29 | 0 |
| DeltaKronecker-all | 4578 | yes | 2.59 | 0 |
| Surfboard-tg-mixed | 4253 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 3345 | yes | 1.49 | 0 |
| Epodonios-all | 3000 | yes | 2.74 | 0 |
| SoliSpirit-all | 3000 | yes | 1.35 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.85 | 0 |
| mheidari-all | 2000 | yes | 2.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.67 | 0 |
| barry-far-vless | 2000 | yes | 0.78 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.074 |
| trojan | 0.042 |
| hysteria2 | 0.0 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1134 |
| geo | 84 |
| speed | 54 |
| sing-box exited 1 | 51 |
| cn-block | 18 |
