# AutoNodes 每日报告

生成时间：2026-06-17 11:05:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 43351 |
| 去重后节点数 | 17819 |
| TCP 可达数 | 1500 |
| 真测通过数 | 258 |
| verified 输出数 | 258 |
| global 输出数 | 277 |
| all 输出数 | 17819 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.4 |
| generate | 41.2 |
| geo | 1.2 |
| real_test | 193.6 |
| tcp | 40.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 13 | 2 | 11 | 15.4% |
| shadowsocks | 206 | 56 | 150 | 27.2% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 373 | 52 | 321 | 13.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 841 | 102 | 739 | 12.1% |
| vmess | 13 | 3 | 10 | 23.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 510 |
| 204:ProxyError | 348 |
| 204:TimeoutError | 111 |
| geo:status | 83 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 58 |
| geo:status | 45 |
| cn-block:TimeoutError | 22 |
| speed:ClientOSError | 13 |
| speed:TimeoutError | 10 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| speed:ProxyError | 5 |
| geo:TimeoutError | 4 |
| geo:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-syu16eci/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-czaejwjk/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-dd7yddrd/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ݽ5k����^�� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1989 |
| ConnectionRefusedError | 444 |
| gaierror | 179 |
| OSError | 35 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.917 | prefer | 45 | 0.933 | 52 |
| Au1rxx-base64 | 0.517 | observe | 80 | 0.512 | 109 |
| roosterkid-openproxylist-v2ray | 0.47 | observe | 26 | 0.462 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3522 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.25 | observe | 86 | 0.163 | 2000 |
| Surfboard-tg-mixed | 0.219 | downweight | 789 | 0.138 | 4546 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 495 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 477 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.078 | downweight | 30 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.08 | downweight | 10 | 0.0 | 0 | 588 |
| Barabama-yudou | 0.099 | downweight | 19 | 0.053 | 0 | 166 |
| ninja-vless | 0.11 | downweight | 24 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| nscl5-all | 0.128 | observe | 3 | 0.0 | 0 | 967 |
| SoliSpirit-all | 0.13 | downweight | 14 | 0.0 | 0 | 3000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4516 |
| 10ium-HighSpeed | 0.137 | observe | 2 | 0.0 | 0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.141 | downweight | 8 | 0.0 | 0 | 2000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.078 | 30 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.08 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.099 | 19 | 0.053 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.11 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.141 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | chromego_merge | 0.149 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.193 | 342 | 0.111 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.219 | 789 | 0.138 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 2 | 2 |
| Epodonios-all | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 3 | 3 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 8 | 8 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| SoliSpirit-all | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 24 | 24 |
| moneyfly1-collectSub | 0.0 | 0 | 30 | 30 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 3.1 | 0 |
| Surfboard-tg-mixed | 4546 | yes | 2.23 | 0 |
| mahdibland-V2RayAggregator | 4516 | yes | 1.39 | 0 |
| Surfboard-tg-vless | 3522 | yes | 1.67 | 0 |
| Epodonios-all | 3000 | yes | 2.78 | 0 |
| SoliSpirit-all | 3000 | yes | 1.64 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.37 | 0 |
| mheidari-all | 2000 | yes | 3.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.11 | 0 |
| barry-far-vless | 2000 | yes | 0.92 | 0 |

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
| 204 | 969 |
| geo | 134 |
| sing-box exited 1 | 80 |
| cn-block | 31 |
| speed | 28 |
