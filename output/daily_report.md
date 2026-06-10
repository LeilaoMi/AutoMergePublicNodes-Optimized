# AutoNodes 每日报告

生成时间：2026-06-10 03:58:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/8 |
| 清理建议：优先/观察 | 1/35 |
| 原始节点数 | 39640 |
| 去重后节点数 | 15507 |
| TCP 可达数 | 1500 |
| 真测通过数 | 413 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15507 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 25.8 |
| geo | 1.2 |
| real_test | 149.7 |
| tcp | 35.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 45 | 43 | 2 | 95.6% |
| hysteria2 | 6 | 1 | 5 | 16.7% |
| shadowsocks | 295 | 96 | 199 | 32.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 129 | 35 | 94 | 27.1% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 995 | 231 | 764 | 23.2% |
| vmess | 17 | 5 | 12 | 29.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 452 |
| 204:ProxyError | 394 |
| 204:TimeoutError | 89 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 37 |
| speed:TimeoutError | 27 |
| geo:status | 26 |
| speed:ClientOSError | 16 |
| cn-block:ClientOSError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:TimeoutError | 6 |
| geo:status | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-c0q02o04/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-hlzov_o6/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ov6t1did/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: of�o���� | ��7���]>kO | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1653 |
| ConnectionRefusedError | 449 |
| gaierror | 204 |
| OSError | 27 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.821 | prefer | 53 | 0.83 | 61 |
| roosterkid-openproxylist-v2ray | 0.548 | observe | 22 | 0.545 | 150 |
| Au1rxx-base64 | 0.511 | observe | 69 | 0.507 | 96 |
| Surfboard-tg-mixed | 0.361 | observe | 960 | 0.28 | 4093 |
| mheidari-all | 0.309 | observe | 103 | 0.223 | 2000 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3270 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.08 | downweight | 28 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.096 | downweight | 6 | 0.0 | 0 | 689 |
| ninja-vless | 0.11 | downweight | 24 | 0.0 | 0 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.118 | downweight | 24 | 0.0 | 0 | 2000 |
| Barabama-we | 0.128 | observe | 1 | 0.0 | 0 | 23 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4536 |
| 10ium-HighSpeed | 0.137 | observe | 2 | 0.0 | 0 | 839 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.08 | 28 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.096 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.11 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.118 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.194 | 13 | 0.154 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.248 | 165 | 0.164 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Barabama-we | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 6 | 6 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 24 | 24 |
| ninja-vless | 0.0 | 0 | 24 | 24 |
| moneyfly1-collectSub | 0.0 | 0 | 28 | 28 |
| nscl5-all | 0.154 | 2 | 11 | 13 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4764 | yes | 2.75 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.32 | 0 |
| Surfboard-tg-mixed | 4093 | yes | 1.84 | 0 |
| Surfboard-tg-vless | 3270 | yes | 1.7 | 0 |
| Epodonios-all | 3000 | yes | 2.84 | 0 |
| SoliSpirit-all | 3000 | yes | 1.13 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.91 | 0 |
| mheidari-all | 2000 | yes | 2.65 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.85 | 0 |
| barry-far-vless | 2000 | yes | 0.69 | 0 |

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
| 204 | 935 |
| sing-box exited 1 | 62 |
| speed | 44 |
| geo | 31 |
| cn-block | 15 |
