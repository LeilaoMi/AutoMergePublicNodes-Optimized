# AutoNodes 每日报告

生成时间：2026-06-11 23:34:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/8 |
| 清理建议：优先/观察 | 1/35 |
| 原始节点数 | 39955 |
| 去重后节点数 | 15027 |
| TCP 可达数 | 1500 |
| 真测通过数 | 338 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15027 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.6 |
| generate | 20.0 |
| geo | 1.2 |
| real_test | 127.1 |
| tcp | 35.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 6 | 1 | 5 | 16.7% |
| shadowsocks | 216 | 61 | 155 | 28.2% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 28 | 20 | 8 | 71.4% |
| trojan | 495 | 86 | 409 | 17.4% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 687 | 121 | 566 | 17.6% |
| vmess | 15 | 7 | 8 | 46.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 571 |
| 204:ProxyError | 306 |
| geo:status | 85 |
| 204:TimeoutError | 57 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 50 |
| geo:status | 30 |
| speed:ClientOSError | 15 |
| cn-block:ClientOSError | 10 |
| cn-block:TimeoutError | 10 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| speed:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-g807djuo/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-nl4heonc/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-y4932bw6/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٽv��{��u�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1860 |
| ConnectionRefusedError | 432 |
| gaierror | 169 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.606 | observe | 71 | 0.606 | 88 |
| roosterkid-openproxylist-v2ray | 0.329 | observe | 29 | 0.31 | 150 |
| Surfboard-tg-mixed | 0.307 | observe | 698 | 0.226 | 4225 |
| mheidari-all | 0.293 | observe | 92 | 0.207 | 2000 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| DeltaKronecker-all | 0.216 | downweight | 492 | 0.134 | 4660 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.097 | downweight | 6 | 0.0 | 0 | 729 |
| ninja-vless | 0.11 | downweight | 24 | 0.0 | 0 | 1791 |
| moneyfly1-collectSub | 0.111 | downweight | 7 | 0.0 | 0 | 1164 |
| nscl5-all | 0.113 | downweight | 5 | 0.0 | 0 | 984 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 24 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4536 |
| SoliSpirit-all | 0.138 | downweight | 9 | 0.0 | 0 | 3000 |
| 10ium-ScrapeCategorize-Vless | 0.144 | downweight | 7 | 0.0 | 0 | 2000 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.097 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.11 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.111 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.113 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.144 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.216 | 492 | 0.134 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 6 | 6 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 7 | 7 |
| moneyfly1-collectSub | 0.0 | 0 | 7 | 7 |
| SoliSpirit-all | 0.0 | 0 | 9 | 9 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| ninja-vless | 0.0 | 0 | 24 | 24 |
| DeltaKronecker-all | 0.134 | 66 | 426 | 492 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.49 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 0.4 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 1.68 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.45 | 0 |
| Epodonios-all | 3000 | yes | 2.47 | 0 |
| SoliSpirit-all | 3000 | yes | 1.72 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.53 | 0 |
| mheidari-all | 2000 | yes | 2.32 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.48 | 0 |
| barry-far-vless | 2000 | yes | 1.2 | 0 |

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
| 204 | 934 |
| geo | 118 |
| sing-box exited 1 | 70 |
| cn-block | 22 |
| speed | 18 |
