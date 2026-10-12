# AutoNodes 每日报告

生成时间：2026-10-12 15:14:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 100392 |
| 去重后节点数 | 27824 |
| TCP 可达数 | 3000 |
| 真测通过数 | 490 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27824 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| generate | 82.0 |
| geo | 1.5 |
| probe | 372.9 |
| real_test | 368.3 |
| tcp | 46.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 55 | 24 | 31 | 43.6% |
| hysteria2 | 19 | 17 | 2 | 89.5% |
| shadowsocks | 145 | 131 | 14 | 90.3% |
| socks | 6 | 3 | 3 | 50.0% |
| trojan | 166 | 145 | 21 | 87.3% |
| vless | 230 | 168 | 62 | 73.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 34 |
| cn-block:TimeoutError | 31 |
| 204:TimeoutError | 26 |
| 204:ProxyConnectionError | 8 |
| geo:ClientOSError | 8 |
| speed:TimeoutError | 7 |
| cn-block:ClientOSError | 6 |
| geo:TimeoutError | 3 |
| speed:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6069 |
| ConnectionRefusedError | 1067 |
| gaierror | 494 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.98 | prefer | 342 | 0.909 | 1816 |
| mheidari-all | 0.961 | prefer | 57 | 0.895 | 24027 |
| Surfboard-tg-mixed | 0.798 | prefer | 37 | 0.73 | 7166 |
| DeltaKronecker-all | 0.663 | observe | 125 | 0.584 | 5701 |
| ermaozi | 0.468 | observe | 57 | 0.439 | 675 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| ermaozi-get_subscribe | 0.276 | observe | 1 | 1.0 | 532 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5028 |
| Epodonios-all | 0.255 | observe | 0 | None | 7671 |

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
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.439 | 25 | 32 | 57 |
| DeltaKronecker-all | 0.584 | 73 | 52 | 125 |
| Surfboard-tg-mixed | 0.73 | 27 | 10 | 37 |
| mheidari-all | 0.895 | 51 | 6 | 57 |
| Au1rxx-base64 | 0.909 | 311 | 31 | 342 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24027 | yes | 6.33 | 0 |
| SoliSpirit-all | 9940 | yes | 4.03 | 0 |
| Epodonios-all | 7671 | yes | 6.56 | 0 |
| Surfboard-tg-mixed | 7166 | yes | 3.73 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.62 | 0 |
| barry-far-vless | 6031 | yes | 1.67 | 0 |
| Surfboard-tg-vless | 5781 | yes | 4.26 | 0 |
| DeltaKronecker-all | 5701 | yes | 7.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5028 | yes | 1.97 | 0 |
| mahdibland-V2RayAggregator | 4314 | yes | 3.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 70 |
| cn-block | 39 |
| geo | 13 |
| speed | 11 |
