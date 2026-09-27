# AutoNodes 每日报告

生成时间：2026-09-27 21:19:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 96200 |
| 去重后节点数 | 26757 |
| TCP 可达数 | 3000 |
| 真测通过数 | 412 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26757 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| generate | 91.1 |
| geo | 1.5 |
| probe | 216.4 |
| real_test | 203.6 |
| tcp | 43.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 36 | 16 | 20 | 44.4% |
| hysteria2 | 22 | 22 | 0 | 100.0% |
| shadowsocks | 177 | 152 | 25 | 85.9% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 20 | 14 | 6 | 70.0% |
| vless | 279 | 206 | 73 | 73.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 26 |
| 204:TimeoutError | 25 |
| 204:ProxyConnectionError | 16 |
| speed:ClientOSError | 14 |
| speed:TimeoutError | 10 |
| cn-block:ClientOSError | 9 |
| geo:TimeoutError | 9 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:35366: bind: address already in use | 1 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5587 |
| ConnectionRefusedError | 974 |
| gaierror | 405 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.895 | prefer | 261 | 0.831 | 1652 |
| Surfboard-tg-mixed | 0.839 | prefer | 164 | 0.762 | 7018 |
| mheidari-all | 0.798 | prefer | 69 | 0.725 | 22680 |
| ermaozi | 0.471 | observe | 35 | 0.457 | 289 |
| DeltaKronecker-all | 0.373 | observe | 5 | 0.6 | 5466 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7540 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9353 |

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

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.457 | 16 | 19 | 35 |
| DeltaKronecker-all | 0.6 | 3 | 2 | 5 |
| mheidari-all | 0.725 | 50 | 19 | 69 |
| Surfboard-tg-mixed | 0.762 | 125 | 39 | 164 |
| Au1rxx-base64 | 0.831 | 217 | 44 | 261 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22680 | yes | 6.17 | 0 |
| SoliSpirit-all | 9353 | yes | 3.55 | 0 |
| Epodonios-all | 7540 | yes | 5.19 | 0 |
| Surfboard-tg-mixed | 7018 | yes | 4.17 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.95 | 0 |
| barry-far-vless | 5823 | yes | 1.95 | 0 |
| Surfboard-tg-vless | 5592 | yes | 3.71 | 0 |
| DeltaKronecker-all | 5466 | yes | 6.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 1.54 | 0 |
| mahdibland-V2RayAggregator | 4185 | yes | 2.03 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 51 |
| cn-block | 36 |
| speed | 25 |
| geo | 11 |
| sing-box exited 1 | 1 |
