# AutoNodes 每日报告

生成时间：2026-10-11 05:26:21

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 97520 |
| 去重后节点数 | 27407 |
| TCP 可达数 | 3000 |
| 真测通过数 | 526 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27407 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 78.8 |
| geo | 1.4 |
| probe | 349.6 |
| real_test | 604.6 |
| tcp | 46.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 9 | 2 | 7 | 22.2% |
| http | 39 | 35 | 4 | 89.7% |
| hysteria2 | 27 | 25 | 2 | 92.6% |
| shadowsocks | 120 | 116 | 4 | 96.7% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 143 | 127 | 16 | 88.8% |
| vless | 505 | 216 | 289 | 42.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 153 |
| speed:TimeoutError | 52 |
| geo:ClientOSError | 35 |
| speed:ClientOSError | 28 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 13 |
| 204:ClientOSError | 12 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 4 |
| speed:ClientPayloadError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6209 |
| ConnectionRefusedError | 1065 |
| gaierror | 433 |
| OSError | 241 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.991 | prefer | 370 | 0.922 | 1799 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.624 | observe | 11 | 0.818 | 7087 |
| ermaozi-get_subscribe | 0.596 | observe | 26 | 0.577 | 610 |
| DeltaKronecker-all | 0.418 | observe | 16 | 0.375 | 5009 |
| mheidari-all | 0.408 | observe | 398 | 0.327 | 23694 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4347 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4999 |
| Epodonios-all | 0.255 | observe | 0 | None | 7576 |

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
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.327 | 130 | 268 | 398 |
| DeltaKronecker-all | 0.375 | 6 | 10 | 16 |
| ermaozi-get_subscribe | 0.577 | 15 | 11 | 26 |
| Surfboard-tg-mixed | 0.818 | 9 | 2 | 11 |
| Au1rxx-base64 | 0.922 | 341 | 29 | 370 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23694 | yes | 5.0 | 0 |
| SoliSpirit-all | 9365 | yes | 2.44 | 0 |
| Epodonios-all | 7576 | yes | 4.2 | 0 |
| Surfboard-tg-mixed | 7087 | yes | 3.01 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.77 | 0 |
| barry-far-vless | 5790 | yes | 1.23 | 0 |
| Surfboard-tg-vless | 5545 | yes | 4.04 | 0 |
| DeltaKronecker-all | 5009 | yes | 3.32 | 0 |
| 10ium-ScrapeCategorize-Vless | 4999 | yes | 1.09 | 0 |
| mahdibland-V2RayAggregator | 4347 | yes | 2.13 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 188 |
| speed | 82 |
| 204 | 33 |
| cn-block | 20 |
