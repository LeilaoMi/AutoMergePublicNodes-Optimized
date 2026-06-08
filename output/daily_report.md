# AutoNodes 每日报告

生成时间：2026-06-08 11:03:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 0/34 |
| 原始节点数 | 38896 |
| 去重后节点数 | 15206 |
| TCP 可达数 | 1500 |
| 真测通过数 | 226 |
| verified 输出数 | 226 |
| global 输出数 | 242 |
| all 输出数 | 15206 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.4 |
| generate | 24.6 |
| geo | 1.2 |
| real_test | 146.7 |
| tcp | 37.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 7 | 16 | 30.4% |
| hysteria2 | 14 | 2 | 12 | 14.3% |
| shadowsocks | 359 | 78 | 281 | 21.7% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 147 | 11 | 136 | 7.5% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 928 | 119 | 809 | 12.8% |
| vmess | 18 | 9 | 9 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 531 |
| 204:ClientOSError | 406 |
| 204:TimeoutError | 106 |
| speed:TimeoutError | 57 |
| geo:status | 36 |
| speed:ClientOSError | 30 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 30 |
| cn-block:TimeoutError | 19 |
| geo:status | 14 |
| cn-block:ClientOSError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| geo:TimeoutError | 4 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 2 |
| geo:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-i1yynwxp/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-0iqgwdsj/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-t2i0d46y/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1903 |
| ConnectionRefusedError | 405 |
| gaierror | 169 |
| OSError | 26 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.607 | observe | 51 | 0.608 | 81 |
| roosterkid-openproxylist-v2ray | 0.441 | observe | 11 | 0.636 | 150 |
| snakem982 | 0.35 | observe | 21 | 0.333 | 47 |
| mheidari-all | 0.328 | observe | 107 | 0.243 | 2000 |
| Surfboard-tg-mixed | 0.265 | observe | 691 | 0.184 | 3742 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 2910 |
| Barabama-yudou | 0.214 | observe | 2 | 0.5 | 166 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.077 | downweight | 31 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.078 | downweight | 11 | 0.0 | 0 | 584 |
| 10ium-HighSpeed | 0.091 | downweight | 68 | 0.044 | 0 | 839 |
| nscl5-all | 0.095 | downweight | 10 | 0.0 | 0 | 957 |
| ninja-vless | 0.122 | downweight | 14 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.128 | downweight | 17 | 0.0 | 0 | 2000 |
| barry-far-vless | 0.13 | downweight | 14 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4533 |
| SoliSpirit-all | 0.133 | downweight | 12 | 0.0 | 0 | 3000 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.077 | 31 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.078 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.091 | 68 | 0.044 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.095 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.122 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.128 | 17 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | barry-far-vless | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.133 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.139 | 425 | 0.056 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 10 | 10 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 11 | 11 |
| SoliSpirit-all | 0.0 | 0 | 12 | 12 |
| ninja-vless | 0.0 | 0 | 14 | 14 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| barry-far-vless | 0.0 | 0 | 14 | 14 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 17 | 17 |
| moneyfly1-collectSub | 0.0 | 0 | 31 | 31 |
| 10ium-HighSpeed | 0.044 | 3 | 65 | 68 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4760 | yes | 2.04 | 0 |
| mahdibland-V2RayAggregator | 4533 | yes | 1.48 | 0 |
| Surfboard-tg-mixed | 3742 | yes | 1.42 | 0 |
| Epodonios-all | 3000 | yes | 2.36 | 0 |
| SoliSpirit-all | 3000 | yes | 1.81 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.09 | 0 |
| Surfboard-tg-vless | 2910 | yes | 0.89 | 0 |
| mheidari-all | 2000 | yes | 2.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.03 | 0 |
| barry-far-vless | 2000 | yes | 0.92 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| trojan | 0.075 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1043 |
| speed | 88 |
| geo | 58 |
| sing-box exited 1 | 55 |
| cn-block | 30 |
