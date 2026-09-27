# AutoNodes 每日报告

生成时间：2026-09-27 16:54:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 0/2 |
| 清理建议：优先/观察 | 3/102 |
| 原始节点数 | 96135 |
| 去重后节点数 | 26661 |
| TCP 可达数 | 3000 |
| 真测通过数 | 397 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26661 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 82.9 |
| geo | 1.5 |
| probe | 225.0 |
| real_test | 189.5 |
| tcp | 43.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 40 | 23 | 17 | 57.5% |
| hysteria2 | 20 | 18 | 2 | 90.0% |
| shadowsocks | 165 | 143 | 22 | 86.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 27 | 20 | 7 | 74.1% |
| vless | 257 | 190 | 67 | 73.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 27 |
| cn-block:TimeoutError | 21 |
| 204:ProxyError | 20 |
| speed:TimeoutError | 19 |
| geo:TimeoutError | 13 |
| speed:ClientOSError | 6 |
| 204:ProxyConnectionError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:48242: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6060 |
| ConnectionRefusedError | 972 |
| gaierror | 408 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.9 | prefer | 303 | 0.838 | 1601 |
| Surfboard-tg-mixed | 0.835 | prefer | 108 | 0.759 | 7109 |
| mheidari-all | 0.765 | prefer | 52 | 0.692 | 22413 |
| ermaozi | 0.633 | observe | 35 | 0.629 | 289 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| Epodonios-all | 0.255 | observe | 0 | None | 7600 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9194 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5703 |
| barry-far-vless | 0.255 | observe | 0 | None | 5938 |

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
| downweight | ermaozi-get_subscribe | 0.158 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.208 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.143 | 1 | 6 | 7 |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| ermaozi | 0.629 | 22 | 13 | 35 |
| mheidari-all | 0.692 | 36 | 16 | 52 |
| Surfboard-tg-mixed | 0.759 | 82 | 26 | 108 |
| Au1rxx-base64 | 0.838 | 254 | 49 | 303 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22413 | yes | 6.11 | 0 |
| SoliSpirit-all | 9194 | yes | 3.69 | 0 |
| Epodonios-all | 7600 | yes | 3.43 | 0 |
| Surfboard-tg-mixed | 7109 | yes | 5.13 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.7 | 0 |
| barry-far-vless | 5938 | yes | 1.92 | 0 |
| Surfboard-tg-vless | 5703 | yes | 3.93 | 0 |
| DeltaKronecker-all | 5466 | yes | 5.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 0.81 | 0 |
| mahdibland-V2RayAggregator | 4277 | yes | 3.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 52 |
| cn-block | 26 |
| speed | 25 |
| geo | 13 |
| sing-box exited 1 | 1 |
