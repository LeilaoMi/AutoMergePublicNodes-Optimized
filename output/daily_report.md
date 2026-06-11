# AutoNodes 每日报告

生成时间：2026-06-11 23:42:48

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
| 真测通过数 | 301 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15027 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 25.1 |
| geo | 1.2 |
| real_test | 138.6 |
| tcp | 35.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 8 | 1 | 7 | 12.5% |
| shadowsocks | 363 | 70 | 293 | 19.3% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 32 | 20 | 12 | 62.5% |
| trojan | 124 | 34 | 90 | 27.4% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 905 | 127 | 778 | 14.0% |
| vmess | 15 | 7 | 8 | 46.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 505 |
| 204:ClientOSError | 337 |
| geo:status | 82 |
| 204:TimeoutError | 67 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 54 |
| geo:status | 42 |
| speed:ClientOSError | 40 |
| cn-block:TimeoutError | 15 |
| cn-block:ClientOSError | 12 |
| speed:TimeoutError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| geo:TimeoutError | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-pf46dcto/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-6cm_743_/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ru1m_4_t/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1873 |
| ConnectionRefusedError | 426 |
| gaierror | 161 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.524 | observe | 71 | 0.521 | 88 |
| roosterkid-openproxylist-v2ray | 0.329 | observe | 29 | 0.31 | 150 |
| Surfboard-tg-mixed | 0.298 | observe | 741 | 0.217 | 4225 |
| mheidari-all | 0.269 | observe | 93 | 0.183 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 501 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 473 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.093 | downweight | 7 | 0.0 | 0 | 729 |
| nscl5-all | 0.107 | downweight | 6 | 0.0 | 0 | 984 |
| moneyfly1-collectSub | 0.108 | downweight | 8 | 0.0 | 0 | 1164 |
| 10ium-HighSpeed | 0.114 | observe | 4 | 0.0 | 0 | 839 |
| ninja-vless | 0.115 | downweight | 21 | 0.0 | 0 | 1791 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 24 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.128 | downweight | 16 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4536 |
| SoliSpirit-all | 0.133 | downweight | 12 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.093 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.107 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.108 | 8 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.115 | 21 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.128 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.133 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.161 | 428 | 0.079 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ts-sf | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 2 | 2 |
| 10ium-HighSpeed | 0.0 | 0 | 4 | 4 |
| nscl5-all | 0.0 | 0 | 6 | 6 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 7 | 7 |
| moneyfly1-collectSub | 0.0 | 0 | 8 | 8 |
| SoliSpirit-all | 0.0 | 0 | 12 | 12 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 16 | 16 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.87 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.42 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 1.87 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.57 | 0 |
| Epodonios-all | 3000 | yes | 2.61 | 0 |
| SoliSpirit-all | 3000 | yes | 2.18 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.32 | 0 |
| mheidari-all | 2000 | yes | 2.43 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.51 | 0 |
| barry-far-vless | 2000 | yes | 1.14 | 0 |

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
| 204 | 909 |
| geo | 130 |
| sing-box exited 1 | 78 |
| speed | 53 |
| cn-block | 29 |
