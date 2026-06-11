# AutoNodes 每日报告

生成时间：2026-06-11 23:11:17

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/12 |
| 清理建议：优先/观察 | 1/31 |
| 原始节点数 | 39941 |
| 去重后节点数 | 15192 |
| TCP 可达数 | 1500 |
| 真测通过数 | 288 |
| verified 输出数 | 288 |
| global 输出数 | 298 |
| all 输出数 | 15192 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| generate | 26.3 |
| geo | 1.2 |
| real_test | 151.0 |
| tcp | 38.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 8 | 1 | 7 | 12.5% |
| shadowsocks | 379 | 75 | 304 | 19.8% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 28 | 20 | 8 | 71.4% |
| trojan | 128 | 33 | 95 | 25.8% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 889 | 110 | 779 | 12.4% |
| vmess | 15 | 7 | 8 | 46.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 461 |
| 204:ClientOSError | 378 |
| geo:status | 107 |
| 204:TimeoutError | 95 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 59 |
| geo:status | 30 |
| cn-block:TimeoutError | 19 |
| cn-block:ClientOSError | 12 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:ClientOSError | 7 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �� | 2 |
| speed:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: i�s���G�k� | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-radmjiyv/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-talkmtuy/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-ygdhhvox/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1851 |
| ConnectionRefusedError | 432 |
| gaierror | 182 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | prefer | 43 | 0.977 | 52 |
| Au1rxx-base64 | 0.566 | observe | 62 | 0.565 | 79 |
| mheidari-all | 0.3 | observe | 98 | 0.214 | 2000 |
| roosterkid-openproxylist-v2ray | 0.296 | observe | 29 | 0.276 | 150 |
| Surfboard-tg-mixed | 0.281 | observe | 751 | 0.2 | 4225 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3224 |
| DeltaKronecker-all | 0.204 | downweight | 216 | 0.12 | 4660 |
| Epodonios-all | 0.184 | observe | 2 | 0.0 | 3000 |
| MatinGhanbari-super-sub | 0.183 | observe | 0 | None | 199 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.069 | downweight | 6 | 0.0 | 0 | 23 |
| mfuu-v2ray | 0.072 | downweight | 10 | 0.0 | 0 | 387 |
| 10ium-HighSpeed | 0.072 | downweight | 76 | 0.026 | 0 | 839 |
| xiaoji235-airport-v2ray-all | 0.076 | downweight | 18 | 0.0 | 0 | 729 |
| moneyfly1-collectSub | 0.093 | downweight | 19 | 0.0 | 0 | 1164 |
| Barabama-yudou | 0.094 | downweight | 21 | 0.048 | 0 | 166 |
| abc-configs-readme-latest30 | 0.105 | observe | 2 | 0.0 | 0 | 24 |
| ermaozi | 0.105 | observe | 2 | 0.0 | 0 | 29 |
| 10ium-ScrapeCategorize-Vless | 0.109 | downweight | 33 | 0.0 | 0 | 2000 |
| ninja-vless | 0.113 | downweight | 22 | 0.0 | 0 | 1791 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | Barabama-we | 0.069 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-HighSpeed | 0.072 | 76 | 0.026 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mfuu-v2ray | 0.072 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.076 | 18 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.093 | 19 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-yudou | 0.094 | 21 | 0.048 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.109 | 33 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.113 | 22 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.116 | 26 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.132 | 13 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| barry-far-Sub2 | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 2 | 2 |
| Epodonios-all | 0.0 | 0 | 2 | 2 |
| barry-far-Sub1 | 0.0 | 0 | 2 | 2 |
| ermaozi | 0.0 | 0 | 2 | 2 |
| nscl5-all | 0.0 | 0 | 4 | 4 |
| Barabama-we | 0.0 | 0 | 6 | 6 |
| mfuu-v2ray | 0.0 | 0 | 10 | 10 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 13 | 13 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 4660 | yes | 2.55 | 0 |
| mahdibland-V2RayAggregator | 4536 | yes | 1.31 | 0 |
| Surfboard-tg-mixed | 4225 | yes | 2.35 | 0 |
| Surfboard-tg-vless | 3224 | yes | 1.45 | 0 |
| Epodonios-all | 3000 | yes | 2.84 | 0 |
| SoliSpirit-all | 3000 | yes | 1.76 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.59 | 0 |
| mheidari-all | 2000 | yes | 2.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.76 | 0 |
| barry-far-vless | 2000 | yes | 0.53 | 0 |

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
| 204 | 934 |
| geo | 140 |
| sing-box exited 1 | 98 |
| cn-block | 31 |
| speed | 9 |
