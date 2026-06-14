# AutoNodes 每日报告

生成时间：2026-06-14 02:31:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/10 |
| 清理建议：优先/观察 | 1/33 |
| 原始节点数 | 40271 |
| 去重后节点数 | 15512 |
| TCP 可达数 | 1500 |
| 真测通过数 | 400 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 15512 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| generate | 15.4 |
| geo | 1.2 |
| real_test | 166.9 |
| tcp | 35.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 10 | 2 | 8 | 20.0% |
| shadowsocks | 216 | 67 | 149 | 31.0% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 439 | 80 | 359 | 18.2% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 763 | 200 | 563 | 26.2% |
| vmess | 17 | 7 | 10 | 41.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 541 |
| 204:ProxyError | 288 |
| speed:TimeoutError | 59 |
| geo:status | 58 |
| 204:TimeoutError | 55 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 33 |
| speed:ClientOSError | 22 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:TimeoutError | 8 |
| geo:TimeoutError | 6 |
| geo:status | 3 |
| cn-block:ClientOSError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: decode public_key: illegal base64 data at input byte 44 | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-7308_xqo/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-o02tz_fm/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-9pnqj1kq/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: վ����N]k� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ���ӧ\�^���5�߽�o>�~�w��w� | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1852 |
| ConnectionRefusedError | 452 |
| gaierror | 212 |
| OSError | 34 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.938 | prefer | 45 | 0.956 | 52 |
| roosterkid-openproxylist-v2ray | 0.582 | observe | 31 | 0.581 | 150 |
| Au1rxx-base64 | 0.481 | observe | 103 | 0.476 | 130 |
| Surfboard-tg-mixed | 0.392 | observe | 664 | 0.312 | 4199 |
| mheidari-all | 0.288 | observe | 99 | 0.202 | 2000 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3299 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| DeltaKronecker-all | 0.218 | downweight | 425 | 0.136 | 4955 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| moneyfly1-collectSub | 0.074 | downweight | 34 | 0.0 | 0 | 1164 |
| 10ium-HighSpeed | 0.107 | downweight | 5 | 0.0 | 0 | 839 |
| ninja-vless | 0.121 | downweight | 15 | 0.0 | 0 | 1791 |
| abc-configs-readme-latest30 | 0.128 | observe | 1 | 0.0 | 0 | 17 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.128 | downweight | 16 | 0.0 | 0 | 2000 |
| mahdibland-V2RayAggregator | 0.132 | downweight | 13 | 0.0 | 0 | 4566 |
| Barabama-yudou | 0.137 | downweight | 21 | 0.095 | 0 | 166 |
| SoliSpirit-all | 0.138 | downweight | 9 | 0.0 | 0 | 3000 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | moneyfly1-collectSub | 0.074 | 34 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.107 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.121 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.128 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.137 | 21 | 0.095 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.138 | 9 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.181 | 13 | 0.154 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.191 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.218 | 425 | 0.136 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 5 | 5 |
| SoliSpirit-all | 0.0 | 0 | 9 | 9 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |
| ninja-vless | 0.0 | 0 | 15 | 15 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 16 | 16 |
| moneyfly1-collectSub | 0.0 | 0 | 34 | 34 |
| Barabama-yudou | 0.095 | 2 | 19 | 21 |
| DeltaKronecker-all | 0.136 | 58 | 367 | 425 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4955 | yes | 2.85 | 0 |
| mahdibland-V2RayAggregator | 4566 | yes | 1.45 | 0 |
| Surfboard-tg-mixed | 4199 | yes | 2.04 | 0 |
| Surfboard-tg-vless | 3299 | yes | 1.37 | 0 |
| Epodonios-all | 3000 | yes | 1.67 | 0 |
| SoliSpirit-all | 3000 | yes | 1.97 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.19 | 0 |
| mheidari-all | 2000 | yes | 2.67 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.52 | 0 |
| barry-far-vless | 2000 | yes | 0.95 | 0 |

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
| 204 | 884 |
| speed | 81 |
| geo | 68 |
| sing-box exited 1 | 56 |
| cn-block | 11 |
