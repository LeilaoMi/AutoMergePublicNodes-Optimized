# AutoNodes 每日报告

生成时间：2026-06-07 04:10:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/8 |
| 清理建议：优先/观察 | 0/36 |
| 原始节点数 | 39721 |
| 去重后节点数 | 15270 |
| TCP 可达数 | 1500 |
| 真测通过数 | 358 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15270 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| generate | 25.6 |
| geo | 1.2 |
| real_test | 157.1 |
| tcp | 35.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 7 | 16 | 30.4% |
| hysteria2 | 18 | 5 | 13 | 27.8% |
| shadowsocks | 351 | 100 | 251 | 28.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 218 | 56 | 162 | 25.7% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 863 | 182 | 681 | 21.1% |
| vmess | 16 | 7 | 9 | 43.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 460 |
| 204:ProxyError | 431 |
| 204:TimeoutError | 88 |
| speed:TimeoutError | 39 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 23 |
| cn-block:TimeoutError | 17 |
| geo:status | 17 |
| geo:status | 15 |
| speed:ClientOSError | 13 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 4 |
| geo:TimeoutError | 2 |
| speed:ClientPayloadError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-95lkrrh0/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-f4b26s9h/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-knh_i4t6/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: s��m� | ���o� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���s�F�������>�m�s� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1688 |
| ConnectionRefusedError | 440 |
| gaierror | 214 |
| OSError | 25 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.642 | observe | 20 | 0.65 | 150 |
| mheidari-all | 0.433 | observe | 100 | 0.35 | 2000 |
| Au1rxx-base64 | 0.389 | observe | 76 | 0.382 | 103 |
| Surfboard-tg-mixed | 0.338 | observe | 897 | 0.258 | 4296 |
| snakem982 | 0.335 | observe | 25 | 0.32 | 47 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3300 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.069 | downweight | 42 | 0.0 | 0 | 1164 |
| ninja-vless | 0.123 | downweight | 13 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.128 | downweight | 16 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4642 |
| SoliSpirit-all | 0.134 | downweight | 11 | 0.0 | 0 | 3000 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| tonykong-base64 | 0.175 | observe | 0 | None | 0 | 5 |
| tonykong-clash | 0.175 | observe | 0 | None | 0 | 5 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.069 | 42 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.123 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.128 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.134 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.22 | 263 | 0.137 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.227 | 14 | 0.214 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.245 | 6 | 0.333 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 11 | 11 |
| ninja-vless | 0.0 | 0 | 13 | 13 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 16 | 16 |
| moneyfly1-collectSub | 0.0 | 0 | 42 | 42 |
| DeltaKronecker-all | 0.137 | 36 | 227 | 263 |
| xiaoji235-airport-v2ray-all | 0.214 | 3 | 11 | 14 |
| Surfboard-tg-mixed | 0.258 | 231 | 666 | 897 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 4642 | yes | 1.24 | 0 |
| DeltaKronecker-all | 4517 | yes | 3.61 | 0 |
| Surfboard-tg-mixed | 4296 | yes | 1.82 | 0 |
| Surfboard-tg-vless | 3300 | yes | 1.48 | 0 |
| Epodonios-all | 3000 | yes | 2.56 | 0 |
| SoliSpirit-all | 3000 | yes | 1.61 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.08 | 0 |
| mheidari-all | 2000 | yes | 2.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.92 | 0 |
| barry-far-vless | 2000 | yes | 0.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| tuic | 0.0 |
| shadowsocksr | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 979 |
| speed | 54 |
| sing-box exited 1 | 50 |
| geo | 35 |
| cn-block | 24 |
