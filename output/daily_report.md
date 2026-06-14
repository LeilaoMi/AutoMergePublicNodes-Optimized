# AutoNodes 每日报告

生成时间：2026-06-14 19:33:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/11 |
| 清理建议：优先/观察 | 1/32 |
| 原始节点数 | 41035 |
| 去重后节点数 | 15688 |
| TCP 可达数 | 1500 |
| 真测通过数 | 214 |
| verified 输出数 | 214 |
| global 输出数 | 219 |
| all 输出数 | 15688 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| generate | 37.7 |
| geo | 1.3 |
| real_test | 193.2 |
| tcp | 39.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 11 | 2 | 9 | 18.2% |
| shadowsocks | 354 | 62 | 292 | 17.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 156 | 9 | 147 | 5.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 910 | 95 | 815 | 10.4% |
| vmess | 14 | 4 | 10 | 28.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 489 |
| 204:ClientOSError | 375 |
| 204:TimeoutError | 184 |
| geo:status | 62 |
| geo:status | 44 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 42 |
| cn-block:TimeoutError | 22 |
| speed:ClientOSError | 13 |
| speed:TimeoutError | 13 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| geo:TimeoutError | 6 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 4 |
| cn-block:ClientOSError | 4 |
| speed:ClientPayloadError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-6we7hjom/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-wi2qlq9s/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-i05oic_f/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �gv�n{�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: � | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2008 |
| ConnectionRefusedError | 447 |
| gaierror | 145 |
| OSError | 41 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.917 | prefer | 45 | 0.933 | 52 |
| Au1rxx-base64 | 0.578 | observe | 87 | 0.575 | 122 |
| roosterkid-openproxylist-v2ray | 0.32 | observe | 33 | 0.303 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3622 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.218 | downweight | 92 | 0.13 | 2000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 477 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.081 | downweight | 11 | 0.0 | 0 | 656 |
| moneyfly1-collectSub | 0.085 | downweight | 24 | 0.0 | 0 | 1164 |
| Barabama-yudou | 0.09 | downweight | 22 | 0.045 | 0 | 166 |
| ninja-vless | 0.118 | downweight | 19 | 0.0 | 0 | 1791 |
| DeltaKronecker-all | 0.12 | downweight | 348 | 0.037 | 0 | 5188 |
| SoliSpirit-all | 0.127 | downweight | 18 | 0.0 | 0 | 3000 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 8 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.128 | downweight | 17 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4511 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.081 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.085 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.09 | 22 | 0.045 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.12 | 348 | 0.037 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.127 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.128 | 17 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.181 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.193 | 759 | 0.112 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| MatinGhanbari-super-sub | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 11 | 11 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 17 | 17 |
| SoliSpirit-all | 0.0 | 0 | 18 | 18 |
| ninja-vless | 0.0 | 0 | 19 | 19 |
| moneyfly1-collectSub | 0.0 | 0 | 24 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 5188 | yes | 3.14 | 0 |
| Surfboard-tg-mixed | 4520 | yes | 0.29 | 0 |
| mahdibland-V2RayAggregator | 4511 | yes | 1.56 | 0 |
| Surfboard-tg-vless | 3622 | yes | 2.01 | 0 |
| Epodonios-all | 3000 | yes | 1.9 | 0 |
| SoliSpirit-all | 3000 | yes | 1.68 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.75 | 0 |
| mheidari-all | 2000 | yes | 3.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.35 | 0 |
| barry-far-vless | 2000 | yes | 1.17 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| trojan | 0.058 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1048 |
| geo | 113 |
| sing-box exited 1 | 70 |
| speed | 28 |
| cn-block | 27 |
