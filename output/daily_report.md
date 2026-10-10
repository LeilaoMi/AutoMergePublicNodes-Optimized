# AutoNodes 每日报告

生成时间：2026-10-10 21:37:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98061 |
| 去重后节点数 | 27327 |
| TCP 可达数 | 3000 |
| 真测通过数 | 462 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27327 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 87.1 |
| geo | 1.3 |
| probe | 256.6 |
| real_test | 313.3 |
| tcp | 46.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 2 | 4 | 33.3% |
| http | 35 | 25 | 10 | 71.4% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 114 | 103 | 11 | 90.4% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 109 | 109 | 0 | 100.0% |
| vless | 255 | 199 | 56 | 78.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 17 |
| cn-block:TimeoutError | 17 |
| speed:ClientOSError | 11 |
| speed:TimeoutError | 9 |
| 204:TimeoutError | 9 |
| geo:ClientOSError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6585 |
| ConnectionRefusedError | 1036 |
| gaierror | 416 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | prefer | 381 | 0.911 | 1850 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| mheidari-all | 0.797 | prefer | 111 | 0.721 | 23925 |
| Surfboard-tg-mixed | 0.489 | observe | 6 | 0.833 | 7118 |
| ermaozi-get_subscribe | 0.3 | observe | 19 | 0.263 | 580 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| DeltaKronecker-all | 0.259 | observe | 3 | 0.333 | 5009 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4999 |
| Epodonios-all | 0.255 | observe | 0 | None | 7597 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| ermaozi-get_subscribe | 0.263 | 5 | 14 | 19 |
| DeltaKronecker-all | 0.333 | 1 | 2 | 3 |
| mheidari-all | 0.721 | 80 | 31 | 111 |
| Surfboard-tg-mixed | 0.833 | 5 | 1 | 6 |
| Au1rxx-base64 | 0.911 | 347 | 34 | 381 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23925 | yes | 4.47 | 0 |
| SoliSpirit-all | 9340 | yes | 1.92 | 0 |
| Epodonios-all | 7597 | yes | 2.05 | 0 |
| Surfboard-tg-mixed | 7118 | yes | 2.48 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.66 | 0 |
| barry-far-vless | 5914 | yes | 1.25 | 0 |
| Surfboard-tg-vless | 5677 | yes | 2.64 | 0 |
| DeltaKronecker-all | 5009 | yes | 3.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 4999 | yes | 0.78 | 0 |
| mahdibland-V2RayAggregator | 4347 | yes | 2.09 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| cn-block | 23 |
| speed | 21 |
| geo | 9 |
