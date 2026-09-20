# AutoNodes 每日报告

生成时间：2026-09-20 20:44:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83660 |
| 去重后节点数 | 23470 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23470 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 75.9 |
| geo | 1.5 |
| probe | 193.8 |
| real_test | 206.3 |
| tcp | 38.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 32 | 27 | 5 | 84.4% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 161 | 145 | 16 | 90.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 24 | 7 | 17 | 29.2% |
| vless | 385 | 278 | 107 | 72.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 30 |
| 204:TimeoutError | 28 |
| geo:TimeoutError | 23 |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 13 |
| speed:ClientOSError | 10 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5079 |
| ConnectionRefusedError | 812 |
| gaierror | 477 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.971 | prefer | 275 | 0.909 | 1621 |
| DeltaKronecker-all | 0.926 | prefer | 24 | 0.875 | 6092 |
| ermaozi | 0.897 | prefer | 24 | 0.917 | 314 |
| mheidari-all | 0.701 | prefer | 56 | 0.625 | 16265 |
| Surfboard-tg-mixed | 0.681 | observe | 226 | 0.602 | 7207 |
| tg-oneclickvpnkeys | 0.403 | observe | 4 | 1.0 | 74 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4315 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7615 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| ermaozi-get_subscribe | 0.0 | 0 | 3 | 3 |
| Surfboard-tg-mixed | 0.602 | 136 | 90 | 226 |
| mheidari-all | 0.625 | 35 | 21 | 56 |
| DeltaKronecker-all | 0.875 | 21 | 3 | 24 |
| Au1rxx-base64 | 0.909 | 250 | 25 | 275 |
| ermaozi | 0.917 | 22 | 2 | 24 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16265 | yes | 4.5 | 0 |
| SoliSpirit-all | 8753 | yes | 2.79 | 0 |
| Epodonios-all | 7615 | yes | 4.79 | 0 |
| Surfboard-tg-mixed | 7207 | yes | 3.27 | 0 |
| DeltaKronecker-all | 6092 | yes | 3.61 | 0 |
| barry-far-vless | 5924 | yes | 0.93 | 0 |
| Surfboard-tg-vless | 5768 | yes | 3.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 5238 | yes | 1.3 | 0 |
| mahdibland-V2RayAggregator | 4315 | yes | 2.86 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.07 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 54 |
| 204 | 43 |
| cn-block | 31 |
| speed | 20 |
