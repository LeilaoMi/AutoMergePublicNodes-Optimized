# AutoNodes 每日报告

生成时间：2026-06-13 19:32:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/11 |
| 清理建议：优先/观察 | 1/32 |
| 原始节点数 | 40141 |
| 去重后节点数 | 15452 |
| TCP 可达数 | 1500 |
| 真测通过数 | 207 |
| verified 输出数 | 207 |
| global 输出数 | 215 |
| all 输出数 | 15452 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 25.5 |
| geo | 1.2 |
| real_test | 149.3 |
| tcp | 36.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 6 | 1 | 5 | 16.7% |
| shadowsocks | 347 | 60 | 287 | 17.3% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 144 | 12 | 132 | 8.3% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 932 | 85 | 847 | 9.1% |
| vmess | 16 | 7 | 9 | 43.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 578 |
| 204:ClientOSError | 326 |
| 204:TimeoutError | 112 |
| geo:status | 108 |
| geo:status | 56 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 40 |
| cn-block:TimeoutError | 19 |
| speed:ClientOSError | 17 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:TimeoutError | 7 |
| cn-block:ClientOSError | 6 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-nlen2zq0/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-xk_62t6d/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-qxs23sbc/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���s�F�������>�m�s� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ݽ5k����^�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1956 |
| ConnectionRefusedError | 451 |
| gaierror | 191 |
| OSError | 32 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.898 | prefer | 46 | 0.913 | 52 |
| Au1rxx-base64 | 0.511 | observe | 65 | 0.508 | 94 |
| roosterkid-openproxylist-v2ray | 0.423 | observe | 34 | 0.412 | 150 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3246 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.235 | downweight | 95 | 0.147 | 2000 |
| Surfboard-tg-mixed | 0.196 | downweight | 645 | 0.115 | 4189 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 498 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.08 | downweight | 12 | 0.0 | 0 | 675 |
| moneyfly1-collectSub | 0.093 | downweight | 18 | 0.0 | 0 | 1164 |
| nscl5-all | 0.099 | downweight | 11 | 0.0 | 0 | 1119 |
| Barabama-yudou | 0.099 | downweight | 19 | 0.053 | 0 | 166 |
| abc-configs-readme-latest30 | 0.105 | observe | 2 | 0.0 | 0 | 22 |
| ninja-vless | 0.107 | downweight | 26 | 0.0 | 0 | 1791 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 8 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.129 | downweight | 15 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4566 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.08 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.093 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.099 | 19 | 0.053 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.099 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.107 | 26 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.134 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.14 | 482 | 0.058 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.196 | 645 | 0.115 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 2 | 2 |
| abc-configs-readme-latest30 | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 11 | 11 |
| SoliSpirit-all | 0.0 | 0 | 11 | 11 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 12 | 12 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 15 | 15 |
| moneyfly1-collectSub | 0.0 | 0 | 18 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4955 | yes | 2.98 | 0 |
| mahdibland-V2RayAggregator | 4566 | yes | 1.4 | 0 |
| Surfboard-tg-mixed | 4189 | yes | 1.9 | 0 |
| Surfboard-tg-vless | 3246 | yes | 1.5 | 0 |
| Epodonios-all | 3000 | yes | 1.78 | 0 |
| SoliSpirit-all | 3000 | yes | 1.9 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.16 | 0 |
| mheidari-all | 2000 | yes | 2.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.68 | 0 |
| barry-far-vless | 2000 | yes | 1.1 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.091 |
| trojan | 0.083 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1016 |
| geo | 165 |
| sing-box exited 1 | 60 |
| cn-block | 28 |
| speed | 24 |
