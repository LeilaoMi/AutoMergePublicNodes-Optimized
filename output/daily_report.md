# AutoNodes 每日报告

生成时间：2026-06-11 23:47:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/7 |
| 清理建议：优先/观察 | 1/36 |
| 原始节点数 | 39955 |
| 去重后节点数 | 15027 |
| TCP 可达数 | 1500 |
| 真测通过数 | 325 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15027 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| generate | 25.1 |
| geo | 1.1 |
| real_test | 139.1 |
| tcp | 35.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 6 | 1 | 5 | 16.7% |
| shadowsocks | 355 | 78 | 277 | 22.0% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 28 | 20 | 8 | 71.4% |
| trojan | 348 | 60 | 288 | 17.2% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 695 | 117 | 578 | 16.8% |
| vmess | 15 | 7 | 8 | 46.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 506 |
| 204:ProxyError | 365 |
| geo:status | 73 |
| 204:TimeoutError | 69 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 52 |
| geo:status | 38 |
| cn-block:TimeoutError | 16 |
| cn-block:ClientOSError | 11 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-p3ai_8oq/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-6ftjci7x/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-zvslowvv/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٽv��{��u�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: վ����N]k� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1914 |
| ConnectionRefusedError | 427 |
| gaierror | 143 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.553 | observe | 69 | 0.551 | 88 |
| Surfboard-tg-mixed | 0.308 | observe | 717 | 0.227 | 4225 |
| roosterkid-openproxylist-v2ray | 0.306 | observe | 28 | 0.286 | 150 |
| mheidari-all | 0.282 | observe | 92 | 0.196 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| DeltaKronecker-all | 0.2 | downweight | 463 | 0.119 | 4660 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 501 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.102 | downweight | 5 | 0.0 | 0 | 729 |
| moneyfly1-collectSub | 0.105 | downweight | 9 | 0.0 | 0 | 1164 |
| ninja-vless | 0.11 | downweight | 24 | 0.0 | 0 | 1791 |
| 10ium-HighSpeed | 0.114 | observe | 4 | 0.0 | 0 | 839 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 24 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| nscl5-all | 0.129 | observe | 3 | 0.0 | 0 | 984 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4536 |
| SoliSpirit-all | 0.132 | downweight | 13 | 0.0 | 0 | 3000 |
| 10ium-ScrapeCategorize-Vless | 0.138 | downweight | 9 | 0.0 | 0 | 2000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.102 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.105 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.11 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.2 | 463 | 0.119 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 3 | 3 |
| 10ium-HighSpeed | 0.0 | 0 | 4 | 4 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 5 | 5 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 9 | 9 |
| moneyfly1-collectSub | 0.0 | 0 | 9 | 9 |
| SoliSpirit-all | 0.0 | 0 | 13 | 13 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.39 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.47 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 1.68 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.4 | 0 |
| Epodonios-all | 3000 | yes | 2.89 | 0 |
| SoliSpirit-all | 3000 | yes | 1.71 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.51 | 0 |
| mheidari-all | 2000 | yes | 2.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.42 | 0 |
| barry-far-vless | 2000 | yes | 1.26 | 0 |

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
| 204 | 940 |
| geo | 114 |
| sing-box exited 1 | 75 |
| cn-block | 28 |
| speed | 18 |
