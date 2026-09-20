# AutoNodes 每日报告

生成时间：2026-09-20 04:33:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 87371 |
| 去重后节点数 | 25387 |
| TCP 可达数 | 3000 |
| 真测通过数 | 581 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25387 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| generate | 25.3 |
| geo | 1.4 |
| probe | 218.9 |
| real_test | 314.5 |
| tcp | 42.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 60 | 45 | 15 | 75.0% |
| hysteria2 | 14 | 10 | 4 | 71.4% |
| shadowsocks | 182 | 169 | 13 | 92.9% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 60 | 39 | 21 | 65.0% |
| vless | 551 | 317 | 234 | 57.5% |
| vmess | 1 | 0 | 1 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 82 |
| speed:TimeoutError | 54 |
| geo:ClientOSError | 49 |
| 204:ProxyError | 20 |
| speed:ClientOSError | 20 |
| cn-block:ClientOSError | 19 |
| 204:ProxyConnectionError | 13 |
| cn-block:TimeoutError | 12 |
| 204:TimeoutError | 12 |
| cn-block:ProxyError | 5 |
| 204:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:38660: bind: address already in use | 1 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5743 |
| ConnectionRefusedError | 905 |
| gaierror | 430 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.921 | prefer | 362 | 0.856 | 1654 |
| ermaozi | 0.742 | prefer | 53 | 0.736 | 365 |
| Surfboard-tg-mixed | 0.694 | observe | 234 | 0.615 | 7138 |
| DeltaKronecker-all | 0.498 | observe | 77 | 0.416 | 6421 |
| mheidari-all | 0.467 | observe | 117 | 0.385 | 15978 |
| ermaozi-get_subscribe | 0.401 | observe | 7 | 0.714 | 394 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4251 |
| 10ium-ScrapeCategorize-Vless | 0.287 | observe | 2 | 0.5 | 5174 |
| xiaoji235-airport-v2ray-all | 0.277 | observe | 15 | 0.2 | 3625 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.2 | 3 | 12 | 15 |
| mheidari-all | 0.385 | 45 | 72 | 117 |
| DeltaKronecker-all | 0.416 | 32 | 45 | 77 |
| 10ium-ScrapeCategorize-Vless | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.615 | 144 | 90 | 234 |
| ermaozi-get_subscribe | 0.714 | 5 | 2 | 7 |
| ermaozi | 0.736 | 39 | 14 | 53 |
| Au1rxx-base64 | 0.856 | 310 | 52 | 362 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15978 | yes | 5.1 | 0 |
| SoliSpirit-all | 8830 | yes | 2.55 | 0 |
| Epodonios-all | 7601 | yes | 3.46 | 0 |
| Surfboard-tg-mixed | 7138 | yes | 4.36 | 0 |
| DeltaKronecker-all | 6421 | yes | 5.68 | 0 |
| barry-far-vless | 5908 | yes | 0.97 | 0 |
| Surfboard-tg-vless | 5693 | yes | 4.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 5174 | yes | 1.26 | 0 |
| mahdibland-V2RayAggregator | 4251 | yes | 0.21 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vmess | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 131 |
| speed | 74 |
| 204 | 48 |
| cn-block | 36 |
| sing-box exited 1 | 1 |
