# AutoNodes 每日报告

生成时间：2026-09-28 05:02:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 95255 |
| 去重后节点数 | 26814 |
| TCP 可达数 | 3000 |
| 真测通过数 | 535 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26814 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| generate | 74.6 |
| geo | 1.5 |
| probe | 326.6 |
| real_test | 467.3 |
| tcp | 43.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 49 | 28 | 21 | 57.1% |
| hysteria2 | 21 | 17 | 4 | 81.0% |
| shadowsocks | 189 | 169 | 20 | 89.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 29 | 23 | 6 | 79.3% |
| vless | 669 | 298 | 371 | 44.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 158 |
| speed:TimeoutError | 73 |
| geo:ClientOSError | 64 |
| speed:ClientOSError | 51 |
| cn-block:TimeoutError | 23 |
| 204:TimeoutError | 19 |
| 204:ProxyError | 16 |
| 204:ProxyConnectionError | 10 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:32349: bind: address already in use | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5638 |
| ConnectionRefusedError | 945 |
| gaierror | 378 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.912 | prefer | 329 | 0.857 | 1437 |
| Surfboard-tg-mixed | 0.784 | prefer | 204 | 0.706 | 6916 |
| ermaozi | 0.642 | observe | 41 | 0.634 | 347 |
| mheidari-all | 0.297 | observe | 367 | 0.215 | 22305 |
| DeltaKronecker-all | 0.263 | observe | 8 | 0.25 | 5466 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7506 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9195 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5591 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.143 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.143 | 1 | 6 | 7 |
| mheidari-all | 0.215 | 79 | 288 | 367 |
| DeltaKronecker-all | 0.25 | 2 | 6 | 8 |
| tg-oneclickvpnkeys | 0.5 | 1 | 1 | 2 |
| ermaozi | 0.634 | 26 | 15 | 41 |
| Surfboard-tg-mixed | 0.706 | 144 | 60 | 204 |
| Au1rxx-base64 | 0.857 | 282 | 47 | 329 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22305 | yes | 5.74 | 0 |
| SoliSpirit-all | 9195 | yes | 3.4 | 0 |
| Epodonios-all | 7506 | yes | 3.33 | 0 |
| Surfboard-tg-mixed | 6916 | yes | 3.84 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.16 | 0 |
| barry-far-vless | 5817 | yes | 1.5 | 0 |
| Surfboard-tg-vless | 5591 | yes | 3.61 | 0 |
| DeltaKronecker-all | 5466 | yes | 6.13 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 1.3 | 0 |
| mahdibland-V2RayAggregator | 4185 | yes | 2.96 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 223 |
| speed | 125 |
| 204 | 48 |
| cn-block | 27 |
| sing-box exited 1 | 1 |
