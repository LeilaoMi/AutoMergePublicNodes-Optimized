# AutoNodes 每日报告

生成时间：2026-06-09 15:00:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 39829 |
| 去重后节点数 | 15719 |
| TCP 可达数 | 1500 |
| 真测通过数 | 280 |
| verified 输出数 | 280 |
| global 输出数 | 292 |
| all 输出数 | 15719 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| generate | 31.3 |
| geo | 1.3 |
| real_test | 169.8 |
| tcp | 37.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 61 | 54 | 7 | 88.5% |
| hysteria2 | 12 | 2 | 10 | 16.7% |
| shadowsocks | 236 | 77 | 159 | 32.6% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 157 | 31 | 126 | 19.7% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 1004 | 111 | 893 | 11.1% |
| vmess | 19 | 5 | 14 | 26.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 462 |
| 204:ProxyError | 393 |
| 204:TimeoutError | 167 |
| geo:status | 56 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 47 |
| geo:status | 19 |
| cn-block:TimeoutError | 16 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:ClientOSError | 6 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 5 |
| cn-block:ProxyError | 4 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 2 |
| speed:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-w6srstyy/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-y7u5gvah/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-lizoig8g/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1894 |
| ConnectionRefusedError | 434 |
| gaierror | 161 |
| OSError | 33 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | prefer | 26 | 1.0 | 61 |
| snakem982 | 0.655 | observe | 44 | 0.659 | 62 |
| Au1rxx-base64 | 0.51 | observe | 77 | 0.506 | 93 |
| roosterkid-openproxylist-v2ray | 0.506 | observe | 22 | 0.5 | 150 |
| mheidari-all | 0.303 | observe | 101 | 0.218 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3260 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.235 | downweight | 904 | 0.154 | 4103 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.083 | downweight | 10 | 0.0 | 0 | 678 |
| moneyfly1-collectSub | 0.093 | downweight | 19 | 0.0 | 0 | 1164 |
| nscl5-all | 0.109 | downweight | 6 | 0.0 | 0 | 1026 |
| 10ium-ScrapeCategorize-Vless | 0.112 | downweight | 29 | 0.0 | 0 | 2000 |
| ninja-vless | 0.118 | downweight | 19 | 0.0 | 0 | 1791 |
| 10ium-HighSpeed | 0.123 | observe | 3 | 0.0 | 0 | 839 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4536 |
| SoliSpirit-all | 0.136 | downweight | 10 | 0.0 | 0 | 3000 |
| Epodonios-all | 0.136 | downweight | 87 | 0.046 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | xiaoji235-airport-v2ray-all | 0.083 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.093 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.109 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.112 | 29 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Epodonios-all | 0.136 | 87 | 0.046 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.136 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.159 | 125 | 0.072 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-mixed | 0.235 | 904 | 0.154 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 3 | 3 |
| nscl5-all | 0.0 | 0 | 6 | 6 |
| SoliSpirit-all | 0.0 | 0 | 10 | 10 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| moneyfly1-collectSub | 0.0 | 0 | 19 | 19 |
| ninja-vless | 0.0 | 0 | 19 | 19 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 29 | 29 |
| Epodonios-all | 0.046 | 4 | 83 | 87 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4764 | yes | 3.17 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.41 | 0 |
| Surfboard-tg-mixed | 4103 | yes | 1.6 | 0 |
| Surfboard-tg-vless | 3260 | yes | 1.88 | 0 |
| Epodonios-all | 3000 | yes | 1.78 | 0 |
| SoliSpirit-all | 3000 | yes | 1.36 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.16 | 0 |
| mheidari-all | 2000 | yes | 2.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.08 | 0 |
| barry-far-vless | 2000 | yes | 0.89 | 0 |

## 趋势报警

无趋势报警。

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
| 204 | 1022 |
| geo | 79 |
| sing-box exited 1 | 73 |
| cn-block | 29 |
| speed | 17 |
