# AutoNodes 每日报告

生成时间：2026-06-14 09:41:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/13 |
| 清理建议：优先/观察 | 1/30 |
| 原始节点数 | 40316 |
| 去重后节点数 | 15630 |
| TCP 可达数 | 1500 |
| 真测通过数 | 239 |
| verified 输出数 | 239 |
| global 输出数 | 248 |
| all 输出数 | 15630 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| generate | 16.0 |
| geo | 1.2 |
| real_test | 173.4 |
| tcp | 35.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 7 | 1 | 6 | 14.3% |
| shadowsocks | 208 | 56 | 152 | 26.9% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 452 | 28 | 424 | 6.2% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 764 | 107 | 657 | 14.0% |
| vmess | 15 | 5 | 10 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 590 |
| 204:ProxyError | 343 |
| 204:TimeoutError | 103 |
| geo:status | 58 |
| geo:status | 50 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 35 |
| speed:ClientOSError | 18 |
| cn-block:TimeoutError | 12 |
| speed:TimeoutError | 10 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 5 |
| geo:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 2 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-kwp9nkhv/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-xf_bf9fz/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-a6qqlsl9/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1839 |
| ConnectionRefusedError | 439 |
| gaierror | 195 |
| OSError | 39 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | prefer | 46 | 0.935 | 52 |
| roosterkid-openproxylist-v2ray | 0.66 | observe | 24 | 0.667 | 150 |
| Au1rxx-base64 | 0.474 | observe | 109 | 0.468 | 140 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3281 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.247 | downweight | 88 | 0.159 | 2000 |
| Surfboard-tg-mixed | 0.219 | downweight | 637 | 0.138 | 4190 |
| Epodonios-all | 0.202 | downweight | 72 | 0.111 | 3000 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 493 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| mfuu-v2ray | 0.059 | downweight | 11 | 0.0 | 0 | 118 |
| moneyfly1-collectSub | 0.071 | downweight | 39 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.094 | downweight | 6 | 0.0 | 0 | 656 |
| Barabama-yudou | 0.098 | downweight | 20 | 0.05 | 0 | 166 |
| nscl5-all | 0.109 | downweight | 7 | 0.0 | 0 | 1123 |
| ninja-vless | 0.117 | downweight | 20 | 0.0 | 0 | 1791 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 12 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 18 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| DeltaKronecker-all | 0.129 | downweight | 382 | 0.047 | 0 | 5188 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | mfuu-v2ray | 0.059 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.071 | 39 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.094 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.098 | 20 | 0.05 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.109 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.117 | 20 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.129 | 382 | 0.047 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.134 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 2 | 2 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 6 | 6 |
| nscl5-all | 0.0 | 0 | 7 | 7 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 9 | 9 |
| SoliSpirit-all | 0.0 | 0 | 11 | 11 |
| mfuu-v2ray | 0.0 | 0 | 11 | 11 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 5188 | yes | 2.84 | 0 |
| mahdibland-V2RayAggregator | 4511 | yes | 0.8 | 0 |
| Surfboard-tg-mixed | 4190 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 3281 | yes | 2.1 | 0 |
| Epodonios-all | 3000 | yes | 1.57 | 0 |
| SoliSpirit-all | 3000 | yes | 1.66 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.28 | 0 |
| mheidari-all | 2000 | yes | 2.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.18 | 0 |
| barry-far-vless | 2000 | yes | 1.5 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| trojan | 0.062 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1036 |
| geo | 116 |
| sing-box exited 1 | 57 |
| speed | 30 |
| cn-block | 22 |
