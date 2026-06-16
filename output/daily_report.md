# AutoNodes 每日报告

生成时间：2026-06-16 20:58:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/12 |
| 清理建议：优先/观察 | 2/30 |
| 原始节点数 | 43663 |
| 去重后节点数 | 18298 |
| TCP 可达数 | 1500 |
| 真测通过数 | 219 |
| verified 输出数 | 219 |
| global 输出数 | 224 |
| all 输出数 | 18298 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.5 |
| generate | 35.3 |
| geo | 1.2 |
| real_test | 182.5 |
| tcp | 39.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 20 | 2 | 18 | 10.0% |
| shadowsocks | 306 | 54 | 252 | 17.6% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 159 | 18 | 141 | 11.3% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 944 | 98 | 846 | 10.4% |
| vmess | 15 | 5 | 10 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 449 |
| 204:ClientOSError | 401 |
| geo:status | 112 |
| 204:TimeoutError | 107 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 67 |
| geo:status | 54 |
| speed:ClientOSError | 17 |
| cn-block:TimeoutError | 12 |
| cn-block:ClientOSError | 12 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| geo:TimeoutError | 8 |
| speed:TimeoutError | 7 |
| cn-block:ProxyError | 6 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-9_k2nr4f/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-muz6bch_/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-zyzg5lzn/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1835 |
| ConnectionRefusedError | 476 |
| gaierror | 214 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.898 | prefer | 46 | 0.913 | 52 |
| roosterkid-openproxylist-v2ray | 0.726 | prefer | 23 | 0.739 | 150 |
| Au1rxx-base64 | 0.563 | observe | 59 | 0.559 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3491 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| abc-configs-readme-latest30 | 0.208 | observe | 2 | 0.5 | 22 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 494 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 476 |
| Surfboard-tg-mixed | 0.193 | downweight | 883 | 0.112 | 4461 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-yudou | 0.052 | downweight | 20 | 0.0 | 0 | 166 |
| Barabama-we | 0.069 | downweight | 6 | 0.0 | 0 | 23 |
| moneyfly1-collectSub | 0.072 | downweight | 38 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.073 | downweight | 21 | 0.0 | 0 | 729 |
| ermaozi | 0.091 | observe | 3 | 0.0 | 0 | 29 |
| Epodonios-all | 0.113 | downweight | 59 | 0.017 | 0 | 3000 |
| nscl5-all | 0.121 | observe | 4 | 0.0 | 0 | 1017 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| ninja-vless | 0.128 | downweight | 10 | 0.0 | 0 | 1791 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | Barabama-yudou | 0.052 | 20 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-we | 0.069 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.072 | 38 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.073 | 21 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Epodonios-all | 0.113 | 59 | 0.017 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.128 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.134 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.17 | 198 | 0.086 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.0 | 0 | 3 | 3 |
| nscl5-all | 0.0 | 0 | 4 | 4 |
| Barabama-we | 0.0 | 0 | 6 | 6 |
| ninja-vless | 0.0 | 0 | 10 | 10 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 11 | 11 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| Barabama-yudou | 0.0 | 0 | 20 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 8110 | yes | 3.49 | 0 |
| mahdibland-V2RayAggregator | 4528 | yes | 1.7 | 0 |
| Surfboard-tg-mixed | 4461 | yes | 1.95 | 0 |
| Surfboard-tg-vless | 3491 | yes | 2.1 | 0 |
| Epodonios-all | 3000 | yes | 1.62 | 0 |
| SoliSpirit-all | 3000 | yes | 2.44 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.7 | 0 |
| mheidari-all | 2000 | yes | 2.98 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.87 | 0 |
| barry-far-vless | 2000 | yes | 1.54 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

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
| 204 | 957 |
| geo | 177 |
| sing-box exited 1 | 92 |
| cn-block | 30 |
| speed | 25 |
