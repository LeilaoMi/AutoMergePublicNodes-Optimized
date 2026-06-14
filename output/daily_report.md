# AutoNodes 每日报告

生成时间：2026-06-14 04:20:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/7 |
| 清理建议：优先/观察 | 1/36 |
| 原始节点数 | 40117 |
| 去重后节点数 | 15438 |
| TCP 可达数 | 1500 |
| 真测通过数 | 359 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15438 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| generate | 35.4 |
| geo | 1.3 |
| real_test | 204.3 |
| tcp | 34.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 10 | 2 | 8 | 20.0% |
| shadowsocks | 346 | 75 | 271 | 21.7% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 149 | 39 | 110 | 26.2% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 922 | 193 | 729 | 20.9% |
| vmess | 17 | 7 | 10 | 41.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 378 |
| 204:ClientOSError | 364 |
| speed:TimeoutError | 118 |
| geo:status | 68 |
| 204:TimeoutError | 67 |
| speed:ClientOSError | 64 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 36 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 2 |
| geo:status | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-uj05kz0j/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-3yo9w_vv/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-pygf4iou/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ݽ5k����^�� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���s�F�������>�m�s� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ٭���7��v�� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1765 |
| ConnectionRefusedError | 447 |
| gaierror | 219 |
| OSError | 40 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | prefer | 46 | 0.935 | 52 |
| roosterkid-openproxylist-v2ray | 0.651 | observe | 29 | 0.655 | 150 |
| Au1rxx-base64 | 0.496 | observe | 104 | 0.49 | 136 |
| Surfboard-tg-mixed | 0.344 | observe | 679 | 0.264 | 4181 |
| Epodonios-all | 0.335 | observe | 53 | 0.245 | 3000 |
| Barabama-yudou | 0.275 | observe | 3 | 0.667 | 166 |
| mheidari-all | 0.255 | observe | 95 | 0.168 | 2000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3160 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.072 | downweight | 37 | 0.0 | 0 | 1164 |
| ninja-vless | 0.101 | downweight | 32 | 0.0 | 0 | 1791 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| mahdibland-V2RayAggregator | 0.13 | downweight | 14 | 0.0 | 0 | 4566 |
| nscl5-all | 0.134 | observe | 3 | 0.0 | 0 | 1123 |
| xiaoji235-airport-v2ray-all | 0.135 | downweight | 11 | 0.091 | 0 | 656 |
| 10ium-ScrapeCategorize-Vless | 0.136 | downweight | 10 | 0.0 | 0 | 2000 |
| SoliSpirit-all | 0.136 | downweight | 10 | 0.0 | 0 | 3000 |
| 10ium-HighSpeed | 0.137 | observe | 2 | 0.0 | 0 | 839 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.072 | 37 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.101 | 32 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.135 | 11 | 0.091 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.136 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.136 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.177 | 371 | 0.094 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 3 | 3 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 10 | 10 |
| SoliSpirit-all | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| ninja-vless | 0.0 | 0 | 32 | 32 |
| moneyfly1-collectSub | 0.0 | 0 | 37 | 37 |
| xiaoji235-airport-v2ray-all | 0.091 | 1 | 10 | 11 |
| DeltaKronecker-all | 0.094 | 35 | 336 | 371 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4955 | yes | 3.38 | 0 |
| mahdibland-V2RayAggregator | 4566 | yes | 0.81 | 0 |
| Surfboard-tg-mixed | 4181 | yes | 2.49 | 0 |
| Surfboard-tg-vless | 3160 | yes | 2.34 | 0 |
| Epodonios-all | 3000 | yes | 1.72 | 0 |
| SoliSpirit-all | 3000 | yes | 2.85 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 2.05 | 0 |
| mheidari-all | 2000 | yes | 2.86 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.89 | 0 |
| barry-far-vless | 2000 | yes | 1.69 | 0 |

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
| 204 | 809 |
| speed | 182 |
| geo | 72 |
| sing-box exited 1 | 60 |
| cn-block | 18 |
