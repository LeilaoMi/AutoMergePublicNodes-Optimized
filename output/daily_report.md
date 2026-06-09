# AutoNodes 每日报告

生成时间：2026-06-09 20:13:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/13 |
| 清理建议：优先/观察 | 1/30 |
| 原始节点数 | 39793 |
| 去重后节点数 | 15819 |
| TCP 可达数 | 1500 |
| 真测通过数 | 251 |
| verified 输出数 | 251 |
| global 输出数 | 265 |
| all 输出数 | 15819 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.7 |
| generate | 22.9 |
| geo | 1.2 |
| real_test | 161.6 |
| tcp | 39.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 45 | 43 | 2 | 95.6% |
| hysteria2 | 12 | 1 | 11 | 8.3% |
| shadowsocks | 374 | 81 | 293 | 21.7% |
| shadowsocksr | 1 | 0 | 1 | 0.0% |
| socks | 7 | 0 | 7 | 0.0% |
| trojan | 185 | 20 | 165 | 10.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 858 | 103 | 755 | 12.0% |
| vmess | 17 | 3 | 14 | 17.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 470 |
| 204:ProxyError | 440 |
| 204:TimeoutError | 138 |
| geo:status | 57 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 38 |
| geo:status | 21 |
| cn-block:TimeoutError | 18 |
| cn-block:ClientOSError | 12 |
| speed:TimeoutError | 9 |
| speed:ClientOSError | 8 |
| geo:TimeoutError | 8 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-1_f9_1bt/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-fjcoc4z6/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-f23iijo_/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: o���mu����� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1885 |
| ConnectionRefusedError | 444 |
| gaierror | 176 |
| OSError | 32 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.821 | prefer | 53 | 0.83 | 61 |
| Au1rxx-base64 | 0.528 | observe | 59 | 0.525 | 93 |
| roosterkid-openproxylist-v2ray | 0.441 | observe | 21 | 0.429 | 150 |
| mheidari-all | 0.286 | observe | 100 | 0.2 | 2000 |
| abc-configs-readme-latest30 | 0.269 | observe | 3 | 0.667 | 20 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Surfboard-tg-mixed | 0.244 | downweight | 743 | 0.163 | 4132 |
| Epodonios-all | 0.207 | observe | 1 | 0.0 | 3000 |
| chromego_merge | 0.195 | downweight | 7 | 0.286 | 55 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| ts-sf | 0.059 | downweight | 10 | 0.0 | 0 | 59 |
| moneyfly1-collectSub | 0.069 | downweight | 43 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.082 | downweight | 11 | 0.0 | 0 | 678 |
| Barabama-yudou | 0.087 | observe | 4 | 0.0 | 0 | 166 |
| 10ium-HighSpeed | 0.102 | downweight | 6 | 0.0 | 0 | 839 |
| Surfboard-tg-vless | 0.109 | downweight | 103 | 0.019 | 0 | 3238 |
| SoliSpirit-all | 0.117 | downweight | 25 | 0.0 | 0 | 3000 |
| ninja-vless | 0.123 | downweight | 13 | 0.0 | 0 | 1791 |
| Barabama-we | 0.128 | observe | 1 | 0.0 | 0 | 23 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ts-sf | 0.059 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.069 | 43 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.082 | 11 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.102 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Surfboard-tg-vless | 0.109 | 103 | 0.019 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.117 | 25 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.123 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.148 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.154 | 269 | 0.071 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Barabama-we | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 4 | 4 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 6 | 6 |
| 10ium-HighSpeed | 0.0 | 0 | 6 | 6 |
| ts-sf | 0.0 | 0 | 10 | 10 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 11 | 11 |
| ninja-vless | 0.0 | 0 | 13 | 13 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 15 | 15 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4764 | yes | 2.45 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.24 | 0 |
| Surfboard-tg-mixed | 4132 | yes | 1.68 | 0 |
| Surfboard-tg-vless | 3238 | yes | 1.38 | 0 |
| Epodonios-all | 3000 | yes | 1.57 | 0 |
| SoliSpirit-all | 3000 | yes | 1.12 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.95 | 0 |
| mheidari-all | 2000 | yes | 2.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.75 | 0 |
| barry-far-vless | 2000 | yes | 0.9 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| hysteria2 | 0.083 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 1048 |
| geo | 87 |
| sing-box exited 1 | 64 |
| cn-block | 33 |
| speed | 17 |
