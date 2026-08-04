# AutoNodes 每日报告

生成时间：2026-08-04 14:33:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 86444 |
| 去重后节点数 | 24261 |
| TCP 可达数 | 3000 |
| 真测通过数 | 548 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24261 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 32.7 |
| geo | 1.3 |
| probe | 60.6 |
| real_test | 128.2 |
| tcp | 36.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 51 | 51 | 0 | 100.0% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 143 | 112 | 31 | 78.3% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 128 | 122 | 6 | 95.3% |
| vless | 332 | 241 | 91 | 72.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 32 |
| geo:ClientOSError | 21 |
| 204:ProxyError | 16 |
| geo:TimeoutError | 11 |
| speed:TimeoutError | 11 |
| cn-block:TimeoutError | 11 |
| speed:ClientOSError | 10 |
| 204:ClientOSError | 7 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:42803: bind: address already in use | 1 |
| speed:ClientPayloadError | 1 |
| geo:ProxyError | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:36461: bind: address already in use | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4895 |
| ConnectionRefusedError | 824 |
| gaierror | 279 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.984 | prefer | 52 | 1.0 | 72 |
| Au1rxx-base64 | 0.913 | prefer | 471 | 0.847 | 1684 |
| DeltaKronecker-all | 0.7 | observe | 119 | 0.622 | 5788 |
| mheidari-all | 0.633 | observe | 19 | 0.579 | 20302 |
| Surfboard-tg-mixed | 0.622 | observe | 15 | 0.667 | 5397 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 58 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5251 |
| Epodonios-all | 0.255 | observe | 0 | None | 5995 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.579 | 11 | 8 | 19 |
| DeltaKronecker-all | 0.622 | 74 | 45 | 119 |
| Surfboard-tg-mixed | 0.667 | 10 | 5 | 15 |
| Au1rxx-base64 | 0.847 | 399 | 72 | 471 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 52 | 0 | 52 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20302 | yes | 4.53 | 0 |
| SoliSpirit-all | 7036 | yes | 2.69 | 0 |
| Epodonios-all | 5995 | yes | 2.34 | 0 |
| DeltaKronecker-all | 5788 | yes | 4.28 | 0 |
| Surfboard-tg-mixed | 5397 | yes | 2.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 5251 | yes | 0.93 | 0 |
| xiaoji235-airport-v2ray-all | 5127 | yes | 1.47 | 0 |
| mahdibland-V2RayAggregator | 5110 | yes | 2.54 | 0 |
| barry-far-vless | 4658 | yes | 1.61 | 0 |
| Surfboard-tg-vless | 4315 | yes | 2.78 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 55 |
| geo | 33 |
| speed | 23 |
| cn-block | 19 |
| sing-box exited 1 | 2 |
