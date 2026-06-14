# AutoNodes 每日报告

生成时间：2026-06-14 14:10:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/13 |
| 清理建议：优先/观察 | 1/30 |
| 原始节点数 | 40637 |
| 去重后节点数 | 15778 |
| TCP 可达数 | 1500 |
| 真测通过数 | 234 |
| verified 输出数 | 234 |
| global 输出数 | 240 |
| all 输出数 | 15778 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| generate | 33.6 |
| geo | 1.2 |
| real_test | 171.9 |
| tcp | 39.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 44 | 42 | 2 | 95.5% |
| hysteria2 | 10 | 2 | 8 | 20.0% |
| shadowsocks | 380 | 66 | 314 | 17.4% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 5 | 0 | 5 | 0.0% |
| trojan | 175 | 19 | 156 | 10.9% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 862 | 100 | 762 | 11.6% |
| vmess | 15 | 5 | 10 | 33.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 471 |
| 204:ClientOSError | 406 |
| 204:TimeoutError | 113 |
| geo:status | 75 |
| geo:status | 58 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 46 |
| cn-block:TimeoutError | 12 |
| speed:ClientOSError | 11 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| cn-block:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: {� | צ����� | 3 |
| geo:TimeoutError | 3 |
| geo:ProxyError | 3 |
| geo:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: i�s���G�k� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �}x�� | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1952 |
| ConnectionRefusedError | 441 |
| gaierror | 184 |
| OSError | 39 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.898 | prefer | 46 | 0.913 | 52 |
| Au1rxx-base64 | 0.599 | observe | 72 | 0.597 | 105 |
| roosterkid-openproxylist-v2ray | 0.492 | observe | 33 | 0.485 | 150 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3454 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |
| mheidari-all | 0.22 | downweight | 91 | 0.132 | 2000 |
| Surfboard-tg-mixed | 0.217 | downweight | 686 | 0.136 | 4381 |
| barry-far-Sub2 | 0.195 | observe | 0 | None | 500 |
| barry-far-Sub1 | 0.194 | observe | 0 | None | 479 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| ts-sf | 0.053 | downweight | 14 | 0.0 | 0 | 67 |
| Barabama-we | 0.069 | downweight | 6 | 0.0 | 0 | 23 |
| moneyfly1-collectSub | 0.072 | downweight | 37 | 0.0 | 0 | 1164 |
| xiaoji235-airport-v2ray-all | 0.082 | downweight | 10 | 0.0 | 0 | 656 |
| ermaozi | 0.091 | observe | 3 | 0.0 | 0 | 29 |
| 10ium-ScrapeCategorize-Vless | 0.091 | downweight | 85 | 0.0 | 0 | 2000 |
| SoliSpirit-all | 0.104 | downweight | 39 | 0.0 | 0 | 3000 |
| 10ium-HighSpeed | 0.114 | observe | 4 | 0.0 | 0 | 839 |
| ninja-vless | 0.117 | downweight | 20 | 0.0 | 0 | 1791 |
| nscl5-all | 0.118 | downweight | 5 | 0.0 | 0 | 1123 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ts-sf | 0.053 | 14 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Barabama-we | 0.069 | 6 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | moneyfly1-collectSub | 0.072 | 37 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | xiaoji235-airport-v2ray-all | 0.082 | 10 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.091 | 85 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | SoliSpirit-all | 0.104 | 39 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | ninja-vless | 0.117 | 20 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | nscl5-all | 0.118 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | mahdibland-V2RayAggregator | 0.129 | 15 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | Epodonios-all | 0.158 | 75 | 0.067 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| chromego_merge | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.0 | 0 | 3 | 3 |
| 10ium-HighSpeed | 0.0 | 0 | 4 | 4 |
| nscl5-all | 0.0 | 0 | 5 | 5 |
| Barabama-we | 0.0 | 0 | 6 | 6 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 10 | 10 |
| ts-sf | 0.0 | 0 | 14 | 14 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 5188 | yes | 2.94 | 0 |
| mahdibland-V2RayAggregator | 4511 | yes | 0.96 | 0 |
| Surfboard-tg-mixed | 4381 | yes | 2.22 | 0 |
| Surfboard-tg-vless | 3454 | yes | 0.89 | 0 |
| Epodonios-all | 3000 | yes | 0.77 | 0 |
| SoliSpirit-all | 3000 | yes | 2.25 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.99 | 0 |
| mheidari-all | 2000 | yes | 3.08 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.5 | 0 |
| barry-far-vless | 2000 | yes | 1.86 | 0 |

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
| 204 | 990 |
| geo | 142 |
| sing-box exited 1 | 94 |
| cn-block | 21 |
| speed | 19 |
