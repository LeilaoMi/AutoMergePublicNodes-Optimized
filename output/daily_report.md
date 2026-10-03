# AutoNodes 每日报告

生成时间：2026-10-03 16:09:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 99539 |
| 去重后节点数 | 27336 |
| TCP 可达数 | 3000 |
| 真测通过数 | 320 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27336 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| generate | 83.0 |
| geo | 1.4 |
| probe | 187.2 |
| real_test | 123.4 |
| tcp | 47.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 24 | 22 | 2 | 91.7% |
| hysteria2 | 11 | 11 | 0 | 100.0% |
| shadowsocks | 107 | 89 | 18 | 83.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 20 | 17 | 3 | 85.0% |
| vless | 208 | 178 | 30 | 85.6% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 13 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 6 |
| 204:ProxyConnectionError | 5 |
| geo:TimeoutError | 5 |
| speed:ClientOSError | 4 |
| speed:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:ClientOSError | 2 |
| cn-block:ClientOSError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6513 |
| ConnectionRefusedError | 1143 |
| gaierror | 407 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.945 | prefer | 260 | 0.877 | 1778 |
| ermaozi | 0.911 | prefer | 24 | 0.917 | 656 |
| mheidari-all | 0.862 | prefer | 85 | 0.788 | 23342 |
| Surfboard-tg-mixed | 0.335 | observe | 1 | 1.0 | 7404 |
| ermaozi-get_subscribe | 0.274 | observe | 1 | 1.0 | 478 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5192 |
| Epodonios-all | 0.255 | observe | 0 | None | 7883 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9374 |

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
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.788 | 67 | 18 | 85 |
| Au1rxx-base64 | 0.877 | 228 | 32 | 260 |
| ermaozi | 0.917 | 22 | 2 | 24 |
| Surfboard-tg-mixed | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23342 | yes | 7.09 | 0 |
| SoliSpirit-all | 9374 | yes | 2.93 | 0 |
| Epodonios-all | 7883 | yes | 3.73 | 0 |
| Surfboard-tg-mixed | 7404 | yes | 5.47 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.07 | 0 |
| barry-far-vless | 6273 | yes | 1.42 | 0 |
| Surfboard-tg-vless | 6035 | yes | 5.68 | 0 |
| DeltaKronecker-all | 5207 | yes | 6.12 | 0 |
| 10ium-ScrapeCategorize-Vless | 5192 | yes | 1.17 | 0 |
| mahdibland-V2RayAggregator | 4335 | yes | 3.2 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 23 |
| cn-block | 16 |
| speed | 8 |
| geo | 7 |
