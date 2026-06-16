# AutoNodes 每日报告

生成时间：2026-06-16 17:00:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/12 |
| 清理建议：优先/观察 | 1/31 |
| 原始节点数 | 43641 |
| 去重后节点数 | 18167 |
| TCP 可达数 | 1500 |
| 真测通过数 | 227 |
| verified 输出数 | 227 |
| global 输出数 | 235 |
| all 输出数 | 18167 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| generate | 36.9 |
| geo | 1.2 |
| real_test | 199.2 |
| tcp | 38.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 19 | 2 | 17 | 10.5% |
| shadowsocks | 394 | 61 | 333 | 15.5% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 7 | 0 | 7 | 0.0% |
| trojan | 243 | 26 | 217 | 10.7% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 770 | 91 | 679 | 11.8% |
| vmess | 14 | 5 | 9 | 35.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 432 |
| 204:ProxyError | 416 |
| 204:TimeoutError | 119 |
| geo:status | 97 |
| geo:status | 61 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 59 |
| cn-block:TimeoutError | 13 |
| cn-block:ClientOSError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:ClientOSError | 6 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 4 |
| geo:ProxyError | 3 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: i�s���G�k� | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: {� | צ����� | 2 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: m�<�� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-k4f1jotd/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-dtfiqev9/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1876 |
| ConnectionRefusedError | 448 |
| gaierror | 193 |
| OSError | 27 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.898 | prefer | 46 | 0.913 | 52 |
| Au1rxx-base64 | 0.524 | observe | 73 | 0.521 | 104 |
| roosterkid-openproxylist-v2ray | 0.367 | observe | 34 | 0.353 | 150 |
| abc-configs-readme-latest30 | 0.367 | observe | 5 | 0.8 | 18 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3446 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| Barabama-yudou | 0.214 | observe | 2 | 0.5 | 166 |
| Surfboard-tg-mixed | 0.209 | downweight | 758 | 0.128 | 4425 |
| mheidari-all | 0.2 | downweight | 90 | 0.111 | 2000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| ts-sf | 0.056 | downweight | 12 | 0.0 | 0 | 81 |
| moneyfly1-collectSub | 0.081 | downweight | 27 | 0.0 | 0 | 1164 |
| 10ium-HighSpeed | 0.102 | downweight | 6 | 0.0 | 0 | 839 |
| SoliSpirit-all | 0.106 | downweight | 37 | 0.0 | 0 | 3000 |
| nscl5-all | 0.114 | downweight | 5 | 0.0 | 0 | 1017 |
| ninja-vless | 0.12 | downweight | 16 | 0.0 | 0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.121 | downweight | 19 | 0.053 | 0 | 729 |
| ninja-tuic | 0.128 | observe | 1 | 0.0 | 0 | 1 |
| chromego_merge | 0.129 | observe | 1 | 0.0 | 0 | 50 |
| mahdibland-V2RayAggregator | 0.129 | downweight | 15 | 0.0 | 0 | 4484 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ts-sf | 0.056 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.081 | 27 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.102 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.106 | 37 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.114 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.12 | 16 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.121 | 19 | 0.053 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.133 | 12 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.145 | 336 | 0.062 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| chromego_merge | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| 10ium-HighSpeed | 0.0 | 0 | 6 | 6 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 12 | 12 |
| ts-sf | 0.0 | 0 | 12 | 12 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 15 | 15 |
| ninja-vless | 0.0 | 0 | 16 | 16 |
| moneyfly1-collectSub | 0.0 | 0 | 27 | 27 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 8110 | yes | 3.55 | 0 |
| mahdibland-V2RayAggregator | 4484 | yes | 0.37 | 0 |
| Surfboard-tg-mixed | 4425 | yes | 1.9 | 0 |
| Surfboard-tg-vless | 3446 | yes | 2.02 | 0 |
| Epodonios-all | 3000 | yes | 0.61 | 0 |
| SoliSpirit-all | 3000 | yes | 2.29 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.73 | 0 |
| mheidari-all | 2000 | yes | 3.13 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.81 | 0 |
| barry-far-vless | 2000 | yes | 1.09 | 0 |

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
| 204 | 967 |
| geo | 164 |
| sing-box exited 1 | 107 |
| cn-block | 27 |
| speed | 8 |
