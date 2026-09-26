# AutoNodes 每日报告

生成时间：2026-09-26 21:03:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 96520 |
| 去重后节点数 | 26455 |
| TCP 可达数 | 3000 |
| 真测通过数 | 403 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26455 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 85.7 |
| geo | 1.4 |
| probe | 262.0 |
| real_test | 188.9 |
| tcp | 43.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 20 | 11 | 9 | 55.0% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 150 | 132 | 18 | 88.0% |
| socks | 6 | 1 | 5 | 16.7% |
| trojan | 7 | 6 | 1 | 85.7% |
| vless | 343 | 230 | 113 | 67.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 49 |
| 204:TimeoutError | 38 |
| cn-block:TimeoutError | 18 |
| 204:ProxyError | 13 |
| speed:TimeoutError | 11 |
| geo:TimeoutError | 8 |
| speed:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:32653: bind: address already in use | 1 |
| geo:ClientOSError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6226 |
| ConnectionRefusedError | 954 |
| gaierror | 349 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.951 | prefer | 277 | 0.888 | 1654 |
| Surfboard-tg-mixed | 0.824 | prefer | 84 | 0.75 | 7263 |
| mheidari-all | 0.574 | observe | 158 | 0.494 | 22366 |
| ermaozi | 0.487 | observe | 17 | 0.529 | 296 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4355 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 66 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5242 |
| Epodonios-all | 0.255 | observe | 0 | None | 7740 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.25 | 1 | 3 | 4 |
| mheidari-all | 0.494 | 78 | 80 | 158 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| tg-LonUp_M | 0.5 | 1 | 1 | 2 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| ermaozi | 0.529 | 9 | 8 | 17 |
| Surfboard-tg-mixed | 0.75 | 63 | 21 | 84 |
| Au1rxx-base64 | 0.888 | 246 | 31 | 277 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22366 | yes | 4.04 | 0 |
| SoliSpirit-all | 8923 | yes | 2.89 | 0 |
| Epodonios-all | 7740 | yes | 0.93 | 0 |
| Surfboard-tg-mixed | 7263 | yes | 1.51 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.96 | 0 |
| barry-far-vless | 6052 | yes | 2.39 | 0 |
| Surfboard-tg-vless | 5823 | yes | 4.27 | 0 |
| DeltaKronecker-all | 5512 | yes | 3.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 5242 | yes | 2.54 | 0 |
| mahdibland-V2RayAggregator | 4355 | yes | 2.52 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 69 |
| 204 | 52 |
| speed | 16 |
| geo | 9 |
| sing-box exited 1 | 1 |
