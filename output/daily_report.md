# AutoNodes 每日报告

生成时间：2026-10-10 12:27:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 97803 |
| 去重后节点数 | 27173 |
| TCP 可达数 | 3000 |
| 真测通过数 | 481 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27173 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 84.0 |
| geo | 1.1 |
| probe | 305.2 |
| real_test | 351.5 |
| tcp | 46.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 23 | 22 | 1 | 95.7% |
| shadowsocks | 160 | 140 | 20 | 87.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 149 | 126 | 23 | 84.6% |
| vless | 235 | 169 | 66 | 71.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 31 |
| 204:TimeoutError | 25 |
| geo:ClientOSError | 12 |
| speed:ClientOSError | 9 |
| cn-block:ClientOSError | 8 |
| speed:TimeoutError | 8 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 5 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6229 |
| ConnectionRefusedError | 1026 |
| gaierror | 483 |
| OSError | 239 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.96 | prefer | 20 | 1.0 | 144 |
| Au1rxx-base64 | 0.951 | prefer | 367 | 0.88 | 1820 |
| mheidari-all | 0.898 | prefer | 42 | 0.833 | 23754 |
| Surfboard-tg-mixed | 0.712 | prefer | 131 | 0.634 | 7103 |
| DeltaKronecker-all | 0.68 | observe | 28 | 0.607 | 5009 |
| ermaozi-get_subscribe | 0.384 | observe | 3 | 1.0 | 653 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4999 |
| Epodonios-all | 0.255 | observe | 0 | None | 7579 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9335 |

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
| DeltaKronecker-all | 0.607 | 17 | 11 | 28 |
| Surfboard-tg-mixed | 0.634 | 83 | 48 | 131 |
| mheidari-all | 0.833 | 35 | 7 | 42 |
| Au1rxx-base64 | 0.88 | 323 | 44 | 367 |
| ermaozi-get_subscribe | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23754 | yes | 4.28 | 0 |
| SoliSpirit-all | 9335 | yes | 3.53 | 0 |
| Epodonios-all | 7579 | yes | 2.89 | 0 |
| Surfboard-tg-mixed | 7103 | yes | 5.14 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.26 | 0 |
| barry-far-vless | 5861 | yes | 0.68 | 0 |
| Surfboard-tg-vless | 5620 | yes | 4.89 | 0 |
| DeltaKronecker-all | 5009 | yes | 3.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 4999 | yes | 0.54 | 0 |
| mahdibland-V2RayAggregator | 4347 | yes | 2.64 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 41 |
| 204 | 36 |
| speed | 18 |
| geo | 16 |
