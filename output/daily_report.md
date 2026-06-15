# AutoNodes 每日报告

生成时间：2026-06-15 04:31:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/11 |
| 清理建议：优先/观察 | 1/32 |
| 原始节点数 | 40677 |
| 去重后节点数 | 15750 |
| TCP 可达数 | 1500 |
| 真测通过数 | 395 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15750 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| generate | 36.0 |
| geo | 1.2 |
| real_test | 230.2 |
| tcp | 38.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 18 | 3 | 15 | 16.7% |
| shadowsocks | 283 | 75 | 208 | 26.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 197 | 60 | 137 | 30.5% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 933 | 209 | 724 | 22.4% |
| vmess | 14 | 4 | 10 | 28.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 423 |
| 204:ProxyError | 307 |
| 204:TimeoutError | 100 |
| geo:status | 58 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 46 |
| speed:TimeoutError | 43 |
| speed:ClientOSError | 38 |
| cn-block:TimeoutError | 17 |
| geo:status | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 7 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: {� | צ����� | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 2 |
| geo:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-0uuaiu9d/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ahthrvow/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-vcty46ej/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1880 |
| ConnectionRefusedError | 440 |
| gaierror | 199 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | prefer | 46 | 0.935 | 52 |
| roosterkid-openproxylist-v2ray | 0.613 | observe | 26 | 0.615 | 150 |
| Au1rxx-base64 | 0.555 | observe | 98 | 0.551 | 131 |
| Surfboard-tg-mixed | 0.356 | observe | 769 | 0.276 | 4432 |
| barry-far-vless | 0.335 | observe | 1 | 1.0 | 2000 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| Epodonios-all | 0.285 | observe | 42 | 0.19 | 3000 |
| mheidari-all | 0.263 | observe | 91 | 0.176 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3330 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| ts-sf | 0.066 | downweight | 7 | 0.0 | 0 | 57 |
| mfuu-v2ray | 0.068 | downweight | 9 | 0.0 | 0 | 252 |
| Barabama-we | 0.069 | downweight | 6 | 0.0 | 0 | 23 |
| moneyfly1-collectSub | 0.085 | downweight | 24 | 0.0 | 0 | 1164 |
| ermaozi | 0.091 | observe | 3 | 0.0 | 0 | 29 |
| SoliSpirit-all | 0.112 | downweight | 29 | 0.0 | 0 | 3000 |
| 10ium-HighSpeed | 0.114 | observe | 4 | 0.0 | 0 | 839 |
| xiaoji235-airport-v2ray-all | 0.115 | downweight | 21 | 0.048 | 0 | 703 |
| ninja-vless | 0.118 | downweight | 18 | 0.0 | 0 | 1791 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 22 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ts-sf | 0.066 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mfuu-v2ray | 0.068 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-we | 0.069 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.085 | 24 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.112 | 29 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.115 | 21 | 0.048 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.118 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.192 | 117 | 0.145 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| Au1rxx-clash | 0.0 | 0 | 1 | 1 |
| chromego_merge | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.0 | 0 | 3 | 3 |
| 10ium-HighSpeed | 0.0 | 0 | 4 | 4 |
| Barabama-we | 0.0 | 0 | 6 | 6 |
| ts-sf | 0.0 | 0 | 7 | 7 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 9 | 9 |
| mfuu-v2ray | 0.0 | 0 | 9 | 9 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 5188 | yes | 2.33 | 0 |
| mahdibland-V2RayAggregator | 4511 | yes | 1.05 | 0 |
| Surfboard-tg-mixed | 4432 | yes | 1.82 | 0 |
| Surfboard-tg-vless | 3330 | yes | 1.63 | 0 |
| Epodonios-all | 3000 | yes | 2.17 | 0 |
| SoliSpirit-all | 3000 | yes | 1.75 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.9 | 0 |
| mheidari-all | 2000 | yes | 3.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.39 | 0 |
| barry-far-vless | 2000 | yes | 0.55 | 0 |

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
| 204 | 830 |
| sing-box exited 1 | 91 |
| speed | 81 |
| geo | 75 |
| cn-block | 28 |
